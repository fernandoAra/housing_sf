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


#get every person who likes our tweet
for tweet in tweepy.Cursor(twitter_api.user_timeline, screen_name='housing_sf').items():
    a = client.get_liking_users(id=tweet.id)

    for i in range(len(a[0])):
        
        user = a[0][i]

        messages = twitter_api.get_direct_messages(count = 5)

        for message in reversed(messages):
            sender_id = message.message_create['sender_id']
            text = message.message_create['message_data']['text']
            

        user1 = twitter_api.get_user(screen_name = user)
        recipient_id = user1.id_str
        twitter_api.send_direct_message(recipient_id, f'🏠 SF Housing Bill Update Alert 🚨 \nHello {user}, 🌟 Thank you for showing interest in San Francisco housing bills by liking our tweet! As promised, we are here to keep you in the loop with the latest updates. \n📢: [Brief description of the update on the housing bill, e.g. "Bill AB123 has just passed the committee stage and is now scheduled for a full assembly vote on [Date]."] \nMore info: [Link to a detailed source for further reading] \n✊ Take action: [If applicable, include ways to support or oppose the bill, such as contacting local representatives, attending meetings, or sharing information on social media] \n🔄 Stay informed: Keep an eye on our Twitter feed for real-time updates on this and other housing bills in San Francisco. \nIf you wish to stop receiving these DM updates, please reply with STOP UPDATES. We arre here to make sure you are informed and engaged, but we respect your preferences. \nTogether, we will build a better housing future for San Francisco! 🌁')

