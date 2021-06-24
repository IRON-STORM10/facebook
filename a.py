import os,sys,subprocess
subprocess.getoutput("pip3 install pyTelegramBotAPI")
subprocess.getoutput("pip3 install telebot")
import telebot,random
from telebot import types
bot = telebot.TeleBot("1725642703:AAFGzGOWgj_gHjuRAdZd5Hwonepr-n52PIo")
@bot.message_handler(commands=["start"])
def srt(message):
 bot.send_message(message.chat.id,text="WELCOM TO MOELSHAFEY BOT\nBOT GENERAT FP ACCOUNT🙂\nTHIS IS V1 ONLY PRO \nTO TURN ON [ /FP ]\nCODED BY @Iron_Storm10 \nالبوت بلغه:🐍")
@bot.message_handler(commands=['FP'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/العراق','/باكستان', '/مصر')
    bot.send_message(message.chat.id, 'اهلا بك اختار ما يناسبك من القائمه بالاسفل 👇🏻', reply_markup=keyboard)
@bot.message_handler(commands=['مصر'])
def srt(message):
 nmr =(str( random.randint(11111111,99999999)))
 low = ['+2010','+2012','+2011']
 op= random.choice(low)
 NOM=(op+nmr)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNT🇪🇬 GENRATED\n–––––––––––––––– \n💠ID:{NOM}\n–––––––––––––––– \n♻️PASSWORD: {1122334455}\n––––––––––––––––\n⚜️️BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(commands=['باكستان'])
def srt(message):
 nmr =(str( random.randint(1111111,9999999)))
 low = ['+92301','+92309','+92304','+92301','+92344']
 op= random.choice(low)
 NOM=(op+nmr)
 pll=('786786',nmr,'pakistan')
 psi= random.choice(pll)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNT🇵🇰 GENRATED\n–––––––––––––––– \n💠ID:{NOM}\n–––––––––––––––– \n♻️PASSWORD: {psi}\n––––––––––––––––\n⚜️️BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(commands=['العراق'])
def sr7t(message):
 nmr =(str( random.randint(1111111,9999999)))
 low = ['+9640772','+9640751','+9640750','+9640782','+9640771']
 op= random.choice(low)
 NOM=(op+nmr)
 pll=('1234512345',NOM,'1122334455')
 psi= random.choice(pll)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNT🇮🇶 GENRATED\n–––––––––––––––– \n💠ID:{NOM}\n–––––––––––––––– \n♻️PASSWORD: {psi}\n––––––––––––––––\n⚜️️BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(func=(lambda message: True))
def s4tr(message):
 bot.send_message(message.chat.id,"WORNG CHOIC /start️")
bot.polling()
