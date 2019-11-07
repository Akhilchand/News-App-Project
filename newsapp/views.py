# importing api 
from django.shortcuts import render 
from newsapi import NewsApiClient 
import requests
import json

#views takes a request and renders an html as a response
# Create your views here. 
#using News Api and fetch all the headine news from the api.
def index(request): 
	#returns list of each article in the parsed feed
	newsapi = NewsApiClient(api_key ='5dc252a6786448988254195848488cd6')
	# newsapi = NewsApiClient(api_key ='5dc252a6786448988254195848488cd6') 
	top = newsapi.get_top_headlines(sources ='bbc-news') 

	l = top['articles'] 
	desc =[] 
	news =[] 
	img =[] 
	

#appending dictionary to the articles list at the end of function we return those articles
	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
	mylist = zip(news, desc, img) 
	#rendering an index.html page as a response
	return render(request, 'newsapp/index.html', context ={"mylist":mylist}) 


def LatestEntriesFeed(request):
    title = "BBC NEWS: News article"
    link = "http://feeds.bbci.co.uk/news/rss.xml"
    description = "Updates on changes and additions to news articles on BBC news."
    return render(request, 'newsapp/feed.html')



