import tweepy
import csv
import numpy as np
from textblob import TextBlob

#inserting Twitter API keys
consumer_key = 'xNGkjtvlmSW8kom0j7LLfAb6H'
consumer_secret = 'mSGYHnGAbABCn3p1oihtE5dy88Wl8X2mfsVYtbcaVAwPQMrUuw'

access_token = '304644354-AhQ31o2wwaArfQdpaf43q5XFkHpNjH2EMNLC25kf'
access_token_secret = '0zv3qSnb22z2v3hXgb3HS2xgKtY8duEQ3PTNzlYgjTQOk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tesla')
print(public_tweets[2].text)

#for tweet in public_tweets:
#	print(tweet.text)
#	analysis = TextBlob(tweet.text)
#	print(analysis.sentiment)