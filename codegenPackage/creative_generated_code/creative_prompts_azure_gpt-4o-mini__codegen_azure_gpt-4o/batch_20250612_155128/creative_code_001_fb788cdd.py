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
  "https://api.example.com/ogma/news": {
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
from datetime import datetime


def fetch_latest_ogma_news():
    """
    Fetches the latest OGMA news articles from an API endpoint or a predefined URL.

    Returns:
        list: A list of dictionaries containing news articles with their titles, publication dates, and summaries.
    """
    # Define the API endpoint for retrieving OGMA news articles
    api_url = "https://api.example.com/ogma/news"  # Replace with the actual API URL

    try:
        # Send an HTTP GET request to the API
        response = requests.get(api_url, timeout=10)  # Timeout ensures program doesn't hang indefinitely
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        news_data = response.json()
        
        # Filter articles related to "Awards for Excellence" and "President's response to tariff threats"
        filtered_articles = [
            article for article in news_data if
            "Awards for Excellence" in article.get("title", "") or
            "President's response to tariff threats" in article.get("title", "")
        ]
        
        return filtered_articles

    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list
        print(f"Error fetching news articles: {e}")
        return []


def display_articles(articles):
    """
    Displays a list of news articles in a readable format.

    Args:
        articles (list): A list of dictionaries containing article details.
    """
    if not articles:
        print("No articles found related to the requested topics.")
        return

    print("\nLatest OGMA News Articles:\n")
    for article in articles:
        title = article.get("title", "No title available")
        pub_date = article.get("publication_date", "Unknown date")
        summary = article.get("summary", "No summary available")
        
        # Format the publication date, if available
        try:
            pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")
        except ValueError:
            pass  # Keep the original date if formatting fails

        print(f"Title: {title}")
        print(f"Published on: {pub_date}")
        print(f"Summary: {summary}\n")
        print("-" * 80)


def main():
    """
    Main function to fetch and display latest OGMA news articles.
    """
    print("Fetching latest OGMA news articles...")
    articles = fetch_latest_ogma_news()
    display_articles(articles)


if __name__ == "__main__":
    main()
```
