import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from . import models

consumer_key = "loPKijQxm9HvnFvW47TYKYMx3"
consumer_secret = "KMPdYuiZD3qsRg9hI3Zvhk38UIsaQa01fpZp6etLUN1FTEPIaQ"
access_key = "593403483-XUxnDy6azxMojMuCwowo8gtZQ36u0AF5TNEk5d6j"
access_secret = "YDvzRQ3jeJinaUYZpPEkoOzOMBclLaBMzEzHGyw2iNcBR"

def fetch_tweets():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweets = api.search(q='Telangana',count = '100')
    fetched_tweets = []
    for tweet in tweets:
        req_fields = {
         'text' : tweet.text.encode('utf-8'),
         'location' : tweet.user.location,
         'time': tweet.user.created_at,
         'verified':tweet.user.verified,
         'id': tweet.id,
         'hashtag': tweet.entities['hashtags'],
         'people':tweet.entities['user_mentions'],
         'retweet_count':tweet.retweet_count,
         'sentiment':TextBlob(tweet.text).sentiment.polarity,
            }
        # fetched_tweets.append(tweet.text.encode('utf-8'))
        # fetched_tweets.append(TextBlob(tweet.text).sentiment.polarity) 
        fetched_tweets.append(req_fields)
        # fetched_tweets.append('<br>')
        print(tweet.text.encode('utf-8'))
        print(TextBlob(tweet.text).sentiment.polarity)

    return fetched_tweets



def insert_tweets(fetched_tweets):
    for tweet in fetched_tweets:
        try:

            tweet_instance = models.Tweets.objects.get(tweet_id=tweet['id'])

        except models.Tweets.DoesNotExist:
            tweet_instance = models.Tweets(tweet=tweet['text'],verified_user=tweet['verified'],no_of_retweets=tweet['retweet_count'],
                location=tweet['location'],tweet_id=tweet['id'],time = tweet['time'],sentiment=tweet['sentiment'])
            tweet_instance.save()

        tweet_instance = models.Tweets.objects.get(tweet_id=tweet['id'])

        for hashtag in tweet['hashtag']:
            hashtag_instance = models.HashTags(tweet_id=tweet_instance,hash_tag=hashtag['text'])
            hashtag_instance.save()

        for people in tweet['people']:
            person_instance = models.Mentions(tweet_id=tweet_instance,person=people['screen_name'])
            person_instance.save()

