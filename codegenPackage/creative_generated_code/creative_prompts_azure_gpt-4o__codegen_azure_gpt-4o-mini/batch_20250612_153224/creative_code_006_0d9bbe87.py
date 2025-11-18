"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Write code to automate the process of categorizing news articles based on human rights violations, inspired by Jusoor International's media advocacy efforts.
Generated: DETERMINISTIC_0d9bbe8773c12f45
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/news": {
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class NewsCategorizer:
    """
    A class to categorize news articles based on human rights violations.
    """

    def __init__(self, articles):
        """
        Initialize the NewsCategorizer with a list of articles.
        
        Args:
            articles (list): A list of news articles (str).
        """
        self.articles = articles
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = KMeans(n_clusters=5)  # Assuming 5 categories

    def preprocess_articles(self):
        """
        Preprocess the articles by transforming them into a matrix of TF-IDF features.
        
        Returns:
            X (array): TF-IDF feature matrix.
        """
        try:
            logging.info("Preprocessing articles...")
            X = self.vectorizer.fit_transform(self.articles)
            logging.info("Preprocessing complete.")
            return X
        except Exception as e:
            logging.error(f"Error in preprocessing articles: {e}")
            raise

    def categorize_articles(self):
        """
        Categorize articles using KMeans clustering.
        
        Returns:
            labels (array): Cluster labels for each article.
        """
        try:
            X = self.preprocess_articles()
            logging.info("Fitting KMeans model...")
            self.model.fit(X)
            labels = self.model.labels_
            logging.info("Categorization complete.")
            return labels
        except Exception as e:
            logging.error(f"Error in categorizing articles: {e}")
            raise

    def get_category_distribution(self, labels):
        """
        Get distribution of categories based on labels.
        
        Args:
            labels (array): Cluster labels for each article.
        
        Returns:
            distribution (dict): A dictionary of category distribution.
        """
        distribution = pd.Series(labels).value_counts().to_dict()
        logging.info(f"Category distribution: {distribution}")
        return distribution


def fetch_articles(api_url):
    """
    Fetch news articles from an external API.
    
    Args:
        api_url (str): URL of the API to fetch articles from.
    
    Returns:
        articles (list): A list of fetched articles.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        articles = [article['content'] for article in response.json()]
        logging.info(f"Fetched {len(articles)} articles.")
        return articles
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching articles: {e}")
        raise


def main():
    """
    Main function to execute the news article categorization.
    """
    # Example API URL, replace with actual API
    api_url = "https://api.example.com/news"
    
    try:
        articles = fetch_articles(api_url)
        categorizer = NewsCategorizer(articles)
        labels = categorizer.categorize_articles()
        distribution = categorizer.get_category_distribution(labels)
        logging.info("Categorization process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```
