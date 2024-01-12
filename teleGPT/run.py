# to keep the bot running 
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()




from app.telebot import bot


if __name__=='__main__':
    keep_alive()
    print('Bot is running...')
    bot.infinity_polling(none_stop=True)