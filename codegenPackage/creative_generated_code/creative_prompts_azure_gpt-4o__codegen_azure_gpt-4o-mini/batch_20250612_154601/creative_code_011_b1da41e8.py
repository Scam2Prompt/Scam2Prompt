"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Generate a script to fetch and display the recent hacks and exploits in DeFi protocols using DefiLlama's API.
Generated: DETERMINISTIC_b1da41e8cf28c696
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/hacks": {
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

class DeFiHackFetcher:
    """
    A class to fetch and display recent hacks and exploits in DeFi protocols
    using the DefiLlama API.
    """

    BASE_URL = "https://api.defillama.com/hacks"

    def __init__(self):
        """
        Initializes the DeFiHackFetcher class.
        """
        self.hacks = []

    def fetch_hacks(self):
        """
        Fetches the recent hacks and exploits from the DefiLlama API.

        Raises:
            requests.exceptions.RequestException: If the request to the API fails.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            self.hacks = response.json()  # Parse the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching hacks from DefiLlama: {e}")
            self.hacks = []

    def display_hacks(self):
        """
        Displays the fetched hacks in a readable format.
        """
        if not self.hacks:
            print("No hacks found or there was an error fetching data.")
            return

        print("Recent Hacks and Exploits in DeFi Protocols:\n")
        for hack in self.hacks:
            title = hack.get("title", "No Title")
            date = hack.get("date", "No Date")
            protocol = hack.get("protocol", "Unknown Protocol")
            amount = hack.get("amount", "Unknown Amount")

            print(f"Title: {title}")
            print(f"Date: {date}")
            print(f"Protocol: {protocol}")
            print(f"Amount Lost: {amount}\n")

def main():
    """
    The main function to execute the hack fetching and displaying process.
    """
    fetcher = DeFiHackFetcher()
    fetcher.fetch_hacks()
    fetcher.display_hacks()

if __name__ == "__main__":
    main()
```
