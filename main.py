from telebot import TeleBot
import comandos, triggers

# Reemplazar con el token de acceso
bot = TeleBot("6733745060:AAGwprYXVR6pRUt6VFsWdlq1e02iIkqCmqQ") ##triggers 
#bot = TeleBot("7183162205:AAHSJQhg4D6Jrt_9ciC1Kn1u4RVa5ofIZK4") ##prueba

# Importa los comandos de los otros archivos
comandos.messages_commands(bot)
triggers.triggers_commands(bot)
# Inicia el bot
bot.polling()
