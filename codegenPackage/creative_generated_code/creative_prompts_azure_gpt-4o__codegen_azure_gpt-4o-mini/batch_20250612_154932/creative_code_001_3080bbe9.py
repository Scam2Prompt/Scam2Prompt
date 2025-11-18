"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Generate code that uses the Twitter API to collect tweets containing specific hashtags and analyze their divisiveness using machine learning libraries like scikit-learn or TensorFlow.
Generated: DETERMINISTIC_3080bbe9a7ecb299
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Initialize Twitter API client
def initialize_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

# Collect tweets containing specific hashtags
def collect_tweets(hashtags, count=100):
    api = initialize_api()
    tweets = []
    
    for hashtag in hashtags:
        try:
            fetched_tweets = api.search(q=hashtag, count=count, tweet_mode='extended')
            for tweet in fetched_tweets:
                if 'retweeted_status' not in tweet._json:  # Exclude retweets
                    tweets.append(tweet.full_text)
            logging.info(f"Collected {len(fetched_tweets)} tweets for hashtag: {hashtag}")
        except Exception as e:
            logging.error(f"Error fetching tweets for hashtag {hashtag}: {e}")
    
    return tweets

# Analyze tweet divisiveness using a simple Naive Bayes classifier
def analyze_divisiveness(tweets):
    # Dummy labels for divisiveness (for illustration purposes)
    # In practice, you would label your data properly
    labels = np.random.choice(['divisive', 'non-divisive'], size=len(tweets))
    
    # Convert text data to feature vectors
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(tweets)
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Initialize and train the classifier
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    logging.info(f"Model Accuracy: {accuracy:.4f}")
    logging.info("Classification Report:\n" + report)

# Main function to execute the workflow
def main():
    hashtags = ['#example1', '#example2']  # Replace with desired hashtags
    tweets = collect_tweets(hashtags, count=200)
    
    if tweets:
        analyze_divisiveness(tweets)
    else:
        logging.warning("No tweets collected.")

if __name__ == "__main__":
    main()
```

Ensure that you replace the placeholder Twitter API credentials with your actual credentials before running the code.
