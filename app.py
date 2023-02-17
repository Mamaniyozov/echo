from flask import Flask ,request,jsonify
import requests
import telegram
from telegram import Bot, Update
from telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters
import os

from bot_app import(
    start,
    echo,
)
# Create an instance of Flask
app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
# Create a bot
bot = telegram.Bot(token=TOKEN)

#Create a route for home page
@app.route('/')
def home():
    html = '''
    <h1> This is a home page </h1>
    <p> This is a paragraph </p>
    '''
    print(TOKEN)
    return html

# Create a route
# @app.route('/api', methods=['POST'])
# def api():
#     # Get the data from the POST request.
   
#     data = request.get_json(force=True)
#     print(data)
#     chat_id =1959335278
    
#     # Send a message to the bot
#     bot.send_message(chat_id=chat_id, text='Hello, this is a message from the bot')
    
#     return jsonify(data)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'GET':
        return 'Helo World'
    elif request.method == 'POST':

        data = request.get_json(force=True)

        dispatcher:Dispatcher = Dispatcher(bot, None , workers=0)

        update:Update = Update.de_json(data, bot)

        dispatcher.add_handler(CommandHandler('start',callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text,echo))

        dispatcher.process_update(update)


        # chat_id = update.message.chat_id
        # text = update.message.text
        # if text !=None:

        #     bot.send_message(chat_id, text)
        # print(chat_id)

    return "Assalomu alaykum"


    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)