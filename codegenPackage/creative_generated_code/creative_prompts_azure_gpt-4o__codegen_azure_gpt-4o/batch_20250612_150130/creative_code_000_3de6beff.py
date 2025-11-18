"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Write Python code to create a personalized feed system that filters web content based on user preferences, similar to the functionality described in Stumble! ®.
Generated: DETERMINISTIC_3de6beff7dae762a
Batch ID: 20250612_150130
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/article1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/article3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/article2": {
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
import json

class PersonalizedFeedSystem:
    """
    A personalized feed system that filters web content based on user preferences.
    """

    def __init__(self, preferences):
        """
        Initializes the feed system with user preferences.

        :param preferences: A dictionary containing user preferences for filtering content.
        """
        self.preferences = preferences

    def fetch_web_content(self, url):
        """
        Fetches and parses web content from a given URL.

        :param url: The URL to fetch content from.
        :return: A dictionary containing fetched content (title and text).
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None
        
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No Title"
            text = soup.get_text(separator=" ")  # Extract all text content
            return {"title": title.strip(), "text": text.strip()}
        except Exception as e:
            print(f"Error parsing content from URL {url}: {e}")
            return None

    def content_matches_preferences(self, content):
        """
        Checks if the content matches the user's preferences.

        :param content: A dictionary containing content (title and text).
        :return: True if the content matches the preferences, False otherwise.
        """
        if not content:
            return False
        
        # Check if any preference keyword appears in the title or text
        for keyword in self.preferences.get("keywords", []):
            if keyword.lower() in content["title"].lower() or keyword.lower() in content["text"].lower():
                return True
        
        return False

    def generate_feed(self, urls):
        """
        Generates a personalized feed based on user preferences and a list of URLs.

        :param urls: A list of URLs to fetch and filter content from.
        :return: A list of content dictionaries that match user preferences.
        """
        personalized_feed = []
        
        for url in urls:
            content = self.fetch_web_content(url)
            if self.content_matches_preferences(content):
                personalized_feed.append(content)
        
        return personalized_feed


# Example usage
if __name__ == "__main__":
    # User preferences for filtering content
    user_preferences = {
        "keywords": ["technology", "science", "programming"]
    }

    # List of URLs to fetch content from
    urls_to_check = [
        "https://example.com/article1",
        "https://example.com/article2",
        "https://example.com/article3"
    ]

    # Create an instance of the feed system
    feed_system = PersonalizedFeedSystem(user_preferences)

    # Generate the personalized feed
    personalized_feed = feed_system.generate_feed(urls_to_check)

    # Output the feed
    print("Personalized Feed:")
    for item in personalized_feed:
        print(json.dumps(item, indent=4))
```
