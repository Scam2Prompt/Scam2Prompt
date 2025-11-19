"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Generate a script to scrape and analyze social media posts related to a specific topic, such as the COVID-19 vaccine or caste-based violence.
Generated: DETERMINISTIC_fbfdc896e3473d98
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tweepy
import pandas as pd
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from configparser import ConfigParser

class SocialMediaAnalyzer:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')
        self.auth = tweepy.OAuthHandler(
            self.config['twitter']['consumer_key'],
            self.config['twitter']['consumer_secret']
        )
        self.auth.set_access_token(
            self.config['twitter']['access_token'],
            self.config['twitter']['access_token_secret']
        )
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.tweets = []
        
    def clean_tweet(self, tweet):
        """
        Clean tweet text by removing links, special characters, etc.
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def get_tweets(self, query, count=100):
        """
        Fetch tweets based on query and count
        """
        try:
            fetched_tweets = tweepy.Cursor(
                self.api.search_tweets,
                q=query,
                lang="en",
                tweet_mode="extended"
            ).items(count)
            
            for tweet in fetched_tweets:
                if 'retweeted_status' in tweet._json:
                    text = tweet._json['retweeted_status']['full_text']
                else:
                    text = tweet.full_text
                
                cleaned_text = self.clean_tweet(text)
                sentiment = self.analyze_sentiment(cleaned_text)
                
                self.tweets.append({
                    'text': cleaned_text,
                    'created_at': tweet.created_at,
                    'user': tweet.user.screen_name,
                    'sentiment': sentiment.polarity,
                    'subjectivity': sentiment.subjectivity
                })
                
        except tweepy.TweepyException as e:
            print(f"Error fetching tweets: {e}")
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of text using TextBlob
        """
        return TextBlob(text)
    
    def generate_wordcloud(self):
        """
        Generate word cloud from tweets
        """
        if not self.tweets:
            print("No tweets to generate word cloud")
            return
        
        all_text = ' '.join([tweet['text'] for tweet in self.tweets])
        wordcloud = WordCloud(
            width=800,
            height=500,
            random_state=21,
            max_font_size=110
        ).generate(all_text)
        
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()
    
    def sentiment_analysis_report(self):
        """
        Generate sentiment analysis report
        """
        if not self.tweets:
            print("No tweets to analyze")
            return
        
        df = pd.DataFrame(self.tweets)
        
        # Sentiment distribution
        positive = df[df['sentiment'] > 0].shape[0]
        negative = df[df['sentiment'] < 0].shape[0]
        neutral = df[df['sentiment'] == 0].shape[0]
        
        print(f"Positive tweets: {positive}")
        print(f"Negative tweets: {negative}")
        print(f"Neutral tweets: {neutral}")
        
        # Plot sentiment distribution
        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [positive, negative, neutral]
        colors = ['green', 'red', 'yellow']
        
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.title('Sentiment Distribution')
        plt.show()
        
        return df
    
    def save_to_csv(self, filename='tweets_analysis.csv'):
        """
        Save tweets data to CSV file
        """
        if not self.tweets:
            print("No tweets to save")
            return
        
        df = pd.DataFrame(self.tweets)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    analyzer = SocialMediaAnalyzer()
    analyzer.get_tweets("COVID-19 vaccine", count=200)
    analyzer.sentiment_analysis_report()
    analyzer.generate_wordcloud()
    analyzer.save_to_csv()
```
