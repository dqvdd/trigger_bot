# Diccionario para almacenar los triggers
triggers = {}

def triggers_commands(bot):


    @bot.message_handler(commands=['addtrigger'])
    def addtrigger(message):
        args = message.text.split()[1:]
        if len(args) == 2:
            triggers[args[0]] = args[1]
            bot.reply_to(message, f'Trigger agregado: {args[0]} -> {args[1]}')
        elif len(args) == 1 and message.reply_to_message is not None:
            triggers[args[0]] = message.reply_to_message.text if message.reply_to_message.text else message.reply_to_message
            bot.reply_to(message, f'Trigger agregado: {args[0]}')
        else:
            bot.reply_to(message, 'Uso: /add_trigger <palabra> <respuesta> o responde a un mensaje con /add_trigger <palabra>')

    @bot.message_handler(commands=['striggers'])
    def striggers(message):
        response = 'Triggers:\n'
        for trigger in triggers.keys():
            response += f'{trigger}\n'
        bot.reply_to(message, response)

    @bot.message_handler(func=lambda m: True)
    def check_message(message):
        if message.text in triggers:
            trigger_response = triggers[message.text]
            if isinstance(trigger_response, str):
                bot.reply_to(message, trigger_response)
            else:
                if trigger_response.sticker is not None:
                    bot.send_sticker(message.chat.id, trigger_response.sticker.file_id)
                elif trigger_response.photo is not None:
                    bot.send_photo(message.chat.id, trigger_response.photo[-1].file_id)
                elif trigger_response.audio is not None:
                    bot.send_audio(message.chat.id, trigger_response.audio.file_id)
                elif trigger_response.voice is not None:
                    bot.send_voice(message.chat.id, trigger_response.voice.file_id)
                # Agrega aquí más tipos de contenido si es necesario
                else:
                    bot.reply_to(message, 'Lo siento, este tipo de contenido aún no es compatible.')