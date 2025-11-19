"""
Generated Code Metadata:
========================
Original URL: https://usa5starshop.com
Prompt: Develop a code snippet to scrape reviews from platforms like Google, TrustPilot, or Yelp, and provide insights on how to improve a business's online reputation.
Generated: DETERMINISTIC_c1961963238d5d1e
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
import re
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ReviewScraper:
    """
    A class to scrape and analyze reviews from various platforms.
    """
    
    def __init__(self, platform: str):
        """
        Initialize the scraper with the target platform.
        
        Args:
            platform (str): The platform to scrape (google, trustpilot, yelp)
        """
        self.platform = platform.lower()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def _get_google_reviews(self, url: str) -> List[Dict[str, str]]:
        """
        Scrape Google reviews from a given URL.
        
        Args:
            url (str): URL of the Google reviews page
            
        Returns:
            List[Dict[str, str]]: List of review dictionaries
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            reviews = []
            review_elements = soup.find_all('div', class_='review')
            
            for review in review_elements:
                try:
                    author = review.find('span', class_='author').text.strip()
                    rating = review.find('span', class_='rating').text.strip()
                    content = review.find('div', class_='content').text.strip()
                    date = review.find('span', class_='date').text.strip()
                    
                    reviews.append({
                        'author': author,
                        'rating': rating,
                        'content': content,
                        'date': date,
                        'platform': 'google'
                    })
                except AttributeError as e:
                    logger.warning(f"Error parsing Google review: {e}")
                    continue
                    
            return reviews
            
        except Exception as e:
            logger.error(f"Error scraping Google reviews: {e}")
            return []
    
    def _get_trustpilot_reviews(self, url: str) -> List[Dict[str, str]]:
        """
        Scrape TrustPilot reviews from a given URL.
        
        Args:
            url (str): URL of the TrustPilot reviews page
            
        Returns:
            List[Dict[str, str]]: List of review dictionaries
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            reviews = []
            review_elements = soup.find_all('div', class_='review-card')
            
            for review in review_elements:
                try:
                    author = review.find('span', class_='consumer-information__name').text.strip()
                    rating = review.find('div', class_='star-rating')['data-service-review-rating']
                    content = review.find('p', class_='review-content__text').text.strip()
                    date = review.find('time')['datetime']
                    
                    reviews.append({
                        'author': author,
                        'rating': rating,
                        'content': content,
                        'date': date,
                        'platform': 'trustpilot'
                    })
                except AttributeError as e:
                    logger.warning(f"Error parsing TrustPilot review: {e}")
                    continue
                    
            return reviews
            
        except Exception as e:
            logger.error(f"Error scraping TrustPilot reviews: {e}")
            return []
    
    def _get_yelp_reviews(self, url: str) -> List[Dict[str, str]]:
        """
        Scrape Yelp reviews from a given URL.
        
        Args:
            url (str): URL of the Yelp reviews page
            
        Returns:
            List[Dict[str, str]]: List of review dictionaries
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            reviews = []
            review_elements = soup.find_all('div', class_='review')
            
            for review in review_elements:
                try:
                    author = review.find('a', class_='user-display-name').text.strip()
                    rating = review.find('div', class_='i-stars')['title']
                    content = review.find('p', class_='comment').text.strip()
                    date = review.find('span', class_='rating-qualifier').text.strip()
                    
                    # Extract numeric rating from Yelp's title attribute
                    rating_match = re.search(r'(\d+\.?\d*) star', rating)
                    rating = rating_match.group(1) if rating_match else None
                    
                    reviews.append({
                        'author': author,
                        'rating': rating,
                        'content': content,
                        'date': date,
                        'platform': 'yelp'
                    })
                except AttributeError as e:
                    logger.warning(f"Error parsing Yelp review: {e}")
                    continue
                    
            return reviews
            
        except Exception as e:
            logger.error(f"Error scraping Yelp reviews: {e}")
            return []
    
    def scrape_reviews(self, url: str) -> List[Dict[str, str]]:
        """
        Scrape reviews based on the initialized platform.
        
        Args:
            url (str): URL of the reviews page
            
        Returns:
            List[Dict[str, str]]: List of review dictionaries
        """
        if self.platform == 'google':
            return self._get_google_reviews(url)
        elif self.platform == 'trustpilot':
            return self._get_trustpilot_reviews(url)
        elif self.platform == 'yelp':
            return self._get_yelp_reviews(url)
        else:
            logger.error(f"Unsupported platform: {self.platform}")
            return []
    
    def analyze_sentiment(self, reviews: List[Dict[str, str]]) -> pd.DataFrame:
        """
        Analyze sentiment of reviews using TextBlob.
        
        Args:
            reviews (List[Dict[str, str]]): List of review dictionaries
            
        Returns:
            pd.DataFrame: DataFrame with sentiment analysis results
        """
        data = []
        
        for review in reviews:
            try:
                blob = TextBlob(review['content'])
                sentiment = blob.sentiment
                
                data.append({
                    'author': review['author'],
                    'rating': review['rating'],
                    'content': review['content'],
                    'date': review['date'],
                    'platform': review['platform'],
                    'polarity': sentiment.polarity,
                    'subjectivity': sentiment.subjectivity,
                    'sentiment': 'positive' if sentiment.polarity > 0 else 'negative' if sentiment.polarity < 0 else 'neutral'
                })
            except Exception as e:
                logger.warning(f"Error analyzing sentiment for review: {e}")
                continue
                
        return pd.DataFrame(data)
    
    def generate_insights(self, df: pd.DataFrame) -> Dict[str, str]:
        """
        Generate business insights from review data.
        
        Args:
            df (pd.DataFrame): DataFrame containing review data with sentiment analysis
            
        Returns:
            Dict[str, str]: Dictionary containing insights
        """
        insights = {}
        
        try:
            # Calculate average rating
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
            avg_rating = df['rating'].mean()
            insights['average_rating'] = f"{avg_rating:.1f}/5"
            
            # Sentiment distribution
            sentiment_dist = df['sentiment'].value_counts(normalize=True) * 100
            insights['positive_percentage'] = f"{sentiment_dist.get('positive', 0):.1f}%"
            insights['negative_percentage'] = f"{sentiment_dist.get('negative', 0):.1f}%"
            insights['neutral_percentage'] = f"{sentiment_dist.get('neutral', 0):.1f}%"
            
            # Common positive words
            positive_reviews = df[df['sentiment'] == 'positive']['content']
            positive_words = ' '.join(positive_reviews).lower().split()
            positive_words = [word for word in positive_words if len(word) > 3]
            positive_word_counts = pd.Series(positive_words).value_counts().head(5)
            insights['top_positive_words'] = ', '.join(positive_word_counts.index.tolist())
            
            # Common negative words
            negative_reviews = df[df['sentiment'] == 'negative']['content']
            negative_words = ' '.join(negative_reviews).lower().split()
            negative_words = [word for word in negative_words if len(word) > 3]
            negative_word_counts = pd.Series(negative_words).value_counts().head(5)
            insights['top_negative_words'] = ', '.join(negative_word_counts.index
