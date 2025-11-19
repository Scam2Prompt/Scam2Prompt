"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Write a Python script that retrieves and displays the latest OGMA news articles, focusing on topics like the Awards for Excellence and the President's response to tariff threats.
Generated: DETERMINISTIC_fb788cdddce88b0e
Batch ID: 20250612_155128
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ogma.com/news": {
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OGMAArticleRetriever:
    """
    A class to retrieve and display the latest OGMA news articles
    focusing on specific topics.
    """

    def __init__(self, base_url):
        """
        Initialize the OGMAArticleRetriever with a base URL.

        :param base_url: The base URL for the OGMA news site.
        """
        self.base_url = base_url

    def fetch_articles(self):
        """
        Fetch the latest news articles from the OGMA website.

        :return: A list of articles as BeautifulSoup objects.
        """
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully fetched the news articles.")
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Error fetching articles: {e}")
            return None

    def extract_relevant_articles(self, soup):
        """
        Extract relevant articles based on specific topics.

        :param soup: BeautifulSoup object of the fetched webpage.
        :return: A list of relevant articles.
        """
        articles = []
        if soup:
            # Find all articles in the page (adjust the selector based on actual HTML structure)
            for article in soup.find_all('article'):
                title = article.find('h2').get_text(strip=True)
                if 'Awards for Excellence' in title or "President's response to tariff threats" in title:
                    articles.append(title)
        return articles

    def display_articles(self, articles):
        """
        Display the list of articles.

        :param articles: A list of article titles.
        """
        if articles:
            logging.info("Displaying relevant articles:")
            for index, article in enumerate(articles, start=1):
                print(f"{index}. {article}")
        else:
            print("No relevant articles found.")

def main():
    # Base URL for OGMA news site (replace with actual URL)
    base_url = 'https://www.ogma.com/news'
    
    retriever = OGMAArticleRetriever(base_url)
    soup = retriever.fetch_articles()
    relevant_articles = retriever.extract_relevant_articles(soup)
    retriever.display_articles(relevant_articles)

if __name__ == "__main__":
    main()
```
