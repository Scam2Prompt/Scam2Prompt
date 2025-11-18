"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Write a Python script that uses an API to fetch trending health articles, including topics like "personalized medicine" and "dental trauma," as discussed on SRH Life Foundation.
Generated: DETERMINISTIC_835a86736edbc01c
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/articles/trending": {
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

# Constants
API_URL = "https://api.example.com/v1/articles/trending"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your actual API key
SEARCH_TOPICS = ["personalized medicine", "dental trauma"]  # Topics to filter articles
TIMEOUT = 10  # Timeout for API requests in seconds

def fetch_trending_articles(api_url, api_key, search_topics):
    """
    Fetches trending health articles from the specified API and filters them by topics.

    :param api_url: URL of the API endpoint to fetch articles.
    :param api_key: API key for authentication.
    :param search_topics: List of topics to search for in the articles.
    :return: List of filtered articles or an empty list in case of errors.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send GET request to fetch trending articles
        response = requests.get(api_url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an HTTPError if the response code is not 2xx

        # Parse JSON response
        articles = response.json()
        if not isinstance(articles, list):
            raise ValueError("Invalid response format: Expected a list of articles.")

        # Filter articles by topics
        filtered_articles = [
            article for article in articles
            if any(topic.lower() in article.get("title", "").lower() or
                   topic.lower() in article.get("summary", "").lower()
                   for topic in search_topics)
        ]

        return filtered_articles

    except requests.exceptions.RequestException as e:
        # Handle errors during the API request
        print(f"Error fetching articles: {e}")
        return []
    except ValueError as e:
        # Handle errors during response processing
        print(f"Error processing articles: {e}")
        return []

def main():
    """
    Main function to fetch and display trending health articles.
    """
    trending_articles = fetch_trending_articles(API_URL, API_KEY, SEARCH_TOPICS)

    if trending_articles:
        print("Trending Health Articles:")
        for idx, article in enumerate(trending_articles, start=1):
            title = article.get("title", "No title")
            summary = article.get("summary", "No summary")
            url = article.get("url", "No URL")
            print(f"\nArticle {idx}:\nTitle: {title}\nSummary: {summary}\nURL: {url}")
    else:
        print("No articles found for the specified topics.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `API_URL` and `API_KEY` with the actual API endpoint and your authentication key.
- Ensure that the API response format matches the code logic (e.g., `title`, `summary`, and `url` fields).
- Install the `requests` library if not already installed (`pip install requests`) before running this script.
