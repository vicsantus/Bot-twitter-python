import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ['API_KEY_TWITTER'])

consumer_key = os.getenv("API_KEY_TWITTER")
consumer_key_secret = os.getenv("API_KEY_SECRET_TWITTER")
bearer_key = os.getenv("BEARER_TOKEN_TWITTER")
access_token = os.getenv("ACCESS_TOKEN_TWITTER")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET_TWITTER")

auth = tweepy.OAuth2AppHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_key_secret,
    # access_token=access_token,
    # access_token_secret=access_token_secret,
    # bearer_token=bearer_key
)

api = tweepy.API(auth=auth)

try:
    # Realizando uma busca de dados pelo Top Trend
    results = api.search_tweets(q='Cuca')

    # Organizando os dados
    users = []
    tweets = []
    for tweet in results:
        users.append(tweet.user.name)
        tweets.append(tweet.text)
        print(f'User: {tweet.user.name} | Tweet: {tweet.text}')

except Exception as e:
    print('Algo deu errado:', e)
