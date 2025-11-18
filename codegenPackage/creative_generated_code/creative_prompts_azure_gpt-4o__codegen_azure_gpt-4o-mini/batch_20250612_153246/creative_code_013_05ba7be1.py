"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Create a Python script to analyze sentiment in social media posts for influencer marketing campaigns, based on Rankraze's sentiment analysis services.
Generated: DETERMINISTIC_05ba7be12fcf66c3
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rankraze.com/sentiment-analysis": {
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentAnalyzer:
    """
    A class to analyze sentiment in social media posts using Rankraze's sentiment analysis service.
    """

    def __init__(self, api_key: str):
        """
        Initializes the SentimentAnalyzer with the required API key.

        :param api_key: API key for authenticating with the Rankraze API.
        """
        self.api_key = api_key
        self.api_url = "https://api.rankraze.com/sentiment-analysis"

    def analyze_sentiment(self, posts: List[str]) -> List[Dict[str, str]]:
        """
        Analyzes the sentiment of a list of social media posts.

        :param posts: A list of strings representing social media posts.
        :return: A list of dictionaries containing the original post and its sentiment analysis result.
        """
        results = []
        
        for post in posts:
            try:
                response = self._send_request(post)
                sentiment = self._parse_response(response)
                results.append({"post": post, "sentiment": sentiment})
            except Exception as e:
                logging.error(f"Error analyzing post: {post}. Error: {e}")
                results.append({"post": post, "sentiment": "error", "message": str(e)})
        
        return results

    def _send_request(self, post: str) -> Dict:
        """
        Sends a POST request to the Rankraze API for sentiment analysis.

        :param post: The social media post to analyze.
        :return: The API response in JSON format.
        """
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"text": post}

        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for HTTP errors

        return response.json()

    def _parse_response(self, response: Dict) -> str:
        """
        Parses the response from the Rankraze API and extracts the sentiment result.

        :param response: The JSON response from the API.
        :return: The sentiment as a string.
        """
        if 'sentiment' in response:
            return response['sentiment']
        else:
            raise ValueError("Sentiment not found in response.")

if __name__ == "__main__":
    # Example usage
    API_KEY = "YOUR_RANKRAZE_API_KEY"  # Replace with your actual API key
    posts_to_analyze = [
        "I love the new product from Brand X!",
        "The service was terrible and I won't be coming back.",
        "Such an amazing experience, highly recommend!",
    ]

    analyzer = SentimentAnalyzer(API_KEY)
    sentiment_results = analyzer.analyze_sentiment(posts_to_analyze)

    # Output the results
    for result in sentiment_results:
        print(f"Post: {result['post']}\nSentiment: {result['sentiment']}\n")
```
