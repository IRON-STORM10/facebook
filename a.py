import os,sys,subprocess
subprocess.getoutput("pip3 install pyTelegramBotAPI")
subprocess.getoutput("pip3 install telebot")
import telebot,random
from telebot import types
bot = telebot.TeleBot("1725642703:AAFGzGOWgj_gHjuRAdZd5Hwonepr-n52PIo")
@bot.message_handler(commands=["start"])
def srt(message):
 bot.send_message(message.chat.id,text="WELCOM TO MOELSHAFEY BOT\nBOT GENERAT FP ACCOUNTð\nTHIS IS V1 ONLY PRO \nTO TURN ON [ /FP ]\nCODED BY @Iron_Storm10 \nØ§ÙØ¨ÙØª Ø¨ÙØºÙ:ð")
@bot.message_handler(commands=['FP'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/Ø§ÙØ¹Ø±Ø§Ù','/Ø¨Ø§ÙØ³ØªØ§Ù', '/ÙØµØ±')
    bot.send_message(message.chat.id, 'Ø§ÙÙØ§ Ø¨Ù Ø§Ø®ØªØ§Ø± ÙØ§ ÙÙØ§Ø³Ø¨Ù ÙÙ Ø§ÙÙØ§Ø¦ÙÙ Ø¨Ø§ÙØ§Ø³ÙÙ ðð»', reply_markup=keyboard)
@bot.message_handler(commands=['ÙØµØ±'])
def srt(message):
 nmr =(str( random.randint(11111111,99999999)))
 low = ['+2010','+2012','+2011']
 op= random.choice(low)
 NOM=(op+nmr)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNTðªð¬ GENRATED\nââââââââââââââââ \nð ID:{NOM}\nââââââââââââââââ \nâ»ï¸PASSWORD: {1122334455}\nââââââââââââââââ\nâï¸ï¸BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(commands=['Ø¨Ø§ÙØ³ØªØ§Ù'])
def srt(message):
 nmr =(str( random.randint(1111111,9999999)))
 low = ['+92301','+92309','+92304','+92301','+92344']
 op= random.choice(low)
 NOM=(op+nmr)
 pll=('786786',nmr,'pakistan')
 psi= random.choice(pll)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNTðµð° GENRATED\nââââââââââââââââ \nð ID:{NOM}\nââââââââââââââââ \nâ»ï¸PASSWORD: {psi}\nââââââââââââââââ\nâï¸ï¸BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(commands=['Ø§ÙØ¹Ø±Ø§Ù'])
def sr7t(message):
 nmr =(str( random.randint(1111111,9999999)))
 low = ['+9640772','+9640751','+9640750','+9640782','+9640771']
 op= random.choice(low)
 NOM=(op+nmr)
 pll=('1234512345',NOM,'1122334455')
 psi= random.choice(pll)
 bot.send_message(message.chat.id,text=f"NEW FP ACCOUNTð®ð¶ GENRATED\nââââââââââââââââ \nð ID:{NOM}\nââââââââââââââââ \nâ»ï¸PASSWORD: {psi}\nââââââââââââââââ\nâï¸ï¸BY @Iron_Storm10 and @MO_SH_FY")
@bot.message_handler(func=(lambda message: True))
def s4tr(message):
 bot.send_message(message.chat.id,"WORNG CHOIC /startï¸")
bot.polling()
