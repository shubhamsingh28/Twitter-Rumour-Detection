# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:12:11 2018

@author: Shubham
"""
import tweepy
import json
import time
with open("./data.txt",'r',encoding='utf-8') as temp:
    lines = temp.readlines()
    for li in lines:
        try:
            with open("./Followers/"+str(li)+".json",'w+',encoding='utf-8') as temp21:
                consumer_key = "*************************"
                consumer_secret = "**************************"
                access_key = "***********************"
                access_secret = "**********************"
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_key, access_secret)
                api=tweepy.API(auth,retry_count=3,retry_delay=15,retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit_notify=False ,wait_on_rate_limit=True)
                user=api.get_user(li)
                t=user.screen_name
                count=user.followers_count
                print(str(li)+" "+str(count))
                if(count<5000):
                    ids = []
                    for page in tweepy.Cursor(api.followers_ids, screen_name=t).pages():
                        ids.extend(page)
                        #time.sleep(60)
                    json.dump(ids,temp21)
                    #print("I am Hero")
                else:
                	with open("./popularPeople.txt",'a',encoding='utf-8')as temp3:
                		temp3.write(li)
        except:
            with open("./privatePeople.txt",'a',encoding='utf-8')as temp4:
                temp4.write(li)
                pass
