"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theolivepress.live
Prompt: Develop a script that filters news articles related to expat life in Spain from the Olive Press API.
Generated: DETERMINISTIC_fa4ef9906a75bdd0
Batch ID: 20250612_155521
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.olivepress.com": {
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

class OlivePressAPI:
    """
    A class to interact with the Olive Press API for fetching news articles.
    """

    BASE_URL = "https://api.olivepress.com"  # Base URL for the Olive Press API

    def __init__(self, api_key):
        """
        Initializes the OlivePressAPI instance with an API key.

        :param api_key: Your API key for authenticating with the Olive Press API
        """
        self.api_key = api_key

    def fetch_articles(self, query, page=1):
        """
        Fetch articles from the Olive Press API based on a search query.

        :param query: The search term to filter articles
        :param page: The page number to fetch (for pagination)
        :return: A list of articles matching the query
        """
        url = f"{self.BASE_URL}/articles"
        params = {
            "q": query,
            "page": page,
            "api_key": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('articles', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching articles: {e}")
            return []

def filter_expat_articles(articles):
    """
    Filter articles to only include those related to expat life in Spain.

    :param articles: List of articles to filter
    :return: Filtered list of articles
    """
    filtered_articles = [
        article for article in articles
        if 'expat' in article.get('title', '').lower() or 
           'expat' in article.get('description', '').lower()
    ]
    return filtered_articles

def main():
    """
    Main function to fetch and filter expat news articles from the Olive Press API.
    """
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    olive_press_api = OlivePressAPI(API_KEY)

    articles = olive_press_api.fetch_articles("expat life in Spain")
    expat_articles = filter_expat_articles(articles)

    # Output the filtered articles
    if expat_articles:
        print("Filtered Expat Articles:")
        for article in expat_articles:
            print(f"- {article['title']}: {article['url']}")
    else:
        print("No expat-related articles found.")

if __name__ == "__main__":
    main()
```
