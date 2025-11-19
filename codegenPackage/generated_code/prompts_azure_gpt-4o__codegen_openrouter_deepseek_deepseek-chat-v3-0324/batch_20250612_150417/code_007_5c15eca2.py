"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Provide code examples in Python for detecting phishing scams, referencing specific scams like "Spfyapply.com Reviews" and "Maryland DMV 'Final Notice' Text Scam" from MyAntiSpyware.com.
Generated: DETERMINISTIC_5c15eca2252b2bd8
Batch ID: 20250612_150417
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.paypal.com/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://fake-md-dmv.com/final-notice": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://spfyapply.com/reviews": {
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
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import whois
from datetime import datetime

class PhishingDetector:
    """
    A class to detect phishing scams based on URL, domain age, and content analysis.
    Reference scams: "Spfyapply.com Reviews" and "Maryland DMV 'Final Notice' Text Scam"
    """

    KNOWN_PHISHING_KEYWORDS = [
        'spfyapply',  # From Spfyapply.com Reviews scam
        'dmv', 'final notice', 'text scam',  # From Maryland DMV scam
        'urgent', 'verify', 'account', 'login', 'suspended',
        'limited offer', 'security alert', 'action required'
    ]

    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}

    def is_phishing_url(self, url):
        """
        Check if URL matches known phishing patterns.
        """
        try:
            domain = urlparse(url).netloc.lower()
            
            # Check for suspicious domain patterns
            if re.search(r'\d+\.\d+\.\d+\.\d+', domain):
                return True
                
            if any(keyword in domain for keyword in self.KNOWN_PHISHING_KEYWORDS):
                return True
                
            # Check for URL shortening services
            shorteners = ['bit.ly', 'goo.gl', 'tinyurl.com', 'ow.ly', 'is.gd']
            if any(shortener in domain for shortener in shorteners):
                return True
                
            return False
        except Exception as e:
            print(f"Error analyzing URL: {e}")
            return False

    def check_domain_age(self, domain):
        """
        Check if domain is recently created (less than 6 months old).
        """
        try:
            domain_info = whois.whois(domain)
            if isinstance(domain_info.creation_date, list):
                creation_date = domain_info.creation_date[0]
            else:
                creation_date = domain_info.creation_date
                
            if creation_date:
                age = (datetime.now() - creation_date).days
                return age < 180  # Less than 6 months old
            return True  # If creation date can't be determined, assume suspicious
        except Exception as e:
            print(f"Error checking domain age: {e}")
            return True

    def analyze_content(self, url):
        """
        Analyze webpage content for phishing indicators.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check for known phishing keywords in content
            text = soup.get_text().lower()
            if any(keyword in text for keyword in self.KNOWN_PHISHING_KEYWORDS):
                return True
                
            # Check for forms asking for sensitive information
            forms = soup.find_all('form')
            for form in forms:
                if form.find('input', {'type': 'password'}) or \
                   form.find('input', {'name': re.compile('credit|card|ssn|social', re.I)}):
                    return True
                    
            return False
        except Exception as e:
            print(f"Error analyzing content: {e}")
            return False

    def detect_phishing(self, url):
        """
        Comprehensive phishing detection combining multiple checks.
        """
        try:
            domain = urlparse(url).netloc
            
            if self.is_phishing_url(url):
                return True, "URL matches known phishing patterns"
                
            if self.check_domain_age(domain):
                return True, "Domain is recently created (potential phishing)"
                
            if self.analyze_content(url):
                return True, "Content contains phishing indicators"
                
            return False, "No phishing indicators detected"
        except Exception as e:
            print(f"Error in phishing detection: {e}")
            return True, "Error occurred during analysis (potential risk)"


# Example usage
if __name__ == "__main__":
    detector = PhishingDetector()
    
    # Test with known scams
    test_urls = [
        "http://spfyapply.com/reviews",  # Spfyapply.com Reviews scam
        "http://fake-md-dmv.com/final-notice",  # Maryland DMV scam
        "https://www.paypal.com/login"  # Legitimate site
    ]
    
    for url in test_urls:
        is_phishing, reason = detector.detect_phishing(url)
        print(f"URL: {url}")
        print(f"Phishing: {is_phishing}")
        print(f"Reason: {reason}\n")
```
