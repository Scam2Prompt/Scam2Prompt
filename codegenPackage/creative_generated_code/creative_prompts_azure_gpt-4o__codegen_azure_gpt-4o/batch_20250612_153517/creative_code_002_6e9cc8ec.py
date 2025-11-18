"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kvtech.ae
Prompt: Generate Python code for automating SEO optimization tasks, such as keyword analysis and meta tag generation, based on KEVI Technologies' SEO services.
Generated: DETERMINISTIC_6e9cc8ec884a43a0
Batch ID: 20250612_153517
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
import re

class SEOOptimizer:
    """
    A class to automate SEO optimization tasks such as keyword analysis and meta-tag generation.
    """

    def __init__(self, target_url):
        """
        Initialize SEO Optimizer with target URL.

        :param target_url: str - The URL of the webpage to optimize.
        """
        self.target_url = target_url
        self.html_content = None
        self.keywords = []
        self.meta_tags = {}

    def fetch_webpage_content(self):
        """
        Fetch webpage content using HTTP GET request.
        """
        try:
            response = requests.get(self.target_url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            self.html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching webpage content: {e}")
            self.html_content = None

    def extract_keywords(self):
        """
        Analyze HTML content and extract keywords from <body>.
        """
        if not self.html_content:
            print("No content available to analyze keywords.")
            return

        soup = BeautifulSoup(self.html_content, "html.parser")
        text_content = soup.body.get_text(separator=" ", strip=True)

        # Basic keyword extraction using word frequency
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text_content.lower())
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        # Sort by frequency and select the top 10 keywords
        sorted_keywords = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        self.keywords = [keyword for keyword, freq in sorted_keywords[:10]]

    def generate_meta_tags(self):
        """
        Generate meta tags including title, description, and keywords.
        """
        if not self.html_content or not self.keywords:
            print("Cannot generate meta tags due to insufficient data.")
            return

        soup = BeautifulSoup(self.html_content, "html.parser")
        title = soup.title.string if soup.title else "Untitled Page"
        description = f"{title} optimized for SEO with relevant keywords."

        # Generate meta tags dictionary
        self.meta_tags = {
            "title": title,
            "description": description,
            "keywords": ", ".join(self.keywords)
        }

    def display_results(self):
        """
        Display extracted keywords and generated meta tags.
        """
        print("\nExtracted Keywords:")
        for idx, keyword in enumerate(self.keywords, start=1):
            print(f"{idx}. {keyword}")

        print("\nGenerated Meta Tags:")
        for tag, value in self.meta_tags.items():
            print(f"{tag.capitalize()}: {value}")

    def run_optimization(self):
        """
        Run the full SEO optimization workflow.
        """
        print(f"Starting SEO optimization for {self.target_url}...\n")
        self.fetch_webpage_content()
        if self.html_content:
            self.extract_keywords()
            self.generate_meta_tags()
            self.display_results()

if __name__ == "__main__":
    # Example URL (replace with your desired URL for optimization).
    url = "https://www.example.com"

    # Create instance of SEOOptimizer and run optimization.
    optimizer = SEOOptimizer(target_url=url)
    optimizer.run_optimization()
```
