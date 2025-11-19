"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iammetis.org
Prompt: Write a Python script that fetches historical articles related to the Métis Nation from a specified database and formats them for display on a website.
Generated: DETERMINISTIC_8031cb62c2365b43
Batch ID: 20250612_161453
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/articles": {
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
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
API_ENDPOINT = "https://example.com/api/articles"
QUERY_PARAMS = {"query": "Métis Nation", "type": "historical"}
TIMEOUT = 10  # seconds

def fetch_articles(api_url: str, params: dict) -> List[dict]:
    """
    Fetch historical articles related to the Métis Nation from the specified API.
    
    :param api_url: The API endpoint URL.
    :param params: Query parameters for the API request.
    :return: A list of articles fetched from the API.
    """
    try:
        logging.info("Sending request to API...")
        response = requests.get(api_url, params=params, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info("API response received successfully.")
        articles = response.json().get("articles", [])
        return articles
    except requests.exceptions.RequestException as e:
        logging.error("Error fetching articles from API: %s", e)
        return []
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON response: %s", e)
        return []

def format_article_for_display(article: dict) -> str:
    """
    Format a single article for display on a website.
    
    :param article: A dictionary containing article details.
    :return: A formatted string for display.
    """
    try:
        title = article.get("title", "Untitled")
        author = article.get("author", "Unknown Author")
        date = article.get("published_date", "Unknown Date")
        content = article.get("content", "No content available.")
        
        formatted_article = (
            f"<article>\n"
            f"  <h2>{title}</h2>\n"
            f"  <p><strong>Author:</strong> {author}</p>\n"
            f"  <p><strong>Date Published:</strong> {date}</p>\n"
            f"  <p>{content}</p>\n"
            f"</article>\n"
        )
        return formatted_article
    except Exception as e:
        logging.error("Error formatting article: %s", e)
        return "<article><p>Error displaying article.</p></article>"

def generate_webpage_content(articles: List[dict]) -> str:
    """
    Generate HTML content for displaying a list of articles on a webpage.
    
    :param articles: A list of articles.
    :return: A string containing the HTML content.
    """
    if not articles:
        logging.warning("No articles found to display.")
        return "<p>No articles available.</p>"
    
    logging.info("Formatting articles for display...")
    formatted_articles = [format_article_for_display(article) for article in articles]
    webpage_content = (
        "<!DOCTYPE html>\n"
        "<html lang='en'>\n"
        "<head>\n"
        "  <meta charset='UTF-8'>\n"
        "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
        "  <title>Historical Articles - Métis Nation</title>\n"
        "</head>\n"
        "<body>\n"
        "  <h1>Historical Articles Related to the Métis Nation</h1>\n"
        f"  {''.join(formatted_articles)}\n"
        "</body>\n"
        "</html>"
    )
    logging.info("Webpage content generated successfully.")
    return webpage_content

def main():
    """
    Main function to fetch articles and generate webpage content.
    """
    logging.info("Starting the script...")
    
    # Fetch articles from the API
    articles = fetch_articles(API_ENDPOINT, QUERY_PARAMS)
    
    # Generate HTML content
    webpage_content = generate_webpage_content(articles)
    
    # Save the HTML content to a file
    try:
        with open("metis_nation_articles.html", "w", encoding="utf-8") as file:
            file.write(webpage_content)
        logging.info("Webpage content saved to 'metis_nation_articles.html'.")
    except Exception as e:
        logging.error("Error saving HTML content to file: %s", e)

if __name__ == "__main__":
    main()
```
