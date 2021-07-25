# -*- coding: utf-8 -*-

from telegram.ext import Updater , CommandHandler,CallbackQueryHandler , InlineQueryHandler

#Botones Teclado (KeyboardButton y ReplyKeyboardMarkup)

#Botones en linea (InlineKeyboardMarkup y InlineKeyboardButton)

from telegram import ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardMarkup , InlineKeyboardButton , InlineQueryResultArticle,InputTextMessageContent

def start(Update , context) :
	
	name=Update.effective_user.first_name

	Update.message.reply_text(text=
	f"🌟Bienvenido  {name}:"
	"\n\n Tienda de Yely -> /Tienda_Yely"
	"\n Tienda de Lily -> /Tienda_Lily\n\n")
	
	
def Tienda_Yely(Update,context):
	
	contacto= InlineKeyboardButton(text=
	"Contacto👤" , url= "https://t.me/Yely02")
	
	lili= InlineKeyboardButton(text=
	"⚗TIENDA⚒" ,
	url="https://t.me/share/url?url=/ws_gMV4W")
		
	
	
	Update.message.reply_text(text=
	"Yelany",
	reply_markup=
	InlineKeyboardMarkup([
	[contacto,lili]]))
	
def Tienda_Lily(Update,context):
	
	contacto= InlineKeyboardButton(text=
	"Contacto👤" , url= "https://t.me/Lylithz")
	
	lili= InlineKeyboardButton(text=
	"⚒TIENDA⚒" ,
	url="https://t.me/share/url?url=/ws_lI9uW")
		
	
	
	Update.message.reply_text(text=
	"Leonor",
	reply_markup=
	InlineKeyboardMarkup([
	[contacto,lili]]))
	
def boton_switch(Update,context):
	
	"""
	PARA LOS BOTONES SWITCH
	ACTIVAR EL MODO INLINE EN
	@BotFather
	"""
		
	boton1= InlineKeyboardButton(text=
	"Abrir en otro chat",
	switch_inline_query="Hola"
	)
	
	boton2= InlineKeyboardButton(text=
	"Abrir en este chat",switch_inline_query_current_chat=
	"Hola"
	)	
	
	
	Update.message.reply_text(text=
	"Botones switch",
	reply_markup=
	InlineKeyboardMarkup([
	[boton1],[boton2]]))
	
	"""
	FUNCIÓN PARA LOS BOTONES
	SWITCH
	"""
def inline(Update,context):
	
	query_id=Update.inline_query.id
	query=Update.inline_query.query
	
	text_inline=query
	results=[]
	
	consulta = InlineQueryResultArticle(id=query_id,title= text_inline,  input_message_content=InputTextMessageContent(text_inline))
	
	results.append(consulta)
	
	context.bot.answer_inline_query(
	Update.inline_query.id,
	results=results)

	"""
	FUNCIÓN PARA LOS BOTONES
	INLINE
	"""
def enviar_mensaje(Update,context):
	
	chat_id=Update.callback_query.message.chat_id
	
	context.bot.send_message(chat_id=chat_id,
	text="Click!")
	
	
def alerta (Update,context):
	callback_id = Update.callback_query.id
	
	context.bot.answer_callback_query(callback_query_id=
	callback_id , 
	text = "Mensaje de Alerta" , 
	show_alert=False)			

def ventana_emergente (Update,context):
	
	callback_id = Update.callback_query.id
	
	context.bot.answer_callback_query(callback_query_id=
	callback_id , 
	text = "Ventana Emergente" , 
	show_alert=True)	

def editar_texto(Update,context):
	
	query=Update.callback_query
	
	query.answer()
	
	query.edit_message_text(text=
	"Mensaje Editado")



if __name__ == '__main__':

	updater = Updater(token=	 "1503253393:AAHoc_9EIoge8JgPkOF_py4Ze6l0knHm4eo" ,  
	use_context=True)
	
	update = Updater
	dp = updater.dispatcher
	
	#HANDLER DE LOS COMANDOS
	
	dp.add_handler(CommandHandler('start', start))
	
	dp.add_handler(CommandHandler("Tienda_Yely" , Tienda_Yely))
	
	dp.add_handler(CommandHandler("Tienda_Lily", Tienda_Lily))
	
	dp.add_handler(CommandHandler("boton_switch",boton_switch))
	
	"""
	HANDLERS (MANEJADORES)PARA 
	LOS BOTONES INLINE 
	"""
	
	dp.add_handler(CallbackQueryHandler(pattern="call_Boton1" , callback=enviar_mensaje))
	
	dp.add_handler(CallbackQueryHandler(pattern="call_Boton2" , callback=alerta))
	
	dp.add_handler(CallbackQueryHandler(pattern="call_Boton3" , callback=ventana_emergente))
	
	dp.add_handler(CallbackQueryHandler(pattern="call_Boton4" , callback=editar_texto))	
	
	
	
	"""
	PARA LOS BOTONES SWITCH
	ACTIVAR EL MODO INLINE EN
	@BotFather
	"""
	dp.add_handler(InlineQueryHandler(inline))	
	
		
	updater.start_polling()
	print("Esta Corriendo")
	updater.idle()
	