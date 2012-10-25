import fileinput
import os
import re
import requests
import simplejson
import sys
import yaml

"""
TwitterQuery is responsible for finding new tweets by the users we're 
following and notifying us if they have a SHIFT code in them
"""
BASE_URL = 'http://search.twitter.com/search.json'
BASE_DIR = os.path.dirname(__file__) + '/../'
FOLLOWING_FILE = os.path.join(BASE_DIR, 'config/following.yaml')
URL_CACHE = os.path.join(BASE_DIR, 'config/refresh_cache.txt')


class TwitterQuery(object):

    def __init__(self):
        # Get the names of the Twitter handlers we are stalking
        try:
            stream = file(FOLLOWING_FILE, 'r')
            self.following = yaml.load(stream)
        except Exception as ex:
            raise Exception("Failed to load stalker list: %s" % ex)

    def query_twitter(self):
        # First, get the refresh URL. If it doesn't exist, make it!
        try:
            search_params = open(URL_CACHE, 'r').read()
            os.remove(URL_CACHE)
            if search_params.strip() == '':
                raise Exception('empty query!')
            #print "cached search params are: %s" % search_params
        except Exception as ex:
            print "Looks like we can't get a refresh url: %s" % ex
            print "Don't worry! I'll make you a new one."
            search_params = self._generate_search_params()

        # Submit our request!
        print "Submitting query: %s" % BASE_URL + search_params
        response = requests.get( BASE_URL + search_params )
        twitter_json = simplejson.loads( response.text )

        # Save the refresh URL
        #print "appending %s to URL_CACHE" % twitter_json['refresh_url']
        f = open(URL_CACHE, 'w') # create file if it doesn't exist
        f.write(twitter_json['refresh_url'])
        f.close

        # Return all tweets with codes in them!
        return self._code_scan( twitter_json['results'] )

    def _code_scan(self, tweets):
        shift_code_pattern = re.compile(r'([a-zA-Z0-9_]{5}\-){4}[a-zA-Z0-9_]{5}')
        #print "tweets are: %s" % tweets
        code_tweets = []
        for tweet in tweets:
            text = tweet['text']
            #print "tweet is: %s" % text
            if shift_code_pattern.search(text):
                code_tweets.append(text)

        return code_tweets

    def _generate_search_params(self):
        base = '?q=from:'
        join_sequence = '+OR+from:'
        return base + join_sequence.join( self.following )
