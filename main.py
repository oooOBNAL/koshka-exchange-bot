# koshka-exchange-bot
import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

start_keyboard = ReplyKeyboardMarkup(
    [["Актуальный курс", "Связаться с менеджером", "Партнеры"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вас приветствует самый дружелюбный и надежный сервис по обмену валют Koshka Exchange 🐱",
        reply_markup=start_keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Актуальный курс":
        await update.message.reply_text(
            "USDT → RUB: 98.3₽\nRUB → THB: 0.36฿\nUSDT → THB: 3.63฿"
        )
    elif text == "Связаться с менеджером":
        await update.message.reply_text("@KoshkaExchanger")
    elif text == "Партнеры":
        await update.message.reply_text("@O000bnal")
    else:
        await update.message.reply_text("Пожалуйста, выберите вариант из меню.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    app.run_polling()
