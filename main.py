from config import TOKEN
import requests
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    filename="dblogs.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'User{update.effective_chat.id} starts bot')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot I send some joke. do u want? (yes or no)")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == 'yes':
        re = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text = re.text[10:-3])
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text = "Again?")

    elif update.message.text.lower() == 'no':
        await context.bot.send_message(chat_id=update.effective_chat.id, text = 'Okey, byby')

    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text = 'There is no such option')


def main():
    logging.info("Start bot")
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    joke_handler = MessageHandler(filters.TEXT, joke)

    application.add_handler(start_handler)
    application.add_handler(joke_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
