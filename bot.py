import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به فروشگاه حامی خوش آمدید 🌸")


def run_flask():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Bot is running!"

    app.run(host="0.0.0.0", port=10000)


def main():
    token = os.getenv("BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("ربات حامی فعال شد...")

    threading.Thread(target=run_flask).start()

    app.run_polling()


if __name__ == "__main__":
    main()
