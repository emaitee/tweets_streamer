import tweepy, json

access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)