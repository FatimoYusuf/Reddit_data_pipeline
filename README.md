# Reddit Data Pipeline

This project is a simple Reddit data pipeline built using:

- 🐍 Python 3.10+
- 🧰 SQLAlchemy (ORM)
- 🐘 MySQL
- 🔁 Alembic (for migrations)
- 🔎 PRAW (Python Reddit API Wrapper)

## 🔧 Features

- Connects to Reddit via API using PRAW
- Fetches hot posts from selected subreddits
- Saves structured data into a MySQL database
- Avoids duplicates using post ID
- Automatically handles migrations with Alembic

## 📌 Subreddits Included

- `nigeria`
- `technology`
- `datascience`
- `machinelearning`
- `programming`
- `worldnews`
- `AskReddit`
- `finance`
- `Futurology`

## ⚙️ Setup Instructions

1. **Clone this repo:**

```bash
git clone https://github.com/FatimoYusuf/Reddit_data_pipeline.git
cd Reddit_data_pipeline
