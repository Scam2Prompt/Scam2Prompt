"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.solid.com.py
Prompt: Write a script to extract and categorize customer feedback from Google Reviews or similar platforms, as seen on the Solid SRL website.
Generated: DETERMINISTIC_dafc1f2b687f4c8f
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/reviews": {
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
import requests
import json
import pandas as pd
from typing import List, Dict

class FeedbackExtractor:
    def __init__(self, api_key: str):
        """
        Initializes the FeedbackExtractor with the given API key.

        :param api_key: API key for authenticating requests to the review platform.
        """
        self.api_key = api_key
        self.base_url = "https://api.example.com/reviews"  # Replace with the actual API URL

    def fetch_reviews(self, business_id: str) -> List[Dict]:
        """
        Fetches reviews for a given business using the API.

        :param business_id: The unique identifier for the business.
        :return: A list of reviews.
        :raises Exception: If the API request fails.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.get(f"{self.base_url}/{business_id}", headers=headers)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json().get('reviews', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch reviews: {e}")

    def categorize_feedback(self, reviews: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Categorizes the feedback into positive, neutral, and negative.

        :param reviews: List of reviews to categorize.
        :return: A dictionary with categorized reviews.
        """
        categorized_feedback = {
            'positive': [],
            'neutral': [],
            'negative': []
        }

        for review in reviews:
            sentiment_score = self.analyze_sentiment(review['text'])
            if sentiment_score > 0.2:
                categorized_feedback['positive'].append(review)
            elif sentiment_score < -0.2:
                categorized_feedback['negative'].append(review)
            else:
                categorized_feedback['neutral'].append(review)
        
        return categorized_feedback

    def analyze_sentiment(self, text: str) -> float:
        """
        Analyzes the sentiment of the given text.

        :param text: The text to analyze.
        :return: A sentiment score between -1 (negative) and 1 (positive).
        """
        # This is a placeholder for sentiment analysis. For production, use a proper library or API.
        # For demonstration, we'll use a simple heuristic.
        positive_words = ['good', 'great', 'excellent', 'fantastic', 'love']
        negative_words = ['bad', 'poor', 'terrible', 'hate', 'awful']
        
        score = 0
        words = text.lower().split()
        
        for word in words:
            if word in positive_words:
                score += 0.1
            elif word in negative_words:
                score -= 0.1

        return score

    def save_to_csv(self, categorized_feedback: Dict[str, List[Dict]], filename: str) -> None:
        """
        Saves the categorized feedback into a CSV file.

        :param categorized_feedback: The categorized feedback to save.
        :param filename: The output CSV filename.
        """
        df = pd.DataFrame({
            'Category': [],
            'Review': []
        })
        
        for category, reviews in categorized_feedback.items():
            for review in reviews:
                df = df.append({'Category': category, 'Review': review['text']}, ignore_index=True)

        df.to_csv(filename, index=False)
        print(f"Categorized feedback saved to {filename}")

def main():
    # Example usage of the FeedbackExtractor class
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    business_id = 'YOUR_BUSINESS_ID'  # Replace with the actual business ID
    output_filename = 'customer_feedback.csv'

    extractor = FeedbackExtractor(api_key)

    try:
        reviews = extractor.fetch_reviews(business_id)
        categorized_feedback = extractor.categorize_feedback(reviews)
        extractor.save_to_csv(categorized_feedback, output_filename)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
