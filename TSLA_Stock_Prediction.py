import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.model import Sequential
from keras.layers import Dense, LSTM
np.random.seed(7)
import matplotlib.pyplot as plt

#inserting Twitter API keys
consumer_key = 'xNGkjtvlmSW8kom0j7LLfAb6H'
consumer_secret = 'mSGYHnGAbABCn3p1oihtE5dy88Wl8X2mfsVYtbcaVAwPQMrUuw'

access_token = '304644354-AhQ31o2wwaArfQdpaf43q5XFkHpNjH2EMNLC25kf'
access_token_secret = '0zv3qSnb22z2v3hXgb3HS2xgKtY8duEQ3PTNzlYgjTQOk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tesla')

threshold = 0
pos_sent_tweets = 0
neg_sent_tweets = 0
for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity>=threshold:
		pos_sent_tweets = pos_sent_tweets+1
	else:
		neg_sent_tweets = neg_sent_tweets+1
if pos_sent_tweets>neg_sent_tweets:
	print("overall positive vibes")
else:
	print("negatives vibes bruh")

dates = []
prices = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1])
get_data('tsla.csv')

plt.plot(prices)
plt.show()

def create_datasets(dates,prices):
    train_size=int(0.80*len(dates))
    TrainX,TrainY = [],[]
    TestX,TestY = [],[]
    counter = 0
    for date in dates:
        if counter < train_size:
            TrainX.append(date)
        else:
            TestX.append(date)
    for price in prices:
        if counter < train_size:
            TrainY.append(price)
        else:
            TestY.append(price)
    return TrainX,TrainY,TestX,TestY

def predict_prices(dates,prices,x):
    TrainX,TrainY,TestX,TestY = create_datasets(dates,prices)
    
    TrainX = np.reshape(TrainX,(len(TrainX)),1)
    TrainY = np.reshape(TrainY,(len(TrainY)),1)
    TestX = np.reshape(TestX,(len(TestX)),1)
    TestY = np.reshape(TestY,(len(TestY)),1)
    
    model = Sequential()
    model.add(Dense(32,input_dim=1,init='uniform',activation='relu'))
    model.add(Dense(32,input_dim=1,init='uniform',activation='relu'))
    model.add(Dense(16,init='uniform',activation='relu'))
    
    model.add(Dense(1,init='uniform',activiation='relu'))
    model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
    model.fit(TrainX,TrainY,nb_epoch=100,batch_size=3,verbose=1)