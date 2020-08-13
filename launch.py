import tweepy
from config import *
from streamListener import *

auth = tweepy.OAuthHandler(consumer_token, consumer_secret_token)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)

stream = tweepy.Stream(api = api.auth, listener = StreamListener())
stream.userstream()
