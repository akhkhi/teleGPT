from dotenv import load_dotenv
from string import punctuation
from .openai_chat import generate_response
import telebot
import os
import time


load_dotenv()
telebot_token = os.getenv('TELEBOT_TOKEN')

bot = telebot.TeleBot(token=telebot_token,parse_mode=None)

#/start command handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    """This function handles the /start command"""
    bot.reply_to(message,'Welcome to my bot, use /help for more info ')
    
    
# /about 
@bot.message_handler(commands=['about'])
def about_handler(message):
    """This function handles the /about command"""

    commands = """this is a chat GPT 3.5 turbo based telegram bot to generate respoces from openAI's chat GPT but through Telegram bot, has its own benefits """
    bot.reply_to(message, commands)


# /help command handler
@bot.message_handler(commands=['help'])
def help_handler(message):
    """This function handles the /help command"""

    commands = """/start - Start the Bot.\n/ai - Ask the Bot a Question.\n/help - Get Help.\n/about - about this bot """
    bot.reply_to(message, commands)

# /ai command handler
@bot.message_handler(commands=['ai']) 
def ai_handler(message): 
    """This function handles the /ai command"""

    if message.text == '/ai':
        bot.reply_to(message,'Please Use the format /ai followed by your question .')

    else:
        bot_message = bot.reply_to(message,'Please wait while I am processing your request')
        response = message_parser(message)

        bot.edit_message_text(response, chat_id=bot_message.chat.id,message_id=bot_message.message_id)







def message_parser(message):
    """This function parses the message and returns the response"""
    refine_message = f"{message.text.replace('/ai','')}" 
        
    if (refine_message.startswith('??') and 'program' in refine_message) or (refine_message.startswith('??') and 'code' in refine_message) :
        response = generate_response(refine_message)     
        return response

    if 'program' in refine_message or 'code' in refine_message:
        refine_message += 'give algorithm not code'
        response = generate_response(refine_message)
        return response

    response = generate_response(refine_message)
    return response


    