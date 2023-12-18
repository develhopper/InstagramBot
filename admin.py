from  flask import Flask
from flask import render_template
from flask import request
from dotenv import load_dotenv
from pyrogram import Client, idle

import os
import Config
import threading

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    error = None
    if request.method == "POST":
        password = request.form['password']
        if password == os.environ.get('ADMIN_PASSWORD'):
            send_message(request.form['message'])
        else:
            error = "Incorrect Password"
            
    return render_template('index.html',error=error)


def send_message(msg):
    with Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,) as client:
        client.send_message(chat_id=2103705885,text=msg)

threading.Thread(target=app.run, daemon=True, kwargs={"host":"0.0.0.0"}).start()
idle()