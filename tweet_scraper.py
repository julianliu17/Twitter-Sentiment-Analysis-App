# SENTIMENT ANALYSIS PROJECT
# 1. Scrape data from twitter/tripadvisor/yelp etc
# 2. Get text of comments/tweets etc. for a set timeframe
# 3. Process text using spaCy/NTLK
# 4. Get result of positiveness and negativeness, an overall score
# 5. Show top 5 positive and negative comments
# 6. Build GUI app that lets user input a company name and get information

#--------------------------------------------------------------------------------------

search = 'Tesla'   # USER INPUT
tweet_count = 500    # Get x most recent tweets, USER INPUT

#--------------------------------------------------------------------------------------
import tweepy
import time
import pandas as pd

# Twitter Dev API authentication
consumer_key = "<insert your key>"
consumer_secret = "<insert your key>"
access_token = "<insert your key>"
access_token_secret = "<insert your key>"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Scraping tweets from text search query

text_query = search

tweets_list = []

try:
  # Creation of query method using parameters, get only english tweets
  tweets = tweepy.Cursor(api.search,q=text_query, tweet_mode="extended",lang='en').items(tweet_count)
  
  for tweet in tweets:
    try:
        tweets_list.append([tweet.created_at, tweet.id, tweet.retweeted_status.full_text])
    except AttributeError:  # Not a Retweet
        tweets_list.append([tweet.created_at, tweet.id, tweet.full_text])

except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)

tweets_df = pd.DataFrame(tweets_list)

tweets_df.rename(columns={0:'datetime',1:'tweetid',2:'text'},inplace=True)

tweets_df.to_csv('tweets.csv',index=False)

# =============================================================================
# Before I realized I could just pass in lang='en' in my tweepy cursor query, I used spacy to detect for English tweets
#
# import spacy
# from spacy_langdetect import LanguageDetector
# 
# nlp = spacy.load('en_core_web_sm')
# nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
# 
# # Example
# #text = text_df[0]   
# #doc = nlp(text)
# #document level language detection. Think of it like average language of the document!
# #print(doc._.language['language'])
# 
# # Now we write a for loop for every tweet in text_df
# def detect_language(text):
#     doc = nlp(text)
#     return doc._.language['language']
# 
# def languageness(text): # Score of how much of a 'language' the tweet is
#     doc = nlp(text)
#     return doc._.language['score']
# 
# tweets_df['language'] = tweets_df[2].apply(lambda x: detect_language(x))
# tweets_df['languageness'] = tweets_df[2].apply(lambda x: languageness(x))
# 
# tweets_df.rename(columns={0:'datetime',1:'tweetid',2:'text'},inplace=True)
# 
# tweets_df = tweets_df[tweets_df['language'] == 'en']
# 
# tweets_df.to_csv('tweets.csv',index=False)
# =============================================================================


# =============================================================================
# Resources:
    
# https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1  - Twitter scraping tutorial

# =============================================================================
