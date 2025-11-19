"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luwukpost.id
Prompt: Draft a news piece covering the police's response to the recent challenges posed by illegal mining activities in the Banggai region, including the threats made against the Kapolda.
Generated: DETERMINISTIC_3fbd61c6cdd779e8
Batch ID: 20250612_160720
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/news/banggai-illegal-mining": {
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

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NewsArticle:
    """Class to represent a news article about police response to illegal mining activities."""

    def __init__(self, title, content):
        """Initialize the news article with a title and content."""
        self.title = title
        self.content = content

    def display_article(self):
        """Display the article title and content."""
        print(f"Title: {self.title}\n")
        print(f"Content: {self.content}\n")

def fetch_news_data(url):
    """Fetch news data from a given URL.

    Args:
        url (str): The URL to fetch the news data from.

    Returns:
        str: The HTML content of the page.

    Raises:
        Exception: If the HTTP request fails or the URL is invalid.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching news data: {e}")
        raise

def parse_article(html_content):
    """Parse the HTML content to extract the news article.

    Args:
        html_content (str): The HTML content of the news page.

    Returns:
        NewsArticle: An instance of NewsArticle with extracted title and content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Assuming the title is within an <h1> tag and content within a <div class="content">
    title = soup.find('h1').get_text(strip=True)
    content = soup.find('div', class_='content').get_text(strip=True)

    return NewsArticle(title, content)

def main():
    """Main function to execute the news article fetching and parsing."""
    url = "http://example.com/news/banggai-illegal-mining"  # Replace with a real URL

    try:
        # Fetch and parse news data
        html_content = fetch_news_data(url)
        article = parse_article(html_content)

        # Display the article
        article.display_article()

    except Exception as e:
        logging.error("Failed to fetch and display news article.")

if __name__ == "__main__":
    main()
```
