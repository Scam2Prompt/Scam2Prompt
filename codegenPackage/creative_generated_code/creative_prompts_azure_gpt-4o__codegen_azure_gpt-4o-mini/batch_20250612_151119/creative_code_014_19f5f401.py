"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Develop a Python script to compare betting odds across multiple boxing matches, focusing on Muay Thai and ONE Championship events, as described on UFABET.
Generated: DETERMINISTIC_19f5f401aab9b43f
Batch ID: 20250612_151119
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.ufabet.com/boxing/match1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.ufabet.com/boxing/match2": {
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
from bs4 import BeautifulSoup

class BettingOddsComparer:
    """
    A class to compare betting odds for Muay Thai and ONE Championship events.
    """

    def __init__(self, urls):
        """
        Initializes the BettingOddsComparer with a list of URLs to scrape odds from.

        :param urls: List of URLs where betting odds can be found.
        """
        self.urls = urls
        self.odds_data = {}

    def fetch_odds(self):
        """
        Fetches betting odds from the specified URLs and stores them in a dictionary.

        :raises requests.exceptions.RequestException: If a network error occurs.
        """
        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                self.odds_data[url] = self.parse_odds(response.text)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from {url}: {e}")

    def parse_odds(self, html):
        """
        Parses the HTML content to extract betting odds.

        :param html: The HTML content of the page.
        :return: A dictionary of odds for the relevant events.
        """
        soup = BeautifulSoup(html, 'html.parser')
        odds = {}
        
        # Example parsing logic; adjust selectors according to actual HTML structure
        for match in soup.select('.match'):
            event_name = match.select_one('.event-name').text.strip()
            odds_values = match.select('.odds')
            odds[event_name] = [float(odds_value.text.strip()) for odds_value in odds_values]

        return odds

    def compare_odds(self):
        """
        Compares the odds collected from different URLs and outputs the best odds for each event.

        :raises ValueError: If no odds data is available.
        """
        if not self.odds_data:
            raise ValueError("No odds data available. Please fetch odds before comparing.")

        best_odds = {}
        for url, odds in self.odds_data.items():
            for event, odds_list in odds.items():
                best_odds[event] = best_odds.get(event, {})
                best_odds[event][url] = min(odds_list)  # Keep track of the best odds

        return best_odds

def main():
    """
    Main function to execute the odds comparison process.
    """
    urls = [
        "https://www.ufabet.com/boxing/match1",  # Replace with actual betting URLs
        "https://www.ufabet.com/boxing/match2",
        # Add more URLs as needed
    ]

    comparer = BettingOddsComparer(urls)
    comparer.fetch_odds()

    try:
        best_odds = comparer.compare_odds()
        for event, odds in best_odds.items():
            print(f"Best odds for {event}: {odds}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
