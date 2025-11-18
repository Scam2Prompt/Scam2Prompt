"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaflancoin.com
Prompt: Generate code to analyze the popularity of articles on the Gaflan Coin website, using metrics like "پر بازدید ها" (most visited) and "محبوبترین ها" (most popular).
Generated: DETERMINISTIC_f71bf7ffaf29f274
Batch ID: 20250612_154454
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gaflan-coin.com/articles": {
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

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
BASE_URL = "https://api.gaflan-coin.com/articles"  # Replace with the actual API endpoint of the Gaflan Coin website

def fetch_articles():
    """
    Fetch articles from the Gaflan Coin API.
    Returns:
        list: A list of articles if the request is successful, otherwise None.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Parse the JSON content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching articles: {e}")
        return None

def analyze_popularity(articles):
    """
    Analyze the popularity of articles based on metrics like "most visited" and "most popular".
    Args:
        articles (list): A list of articles with their metadata.
    Returns:
        dict: A dictionary containing the most visited and most popular articles.
    """
    if not articles:
        logging.warning("No articles to analyze.")
        return {"most_visited": None, "most_popular": None}

    try:
        # Sort articles by "views" and "likes" metrics
        most_visited = sorted(articles, key=lambda x: x.get('views', 0), reverse=True)[0]
        most_popular = sorted(articles, key=lambda x: x.get('likes', 0), reverse=True)[0]
        
        return {
            "most_visited": most_visited,
            "most_popular": most_popular
        }
    except KeyError as e:
        logging.error(f"Key error while analyzing articles: {e}")
        return {"most_visited": None, "most_popular": None}

def display_results(results):
    """
    Display the results of the popularity analysis.
    Args:
        results (dict): A dictionary containing the most visited and most popular articles.
    """
    if results["most_visited"]:
        print("Most Visited Article:")
        print(f"Title: {results['most_visited']['title']}")
        print(f"Views: {results['most_visited']['views']}")
        print()

    if results["most_popular"]:
        print("Most Popular Article:")
        print(f"Title: {results['most_popular']['title']}")
        print(f"Likes: {results['most_popular']['likes']}")
        print()

def main():
    """
    Main function to orchestrate the analysis of Gaflan Coin articles.
    """
    logging.info("Fetching articles...")
    articles = fetch_articles()

    if articles:
        logging.info("Analyzing article popularity...")
        results = analyze_popularity(articles)

        logging.info("Displaying results...")
        display_results(results)
    else:
        logging.error("Failed to fetch articles. Exiting...")

if __name__ == "__main__":
    main()
```
