from origamibot import OrigamiBot as Bot
from app.models.listeners.message_listener import MessageListener
from app.models.chat_models.openai_model import SimpleChatBot
from time import sleep


def run_bot(bot_token: str) -> None:
    bot = Bot(token=bot_token)
    model = SimpleChatBot()
    listener = MessageListener(bot=bot, ai_model=model)
    bot.add_listener(listener)
    bot.start()
    while True:
        sleep(1)
