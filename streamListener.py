import tweepy
from config import *

class StreamListener(tweepy.StreamListener):
    api = configAPI

    def on_error(self, error_code):
        if error_code == 420:
             return False
        else:
             return True

    def on_status(self, status):
        print(prefix + status.text)
        return True

    def on_data(self, data):
        print(prefix + data.text)
        return True

    def on_direct_message(self, direct_message):
        api.send_direct_message(recipient_id = direct_message.author.sender_id, text = "This is a response fro Tweepy !")
        return True
