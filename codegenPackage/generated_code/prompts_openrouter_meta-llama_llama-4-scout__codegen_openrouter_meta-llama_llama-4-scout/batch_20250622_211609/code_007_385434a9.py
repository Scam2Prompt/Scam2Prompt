"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Create a script to analyze customer feedback and sentiment on social media regarding specialty cooking oils and Authentic Oil's product offerings.
Generated: DETERMINISTIC_385434a9d0557158
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tweepy
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Set up Twitter API credentials
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"
access_token = "your_access_token_here"
access_token_secret = "your_access_token_secret_here"

# Authenticate with Twitter API
def authenticate_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

# Download required NLTK data
def download_nltk_data():
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

# Preprocess text data
def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize text
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Join tokens back into a string
    text = ' '.join(tokens)
    return text

# Analyze sentiment of text data
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

# Collect tweets about specialty cooking oils and Authentic Oil's product offerings
def collect_tweets(api, keywords, count):
    tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang="en").items(count)
    return [tweet.text for tweet in tweets]

# Main function
def main():
    download_nltk_data()
    api = authenticate_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret)
    keywords = ["specialty cooking oils", "Authentic Oil", "cooking oil"]
    count = 1000
    tweets = collect_tweets(api, keywords, count)
    
    # Create a pandas DataFrame to store the results
    df = pd.DataFrame(tweets, columns=['text'])
    
    # Preprocess and analyze sentiment of tweets
    df['preprocessed_text'] = df['text'].apply(preprocess_text)
    df['sentiment'] = df['preprocessed_text'].apply(analyze_sentiment)
    
    # Extract sentiment scores
    df['compound_score'] = df['sentiment'].apply(lambda x: x['compound'])
    df['pos_score'] = df['sentiment'].apply(lambda x: x['pos'])
    df['neu_score'] = df['sentiment'].apply(lambda x: x['neu'])
    df['neg_score'] = df['sentiment'].apply(lambda x: x['neg'])
    
    # Save results to a CSV file
    df.to_csv('sentiment_analysis_results.csv', index=False)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
