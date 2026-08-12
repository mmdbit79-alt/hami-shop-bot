bot.py
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 به فروشگاه حامی خوش آمدید!")

def main():
    app = Application.builder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))

    print("ربات حامی فعال شد...")
    app.run_polling()

if __name__ == "__main__":
    main()
