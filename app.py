import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://github.com/Azithro721/LazyPrincess okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
