# Discord AI Support Bot for Washing Machine Queries
Powered by LLaMA 3.3 (Groq) + MantisHub + SQLite

## 📌 Description
This project implements an AI-powered Discord chatbot that assists users with washing machine-related queries. It intelligently decides whether to answer directly using LLaMA 3.3 (via Groq Cloud) or escalate the issue by creating a support ticket via MantisHub. Each user’s ticket is tracked using a lightweight SQLite database.

## Wokring Demo Video
[Demo](https://drive.google.com/file/d/1cY5Aw5FfxzaPZc6PBJUQTgdnFWLsIhyb/view?usp=sharing)

## 🧠 Features

🤖 Answers user queries with Groq’s LLaMA 3.3 model

🧾 Automatically raises a support ticket if needed

🧷 Persists user-ticket mapping with SQLite

📌 Responds with open ticket number in every message

✅ Allows ticket closure via !close command



## 🧰 Tech Stack
Layer	Technology
Bot Platform	Discord (discord.py)
AI Query Resolution	Groq API (LLaMA 3.3)
Ticketing System	MantisHub REST API
Database	SQLite
Backend	Python 3

## 📊 Architecture Diagram

```
flowchart TD
    User["🧑 User on Discord"]
    Bot["🤖 Discord Bot (discord.py)"]
    LLM["🧠 Groq LLaMA 3.3 API"]
    Mantis["🧾 MantisHub API"]
    DB["💽 SQLite DB (ticket map)"]

    User -->|!ask <query>| Bot
    Bot -->|API call| LLM
    LLM -->|Response| Bot
    Bot -->|Ticket Needed?| Mantis
    Bot -->|Store ticket ID| DB
    Bot -->|Respond + Ticket ID| User
    User -->|!status / !close| Bot
    Bot --> DB
```

## 🔄 Workflow
User sends a query using !ask <message>

Bot forwards query to Groq LLaMA 3.3

LLM responds with troubleshooting steps or suggests ticket creation

If user confirms, a ticket is created in MantisHub

The ticket ID is saved against the user in SQLite

For future messages:

LLM still responds

Ticket number is always displayed

Users can run !status or !close as needed

## ⚙️ Project Setup
1️⃣ Clone the Repo
bash

```
git clone https://github.com/yourusername/discord-washerbot.git
cd discord-washerbot
```
## 2️⃣ Install Dependencies
bash
```
pip install -r requirements.txt
```

## 3️⃣ Configure config.py
python

```
DISCORD_BOT_TOKEN = 'your-discord-bot-token'

GROQ_API_KEY = 'your-groq-api-key'
MANTIS_API_TOKEN = 'your-mantis-api-token'
MANTIS_PROJECT_ID = 123456  # Get this from MantisHub project URL
MANTIS_CATEGORY = 'General'
MANTIS_BASE_URL = 'https://your-subdomain.mantishub.io'

DB_FILE = 'tickets.db'
```

## 4️⃣ Run the Bot
bash
```
python bot.py
```

## 💬 Bot Commands
Command	Description
```
!ask <query>	Ask a question about your washing machine
!status	Show your current open ticket (if any)
!close	Close your current ticket and delete it from memory
```

## 🛠 How to Recreate the Project
✅ Create a Discord Bot

Discord Developer Portal

Enable Message Content Intent

Copy your bot token

🧠 Get Groq API Key

Sign up at https://console.groq.com

Use model: llama3-70b-8192

🧾 Set up MantisHub

Create project and category

Go to "My Account" → "API Tokens"

Copy token and project ID

💽 Configure config.py

Add tokens and API keys

Get your MantisHub project ID and subdomain

🧠 Use llm.py to connect with Groq

🧾 Use mantis.py to open tickets

💬 Use handlers/*.py for each command

🧠 Use memory.py for tracking ticket-user mappings

🎯 Run bot.py — your full bot!

## 🧪 Testing Tips
```
Try !ask My washer isn’t spinning

If ticket is suggested → type yes

Try !status to see ticket

Try !close and then !status again
```


## 🙋‍♀️ Future Ideas
Add MantisHub ticket status syncing

Allow attachments

Admin dashboard (Flask or Streamlit)

Multi-ticket support

Auto-summarize issue history

