"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Generate a Python script to compare Tamil-language claims against verified fact-checking archives, such as those maintained by Fact Crescendo Tamil.
Generated: DETERMINISTIC_739e7d9b91202b91
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.factcrescendo.com/tamil-archive": {
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
import json
import re
from bs4 import BeautifulSoup

class FactChecker:
    """
    A class to compare Tamil-language claims against verified fact-checking archives.
    """

    def __init__(self, archive_url):
        """
        Initializes the FactChecker with the URL of the fact-checking archive.
        
        :param archive_url: URL of the fact-checking archive (e.g. Fact Crescendo Tamil).
        """
        self.archive_url = archive_url

    def fetch_archive_data(self):
        """
        Fetches fact-checking data from the provided archive URL.
        
        :return: List of fact-checked claims as dictionaries.
        """
        try:
            response = requests.get(self.archive_url)
            response.raise_for_status()  # Raise an error for bad responses
            # Here we assume the response is in JSON format
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")
        
        return []

    def clean_text(self, text):
        """
        Cleans the input text for better comparison.
        
        :param text: The text to clean.
        :return: Cleaned text.
        """
        return re.sub(r'\s+', ' ', text).strip()

    def compare_claims(self, claims):
        """
        Compares a list of claims against the fact-checked data.
        
        :param claims: List of claims to compare.
        :return: List of comparison results.
        """
        verified_data = self.fetch_archive_data()
        results = []

        for claim in claims:
            cleaned_claim = self.clean_text(claim)
            matched = [data for data in verified_data if self.clean_text(data['claim']) == cleaned_claim]
            
            if matched:
                results.append({
                    'claim': cleaned_claim,
                    'status': 'Verified',
                    'details': matched
                })
            else:
                results.append({
                    'claim': cleaned_claim,
                    'status': 'Not Verified',
                    'details': None
                })
        
        return results

def main():
    # Example: Replace with the actual URL of the Tamil fact-checking archive
    fact_checker = FactChecker("https://api.factcrescendo.com/tamil-archive")

    # Sample claims to compare
    claims_to_check = [
        "இந்த செய்தி உண்மையாகும்.",
        "பொய் தகவல்கள் இங்கு உள்ளன."
    ]

    # Compare claims
    results = fact_checker.compare_claims(claims_to_check)

    # Output results
    for result in results:
        print(json.dumps(result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
```
