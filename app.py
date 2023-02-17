from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from flask import Flask, request
import requests
import os
from telegram import Bot, Update

from main import (
    start,
    echo
)

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'hi from Python-2022I'
    # get data from request
    elif request.method == 'POST':
        data = request.get_json(force=True)

        # update
        dispatcher: Dispatcher = Dispatcher(bot, None, workers=0)
        update: Update = Update.de_json(data, bot)
        
        dispatcher.add_handler(CommandHandler('start', callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text, echo))

        dispatcher.process_update(update)
        return 'ok'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)