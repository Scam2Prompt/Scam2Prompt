"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aiiocating-optimism.app
Prompt: Develop a function that simulates the behavior of Cloudflare's phishing detection, using criteria mentioned in the warning from https://aiiocating-optimism.app.
Generated: DETERMINISTIC_ace6ad668d6a0101
Batch ID: 20250612_162504
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://secure.test.com/account-update": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://validsite.com?item=login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://legitimate-site.com/welcome": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://phishing-site.com": {
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
import re
from urllib.parse import urlparse

class PhishingDetector:
    """
    A class to simulate the behavior of a phishing detection system.
    """

    def __init__(self):
        # Define patterns or rules for detecting phishing URLs
        self.phishing_keywords = [
            r"login", r"secure", r"verify", r"update", r"account", r"webmail",
            r"bank", r"signin", r"confirmation", r"password", r"click", r"here"
        ]
        self.phishing_domains = [
            "example.com", "test.com"  # Add known phishing domains here
        ]

    def is_phishing_url(self, url):
        """
        Determine if the given URL is likely to be a phishing attempt.

        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL is likely phishing, False otherwise.
        """
        try:
            parsed_url = urlparse(url)
            # Check for empty URL
            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError("Invalid URL format.")

            # Check for known phishing domains
            if parsed_url.netloc in self.phishing_domains:
                return True
            
            # Check for phishing keywords in the path and query
            combined_path = f"{parsed_url.path} {parsed_url.query}".lower()
            for keyword in self.phishing_keywords:
                if re.search(keyword, combined_path):
                    return True

            return False

        except Exception as e:
            # Handle exceptions and log error messages
            print(f"Error checking URL: {url}. Exception: {str(e)}")
            return False


# Example of using the PhishingDetector class
if __name__ == "__main__":
    detector = PhishingDetector()
    test_urls = [
        "http://example.com/login",
        "http://secure.test.com/account-update",
        "http://legitimate-site.com/welcome",
        "http://phishing-site.com",
        "https://validsite.com?item=login"
    ]

    for url in test_urls:
        if detector.is_phishing_url(url):
            print(f"Phishing detected: {url}")
        else:
            print(f"Safe URL: {url}")
```
