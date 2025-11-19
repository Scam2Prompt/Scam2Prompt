"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protsahitnews18.com
Prompt: Generate a news article summarizing the recent updates on the 49,000 crore Bodhghat project and its significance in Chhattisgarh.
Generated: DETERMINISTIC_07da2805602fd08d
Batch ID: 20250612_155200
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/news/bodhghat-project-update": {
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

class NewsArticleSummarizer:
    def __init__(self, url):
        """
        Initializes the NewsArticleSummarizer with a URL to fetch the news article.
        
        Args:
            url (str): The URL of the news article to summarize.
        """
        self.url = url
        self.article_content = ""

    def fetch_article(self):
        """
        Fetches the article content from the provided URL.
        
        Raises:
            Exception: Raises an exception if the request to the URL fails.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check for HTTP errors
            self.article_content = response.text
        except requests.RequestException as e:
            raise Exception(f"Error fetching article: {e}")

    def summarize_article(self):
        """
        Summarizes the article content.
        
        Returns:
            str: A summary of the article.
        """
        # Parsing the article content using BeautifulSoup
        soup = BeautifulSoup(self.article_content, 'html.parser')
        
        # Extracting the main content (assuming it's in a <div> with class 'article-content')
        content_div = soup.find('div', class_='article-content')
        
        if content_div:
            paragraphs = content_div.find_all('p')
            summary = " ".join([para.get_text() for para in paragraphs[:3]])  # Summarizing the first three paragraphs
            return summary
        else:
            raise Exception("Content not found in the article.")

def main():
    url = "https://example.com/news/bodhghat-project-update"  # Replace with the actual URL
    summarizer = NewsArticleSummarizer(url)

    try:
        summarizer.fetch_article()
        summary = summarizer.summarize_article()
        print("Article Summary:")
        print(summary)
    except Exception as e:
        print(f"Failed to summarize the article: {e}")

if __name__ == "__main__":
    main()
```
