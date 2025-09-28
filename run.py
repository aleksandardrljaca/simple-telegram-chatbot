import os
from dotenv import load_dotenv
from app import run_bot

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


if __name__ == "__main__":
    run_bot(bot_token=TELEGRAM_TOKEN)
