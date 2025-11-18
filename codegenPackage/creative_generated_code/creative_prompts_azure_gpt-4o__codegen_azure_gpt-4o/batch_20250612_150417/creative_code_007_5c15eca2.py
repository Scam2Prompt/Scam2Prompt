"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: Provide code examples in Python for detecting phishing scams, referencing specific scams like "Spfyapply.com Reviews" and "Maryland DMV 'Final Notice' Text Scam" from MyAntiSpyware.com.
Generated: DETERMINISTIC_5c15eca2252b2bd8
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://spfyapply.com": {
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
from bs4 import BeautifulSoup


class PhishingScamDetector:
    """
    A class to detect phishing scams by analyzing URLs and text patterns for suspicious content.
    """

    def __init__(self):
        # Known phishing patterns and keywords
        self.known_phishing_domains = [
            "spfyapply.com",  # Example phishing domain
        ]
        self.suspicious_keywords = [
            "final notice",  # Common in phishing text messages (e.g., "Maryland DMV 'Final Notice'")
            "urgent", "apply now", "account locked", "verify your account"
        ]

    def is_phishing_url(self, url):
        """
        Check if a given URL is suspicious or matches known phishing domains.
        
        Args:
            url (str): The URL to analyze.
        
        Returns:
            bool: True if the URL is flagged as a phishing attempt, False otherwise.
        """
        try:
            # Check if the URL domain matches any known phishing domains
            for domain in self.known_phishing_domains:
                if domain in url:
                    return True

            # Fetch the website content
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            website_content = response.text

            # Check for suspicious keywords in website content
            for keyword in self.suspicious_keywords:
                if keyword.lower() in website_content.lower():
                    return True

            return False
        except requests.RequestException as e:
            # Handle network-related errors gracefully
            print(f"Error fetching URL content: {e}")
            return True  # Flag as suspicious if there's an error fetching the URL

    def is_phishing_text(self, text):
        """
        Check if provided text contains suspicious keywords or patterns.
        
        Args:
            text (str): The text to analyze.
        
        Returns:
            bool: True if the text is flagged as a phishing attempt, False otherwise.
        """
        for keyword in self.suspicious_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text.lower()):
                return True
        return False


if __name__ == "__main__":
    # Example usage of the PhishingScamDetector class

    detector = PhishingScamDetector()

    # Example URL to test
    test_url = "https://spfyapply.com"
    if detector.is_phishing_url(test_url):
        print(f"Warning: '{test_url}' is flagged as a potential phishing website!")
    else:
        print(f"'{test_url}' appears safe.")

    # Example text to test
    test_text = "Maryland DMV Final Notice: Your license will be suspended unless payment is made immediately."
    if detector.is_phishing_text(test_text):
        print(f"Warning: Suspicious text detected: '{test_text}'")
    else:
        print("Text appears safe.")
```
