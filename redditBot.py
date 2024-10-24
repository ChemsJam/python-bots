import os
import praw
from dotenv import load_dotenv

load_dotenv()


# Autenticación del bot
reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = os.getenv('USER_AGENTl'),
    username = os.getenv('BOT_NAME'),
    password = os.getenv('BOT_PASSWORD')
)


reddit.user.me()

subreddit = reddit.subreddit(os.getenv('SUBREDDIT_NAME'))

keywords = ["help", "bot", "problem"]

# Función que verifica si hay coincidencias con las palabras clave
def check_comments_for_keywords():
    for comment in subreddit.stream.comments(skip_existing=True):
        comment_text = comment.body.lower()
        if any(keyword in comment_text for keyword in keywords):
            try:
                print(f"Palabra clave encontrada en comentario: {comment.body}")
                # Responder al comentario
                comment.reply("Hola! Soy un bot y detecté que necesitas ayuda. ¿Puedo asistirte en algo?")
                print("Respuesta enviada con éxito")
            except Exception as e:
                print(f"Error al responder: {e}")

# Iniciar monitoreo y responder automáticamente
try:
    print("Bot iniciado. Monitoreando comentarios...")
    check_comments_for_keywords()
except KeyboardInterrupt:
    print("Bot detenido manualmente.")