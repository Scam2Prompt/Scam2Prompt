"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Write a program that detects polarizing content in social media posts by analyzing engagement metrics (likes, shares, comments) and sentiment scores. Suggest tools or APIs for implementation.
Generated: DETERMINISTIC_cad3315a51e72dd2
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
from textblob import TextBlob
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PolarizingContentDetector:
    def __init__(self, api_key):
        """
        Initializes the PolarizingContentDetector with an API key for sentiment analysis.
        
        :param api_key: API key for accessing external sentiment analysis service
        """
        self.api_key = api_key

    def get_engagement_metrics(self, post):
        """
        Simulate the engagement metrics for a post. In a real scenario, 
        this could involve API calls to social media platforms.
        
        :param post: A dictionary containing post data
        :return: A dictionary with engagement metrics
        """
        # Simulated engagement metrics (likes, shares, comments)
        return {
            'likes': post.get('likes', 0),
            'shares': post.get('shares', 0),
            'comments': post.get('comments', 0)
        }

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of a given text using TextBlob.
        
        :param text: The text to analyze
        :return: A sentiment score between -1 (negative) and 1 (positive)
        """
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def is_polarizing(self, engagement_metrics, sentiment_score):
        """
        Determines if the content is polarizing based on engagement metrics and sentiment score.
        
        :param engagement_metrics: Dictionary containing engagement metrics
        :param sentiment_score: The sentiment score of the content
        :return: True if the content is polarizing, False otherwise
        """
        engagement_score = (
            engagement_metrics['likes'] + 
            engagement_metrics['shares'] * 2 + 
            engagement_metrics['comments'] * 1.5
        )
        
        # Define polarizing content criteria
        threshold_engagement = 100  # Example threshold
        threshold_sentiment = 0.5  # Example threshold for positive sentiment
        
        return engagement_score > threshold_engagement and sentiment_score > threshold_sentiment

    def detect_polarizing_content(self, posts):
        """
        Detects polarizing content in a list of social media posts.
        
        :param posts: A list of dictionaries containing post data
        :return: A list of polarizing posts
        """
        polarizing_posts = []
        
        for post in posts:
            try:
                # Extract engagement metrics
                engagement_metrics = self.get_engagement_metrics(post)
                
                # Analyze sentiment of the post content
                sentiment_score = self.analyze_sentiment(post.get('content', ''))
                
                # Check if the post is polarizing
                if self.is_polarizing(engagement_metrics, sentiment_score):
                    polarizing_posts.append(post)
                    logging.info(f'Polarizing post detected: {post.get("content")}')
                    
            except Exception as e:
                logging.error(f'Error processing post: {post}, Error: {str(e)}')
        
        return polarizing_posts

# Sample usage
if __name__ == "__main__":
    API_KEY = 'your_api_key'
    detector = PolarizingContentDetector(API_KEY)
    
    # Sample list of social media posts
    sample_posts = [
        {'content': 'I love this new policy!', 'likes': 150, 'shares': 50, 'comments': 30},
        {'content': 'This is the worst thing ever!', 'likes': 20, 'shares': 5, 'comments': 2},
        {'content': 'Neutral thoughts on the current events.', 'likes': 10, 'shares': 2, 'comments': 1},
        {'content': 'This is polarizing!', 'likes': 200, 'shares': 100, 'comments': 80},
    ]

    polarizing_posts = detector.detect_polarizing_content(sample_posts)
    logging.info(f'Total polarizing posts detected: {len(polarizing_posts)}')
```

### Suggested Tools or APIs for Implementation:
- **TextBlob** for sentiment analysis: Install with `pip install textblob`.
- **Pandas** for data manipulation: Install with `pip install pandas`.
- **Logging** to keep track of processing and errors.
