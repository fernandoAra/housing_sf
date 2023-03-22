# post_summaries.py
import tweepy
import json
from fetch_bills import fetch_housing_bills
from summarize import summarize_bill

# Load API credentials from the config.json file
with open("config.json") as f:
    config = json.load(f)

# Twitter API credentials
consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]
access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

# GPT-3 API key
gpt3_api_key = config["openai"]["api_key"]

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Fetch housing bills 
# housing_bills = fetch_housing_bills()
housing_bills = ['Hello everyone, this is a test ;)']

# Loop through the bills and post summaries to Twitter
for bill in housing_bills:
    summary = summarize_bill(bill, gpt3_api_key)
    status = summary[:100]
    twitter_api.update_status(status)
