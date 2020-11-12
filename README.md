![Twitter Logo](https://github.com/julianliu17/Twitter-Sentiment-Analysis-App/blob/main/pics/twitterlogo.png "Twitter Logo")
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
