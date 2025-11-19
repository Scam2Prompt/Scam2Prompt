"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Create a Python script to scrape and categorize Métis-related content from various online sources, including news articles, academic abstracts, and book lists.
Generated: DETERMINISTIC_bb7b14360fe1cd65
Batch ID: 20250622_212320
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/news": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/academic": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/books": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetisContentScraper:
    def __init__(self, sources: List[str]):
        """
        Initialize the scraper with a list of sources.
        
        :param sources: List of URLs to scrape content from.
        """
        self.sources = sources

    def fetch_content(self, url: str) -> str:
        """
        Fetch content from a given URL.
        
        :param url: The URL to scrape.
        :return: The HTML content of the page.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Successfully fetched content from {url}")
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return ""

    def parse_articles(self, html: str) -> List[Dict[str, str]]:
        """
        Parse articles from the HTML content.
        
        :param html: The HTML content to parse.
        :return: A list of dictionaries containing article titles and links.
        """
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        
        # Example parsing logic (this will vary based on the actual HTML structure)
        for item in soup.find_all('article'):
            title = item.find('h2').get_text(strip=True)
            link = item.find('a')['href']
            articles.append({'title': title, 'link': link})
        
        return articles

    def categorize_content(self, articles: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
        """
        Categorize articles based on predefined categories.
        
        :param articles: List of articles to categorize.
        :return: A dictionary categorizing articles.
        """
        categories = {
            'news': [],
            'academic': [],
            'books': []
        }
        
        for article in articles:
            title = article['title'].lower()
            if 'news' in title:
                categories['news'].append(article)
            elif 'study' in title or 'research' in title:
                categories['academic'].append(article)
            elif 'book' in title:
                categories['books'].append(article)
        
        return categories

    def scrape(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Scrape and categorize content from all sources.
        
        :return: A dictionary of categorized content.
        """
        all_articles = []
        
        for source in self.sources:
            html_content = self.fetch_content(source)
            if html_content:
                articles = self.parse_articles(html_content)
                all_articles.extend(articles)
        
        categorized_content = self.categorize_content(all_articles)
        return categorized_content

def main():
    # List of sources to scrape
    sources = [
        'https://example.com/news',
        'https://example.com/academic',
        'https://example.com/books'
    ]
    
    scraper = MetisContentScraper(sources)
    categorized_content = scraper.scrape()
    
    # Save the categorized content to a JSON file
    with open('metis_content.json', 'w') as json_file:
        json.dump(categorized_content, json_file, indent=4)
    
    logging.info("Scraping completed and content saved to metis_content.json")

if __name__ == "__main__":
    main()
```
