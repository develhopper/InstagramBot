from  flask import Flask
from flask import render_template
from flask import request
from pyrogram import Client, idle
from Instaloader.database.users_sql import users

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
        for row in users():
            client.send_message(chat_id=row[0],text=msg)

threading.Thread(target=app.run, daemon=True, kwargs={"host":"0.0.0.0"}).start()
idle()