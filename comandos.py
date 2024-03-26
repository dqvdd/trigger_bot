from telebot.apihelper import ApiException

def messages_commands(bot):

    # Comando Start, para saludar al bot
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Hola, soy el bot del grupo Exotic para los triggers.")


    # Comando help, para explicar los comandos disponibles
    @bot.message_handler(commands=["help"])
    def help(message):
        help_message = "Los comandos disponibles son:\n/start: Saluda al bot"
        bot.send_message(message.chat.id, help_message)




