"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs-boom.pages.dev
Prompt: Provide an example of how to use Sonic Labs' external blog API to fetch and display articles related to blockchain development.
Generated: DETERMINISTIC_99ae9b94aab34f24
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.soniclabs.com/blog": {
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

class BlogAPI:
    """
    A class to interact with Sonic Labs' external blog API.

    Attributes:
        base_url (str): The base URL for the blog API.
    """

    def __init__(self, base_url):
        """
        Initializes the BlogAPI with the given base URL.

        Args:
            base_url (str): The base URL for the blog API.
        """
        self.base_url = base_url

    def fetch_articles(self, topic, page=1, limit=10):
        """
        Fetches articles related to a specific topic.

        Args:
            topic (str): The topic to search for (e.g., 'blockchain development').
            page (int): The page number to retrieve (default is 1).
            limit (int): The number of articles to retrieve per page (default is 10).

        Returns:
            list: A list of articles related to the topic.

        Raises:
            Exception: Raises an exception if the API request fails.
        """
        try:
            response = requests.get(f"{self.base_url}/articles", params={
                'topic': topic,
                'page': page,
                'limit': limit
            })
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('articles', [])
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch articles: {e}")

def display_articles(articles):
    """
    Displays the fetched articles in a readable format.

    Args:
        articles (list): A list of articles to display.
    """
    if not articles:
        print("No articles found.")
        return

    for article in articles:
        print(f"Title: {article.get('title')}")
        print(f"Author: {article.get('author')}")
        print(f"Published: {article.get('published_date')}")
        print(f"Summary: {article.get('summary')}")
        print(f"Link: {article.get('url')}")
        print("-" * 40)

def main():
    """
    Main function to execute the blog article fetching and displaying process.
    """
    # Define the base URL for the Sonic Labs blog API
    base_url = "https://api.soniclabs.com/blog"
    
    # Create an instance of the BlogAPI class
    blog_api = BlogAPI(base_url)

    # Define the topic to search for
    topic = "blockchain development"

    try:
        # Fetch articles related to the specified topic
        articles = blog_api.fetch_articles(topic)
        
        # Display the fetched articles
        display_articles(articles)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
