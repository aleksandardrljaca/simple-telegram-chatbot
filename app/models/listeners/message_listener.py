from origamibot.listener import Listener
from origamibot import OrigamiBot as Bot
from app.models.chat_models.openai_model import SimpleChatBot
from origamibot.core.teletypes.message import Message


class MessageListener(Listener):  # Event listener must inherit Listener
    def __init__(self, bot: Bot, ai_model: SimpleChatBot):
        self.bot = bot
        self.ai_model = ai_model
        self.m_count = 0

    def on_message(self, message: Message):  # called on every message
        self.m_count += 1
        print(f"Total messages: {self.m_count}")
        received_msg = message.text
        response = self.ai_model.ask(received_msg)
        self.bot.send_message(chat_id=message.chat.id, text=response)

    def on_command_failure(self, message: Message, err=None):  # When command fails
        if err is None:
            self.bot.send_message(message.chat.id, "Command failed to bind arguments!")
        else:
            self.bot.send_message(message.chat.id, f"Error in command:\n{err}")
