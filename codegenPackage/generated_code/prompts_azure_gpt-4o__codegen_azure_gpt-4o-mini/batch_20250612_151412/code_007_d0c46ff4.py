"""
Generated Code Metadata:
========================
Original URL: https://test.metamask-phishing.io
Prompt: Develop a tool to analyze and display MetaMask phishing warnings for a set of URLs, inspired by the MetaMask Phishing Test Page.
Generated: DETERMINISTIC_d0c46ff4fdac7351
Batch ID: 20250612_151412
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example2.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example3.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetaMaskPhishingAnalyzer:
    def __init__(self, urls):
        """
        Initialize the analyzer with a list of URLs.

        :param urls: List of URLs to analyze
        """
        self.urls = urls
        self.phishing_warnings = {}

    def analyze_urls(self):
        """
        Analyze each URL for phishing warnings.
        """
        for url in self.urls:
            try:
                logging.info(f'Analyzing URL: {url}')
                warning = self.check_phishing_warning(url)
                self.phishing_warnings[url] = warning
            except Exception as e:
                logging.error(f'Error analyzing {url}: {e}')
                self.phishing_warnings[url] = 'Error during analysis'

    def check_phishing_warning(self, url):
        """
        Check the given URL for phishing warnings by scraping the MetaMask phishing test page.

        :param url: URL to check
        :return: Warning message if phishing is detected, otherwise None
        """
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for phishing warning in the page content
        if "phishing" in soup.text.lower():
            return "Phishing warning detected!"
        else:
            return "No phishing warning."

    def display_results(self):
        """
        Display the results of the phishing analysis.
        """
        for url, warning in self.phishing_warnings.items():
            print(f'URL: {url} - Warning: {warning}')

if __name__ == "__main__":
    # Example list of URLs to analyze
    urls_to_analyze = [
        "https://example1.com",
        "https://example2.com",
        "https://example3.com"
    ]

    # Create an instance of the analyzer
    analyzer = MetaMaskPhishingAnalyzer(urls_to_analyze)

    # Analyze the URLs
    analyzer.analyze_urls()

    # Display the results
    analyzer.display_results()
```
