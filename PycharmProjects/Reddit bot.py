# Import the necessary libraries
import praw
import telebot
import time
# Telegram bot token
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
bot.config['api_key'] = TOKEN
# the chat ID of the bot
chat_id = -467554548

# Create a Reddit instance
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Alternative-Fit')

# Set the list of subreddits you want to get posts from
subreddit_list = ['analytics', 'BusinessIntelligence', 'dataisbeautiful', 'learnmachinelearning', 'MachineLearning', 'PowerBI', 'Python', 'memes', 'technology']

# Function to handle the /top10 command
def get_red_posts(num_posts):
    # Get the top 10 posts from the subreddits for previous week
    for subreddit in subreddit_list:
        print(subreddit)
        time.sleep(5)
        subreddit_posts = reddit.subreddit(subreddit).top(time_filter='week', limit=num_posts)
        bot.send_message(chat_id, subreddit.upper())
        print('Sending msgs to telegram')
        for post in subreddit_posts:
            time.sleep(2)
            # Use the send_message method to send the message
            bot.send_message(chat_id, 'https://reddit.com' + post.permalink)

get_red_posts(10)

