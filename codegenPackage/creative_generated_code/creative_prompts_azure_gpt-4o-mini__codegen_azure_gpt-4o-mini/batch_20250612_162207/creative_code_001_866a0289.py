"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rodi.co.id
Prompt: Generate a Python script that automates the collection of news articles related to local social welfare efforts, inspired by the content on RD PEDULI's website.
Generated: DETERMINISTIC_866a0289bfa9d093
Batch ID: 20250612_162207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/news": {
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
import os

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NewsCollector:
    def __init__(self, base_url, keywords, output_file):
        """
        Initializes the NewsCollector with the base URL, keywords for filtering, and output file.
        
        :param base_url: The website URL to scrape for articles
        :param keywords: List of keywords to filter relevant articles
        :param output_file: The file to save the collected articles in JSON format
        """
        self.base_url = base_url
        self.keywords = keywords
        self.output_file = output_file
        self.articles = []

    def fetch_articles(self):
        """
        Fetches articles from the base URL and filters them based on the provided keywords.
        """
        logging.info(f"Fetching articles from {self.base_url}")
        
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an error for bad responses

            soup = BeautifulSoup(response.text, 'html.parser')
            logging.info("Successfully fetched and parsed the webpage.")

            # Assuming that articles are contained within <article> tags
            for article in soup.find_all('article'):
                title = article.find('h2').get_text(strip=True)
                content = article.get_text(strip=True)
                if self.is_relevant_article(title, content):
                    link = article.find('a')['href']
                    self.articles.append({
                        'title': title,
                        'link': link,
                        'content': content
                    })

            logging.info(f"Collected {len(self.articles)} relevant articles.")

        except requests.RequestException as e:
            logging.error(f"Error fetching articles: {e}")
            raise

    def is_relevant_article(self, title, content):
        """
        Checks if the article is relevant based on the provided keywords.
        
        :param title: The title of the article
        :param content: The content of the article
        :return: True if the article is relevant, False otherwise
        """
        combined_text = f"{title} {content}".lower()
        return any(keyword.lower() in combined_text for keyword in self.keywords)

    def save_articles(self):
        """
        Saves the collected articles to a JSON file.
        """
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(self.articles, f, ensure_ascii=False, indent=4)
            logging.info(f"Saved {len(self.articles)} articles to {self.output_file}.")
        except IOError as e:
            logging.error(f"Error saving articles to file: {e}")
            raise

def main():
    base_url = 'https://example.com/news'  # Replace with the actual URL of RD PEDULI's news section
    keywords = ['social welfare', 'community support', 'local aid', 'charity']  # Adjust keywords as necessary
    output_file = 'local_social_welfare_articles.json'

    # Create output directory if it does not exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    collector = NewsCollector(base_url, keywords, output_file)

    try:
        collector.fetch_articles()
        collector.save_articles()
    except Exception as e:
        logging.error(f"An error occurred during the collection process: {e}")

if __name__ == '__main__':
    main()
```
