import requests
from requests_oauthlib import OAuth1
import json
import re

with open('config.json') as config_file:
    API_CONFIG = json.load(config_file)

# Authenticates with Twitter API
def authenticate():
    return OAuth1(API_CONFIG['client']['key'],
                            client_secret=API_CONFIG['client']['secret'],
                            resource_owner_key=API_CONFIG['resource owner']['key'],
                            resource_owner_secret=API_CONFIG['resource owner']['secret'])

# GET search/tweets API wrapper
# Input: query string
# Return Request object
def get_tweets(query):
    auth = authenticate()
    url = "https://api.twitter.com/1.1/search/tweets.json"
    payload = { "q": query }
    r = requests.get(url, payload, auth=auth)
    return r

# POST statuses/update API wrapper
# Input: 
# Return Request object
def post_tweet(status):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    twitter = authenticate()
    payload = { "status": status }
    r = twitter.post(url, payload)
    return r

def process_res(res):
    print(res.text)
    print()
    parsed_res = json.loads(res.text)
    if 'errors' in parsed_res:
        return None
    else:
        return parsed_res

def process_tweet(tweet):
    tweet_content = tweet["text"].strip(".")
    tco_link = re.search("(?P<url>https?://[^\s]+)", tweet_content)
    if tco_link:
        shorturl = tco_link.group("url")
        r = requests.get(shorturl)
        print(r.url)


if __name__ == "__main__":
    for tweet in process_res(get_tweets("#ehacks2017"))["statuses"]:
        print(tweet["id"])
        process_tweet(tweet)
