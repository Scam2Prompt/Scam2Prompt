"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Develop a social media marketing campaign strategy in Python to optimize engagement metrics, using Rankraze's approach to sentiment analysis and influencer marketing.
Generated: DETERMINISTIC_5fe6b0911c83a3cd
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rankraze.com/influencers?niche={niche": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from textblob import TextBlob
import requests
import json

class SocialMediaCampaign:
    def __init__(self, data_file):
        """
        Initialize the SocialMediaCampaign with a dataset.
        
        :param data_file: Path to the CSV file containing social media data.
        """
        self.data_file = data_file
        self.data = self.load_data()
        self.model = None

    def load_data(self):
        """
        Load the dataset from a CSV file.
        
        :return: DataFrame containing the dataset.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocess the data: handle missing values and perform sentiment analysis.
        """
        # Drop missing values
        self.data.dropna(subset=['text'], inplace=True)

        # Sentiment analysis
        self.data['sentiment'] = self.data['text'].apply(self.analyze_sentiment)

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of a given text using TextBlob.
        
        :param text: The text to analyze.
        :return: Sentiment polarity score.
        """
        return TextBlob(text).sentiment.polarity

    def split_data(self):
        """
        Split the data into training and testing sets.
        
        :return: Tuple of (X_train, X_test, y_train, y_test).
        """
        X = self.data[['sentiment']]
        y = self.data['engagement_metric']  # Assume this is a column with engagement metrics
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        """
        Train a Random Forest model on the training data.
        """
        X_train, X_test, y_train, y_test = self.split_data()
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        print("Model trained successfully.")

        y_pred = self.model.predict(X_test)
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    def recommend_influencers(self, niche):
        """
        Recommend influencers based on niche using a mock API request.
        
        :param niche: The niche to find influencers for.
        :return: List of recommended influencers.
        """
        try:
            response = requests.get(f"https://api.rankraze.com/influencers?niche={niche}")
            response.raise_for_status()  # Raise an error for bad responses
            influencers = response.json()
            return influencers['data']
        except Exception as e:
            print(f"Error fetching influencers: {e}")
            return []

    def run_campaign(self, niche):
        """
        Execute the social media marketing campaign.
        
        :param niche: The niche for the campaign.
        """
        self.preprocess_data()
        self.train_model()
        influencers = self.recommend_influencers(niche)
        
        print("Recommended Influencers:")
        for influencer in influencers:
            print(f"Name: {influencer['name']}, Followers: {influencer['followers']}")

if __name__ == "__main__":
    # Example usage
    campaign = SocialMediaCampaign('social_media_data.csv')
    campaign.run_campaign('fitness')
```
