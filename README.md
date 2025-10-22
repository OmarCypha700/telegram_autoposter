# 📚 Telegram AutoPoster  
_Automated weekly Telegram posting of E-books (PDFs) for academic libraries and learning platforms_

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Schedule](https://img.shields.io/badge/Automation-Weekly-orange)

---

## 🧭 Overview

**Telegram AutoPoster** is a lightweight Python automation script that uploads **PDF resources** (books, lecture notes, open-access materials) to a **Telegram channel or group** on a **weekly schedule**.

The script detects **new, unposted files** in a folder and sends them automatically with **metadata-rich captions**.  
Designed for **academic libraries**, **digital repositories**, and **educational institutions** that want to share materials efficiently.

---

## 🚀 Features

✅ Automatically posts PDFs to your Telegram channel or group  
✅ Prevents reposting of old files using `posted_files.json` log file for tracking  
✅ Includes title, author, year, and description in captions using `metadata.json`  
✅ Randomly selects one new PDF per week  
✅ Easy to host and schedule on **PythonAnywhere** or locally  
✅ 100% open-source and customizable  

---

## 📁 Folder Structure

``` bash
📁 telegram-autoposter/
│
├── telegram_autoposter.py       # Main Python script
├── metadata.json                # Tracks posted files and metadata
├── pdfs/                        # Folder containing all your PDFs
│   ├── Book1.pdf
│   ├── Book2.pdf
│   └── ...
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/telegram-autoposter.git
cd telegram-autoposter
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a Telegram Bot
- Open Telegram and search for @BotFather
- Run /newbot and follow the setup prompts
- Copy your API token

### 5️⃣ Get Your Channel or Group ID
- Add your bot as an Admin of your channel or group
- Use `@userinfobot` to get your Chat ID

### 6️⃣ Configure the Script
Open the script and update:
```bash
TELEGRAM_BOT_TOKEN = "your_bot_token_here"
MY_CHANNEL_ID = "@yourchannelusername"

```

---

## 🧠 How It Works

1. The script scans the pdfs/ folder.
2. It checks metadata.json to find which PDFs are new.
3. Randomly selects one unposted file.
4. Sends it to your Telegram channel with metadata caption.
5. Updates metadata.json so it’s not reposted next week.

---
## 🧾 Example metadata.json

```json
{  "Anatomy_for_Nurses.pdf": {
    "title": "Anatomy for Nurses",
    "author": "OpenStax",
    "category": "Nursing / Basic Sciences",
    "description": "An open-access textbook covering human anatomy and physiology for nursing students."
  }
}
```
---
## 🤝 Contributing

Pull requests are welcome!
If you have suggestions for improving automation or formatting, please open an issue first to discuss.


## 👨‍💻 Author

Adjei-Kumi Nana Caleb (Cypha Omar)\
📚 College Librarian | Information Scientist | Research Consultant\
🌍 Ghana | 💡 Passionate about open access & digital transformation | 📚⚙️ Library Systems\
🔗 [LinkedIn](https://www.linkedin.com/in/nana-adjei-caleb)\
📧 [Email](mailto:omarcypha@gmail.com)


## 🪙 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

>⭐ If you find this project helpful, give it a star on GitHub and share it with your fellow librarians or developers!