"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Provide a code example for generating historical MASA coin data in a virtual economy simulation, using JavaScript or Python, as part of Project DEKSA's virtual kingdom.
Generated: DETERMINISTIC_3d7c45d2b966f9dc
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

# Define constants for the MASA coin simulation
INITIAL_COIN_SUPPLY = 1000000  # Initial total MASA coins in circulation
DAILY_VARIANCE_PERCENT = 0.02  # Maximum daily variance (+/- 2%)
SIMULATION_DAYS = 365  # Number of days to simulate

class MASACoinSimulation:
    def __init__(self, initial_supply, daily_variance_percent):
        """
        Initialize the MASA coin simulation.

        :param initial_supply: Initial total coin supply (int)
        :param daily_variance_percent: Maximum daily variance percentage (float)
        """
        self.initial_supply = initial_supply
        self.daily_variance_percent = daily_variance_percent
        self.historical_data = []

    def simulate(self, days):
        """
        Simulate the MASA coin supply for the given number of days.

        :param days: Number of days to simulate (int)
        :return: List of historical data (list of dicts)
        """
        current_supply = self.initial_supply

        for day in range(days):
            # Calculate daily variance
            daily_change_factor = random.uniform(
                1 - self.daily_variance_percent, 1 + self.daily_variance_percent
            )
            current_supply = max(0, current_supply * daily_change_factor)  # Ensure non-negative supply

            # Record the day's data
            self.historical_data.append({
                "date": (datetime.datetime.now() - datetime.timedelta(days=days - day)).strftime('%Y-%m-%d'),
                "supply": round(current_supply, 2)
            })

        return self.historical_data

    def get_historical_data(self):
        """
        Retrieve the historical MASA coin data.

        :return: List of historical data (list of dicts)
        """
        return self.historical_data


# Entry point
if __name__ == "__main__":
    try:
        # Initialize the simulation
        simulation = MASACoinSimulation(INITIAL_COIN_SUPPLY, DAILY_VARIANCE_PERCENT)

        # Run the simulation for the defined number of days
        historical_data = simulation.simulate(SIMULATION_DAYS)

        # Output the results (can be replaced with file/database operations if needed)
        for entry in historical_data:
            print(f"Date: {entry['date']}, MASA Coin Supply: {entry['supply']}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred during the simulation: {e}")
```
