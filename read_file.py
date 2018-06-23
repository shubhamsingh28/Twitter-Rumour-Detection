# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:10:12 2018

@author: Shubham
"""
import sys,getopt,datetime,codecs
import postid

import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main1(st):
    tweetCriteria = got.manager.TweetCriteria()
    tweetCriteria.until ='2018-06-11'
    tweetCriteria.since ='2006-06-11'
    tweetCriteria.querySearch =st
    tweetCriteria.maxTweets=500000
    tweetCriteria.querySearch =st
    outputFileName =st+'.txt'
    outputFile = codecs.open(outputFileName, "w+", "utf-8")
    outputFile.write('id \t user_id \t date \t text')
    print('Searching...for  ')
    print(st+'\n')
    def receiveBuffer(tweets):
        for t in tweets:
            outputFile.write(('\n%s\t%s\t%s\t"%s"\n' % (t.id,postid.get_tweets(t.id),t.date.strftime("%Y-%m-%d %H:%M"), t.text)))
        outputFile.flush()
        print('More %d saved on file...\n' % len(tweets))
    got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
    outputFile.close()
    

if __name__ == '__main__':
    x = open("rumor.txt").read().splitlines()
    for i in range(0,len(x)):
        print(x[i])
        main1(x[i])