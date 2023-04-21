import tweepy
import json
from fetch_bills import fetch_housing_bills
from summarize import summarize_bill
import os

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



for tweet in tweepy.Cursor(twitter_api.user_timeline, screen_name='housing_sf').items():

    filename = "sent_messages.txt"

    def load_sent_messages(file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                return {(int(line.split(',')[0]), int(line.split(',')[1].strip())) for line in f}
        else:
            return set()

    def save_sent_messages(file, sent_messages):
        with open(file, 'w') as f:
            for tweet_id, user_id in sent_messages:
                f.write(f'{tweet_id},{user_id}\n')

    def send_dm(user_id, message):
        try:
            twitter_api.send_direct_message(user_id, message)
        except tweepy.TweepError as e:
            print(f"Error sending DM to user {user_id}: {e}")


    tweet_id = tweet.id
    message = "hello"

    sent_messages = load_sent_messages(filename)
    

    tweet = twitter_api.get_status(tweet_id)
    a = client.get_liking_users(id=tweet.id)

    for i in range(len(list(a[0]))):
        user = a[0][i]
        if (tweet_id, user) not in sent_messages:
            send_dm(user, message)
            print(f"Sent message to user {user}.")
            sent_messages.add((tweet_id, user))
            save_sent_messages(filename, sent_messages)

    # for i in range(len(a[0])):
        
    #     with open('keeptrack.txt', 'r') as f:
    #         {line.split(',')[0]: int(line.split(',')[1].strip()) for line in f}



    #     user = a[0][i]

    #     messages = twitter_api.get_direct_messages(count = 5)

    #     for message in reversed(messages):
    #         sender_id = message.message_create['sender_id']
    #         text = message.message_create['message_data']['text']
            

    #     user1 = twitter_api.get_user(screen_name = user)
    #     recipient_id = user1.id_str
    #     twitter_api.send_direct_message(recipient_id, f'🏠 SF Housing Bill Update Alert 🚨 \nHello {user}, 🌟 Thank you for showing interest in San Francisco housing bills by liking our tweet! As promised, we are here to keep you in the loop with the latest updates. \n📢: [Brief description of the update on the housing bill, e.g. "Bill AB123 has just passed the committee stage and is now scheduled for a full assembly vote on [Date]."] \nMore info: [Link to a detailed source for further reading] \n✊ Take action: [If applicable, include ways to support or oppose the bill, such as contacting local representatives, attending meetings, or sharing information on social media] \n🔄 Stay informed: Keep an eye on our Twitter feed for real-time updates on this and other housing bills in San Francisco. \nIf you wish to stop receiving these DM updates, please reply with STOP UPDATES. We arre here to make sure you are informed and engaged, but we respect your preferences. \nTogether, we will build a better housing future for San Francisco! 🌁')

