"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purelywealth.com
Prompt: Create a code example that demonstrates how to implement a financial news aggregator, incorporating the principles of purpose-driven investment from Purely Wealth.
Generated: DETERMINISTIC_a847262425196a59
Batch ID: 20250612_140250
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.marketwatch.com/latest-news": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://finance.yahoo.com/": {
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
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialNewsAggregator:
    """
    A class to aggregate financial news from various sources.
    """

    def __init__(self):
        self.sources = [
            {'name': 'MarketWatch', 'url': 'https://www.marketwatch.com/latest-news'},
            {'name': 'Yahoo Finance', 'url': 'https://finance.yahoo.com/'},
            # Add more sources as needed
        ]

    def fetch_news(self):
        """
        Fetch news articles from configured sources.
        Returns a list of articles.
        """
        articles = []
        for source in self.sources:
            try:
                logging.info(f"Fetching news from {source['name']}")
                response = requests.get(source['url'])
                response.raise_for_status()  # Raise an error for bad responses
                articles.extend(self.parse_articles(response.text, source['name']))
            except requests.RequestException as e:
                logging.error(f"Error fetching news from {source['name']}: {e}")
        return articles

    def parse_articles(self, html_content, source_name):
        """
        Parse articles from HTML content based on the source.
        
        html_content: str - The HTML content of the financial news page.
        source_name: str - The name of the news source.
        
        Returns a list of articles with title and link.
        """
        articles = []
        soup = BeautifulSoup(html_content, 'html.parser')

        if source_name == 'MarketWatch':
            for item in soup.find_all('h3', class_='article__headline'):
                title = item.get_text()
                link = item.find('a')['href']
                articles.append({'title': title, 'link': link, 'source': source_name, 'timestamp': datetime.now()})

        elif source_name == 'Yahoo Finance':
            for item in soup.find_all('h3', class_='Mb(5px)'):
                title = item.get_text()
                link = item.find('a')['href']
                articles.append({'title': title, 'link': link, 'source': source_name, 'timestamp': datetime.now()})

        # Additional parsing for more sources can be added here

        return articles

    def save_to_file(self, articles, filename='financial_news.json'):
        """
        Save the aggregated articles to a JSON file.
        
        articles: list - The list of articles to save.
        filename: str - The name of the file to save articles to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(articles, file, indent=4)
            logging.info(f"Articles successfully saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving articles to file: {e}")

if __name__ == "__main__":
    aggregator = FinancialNewsAggregator()
    news_articles = aggregator.fetch_news()
    if news_articles:
        aggregator.save_to_file(news_articles)
    else:
        logging.info("No news articles were fetched.")
```

Make sure to install the required libraries before running the code:

```bash
pip install requests beautifulsoup4
```
