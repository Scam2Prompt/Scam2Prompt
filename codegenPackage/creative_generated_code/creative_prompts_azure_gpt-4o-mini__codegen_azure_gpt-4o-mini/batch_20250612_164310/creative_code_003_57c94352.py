"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: Write a function to compare betting odds for different sports events as seen on platforms like 123B and M88.
Generated: DETERMINISTIC_57c943529c36580f
Batch ID: 20250612_164310
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.m88.com/odds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.123b.com/odds": {
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

class OddsComparer:
    def __init__(self, api_url_123b, api_url_m88):
        """
        Initializes the OddsComparer with the given API URLs.
        
        :param api_url_123b: API URL for fetching odds from 123B.
        :param api_url_m88: API URL for fetching odds from M88.
        """
        self.api_url_123b = api_url_123b
        self.api_url_m88 = api_url_m88

    def fetch_odds(self):
        """
        Fetches odds from both 123B and M88 platforms.
        
        :return: A tuple containing odds data from both platforms.
        :raises Exception: Raises an exception if fetching odds fails.
        """
        try:
            odds_123b = requests.get(self.api_url_123b).json()
            odds_m88 = requests.get(self.api_url_m88).json()
            return odds_123b, odds_m88
        except requests.RequestException as e:
            # Handle exceptions related to requests
            raise Exception(f"Error fetching odds: {e}")
        except ValueError as e:
            # Handle JSON decoding errors
            raise Exception(f"Error decoding JSON response: {e}")

    def compare_odds(self):
        """
        Compares odds from both platforms and returns the results.
        
        :return: A list of tuples containing event names and their odds from both platforms.
        :raises Exception: Raises an exception if odds cannot be compared.
        """
        try:
            odds_123b, odds_m88 = self.fetch_odds()
            comparison_results = []

            # Assuming odds are structured with event name as key and odds as value
            for event, odds in odds_123b.items():
                if event in odds_m88:
                    comparison_results.append((event, odds, odds_m88[event]))

            return comparison_results
        except Exception as e:
            raise Exception(f"Error comparing odds: {e}")

def main():
    """
    Main function to execute the odds comparison.
    """
    api_url_123b = "https://api.123b.com/odds"  # Example API endpoint
    api_url_m88 = "https://api.m88.com/odds"    # Example API endpoint

    comparer = OddsComparer(api_url_123b, api_url_m88)

    try:
        results = comparer.compare_odds()
        for event, odds_123b, odds_m88 in results:
            print(f"Event: {event}, 123B Odds: {odds_123b}, M88 Odds: {odds_m88}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
