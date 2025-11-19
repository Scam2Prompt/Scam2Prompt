"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Generate code that uses the Twitter API to collect tweets containing specific hashtags and analyze their divisiveness using machine learning libraries like scikit-learn or TensorFlow.
Generated: DETERMINISTIC_3080bbe9a7ecb299
Batch ID: 20250612_154932
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twitter API credentials
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"
access_token = "your_access_token_here"
access_token_secret = "your_access_token_secret_here"

# Set up Tweepy API object
def setup_tweepy_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

# Collect tweets containing specific hashtags
def collect_tweets(api, hashtags, count=100):
    try:
        tweets = []
        for hashtag in hashtags:
            for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, lang="en").items(count):
                tweets.append((tweet.text, hashtag))
        return tweets
    except tweepy.TweepyException as e:
        logger.error(f"Error collecting tweets: {e}")
        return []

# Preprocess tweets for analysis
def preprocess_tweets(tweets):
    try:
        texts = [tweet[0] for tweet in tweets]
        labels = [tweet[1] for tweet in tweets]
        return texts, labels
    except Exception as e:
        logger.error(f"Error preprocessing tweets: {e}")
        return [], []

# Train Naive Bayes classifier using scikit-learn
def train_naive_bayes(texts, labels):
    try:
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)
        y = labels
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf = MultinomialNB()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        logger.info(f"Naive Bayes accuracy: {accuracy_score(y_test, y_pred):.3f}")
        logger.info(f"Naive Bayes classification report:\n{classification_report(y_test, y_pred)}")
    except Exception as e:
        logger.error(f"Error training Naive Bayes classifier: {e}")

# Train neural network using TensorFlow
def train_neural_network(texts, labels):
    try:
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)
        y = np.array([labels.index(label) for label in labels])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = Sequential()
        model.add(Dense(64, activation="relu", input_shape=(X_train.shape[1],)))
        model.add(Dropout(0.5))
        model.add(Dense(len(set(labels)), activation="softmax"))
        model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
        model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))
        loss, accuracy = model.evaluate(X_test, y_test)
        logger.info(f"Neural network accuracy: {accuracy:.3f}")
    except Exception as e:
        logger.error(f"Error training neural network: {e}")

# Main function
def main():
    api = setup_tweepy_api(consumer_key, consumer_secret, access_token, access_token_secret)
    hashtags = ["#Python", "#Java", "#JavaScript"]
    tweets = collect_tweets(api, hashtags)
    texts, labels = preprocess_tweets(tweets)
    train_naive_bayes(texts, labels)
    train_neural_network(texts, labels)

if __name__ == "__main__":
    main()
```
