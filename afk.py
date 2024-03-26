import json, os, time

def afk_commands(bot):
    # Archivo para almacenar usuarios AFK y sus mensajes
    afk_file = 'afk_users.json'

    # Cargar usuarios AFK desde el archivo
    if os.path.exists(afk_file):
        with open(afk_file, 'r') as f:
            afk_users = json.load(f)
    else:
        afk_users = {}

    # Función para guardar usuarios AFK en el archivo
    def save_afk_users():
        with open(afk_file, 'w') as f:
            json.dump(afk_users, f)

    # Función para detectar AFK
    @bot.message_handler(commands=["afk"])
    def afk(message):
        user_id = str(message.from_user.id)  # Convertir a str porque JSON no permite int como claves
        afk_users[user_id] = (time.time(), None)
        save_afk_users()
        bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK.")

    # Función para detectar "brb"
    @bot.message_handler(func=lambda message: message.text.lower().startswith("brb"))
    def brb(message):
        user_id = str(message.from_user.id)  # Convertir a str porque JSON no permite int como claves
        afk_message = message.text[4:] if len(message.text) > 4 else None
        afk_users[user_id] = (time.time(), afk_message)
        save_afk_users()
        if afk_message:
            bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK. \nRazón: {afk_message}")
        else:
            bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK.")

    # Función para calcular el tiempo AFK
    def get_afk_time(user_id):
        user_id = str(user_id)  # Convertir a str porque JSON no permite int como claves
        if user_id in afk_users:
            return time.time() - afk_users[user_id][0]
        return None

    @bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
    def handle_all(message):
        user_id = str(message.from_user.id)  # Convertir a str porque JSON no permite int como claves
        if user_id in afk_users:
            # Verifica si el mensaje es una respuesta a un mensaje propio
            if message.reply_to_message and message.reply_to_message.from_user.id == int(user_id):  # Convertir a int para comparar con el id del mensaje
                return
            afk_time, afk_message = afk_users[user_id]
            bot.send_message(message.chat.id, f"{message.from_user.first_name} volvió después de estar AFK durante {format_time(get_afk_time(int(user_id)))}.")  # Convertir a int para la función get_afk_time
            del afk_users[user_id]
            save_afk_users()  # Guardar cambios en el archivo
        elif message.reply_to_message and str(message.reply_to_message.from_user.id) in afk_users:  # Convertir a str para buscar en afk_users
            # Función para responder a menciones
            user_id = str(message.reply_to_message.from_user.id)  # Convertir a str porque JSON no permite int como claves
            afk_time, afk_message = afk_users[user_id]
            if afk_time:
                if afk_message:
                    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} está AFK desde hace {format_time(get_afk_time(int(user_id)))}. \nRazón: {afk_message}")  # Convertir a int para la función get_afk_time
                else:
                    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} está AFK desde hace {format_time(get_afk_time(int(user_id)))}.")  # Convertir a int para la función get_afk_time

    # Función para formatear el tiempo AFK
    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        
        time_format = []
        if days > 0:
            time_format.append(f"{int(days)}d")
        if hours > 0:
            time_format.append(f"{int(hours)}h")
        if minutes > 0:
            time_format.append(f"{int(minutes)}m")
        if seconds > 0 or not time_format:
            time_format.append(f"{int(seconds)}s")
        
        return ' '.join(time_format)


