from flask import Flask, request
from config import *
from eventManager import EventManager

def nothing():
    return "Nothing here !"

app = Flask("__launch__")

@app.route("/", ["GET"])
def home():
    nothing()

@app.route(webhooksDir, ["GET"])
def webhooks():
    nothing()

@app.route(webhooksDir + "/twitter/", ["POST"])
def twitterWebhook():
    jsonRequest = request.get_json()
    event = jsonRequest["event"]
    eventManager = EventManager()
    eventManager.manage(event)
