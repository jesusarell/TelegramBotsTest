from telegram.ext import Updater, CommandHandler
import requests
import re
from personal_token import  * #archivo con el token generado mediante BotFather para el control de bot

#Codigo original y tutorial: https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_image_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def mimos(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(PERSONAL_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('mimos',mimos))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()