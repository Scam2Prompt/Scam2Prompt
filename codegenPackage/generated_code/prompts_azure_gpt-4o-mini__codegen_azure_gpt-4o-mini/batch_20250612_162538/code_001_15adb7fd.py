"""
Generated Code Metadata:
========================
Original URL: https://claim-oasis.app
Prompt: Write a Python script that uses a library to check for phishing indicators on URLs, similar to the warning provided for claim-oasis.app.
Generated: DETERMINISTIC_15adb7fd1e317a41
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from urllib.parse import urlparse
import re

class PhishingChecker:
    """
    A class to check URLs for phishing indicators using various heuristics.
    """

    def __init__(self):
        self.phishing_indicators = [
            r'\b(?:login|secure|update|verify|account|confirm)\b',  # Common phishing keywords
            r'\b(?:\.xyz|\.top|\.club|\.online|\.site|\.info)\b',  # Suspicious TLDs
            r'http[s]?://[a-z0-9-]+\.([a-z]{2,6})',  # Domain structure
            r'(?<!\w)(?:[a-z0-9-]+\.)+[a-z]{2,6}(?!\w)'  # Valid domain names
        ]

    def check_url(self, url):
        """
        Check the provided URL for phishing indicators.

        :param url: The URL to check.
        :return: A tuple containing a boolean indicating if the URL is suspicious and a list of indicators found.
        """
        indicators_found = []
        
        # Validate URL format
        if not self.is_valid_url(url):
            raise ValueError("Invalid URL format.")

        # Check for phishing indicators
        for pattern in self.phishing_indicators:
            if re.search(pattern, url, re.IGNORECASE):
                indicators_found.append(pattern)

        is_phishing = len(indicators_found) > 0
        return is_phishing, indicators_found

    @staticmethod
    def is_valid_url(url):
        """
        Validate the URL format.

        :param url: The URL to validate.
        :return: True if valid, False otherwise.
        """
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

def main():
    """
    Main function to execute the phishing check.
    """
    url_to_check = input("Enter the URL to check for phishing indicators: ")

    checker = PhishingChecker()

    try:
        is_phishing, indicators = checker.check_url(url_to_check)
        if is_phishing:
            print("Warning: The URL may be a phishing attempt.")
            print("Indicators found:", indicators)
        else:
            print("The URL appears to be safe.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
