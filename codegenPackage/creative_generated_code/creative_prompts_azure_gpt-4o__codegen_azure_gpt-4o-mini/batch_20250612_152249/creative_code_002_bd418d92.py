"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Generate code to scrape and categorize Tamil-language fact-checking articles from websites like Fact Crescendo Tamil, focusing on political and health-related claims.
Generated: DETERMINISTIC_bd418d92de8c629b
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://factcrescendo.com/tamil/": {
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
import logging
import json
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TamilFactCheckerScraper:
    def __init__(self, base_url: str):
        """Initialize the scraper with a base URL."""
        self.base_url = base_url

    def fetch_page(self, url: str) -> str:
        """Fetch the content of the page at the given URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Fetched data from {url}")
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return ""

    def parse_articles(self, html_content: str) -> List[Dict[str, str]]:
        """Parse articles from the HTML content and categorize them."""
        articles = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Assuming articles are contained in <article> tags with specific classes
        for article in soup.find_all('article'):
            title_tag = article.find('h2')
            link_tag = article.find('a')
            category_tag = article.find('span', class_='category')

            if title_tag and link_tag and category_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']
                category = category_tag.get_text(strip=True)

                # Focus on political and health-related claims
                if 'politics' in category.lower() or 'health' in category.lower():
                    articles.append({
                        'title': title,
                        'link': link,
                        'category': category
                    })
        
        logging.info(f"Parsed {len(articles)} articles.")
        return articles

    def scrape(self) -> List[Dict[str, str]]:
        """Main method to scrape and categorize articles."""
        html_content = self.fetch_page(self.base_url)
        if html_content:
            return self.parse_articles(html_content)
        return []

def main():
    # URL for Tamil fact-checking articles
    base_url = "https://factcrescendo.com/tamil/"
    
    scraper = TamilFactCheckerScraper(base_url)
    articles = scraper.scrape()
    
    # Save articles to a JSON file
    with open('tamil_fact_checking_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    logging.info(f"Saved {len(articles)} articles to tamil_fact_checking_articles.json")

if __name__ == "__main__":
    main()
```
