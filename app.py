from flask import Flask, request, jsonify
# Import library to get environment variable
import os 
# Import library for Telegram bot
import telegram
from telegram import Bot, Update
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
@app.route('/api', methods=['POST'])
def api():
    # Get the data from the POST request.
   
    data = request.get_json(force=True)
    print(data)
    chat_id =1959335278
    # Send a message to the bot
    bot.send_message(chat_id=chat_id, text='Hello, this is a message from the bot')
    
    return jsonify(data)
@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    data = request.get_json(force=True)

    # update
    update: Update = Update.de_json(data, bot)

    # get chat_id, text from update
    chat_id = update.message.chat.id
    text = update.message.text

    # sendMessage
    bot.send_message(chat_id, text)

    return 'ok'


    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)