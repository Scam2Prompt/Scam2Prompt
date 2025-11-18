"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Generate code to perform SEO keyword analysis using Python, focusing on strategies relevant to digital marketing agencies like TDA SEO services.
Generated: DETERMINISTIC_6bcd57308dea3fcf
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
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
from collections import Counter
import re

class SEOKeywordAnalyzer:
    """
    A class to perform SEO keyword analysis for digital marketing strategies.
    """

    def __init__(self, url):
        """
        Initializes the analyzer with the target URL.

        :param url: The URL of the web page to analyze.
        """
        self.url = url
        self.text_content = ""
        self.keywords = []

    def fetch_page_content(self):
        """
        Fetches the HTML content of the target web page.

        :raises Exception: If the HTTP request fails.
        """
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            self.text_content = self._extract_text_from_html(response.text)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch the page content: {str(e)}")

    def _extract_text_from_html(self, html_content):
        """
        Extracts and returns the textual content from the HTML source.

        :param html_content: Raw HTML content of the web page.
        :return: Extracted text content as a string.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(separator=" ").strip()

    def analyze_keywords(self):
        """
        Analyzes the keywords in the fetched text content.

        :return: A list of tuples containing keywords and their frequency, sorted in descending order.
        """
        if not self.text_content:
            raise Exception("No page content available for analysis. Fetch the page first.")

        # Clean the text content
        cleaned_text = re.sub(r'[^\w\s]', '', self.text_content.lower())  # Remove punctuation and convert to lowercase
        words = cleaned_text.split()

        # Count occurrences of each word
        word_counts = Counter(words)

        # Filter out common stopwords (you can expand this list as needed)
        stopwords = set([
            "the", "and", "in", "on", "at", "for", "to", "of", "a", "an", "is", "are", "by", "as", "with", "from", "that",
            "this", "it", "be", "or", "was", "were", "can", "not", "will", "if", "but", "about", "which", "their", "more",
            "these", "has", "have", "had", "also"
        ])
        filtered_keywords = {word: count for word, count in word_counts.items() if word not in stopwords}

        # Sort keywords by frequency (descending order)
        self.keywords = sorted(filtered_keywords.items(), key=lambda x: x[1], reverse=True)
        return self.keywords

    def display_keywords(self, top_n=20):
        """
        Displays the top N keywords by frequency.

        :param top_n: Number of top keywords to display.
        """
        if not self.keywords:
            print("No keywords available for display. Perform keyword analysis first.")
            return

        print(f"Top {top_n} keywords:")
        for idx, (keyword, freq) in enumerate(self.keywords[:top_n], start=1):
            print(f"{idx}. {keyword}: {freq}")


if __name__ == "__main__":
    # Example usage
    target_url = "https://www.example.com"  # Replace with the target URL
    analyzer = SEOKeywordAnalyzer(target_url)

    try:
        print("Fetching page content...")
        analyzer.fetch_page_content()
        print("Analyzing keywords...")
        analyzer.analyze_keywords()
        analyzer.display_keywords(top_n=10)
    except Exception as e:
        print(f"Error: {str(e)}")
```
