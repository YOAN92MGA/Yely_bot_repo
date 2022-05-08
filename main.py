import Constants as keys
import Responses as R
from telegram.ext import *
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent

print("bot started...")

def start_command(update, context):
    update.message.reply_text('Type something ramdom to get started')
    name = update.effective_user.first_name

    update.message.reply_text(text=
                              f"🌟Bienvenido  {name}:"
                              "\n Tienda de Lily -> /Tienda_Lily\n\n")

def help_command(update, context):
    update.message.reply_text('If you need help! You shoul ask for it on Google!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    respuesta = R.sample_response(text)

    update.message.reply_text(respuesta)

def error(update, context):
    print(f"Update {update} caused error {context.erroe}")

def myInfo (Update, context):

    chat_id = Update.message.chat.id
    name = Update.effective_user.first_name
    id = Update.effective_user.id
    username = Update.effective_user.username

    list_id = open("id_list.txt", "a", encoding="utf-8")
    list_id.write(str(id) + "\n")
    Update.message.reply_text("Nombre: " + name + "\nID: " + str(id) + "\nUsername: @" + username)

def Tienda_Lily(Update, context):
    contacto = InlineKeyboardButton(text="👤Contacto👤", url="https://t.me/Lylithz")

    lili = InlineKeyboardButton(text="⚒TIENDA⚒", url="https://telegram.me/chtwrsbot/share/url?url=/ws_lI9uW")

    Update.message.reply_text(text="📦-⚒ Leonor @Lylithz", reply_markup=InlineKeyboardMarkup([[contacto, lili]]))

if __name__ == '__main__':
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("herreria", Tienda_Lily))
    dp.add_handler(CommandHandler("info", myInfo))
    dp.add_handler(MessageHandler(Filters.text, handle_message))



    updater.start_polling()
    print("corriendo....")
    updater.idle()
