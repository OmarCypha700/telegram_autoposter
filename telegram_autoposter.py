import os
import json
import asyncio
import datetime
import random
from dotenv import load_dotenv
from telegram import Bot

# === LOAD ENVIRONMENT ===
load_dotenv()

# === CONFIGURATION ===
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")        # Telegram channel ID
MY_CHANNEL_ID = os.getenv("MY_CHANNEL_ID")  # Your personal Telegram chat ID for notifications
PDF_FOLDER = os.getenv("PDF_FOLDER")        # Folder containing PDFs
LOG_FILE = os.getenv("LOG_FILE")            # Tracks posted PDFs
METADATA_FILE = os.getenv("METADATA_FILE")  # Optional metadata file

# === SCHEDULE SETTINGS ===
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
POST_DAY = 4  # Change this number for another day (e.g., 2 for Wednesday)
PREVIEW_DAY = (POST_DAY - 1) % 7  # The day before posting


# === HELPER FUNCTIONS ===
def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_metadata():
    """Load metadata for PDFs if available."""
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# === CORE POST FUNCTION ===
async def post_pdf(bot, pdf_path, metadata=None):
    filename = os.path.basename(pdf_path)
    title = metadata.get("title", os.path.splitext(filename)[0])
    author = metadata.get("author", "Unknown Author")
    category = metadata.get("category", "General")
    description = metadata.get("description", "")

    caption = (
        f"📘 *{title}*\n"
        f"👩‍🏫 Author: {author}\n"
        f"🏷️ Category: {category}\n"
        f"🗒️ Description: {description}\n\n"
        f"📑 Download pdf"
    )

    with open(pdf_path, "rb") as pdf_file:
        await bot.send_document(
            chat_id=CHANNEL_ID,
            document=pdf_file,
            caption=caption,
            parse_mode="Markdown"
        )

    await bot.send_message(chat_id=MY_CHANNEL_ID, text=f"✅ Uploaded: {filename}")
    print(f"✅ Uploaded: {filename}")

# === MAIN FUNCTION ===
async def main():
    bot = Bot(token=TOKEN)
    today = datetime.datetime.today().weekday()

    log = load_json(LOG_FILE, [])
    metadata_dict = load_json(METADATA_FILE, {})
    unposted_files = [
        f for f in os.listdir(PDF_FOLDER)
        if f.endswith(".pdf") and f not in log
    ]

    # === PREVIEW DAY ===
    if today == PREVIEW_DAY:
        if unposted_files:
            next_pdf = random.choice(unposted_files)
            metadata = metadata_dict.get(next_pdf, {})
            title = metadata.get("title", os.path.splitext(next_pdf)[0])
            await bot.send_message(
                chat_id=MY_CHANNEL_ID,
                text=f"📅 Preview: Next week’s scheduled PDF is *{title}*."
            )
            print(f"📅 Preview sent for: {next_pdf}")
        else:
            await bot.send_message(chat_id=MY_CHANNEL_ID, text="⚠️ No unposted PDFs available for next week.")
        return

    # === POSTING DAY ===
    if today == POST_DAY:
        if not unposted_files:
            await bot.send_message(chat_id=MY_CHANNEL_ID, text="📂 No new PDFs found to post.")
            print("📂 No new PDFs found to post.")
            return

        selected_file = random.choice(unposted_files)
        full_path = os.path.join(PDF_FOLDER, selected_file)
        metadata = metadata_dict.get(selected_file, {})

        await bot.send_message(chat_id=MY_CHANNEL_ID, text=f"📅 Posting day! Uploading: {selected_file}")
        await post_pdf(bot, full_path, metadata)

        log.append(selected_file)
        save_json(LOG_FILE, log)

        await bot.send_message(chat_id=MY_CHANNEL_ID, text=f"✅ Successfully posted 1 new PDF this week!")
        print("✅ Posted 1 new PDF successfully!")
        return

    # === NON-SCHEDULED DAYS ===
    await bot.send_message(chat_id=MY_CHANNEL_ID, text="⏸️ Not a scheduled day for posting.")
    print("⏸️ Not a scheduled day for posting.")

# === RUN ===
if __name__ == "__main__":
    asyncio.run(main())
