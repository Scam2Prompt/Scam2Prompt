"""
Generated Code Metadata:
========================
Original URL: https://enrolling-ordinal.app
Prompt: What libraries can I use in Python to detect phishing attempts based on URL analysis?
Generated: DETERMINISTIC_3ad1f9e8f14816f2
Batch ID: 20250612_162716
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://paypal.verify-account.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://192.168.1.1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bit.ly/2kxBqK9": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://\u0430\u0440\u0440\u04cf\u0435.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com": {
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
import tldextract
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class PhishingURLDetector:
    """
    A class to detect phishing attempts based on URL analysis.
    Uses various heuristics and checks to identify suspicious URLs.
    """

    def __init__(self):
        """
        Initialize the detector with common phishing indicators.
        """
        # List of known phishing indicators in URLs
        self.phishing_indicators = [
            r'https?://\d+\.\d+\.\d+\.\d+',  # IP address in URL
            r'@',                             # '@' symbol in URL
            r'\.exe$',                        # Direct executable download
            r'\.zip$',                        # Compressed file
            r'\.rar$',
            r'login',                         # Common phishing keywords
            r'account',
            r'verify',
            r'secure',
            r'webscr',
            r'banking',
            r'paypal',
            r'ebay',
            r'amazon'
        ]
        
        # Known legitimate domains (whitelist)
        self.whitelist = [
            'google.com',
            'microsoft.com',
            'github.com',
            'example.com'
        ]

    def is_url_suspicious(self, url):
        """
        Check if a URL is suspicious based on various heuristics.
        
        Args:
            url (str): The URL to analyze
            
        Returns:
            bool: True if suspicious, False otherwise
        """
        try:
            # Check if URL is empty
            if not url or not url.strip():
                return False

            # Parse URL
            parsed = urlparse(url)
            
            # Check for IP address in URL
            if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
                return True
                
            # Check for '@' symbol (credentials in URL)
            if '@' in url:
                return True
                
            # Extract domain using tldextract
            ext = tldextract.extract(url)
            domain = f"{ext.domain}.{ext.suffix}"
            
            # Check against whitelist
            if domain in self.whitelist:
                return False
                
            # Check for suspicious keywords in domain or path
            for indicator in self.phishing_indicators:
                if re.search(indicator, url, re.IGNORECASE):
                    return True
                    
            # Check for URL shortening services
            if self.is_shortened_url(url):
                return True
                
            # Check for homoglyphs or visually similar characters
            if self.has_homoglyphs(domain):
                return True
                
            return False
            
        except Exception as e:
            print(f"Error analyzing URL: {e}")
            return False

    def is_shortened_url(self, url):
        """
        Check if URL is from a known URL shortening service.
        
        Args:
            url (str): The URL to check
            
        Returns:
            bool: True if shortened URL, False otherwise
        """
        shortened_domains = [
            'bit.ly',
            'goo.gl',
            'tinyurl.com',
            'ow.ly',
            't.co',
            'is.gd',
            'buff.ly',
            'adf.ly'
        ]
        
        ext = tldextract.extract(url)
        domain = f"{ext.domain}.{ext.suffix}"
        return domain in shortened_domains

    def has_homoglyphs(self, domain):
        """
        Check for homoglyphs or visually similar characters in domain.
        
        Args:
            domain (str): The domain to check
            
        Returns:
            bool: True if homoglyphs detected, False otherwise
        """
        # Common homoglyph substitutions
        homoglyphs = {
            'a': ['а', 'α', 'а'],
            'e': ['е', 'є', 'ε'],
            'i': ['і', 'ï', 'ì'],
            'o': ['о', 'ο', 'ө'],
            'u': ['μ', 'υ', 'ц'],
            'c': ['с', 'ϲ', 'ς'],
            'd': ['ԁ', 'ժ', 'd'],
            'l': ['ӏ', 'І', 'l'],
            's': ['ѕ', 'š', 'ʂ'],
            'n': ['ո', 'п', 'η']
        }
        
        for char in domain:
            for key, values in homoglyphs.items():
                if char in values:
                    return True
        return False

    def get_redirect_url(self, url):
        """
        Get the final redirect URL (for checking shortened URLs).
        
        Args:
            url (str): The URL to check
            
        Returns:
            str: The final URL after redirects
        """
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.url
        except requests.RequestException:
            return url

# Example usage
if __name__ == "__main__":
    detector = PhishingURLDetector()
    test_urls = [
        "https://www.google.com",
        "https://example.com/login",
        "http://192.168.1.1",
        "https://paypal.verify-account.com",
        "https://bit.ly/2kxBqK9",
        "https://аррӏе.com"  # Homoglyph example
    ]
    
    for url in test_urls:
        print(f"URL: {url}")
        print(f"Is suspicious: {detector.is_url_suspicious(url)}")
        print()
```
