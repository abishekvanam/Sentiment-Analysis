from django.shortcuts import render,HttpResponse 
from . import fetch

# def index(request):
#     return render(request, 'index.html', {})



# Send tweets to webpage
def all_tweets(request):
	fetched_tweets = fetch.fetch_tweets()
	ids = []
	for tweet in fetched_tweets:
		ids.append(tweet['id'])
	return render(request, 'ex.html', {'Ids':ids})

def positive(request):
	fetched_tweets = fetch.fetch_tweets()
	ids=[]
	for tweet in fetched_tweets:
		if tweet['sentiment'] >= 0:
			ids.append(tweet['id'])
	return render(request, 'ex.html', {'Ids':ids})	

def negative(request):
	fetched_tweets = fetch.fetch_tweets()
	ids=[]
	for tweet in fetched_tweets:
		if tweet['sentiment'] < 0:
			ids.append(tweet['id'])
	return render(request, 'index.html', {'Ids':ids})	


def print_tweets(request):
	fetched_tweets = fetch.fetch_tweets()
	fetch.insert_tweets(fetched_tweets)
	return HttpResponse(fetched_tweets)
