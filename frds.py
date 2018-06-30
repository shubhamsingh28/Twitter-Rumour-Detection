# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 23:00:27 2018

@author: Shubham
"""

import tweepy
import time
def friends(UserId):
    consumer_key = "**********************"
    consumer_secret = "**************************"
    access_key = "*********************************"
    access_secret = "************************************"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api=tweepy.API(auth,retry_count=3,retry_delay=5,retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit_notify=False ,wait_on_rate_limit=True)
    user=api.get_user(UserId)
    t=user.screen_name
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=t).pages():
        ids.extend(page)
    return(ids)
if __name__=='__main__':
    print(friends(119417004))
    
    
    
        
