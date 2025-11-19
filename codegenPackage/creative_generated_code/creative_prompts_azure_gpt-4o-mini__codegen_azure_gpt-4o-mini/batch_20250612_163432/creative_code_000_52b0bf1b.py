"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pledge-moso.app
Prompt: Write a Python script that detects phishing attempts by analyzing URLs and checking them against a list of known phishing sites.
Generated: DETERMINISTIC_52b0bf1b1736a4b1
Batch ID: 20250612_163432
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://malicious-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://phishing-example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/phishing_sites.txt": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://safe-site.com": {
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

class PhishingDetector:
    def __init__(self, phishing_sites_url):
        """
        Initializes the PhishingDetector with a URL to fetch known phishing sites.
        
        :param phishing_sites_url: URL to the file containing known phishing URLs
        """
        self.phishing_sites_url = phishing_sites_url
        self.phishing_sites = self.load_phishing_sites()

    def load_phishing_sites(self):
        """
        Loads the known phishing sites from the provided URL.
        
        :return: A set of known phishing URLs
        """
        try:
            response = requests.get(self.phishing_sites_url)
            response.raise_for_status()  # Raise an error for bad responses
            # Split the response text into a set of URLs, stripping whitespace
            phishing_sites = set(line.strip() for line in response.text.splitlines() if line.strip())
            return phishing_sites
        except requests.RequestException as e:
            print(f"Error fetching phishing sites: {e}")
            return set()  # Return an empty set on failure

    def is_phishing(self, url):
        """
        Checks if the given URL is in the list of known phishing sites.
        
        :param url: The URL to check
        :return: True if the URL is a phishing site, False otherwise
        """
        return url in self.phishing_sites

def main():
    # Example URL for known phishing sites (this should be a valid URL in a real application)
    phishing_sites_url = 'https://example.com/phishing_sites.txt'
    
    detector = PhishingDetector(phishing_sites_url)
    
    # Example usage
    test_urls = [
        'http://malicious-site.com',
        'https://safe-site.com',
        'http://phishing-example.com'
    ]
    
    for url in test_urls:
        if detector.is_phishing(url):
            print(f"Warning: The URL '{url}' is a known phishing site!")
        else:
            print(f"The URL '{url}' appears to be safe.")

if __name__ == '__main__':
    main()
```
