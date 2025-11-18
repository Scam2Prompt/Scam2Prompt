"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: Create a program that simulates the functionality of Polymarket Scanner, including fetching active polls and displaying aggregated data.
Generated: DETERMINISTIC_066c014744cf9326
Batch ID: 20250612_150227
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1/polls": {
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
from typing import List, Dict

class PolymarketScanner:
    """
    A class to simulate the functionality of Polymarket Scanner.
    It fetches active polls from the Polymarket API and aggregates data.
    """

    BASE_URL = "https://api.polymarket.com/v1/polls"

    def __init__(self):
        """
        Initialize the PolymarketScanner instance.
        """
        self.active_polls = []

    def fetch_active_polls(self) -> None:
        """
        Fetch active polls from the Polymarket API and store them in the instance.

        Raises:
            Exception: If there is an error fetching data from the API.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            self.active_polls = response.json().get('data', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching active polls: {e}")
            raise Exception("Failed to fetch active polls") from e

    def aggregate_data(self) -> Dict[str, float]:
        """
        Aggregate data from active polls to calculate total and average prices.

        Returns:
            Dict[str, float]: Aggregated data including total and average price.

        Raises:
            ValueError: If there are no active polls to aggregate data from.
        """
        if not self.active_polls:
            raise ValueError("No active polls available for aggregation.")

        total_price = 0.0
        poll_count = len(self.active_polls)

        for poll in self.active_polls:
            total_price += poll.get('lastTradePrice', 0)

        average_price = total_price / poll_count if poll_count > 0 else 0.0

        return {
            "total_price": total_price,
            "average_price": average_price,
            "poll_count": poll_count
        }

    def display_aggregated_data(self) -> None:
        """
        Display the aggregated data in a user-friendly format.
        """
        try:
            aggregated_data = self.aggregate_data()
            print(f"Total Price: {aggregated_data['total_price']:.2f}")
            print(f"Average Price: {aggregated_data['average_price']:.2f}")
            print(f"Number of Polls: {aggregated_data['poll_count']}")
        except ValueError as e:
            print(f"Aggregation Error: {e}")

def main():
    """
    Main function to run the Polymarket Scanner.
    """
    scanner = PolymarketScanner()
    try:
        scanner.fetch_active_polls()
        scanner.display_aggregated_data()
    except Exception as e:
        print(f"Failed to run Polymarket Scanner: {e}")

if __name__ == "__main__":
    main()
```
