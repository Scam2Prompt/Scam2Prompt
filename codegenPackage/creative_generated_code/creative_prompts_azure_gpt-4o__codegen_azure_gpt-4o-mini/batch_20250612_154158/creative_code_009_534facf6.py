"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskofficial.support
Prompt: Generate code to simulate phishing detection in a local environment without relying on cloud-based models, as emphasized by the parody site's critique of automation.
Generated: DETERMINISTIC_534facf64bed080c
Batch ID: 20250612_154158
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://malicious-site.com/verify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://safe-site.com/home": {
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
  },
  "https://secure-site.com/account": {
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
import requests
from urllib.parse import urlparse

class PhishingDetector:
    """
    A class to detect phishing URLs using a set of heuristic rules.
    """

    def __init__(self):
        # Define patterns and heuristics to identify phishing URLs
        self.blacklist = [
            "login", "account", "secure", "verify", "update", "bank", "service"
        ]

    def is_suspicious_url(self, url: str) -> bool:
        """
        Check if the URL is suspicious based on several heuristics.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is suspicious, False otherwise.
        """
        # Check for common phishing keywords in the URL
        for keyword in self.blacklist:
            if keyword in url.lower():
                return True

        # Check if the URL structure is suspicious
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ['http', 'https']:
            return True  # Only allow HTTP and HTTPS

        if not self.is_valid_domain(parsed_url.netloc):
            return True  # Invalid domain

        return False

    def is_valid_domain(self, domain: str) -> bool:
        """
        Validate the domain against known safe domains.

        Args:
            domain (str): The domain to validate.

        Returns:
            bool: True if the domain is valid, False otherwise.
        """
        # Basic check: length and pattern of the domain
        if len(domain) < 3:
            return False
        
        # Regex pattern to check for valid domain names
        pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, domain) is not None

    def check_url(self, url: str) -> str:
        """
        Check a URL for phishing indicators.

        Args:
            url (str): The URL to check.

        Returns:
            str: Result of the phishing check.
        """
        try:
            if self.is_suspicious_url(url):
                return "Phishing suspected!"
            else:
                return "URL appears safe."
        except Exception as e:
            return f"Error checking URL: {str(e)}"

def main():
    detector = PhishingDetector()

    # Sample URLs for testing
    urls_to_check = [
        "http://example.com/login",
        "https://secure-site.com/account",
        "http://safe-site.com/home",
        "ftp://unknown-protocol.com",
        "http://malicious-site.com/verify"
    ]

    for url in urls_to_check:
        result = detector.check_url(url)
        print(f"Checking URL: {url} -> Result: {result}")

if __name__ == "__main__":
    main()
```
