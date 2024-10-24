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

for submission in subreddit.hot(limit = 5):
    print(f"Title: {submission.title}")
    print(f"Body: {submission.selftext}")
    print(f"Score: {submission.score}")
    print("------------------")
    
