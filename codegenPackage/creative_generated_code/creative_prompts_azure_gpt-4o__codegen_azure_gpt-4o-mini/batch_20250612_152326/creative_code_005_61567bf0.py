"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wemix-shoebill.pages.dev
Prompt: Develop a program to track stWEMIX exchange rate changes over time and simulate the staking rewards accumulation process described on the Shoebill Finance webpage.
Generated: DETERMINISTIC_61567bf010f64f24
Batch ID: 20250612_152326
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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
import time
from datetime import datetime, timedelta

class StWEMIXTracker:
    """
    A class to track stWEMIX exchange rate changes and simulate staking rewards.
    """

    BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
    CURRENCY = "wemix"  # Currency to track (stWEMIX)
    REWARD_RATE = 0.1  # Simulated annual reward rate (10%)
    STAKING_PERIOD_DAYS = 365  # Staking period in days

    def __init__(self):
        self.exchange_rates = []  # List to store exchange rate history
        self.start_time = datetime.now()  # Track when the tracking starts

    def fetch_exchange_rate(self):
        """
        Fetches the current exchange rate for stWEMIX from the CoinGecko API.
        Returns the current exchange rate in WEMIX.
        """
        try:
            response = requests.get(self.BASE_URL, params={'ids': 'wemix', 'vs_currencies': 'usd'})
            response.raise_for_status()  # Raises an error for bad responses
            data = response.json()
            return data[self.CURRENCY]['usd']
        except (requests.RequestException, KeyError) as e:
            print(f"Error fetching exchange rate: {e}")
            return None

    def simulate_staking(self, initial_amount, days):
        """
        Simulates the staking process and calculates accumulated rewards.
        :param initial_amount: Initial amount staked in USD
        :param days: Number of days to simulate staking
        :return: Total amount after staking period
        """
        total_amount = initial_amount
        for _ in range(days):
            rewards = total_amount * (self.REWARD_RATE / 365)  # Daily rewards
            total_amount += rewards
        return total_amount

    def track_exchange_rates(self, duration_days, interval_seconds):
        """
        Tracks the exchange rates over a specified duration and interval.
        :param duration_days: Number of days to track
        :param interval_seconds: Interval in seconds for fetching rates
        """
        end_time = datetime.now() + timedelta(days=duration_days)
        while datetime.now() < end_time:
            rate = self.fetch_exchange_rate()
            if rate is not None:
                self.exchange_rates.append((datetime.now(), rate))
                print(f"Fetched rate: {rate} on {datetime.now()}")
            time.sleep(interval_seconds)

    def display_exchange_history(self):
        """
        Displays the tracked exchange rate history.
        """
        print("Exchange Rate History:")
        for timestamp, rate in self.exchange_rates:
            print(f"{timestamp}: {rate} USD")

if __name__ == "__main__":
    tracker = StWEMIXTracker()

    # Track exchange rates for 7 days, fetching every hour (3600 seconds)
    tracker.track_exchange_rates(duration_days=7, interval_seconds=3600)

    # Simulate staking of $1000 for the defined staking period
    initial_stake = 1000  # USD
    total_after_staking = tracker.simulate_staking(initial_amount=initial_stake, days=StWEMIXTracker.STAKING_PERIOD_DAYS)

    print(f"Total amount after staking for {StWEMIXTracker.STAKING_PERIOD_DAYS} days: ${total_after_staking:.2f}")

    # Display the tracked exchange rate history
    tracker.display_exchange_history()
```
