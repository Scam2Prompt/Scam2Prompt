"""
Generated Code Metadata:
========================
Original URL: https://allocation-pepecoineth.app
Prompt: Write a Python script to simulate a basic phishing detection system that flags suspicious URLs based on predefined keywords.
Generated: DETERMINISTIC_8d5b67ab74c3c4a6
Batch ID: 20250622_211032
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/home": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://secure.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/about": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://phishing-site.com/verify-account": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/login": {
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
import re
import logging
from typing import List, Tuple

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PhishingDetector:
    def __init__(self, keywords: List[str]):
        """
        Initializes the PhishingDetector with a list of suspicious keywords.

        :param keywords: A list of keywords that are commonly found in phishing URLs.
        """
        self.keywords = keywords
        logging.info("PhishingDetector initialized with keywords: %s", keywords)

    def is_suspicious(self, url: str) -> bool:
        """
        Checks if the given URL contains any of the suspicious keywords.

        :param url: The URL to be checked.
        :return: True if the URL is suspicious, False otherwise.
        """
        # Normalize the URL to lower case for case-insensitive matching
        url_lower = url.lower()
        logging.debug("Checking URL: %s", url_lower)

        # Check for the presence of any suspicious keywords in the URL
        for keyword in self.keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', url_lower):
                logging.warning("Suspicious URL detected: %s (contains keyword: %s)", url, keyword)
                return True
        return False

    def flag_suspicious_urls(self, urls: List[str]) -> List[Tuple[str, bool]]:
        """
        Flags suspicious URLs from a list of URLs.

        :param urls: A list of URLs to be checked.
        :return: A list of tuples containing the URL and a boolean indicating if it is suspicious.
        """
        flagged_urls = []
        for url in urls:
            try:
                is_suspicious = self.is_suspicious(url)
                flagged_urls.append((url, is_suspicious))
            except Exception as e:
                logging.error("Error checking URL %s: %s", url, e)
                flagged_urls.append((url, None))  # None indicates an error occurred
        return flagged_urls

def main():
    # Predefined list of suspicious keywords
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'confirm', 'bank', 'password']

    # Initialize the phishing detector
    detector = PhishingDetector(suspicious_keywords)

    # Sample URLs to check
    urls_to_check = [
        "http://example.com/login",
        "https://secure.example.com",
        "http://example.com/home",
        "http://phishing-site.com/verify-account",
        "http://example.com/about"
    ]

    # Flag suspicious URLs
    flagged_results = detector.flag_suspicious_urls(urls_to_check)

    # Output the results
    for url, is_suspicious in flagged_results:
        if is_suspicious is None:
            print(f"Error checking URL: {url}")
        else:
            status = "Suspicious" if is_suspicious else "Safe"
            print(f"URL: {url} - Status: {status}")

if __name__ == "__main__":
    main()
```
