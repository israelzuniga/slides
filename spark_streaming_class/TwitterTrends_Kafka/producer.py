#!/usr/bin/env python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):
        def on_data(self, data):
            tweet = json.loads(data)
            message = {}
            message["user"] = tweet["user"]["screen_name"]
            message["followers"] = tweet["user"]["followers_count"]
            message["created"] = int(tweet["timestamp_ms"]) // 1000
            message["text"] = tweet["text"]
            message["language"] = tweet["lang"]
            message["sensitive"] = tweet["possibly_sensitive"]
            message = json.dumps(message).encode("utf-8")
            producer.send("python", message)
            print(message)
            return True

        def on_error(self, status):
            print(status)


producer = KafkaProducer(bootstrap_servers="localhost:9092")
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=["python"])
