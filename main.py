from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *


updater = Updater('5773231193:AAE1-4a6Bxjwrzu5Bq-pxl9xUYh1LmcZyFI')

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mul', mul_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))

updater.dispatcher.add_handler(MessageHandler(Filters.text, analize_command))

updater.start_polling()
updater.idle()

