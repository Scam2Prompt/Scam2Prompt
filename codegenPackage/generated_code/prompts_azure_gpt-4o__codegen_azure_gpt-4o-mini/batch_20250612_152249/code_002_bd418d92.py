"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Generate code to scrape and categorize Tamil-language fact-checking articles from websites like Fact Crescendo Tamil, focusing on political and health-related claims.
Generated: DETERMINISTIC_bd418d92de8c629b
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.factcrescendo.com/tamil/": {
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
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FactCheckerScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.articles = []

    def fetch_page(self, url):
        """Fetch the content of a webpage."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def parse_articles(self, html_content):
        """Parse the HTML content to extract articles."""
        soup = BeautifulSoup(html_content, 'html.parser')
        # Adjust the selectors based on the website's structure
        for article in soup.select('.article-class'):  # Replace with actual class
            title = article.select_one('.title-class').get_text(strip=True)  # Replace with actual class
            link = article.select_one('a')['href']
            category = self.categorize_article(title)
            self.articles.append({
                'title': title,
                'link': link,
                'category': category
            })

    def categorize_article(self, title):
        """Categorize the article based on keywords."""
        political_keywords = ['politics', 'election', 'government']
        health_keywords = ['health', 'disease', 'vaccine']

        if any(keyword in title.lower() for keyword in political_keywords):
            return 'Political'
        elif any(keyword in title.lower() for keyword in health_keywords):
            return 'Health'
        else:
            return 'Other'

    def scrape(self):
        """Main method to scrape articles from the website."""
        logging.info(f"Starting to scrape articles from {self.base_url}")
        html_content = self.fetch_page(self.base_url)
        if html_content:
            self.parse_articles(html_content)
            logging.info(f"Scraped {len(self.articles)} articles.")
        else:
            logging.warning("No articles were scraped due to an error in fetching the page.")

    def save_to_csv(self, filename):
        """Save the scraped articles to a CSV file."""
        df = pd.DataFrame(self.articles)
        try:
            df.to_csv(filename, index=False)
            logging.info(f"Saved articles to {filename}")
        except Exception as e:
            logging.error(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    # Example usage
    base_url = 'https://www.factcrescendo.com/tamil/'  # Replace with the actual URL
    scraper = FactCheckerScraper(base_url)
    scraper.scrape()
    scraper.save_to_csv('fact_checking_articles.csv')
```

**Note:** Make sure to replace the placeholder selectors (e.g., `.article-class`, `.title-class`) with the actual CSS selectors used on the target website. Additionally, ensure that web scraping complies with the website's `robots.txt` and terms of service.
