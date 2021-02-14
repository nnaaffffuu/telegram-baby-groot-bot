import constants as keys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import responses as reply

print("Bot Started...")


def start_command(update, context):
    update.message.reply_text('I am Groot')


def help_command(update, context):
    update.message.reply_text('I am Groot')


def handle_message(update, context):
    update.message.reply_text(reply.responses())


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
