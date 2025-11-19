"""
Generated Code Metadata:
========================
Original URL: https://jasmyevent.com
Prompt: Write a Python script to scrape news articles from the 光明网 (Guangming Net) website, specifically from the "新闻视野" (News Perspective) section, and store the titles and summaries in a JSON file.
Generated: DETERMINISTIC_1bc17a755e94f526
Batch ID: 20250622_211141
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.guangming.cn/portal/article/column/column_54.shtml": {
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

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_news_perspective(url):
    """
    Scrape news articles from the "新闻视野" (News Perspective) section of 光明网 (Guangming Net).

    Args:
        url (str): URL of the News Perspective section

    Returns:
        list: List of dictionaries containing article titles and summaries
    """
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article items on the page
        article_items = soup.find_all('div', class_='article-item')

        # Initialize an empty list to store article data
        articles = []

        # Iterate over each article item
        for item in article_items:
            # Extract article title
            title = item.find('h3').text.strip()

            # Extract article summary
            summary = item.find('p', class_='summary').text.strip()

            # Append article data to the list
            articles.append({
                'title': title,
                'summary': summary
            })

        return articles

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return []
    except Exception as e:
        logging.error(f"Scraping error: {e}")
        return []

def save_to_json(articles, output_file):
    """
    Save article data to a JSON file.

    Args:
        articles (list): List of dictionaries containing article titles and summaries
        output_file (str): Path to the output JSON file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=4)
        logging.info(f"Articles saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving to JSON: {e}")

def main():
    url = "https://www.guangming.cn/portal/article/column/column_54.shtml"
    output_file = "news_articles.json"

    articles = scrape_news_perspective(url)
    save_to_json(articles, output_file)

if __name__ == "__main__":
    main()
```
