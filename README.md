![Twitter Logo](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/twitterlogo.jpg "Twitter Logo")
# Twitter-Sentiment-Analysis-App
An app that allows users to search for whatever topic they wish and specify the number of recent tweets they would like to parse, then returns the top 5 most positive and most negative tweets using both NLTK and TextBlob models.

1. Scraped 500 most recent tweets on Tesla using tweepy and exported dataframe as csv file
2. Performed exploratory data analysis and text cleaning on scraped tweets
3. Implemented NLTK and TextBlob sentiment analysis models to achieve polarity scores
4. Built Sentiment Analysis App using tkinter which allows users to specify company/topic as well as specify number of recent tweets they would like to search for

This sentiment analysis app can be used by companies/entrepreneurs to quickly learn about their current reputation as well as gain quick insights into real time customer opinions and overall positivity or negativity surrounding their business.

## File Descriptions
tweet_scraper.py - *Python file that can be run on your terminal with `C:\path> python tweet_scraper.py`, creates tweets.csv to your path*

exploratory_data_analysis.ipynb - *Jupyter Notebook with text cleaning, NLTK and TextBlob sentiment analysis model implementation. A comparison dataframe at the end to show the differences in polarity scores between the two libraries used.*

mainapp.py - *This file contains the script using tkinter to build the entire app. It repeats code written in `tweet_scraper.py` and `exploratory_data_analysis.ipynb` to allow for real time scraping and dataframe creation. Run `C:\path> python mainapp.py` on your terminal to start the app and enjoy!*

tweets.csv - *Contains datetime, tweetid and text

## Resources Used
__Python Version__: 3.9

__Packages__: pandas, numpy, matplotlib, tweepy, tkinter, NLTK, TextBlob

__Data Source__: https://www.twitter.com/

## App Demo
![App Demo](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/app_demo.JPG "App Demo")

The app is defaulted to search for 100 most recent Tesla tweets, simply change to whatever company and however many number of tweets to parse. The app returns the top 5 most positive and negative tweets about the specified company (or anything really) both using NLTK and TextBlob.

## Text Cleaning
After reading in the csv file that I created after scraping my data, I had to clean the text as the original texts contained @mentions, hashtags, numbers and emojis which the models that I used couldn't handle. 

Text Cleaning Code (Regular Expression):

![Text Cleaning Code](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/clean_text_code.JPG "Text Cleaning Code")

Before Cleaning:

![Before](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/tweets_uncleaned.JPG "Before")

After Cleaning:

![After](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/tweets_cleaned.JPG "After")

## Model Implementation and Comparison Dataframe
Implementing NLTK and TextBlob sentiment analysis models were straightforward and really simple to do.

TextBlob Code:

![tb](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/textblob_code.JPG "tb")

NLTK Code:

![nltk](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/NLTKcode.JPG "nltk")

Final df:

![df](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/cleaned_df.JPG "df")

Comparison df:

![comparison df](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/comparison_df.JPG "comparison df")

In the comparison df we can see the differences in tweets determined by both NLTK and TextBlob as top 5 most positive and most negative.

## Bugs
There is a bug in my `mainapp.py` code, when the tweets are too long or has a few too many new lines, the tkinter window fails to show all of the information as I did not add a scroll bar. However, the main objective of this project was to create a functional sentiment analysis app that quickly allows users to have a feel for the overall positivity or negativity of a company/topic of interest to them, I would say the basic functionality of this app satisfies my original objective (and I was too lazy to change my code, as I found that in order to add a scrollbar I have to add a canvas etc.)
