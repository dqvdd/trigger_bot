from telebot import TeleBot
import comandos, afk, triggers

# Reemplazar con el token de acceso
#bot = TeleBot("6860570837:AAG8-_OXoUJR90fD2fjZBvj9DqQ9skBS9pQ") ##fekita
bot = TeleBot("7183162205:AAHSJQhg4D6Jrt_9ciC1Kn1u4RVa5ofIZK4") ##prueba

# Importa los comandos de los otros archivos
comandos.messages_commands(bot)
triggers.triggers_commands(bot)
# Inicia el bot
bot.polling()
