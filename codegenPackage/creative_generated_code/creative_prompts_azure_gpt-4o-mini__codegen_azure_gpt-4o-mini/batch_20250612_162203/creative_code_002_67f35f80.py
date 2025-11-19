"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Write a Python script that fetches and displays the latest news articles related to cycling teams and sponsorships, similar to those on Race Ride Fire's website.
Generated: DETERMINISTIC_67f35f80c64e0b21
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.raceridefire.com": {
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

def fetch_latest_news(url):
    """
    Fetches the latest news articles from the specified URL.

    Args:
        url (str): The URL of the news website to fetch articles from.

    Returns:
        list: A list of dictionaries containing article titles and links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    except requests.RequestException as e:
        logging.error(f"Error fetching news: {e}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract news articles (Update the selectors based on the actual website structure)
    articles = []
    for article in soup.find_all('article'):
        title_tag = article.find('h2')
        link_tag = article.find('a')

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            articles.append({'title': title, 'link': link})

    return articles

def display_articles(articles):
    """
    Displays the fetched articles.

    Args:
        articles (list): List of articles to display.
    """
    if not articles:
        logging.info("No articles found.")
        return

    logging.info("Latest Cycling Teams and Sponsorships News:")
    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article['title']}\n   Link: {article['link']}\n")

def main():
    """
    Main function to execute the news fetching and displaying logic.
    """
    url = 'https://www.raceridefire.com'  # Replace with the actual URL of the news site
    articles = fetch_latest_news(url)
    display_articles(articles)

if __name__ == '__main__':
    main()
```
