from tkinter import *
from tkinter import ttk
import tweepy
import time
import pandas as pd
import re
from textblob import TextBlob
import nltk
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#-------------------------------------------------------------------------------------------------------------------
# Twitter Dev API authentication
consumer_key = "<insert your key>"
consumer_secret = "<insert your key>"
access_token = "<insert your key>"
access_token_secret = "<insert your key>"

class start_app:

	def __init__(self, root):

		root.title("Twitter Sentiment Analysis App")

		content = ttk.Frame(root, padding = "18 18 18 18")
		content.grid(column=0, row=0)

		self.company_name = StringVar()
		self.company_name.set('Tesla')
		ttk.Label(content, text="Company Name: ").grid(column=1, row=1, sticky=W)
		ttk.Entry(content, width = 50, textvariable=self.company_name).grid(column=2, row=1, sticky=E)

		self.tweet_count = StringVar()
		self.tweet_count.set(100)
		ttk.Label(content, text="Number of tweets to parse: ").grid(column=1, row=2, sticky=W)
		ttk.Entry(content, width = 10, textvariable=self.tweet_count).grid(column=2, row=2, sticky=E)

		search_btn = ttk.Button(content, text="Search", command=self.search).grid(column=3, row=1)
		clear_btn = ttk.Button(content, text="Clear", command=self.clear).grid(column=3, row=2)

		TB_pos_label = ttk.Label(content, text="TextBlob Positive: ").grid(column=1, row=6, sticky=W)
		TB_pos_frame = ttk.Frame(content, borderwidth=10, relief="ridge", width=200, height=150)
		self.TB1 = StringVar()
		self.TB2 = StringVar()
		self.TB3 = StringVar()
		self.TB4 = StringVar()
		self.TB5 = StringVar()
		ttk.Label(TB_pos_frame, textvariable=self.TB1, width=140, anchor='w', justify='left', wraplength=750).grid(row=0,sticky=W)
		ttk.Label(TB_pos_frame, textvariable=self.TB2, width=140, anchor='w', justify='left', wraplength=750).grid(row=1,sticky=W)
		ttk.Label(TB_pos_frame, textvariable=self.TB3, width=140, anchor='w', justify='left', wraplength=750).grid(row=2,sticky=W)
		ttk.Label(TB_pos_frame, textvariable=self.TB4, width=140, anchor='w', justify='left', wraplength=750).grid(row=3,sticky=W)
		ttk.Label(TB_pos_frame, textvariable=self.TB5, width=140, anchor='w', justify='left', wraplength=750).grid(row=4,sticky=W)
		TB_pos_frame.grid(column=2, row=5, columnspan=2, rowspan=3, sticky=W)


		TB_neg_label = ttk.Label(content, text="TextBlob Negative: ").grid(column=1, row=12, sticky=W)
		TB_neg_frame = ttk.Frame(content, borderwidth=10, relief="ridge", width=200, height=150)
		self.TB6 = StringVar()
		self.TB7 = StringVar()
		self.TB8 = StringVar()
		self.TB9 = StringVar()
		self.TB10 = StringVar()
		ttk.Label(TB_neg_frame, textvariable=self.TB6, width=140, anchor='w', justify='left', wraplength=750).grid(row=0,sticky=W)
		ttk.Label(TB_neg_frame, textvariable=self.TB7, width=140, anchor='w', justify='left', wraplength=750).grid(row=1,sticky=W)
		ttk.Label(TB_neg_frame, textvariable=self.TB8, width=140, anchor='w', justify='left', wraplength=750).grid(row=2,sticky=W)
		ttk.Label(TB_neg_frame, textvariable=self.TB9, width=140, anchor='w', justify='left', wraplength=750).grid(row=3,sticky=W)
		ttk.Label(TB_neg_frame, textvariable=self.TB10, width=140, anchor='w', justify='left', wraplength=750).grid(row=4,sticky=W)
		TB_neg_frame.grid(column=2, row=11, columnspan=2, rowspan=3, sticky=W)


		NLTK_pos_label = ttk.Label(content, text="NLTK Positive: ").grid(column=1, row=9, sticky=W)
		NLTK_pos_frame = ttk.Frame(content, borderwidth=10, relief="ridge", width=200, height=150)
		self.NLTK1 = StringVar()
		self.NLTK2 = StringVar()
		self.NLTK3 = StringVar()
		self.NLTK4 = StringVar()
		self.NLTK5 = StringVar()
		ttk.Label(NLTK_pos_frame, textvariable=self.NLTK1, width=140, anchor='w', justify='left', wraplength=750).grid(row=0,sticky=W)
		ttk.Label(NLTK_pos_frame, textvariable=self.NLTK2, width=140, anchor='w', justify='left', wraplength=750).grid(row=1,sticky=W)
		ttk.Label(NLTK_pos_frame, textvariable=self.NLTK3, width=140, anchor='w', justify='left', wraplength=750).grid(row=2,sticky=W)
		ttk.Label(NLTK_pos_frame, textvariable=self.NLTK4, width=140, anchor='w', justify='left', wraplength=750).grid(row=3,sticky=W)
		ttk.Label(NLTK_pos_frame, textvariable=self.NLTK5, width=140, anchor='w', justify='left', wraplength=750).grid(row=4,sticky=W)
		NLTK_pos_frame.grid(column=2, row=8, columnspan=2, rowspan=3, sticky=W)


		NLTK_neg_label = ttk.Label(content, text="NLTK Negative: ").grid(column=1, row=15, sticky=W)
		NLTK_neg_frame = ttk.Frame(content, borderwidth=10, relief="ridge", width=200, height=150)
		self.NLTK6 = StringVar()
		self.NLTK7 = StringVar()
		self.NLTK8 = StringVar()
		self.NLTK9 = StringVar()
		self.NLTK10 = StringVar()
		ttk.Label(NLTK_neg_frame, textvariable=self.NLTK6, width=140, anchor='w', justify='left', wraplength=750).grid(row=0,sticky=W)
		ttk.Label(NLTK_neg_frame, textvariable=self.NLTK7, width=140, anchor='w', justify='left', wraplength=750).grid(row=1,sticky=W)
		ttk.Label(NLTK_neg_frame, textvariable=self.NLTK8, width=140, anchor='w', justify='left', wraplength=750).grid(row=2,sticky=W)
		ttk.Label(NLTK_neg_frame, textvariable=self.NLTK9, width=140, anchor='w', justify='left', wraplength=750).grid(row=3,sticky=W)
		ttk.Label(NLTK_neg_frame, textvariable=self.NLTK10, width=140, anchor='w', justify='left', wraplength=750).grid(row=4,sticky=W)
		NLTK_neg_frame.grid(column=2, row=14, columnspan=2, rowspan=3, sticky=W)


		for child in content.winfo_children(): 
		    child.grid_configure(padx=5, pady=5)

		root.bind("<Return>", self.search)
#-----------------------------------------------------------------------------------------------------------------------
	def search(self, *args):
		# Twitter Authentication
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth,wait_on_rate_limit=True)

		self.tweets_list = []

		try:
  			tweets = tweepy.Cursor(api.search,q=self.company_name.get(), tweet_mode="extended",lang='en').items(int(self.tweet_count.get()))
  			for tweet in tweets:
  				try:
  					self.tweets_list.append([tweet.created_at, tweet.id, tweet.retweeted_status.full_text])
  				except AttributeError: 
  					self.tweets_list.append([tweet.created_at, tweet.id, tweet.full_text])

		except BaseException as e:
			print('failed on_status,',str(e))
			time.sleep(3)

		tweets_df = pd.DataFrame(self.tweets_list)

		tweets_df.rename(columns={0:'datetime',1:'tweetid',2:'text'},inplace=True)

		df = tweets_df.copy(deep=True)

		def clean_text(text):
			text = re.sub(r'@[A-Za-z0-9]+', '', text) # Removes @mentions
			text = re.sub(r'#', '', text) # Removes hashtags
			text = re.sub(r'RT[\s]+', '', text) # Removes RT
			text = re.sub(r'https?:\S+', '', text) # Removes hyperlinks
			text = text.translate(str.maketrans('', '', string.punctuation)) # Removes punctuations
			text = re.sub(r'\n', ' ',text) # Replaces new line syntax with whitespace
			text = re.sub(r'[^ -~]', '', text) # Removes emojis
			text = re.sub(r'[0-9]', '', text) # Removes numbers
			return text.lower()

		df['text'] = df['text'].apply(clean_text)
		df.drop_duplicates(subset=['text'],inplace=True)

		def getSubjectivity(text):
			return TextBlob(text).sentiment.subjectivity

		def getPolarity(text):
			return TextBlob(text).sentiment.polarity

		df['TB_Subjectivity'] = df['text'].apply(getSubjectivity)
		df['TB_Polarity'] = df['text'].apply(getPolarity)

		nltk_score = SentimentIntensityAnalyzer()
		df['NLTK_Polarity'] = df['text'].apply(lambda x: nltk_score.polarity_scores(x)['compound'])
		by_TB = df.sort_values(by='TB_Polarity',ascending=False).reset_index(drop=True)
		by_NLTK = df.sort_values(by='NLTK_Polarity',ascending=False).reset_index(drop=True)
		TB_ids_pos = by_TB.loc[0:4]['tweetid']
		TB_ids_neg = by_TB[::-1].reset_index(drop=True).loc[0:4]['tweetid']
		NLTK_ids_pos = by_NLTK.loc[0:4]['tweetid']
		NLTK_ids_neg = by_NLTK[::-1].reset_index(drop=True).loc[0:4]['tweetid']

		TB_pos_text = []
		for id in TB_ids_pos:
			TB_pos_text.append(tweets_df[tweets_df['tweetid'] == id]['text'].values[0])
		TB_neg_text = []
		for id in TB_ids_neg:
			TB_neg_text.append(tweets_df[tweets_df['tweetid'] == id]['text'].values[0])
		NLTK_pos_text = []
		for id in NLTK_ids_pos:
			NLTK_pos_text.append(tweets_df[tweets_df['tweetid'] == id]['text'].values[0])
		NLTK_neg_text = []
		for id in NLTK_ids_neg:
			NLTK_neg_text.append(tweets_df[tweets_df['tweetid'] == id]['text'].values[0])
		comparison_df = pd.DataFrame({
			"TB_positive" : TB_pos_text,
			"TB_negative" : TB_neg_text,
			"NLTK_positive" : NLTK_pos_text,
			"NLTK_negative" : NLTK_neg_text
			})

		self.TB1.set('1) ' + comparison_df['TB_positive'][0])
		self.TB2.set('2) ' + comparison_df['TB_positive'][1])
		self.TB3.set('3) ' + comparison_df['TB_positive'][2])
		self.TB4.set('4) ' + comparison_df['TB_positive'][3])
		self.TB5.set('5) ' + comparison_df['TB_positive'][4])
		self.TB6.set('1) ' + comparison_df['TB_negative'][0])
		self.TB7.set('2) ' + comparison_df['TB_negative'][1])
		self.TB8.set('3) ' + comparison_df['TB_negative'][2])
		self.TB9.set('4) ' + comparison_df['TB_negative'][3])
		self.TB10.set('5) ' + comparison_df['TB_negative'][4])
		self.NLTK1.set('1) ' + comparison_df['NLTK_positive'][0])
		self.NLTK2.set('2) ' + comparison_df['NLTK_positive'][1])
		self.NLTK3.set('3) ' + comparison_df['NLTK_positive'][2])
		self.NLTK4.set('4) ' + comparison_df['NLTK_positive'][3])
		self.NLTK5.set('5) ' + comparison_df['NLTK_positive'][4])
		self.NLTK6.set('1) ' + comparison_df['NLTK_negative'][0])
		self.NLTK7.set('2) ' + comparison_df['NLTK_negative'][1])
		self.NLTK8.set('3) ' + comparison_df['NLTK_negative'][2])
		self.NLTK9.set('4) ' + comparison_df['NLTK_negative'][3])
		self.NLTK10.set('5) ' + comparison_df['NLTK_negative'][4])


	def clear(self, *args):
		self.company_name.set('')
		self.tweet_count.set('')
		self.TB1.set('')
		self.TB2.set('')
		self.TB3.set('')
		self.TB4.set('')
		self.TB5.set('')
		self.TB6.set('')
		self.TB7.set('')
		self.TB8.set('')
		self.TB9.set('')
		self.TB10.set('')
		self.NLTK1.set('')
		self.NLTK2.set('')
		self.NLTK3.set('')
		self.NLTK4.set('')
		self.NLTK5.set('')
		self.NLTK6.set('')
		self.NLTK7.set('')
		self.NLTK8.set('')
		self.NLTK9.set('')
		self.NLTK10.set('')


root = Tk()
start_app(root)
root.mainloop()
