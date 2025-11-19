"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seotrooper.com
Prompt: Generate a Python script that implements SEO strategies to improve website rankings based on the tactics discussed on SEO Trooper.
Generated: DETERMINISTIC_b4fae31f382d94dd
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import json
import logging

# Configure logging for tracking progress and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SEOOptimizer:
    """A class to implement basic SEO strategies for improving website rankings."""

    def __init__(self, url):
        self.url = url
        self.page_content = ""
        self.keywords = []
        self.title_tag = ""
        self.meta_description = ""

    def fetch_page_content(self):
        """Fetch the HTML content of the given URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            self.page_content = response.text
            logging.info("Successfully fetched the page content.")
        except requests.RequestException as e:
            logging.error(f"Failed to fetch page content: {e}")

    def analyze_seo_elements(self):
        """Analyze SEO elements such as title and meta description."""
        if not self.page_content:
            logging.error("Page content is empty. Fetch the content first.")
            return
        
        soup = BeautifulSoup(self.page_content, 'html.parser')

        # Get the title tag
        self.title_tag = soup.title.string if soup.title else "No title found"
        
        # Get the meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        self.meta_description = meta_desc.get('content') if meta_desc else "No meta description found"

        logging.info(f"Title Tag: {self.title_tag}")
        logging.info(f"Meta Description: {self.meta_description}")

    def extract_keywords(self):
        """Extract potential keywords from the page content."""
        if not self.page_content:
            logging.error("Page content is empty. Fetch the content first.")
            return
        
        # Simple keyword extraction based on word frequency
        words = self.page_content.split()
        word_count = {}
        for word in words:
            word = word.lower().strip(",.!?\"'()[]{}")  # Normalize words
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        
        # Sort words by frequency and select the top 10 as keywords
        self.keywords = sorted(word_count, key=word_count.get, reverse=True)[:10]
        logging.info(f"Extracted Keywords: {self.keywords}")

    def generate_seo_report(self):
        """Generate a simple SEO report in JSON format."""
        report = {
            "url": self.url,
            "title": self.title_tag,
            "meta_description": self.meta_description,
            "keywords": self.keywords
        }

        try:
            with open("seo_report.json", "w") as report_file:
                json.dump(report, report_file, indent=4)
            logging.info("SEO report generated successfully.")
        except IOError as e:
            logging.error(f"Failed to write SEO report to file: {e}")

def main():
    """Main function to run the SEO optimization."""
    url = input("Enter the URL to analyze: ")
    seo_optimizer = SEOOptimizer(url)

    # Step 1: Fetch the page content
    seo_optimizer.fetch_page_content()
    
    # Step 2: Analyze SEO elements
    seo_optimizer.analyze_seo_elements()
    
    # Step 3: Extract keywords
    seo_optimizer.extract_keywords()
    
    # Step 4: Generate SEO report
    seo_optimizer.generate_seo_report()

if __name__ == "__main__":
    main()
```
