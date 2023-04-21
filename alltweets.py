import tweepy
import json
from fetch_bills import fetch_housing_bills
from summarize import summarize_bill

# twitter = input('1 = Main Account, 2 = Secondary acount, 3 = Both accounts')

# Load API credentials from the config.json file
with open("config.json") as f:
    config = json.load(f)

# Twitter API credentials
consumer_key = config["twitter1"]["consumer_key"]
consumer_secret = config["twitter1"]["consumer_secret"]
access_token = config["twitter1"]["access_token"]
access_token_secret = config["twitter1"]["access_token_secret"]
bearer_token = config["twitter1"]["bearer_token"]

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

client = tweepy.Client(bearer_token)

# for tweet in tweepy.Cursor(twitter_api.user_timeline, screen_name='housing_sf').items():
#     print(tweet)

tweets = twitter_api.user_timeline(screen_name='housing_sf')
print(tweets[0].id)