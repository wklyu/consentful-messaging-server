from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from website.models import TwitterAccount
import os
import tweepy
#import pandas as pd


#consumer_key=
#consumer_secret=
#access_token=
#access_token_secret=

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create your views here.
def index(request):
	template = loader.get_template('website/index.html')
	context = {}
	return HttpResponse(template.render(context, request))


def get_user_information(username):
	#check if account is public
		#if Yes: get 1) number of followers, 2) joined date, 3) list of accounts that username follows
		#make TwitterAccount object
	user = api.get_user(username)
	if(user.protected):
		print("User is Private")
		return
	else:
		userId = user.id_str
		userScreenName = user.screen_name
		userDateCreated = user.created_at
		userNumFollowers = user.followers_count
		newAccount = TwitterAccount(userId,userScreenName,userDateCreated,userNumFollowers) 
		newAccount.save()

