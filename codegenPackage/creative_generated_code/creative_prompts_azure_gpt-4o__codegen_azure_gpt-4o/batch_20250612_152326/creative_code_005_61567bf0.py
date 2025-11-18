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
  "https://api.example.com/wemix/exchange_rate": {
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
from datetime import datetime


class ExchangeRateTracker:
    """
    A class to track WEMIX exchange rate changes and simulate staking rewards accumulation.
    """

    def __init__(self, api_url: str, staking_rate: float):
        """
        Initialize the ExchangeRateTracker.
        Args:
            api_url (str): The endpoint to fetch WEMIX exchange rate data.
            staking_rate (float): Annual staking rate in percentage (e.g., 10 for 10%).
        """
        self.api_url = api_url
        self.staking_rate = staking_rate / 100  # Convert percentage to a decimal
        self.exchange_rate_history = []  # To store historical exchange rates
        self.staking_rewards = 0.0  # Accumulated staking rewards
        self.last_update_time = None  # Timestamp of the last update

    def fetch_exchange_rate(self) -> float:
        """
        Fetch the current WEMIX exchange rate from the API.
        Returns:
            float: The current exchange rate.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()
            # Assume the API returns a JSON object with a field 'exchange_rate'
            return float(data['exchange_rate'])
        except requests.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None
        except KeyError:
            print("Error: Unexpected response format. 'exchange_rate' not found.")
            return None

    def update_exchange_rate(self):
        """
        Update the exchange rate and record to the history.
        """
        current_rate = self.fetch_exchange_rate()
        if current_rate is not None:
            timestamp = datetime.now()
            self.exchange_rate_history.append((timestamp, current_rate))
            self.last_update_time = timestamp
            print(f"{timestamp}: Exchange rate updated to {current_rate}")
        else:
            print("Failed to update exchange rate.")

    def simulate_staking_rewards(self, principal: float, time_interval_in_seconds: int):
        """
        Simulate staking rewards accumulation.
        Args:
            principal (float): Initial amount staked.
            time_interval_in_seconds (int): Time interval for simulation in seconds.
        """
        if self.last_update_time is None:
            print("Error: Exchange rate must be updated at least once before simulating rewards.")
            return

        # Formula for staking rewards: R = P * (r / 365) * (t / 86400)
        # Where:
        # P = principal, r = annual staking rate, t = time interval in seconds
        staking_reward = principal * (self.staking_rate / 365) * (time_interval_in_seconds / 86400)
        self.staking_rewards += staking_reward
        print(f"Staking rewards accumulated: {staking_reward:.8f} WEMIX")
        print(f"Total staking rewards: {self.staking_rewards:.8f} WEMIX")

    def get_exchange_rate_history(self):
        """
        Get the history of exchange rates.
        Returns:
            list: A list of tuples containing timestamps and exchange rates.
        """
        return self.exchange_rate_history

    def run_tracker(self, principal: float, update_interval: int, simulation_interval: int, duration: int):
        """
        Run the tracker to continuously update exchange rates and simulate staking rewards.
        Args:
            principal (float): Initial amount staked.
            update_interval (int): Interval for updating exchange rate in seconds.
            simulation_interval (int): Interval for simulating staking rewards in seconds.
            duration (int): Total duration to run the tracker in seconds.
        """
        start_time = time.time()
        while (time.time() - start_time) < duration:
            self.update_exchange_rate()
            self.simulate_staking_rewards(principal, simulation_interval)
            time.sleep(update_interval)

        print("Tracker stopped. Final exchange rate history and staking rewards:")
        print(self.get_exchange_rate_history())
        print(f"Total staking rewards: {self.staking_rewards:.8f} WEMIX")


# Example usage:

if __name__ == "__main__":
    # Replace 'API_URL' with the actual API endpoint providing the exchange rate
    API_URL = "https://api.example.com/wemix/exchange_rate"
    ANNUAL_STAKING_RATE = 10.0  # Annual staking rate in percentage
    INITIAL_PRINCIPAL = 1000  # Initial staked amount in WEMIX
    UPDATE_INTERVAL = 60  # Update exchange rate every 60 seconds
    SIMULATION_INTERVAL = 60  # Simulate staking rewards every 60 seconds
    DURATION = 3600  # Run tracker for 3600 seconds (1 hour)

    tracker = ExchangeRateTracker(API_URL, ANNUAL_STAKING_RATE)
    tracker.run_tracker(INITIAL_PRINCIPAL, UPDATE_INTERVAL, SIMULATION_INTERVAL, DURATION)
```
