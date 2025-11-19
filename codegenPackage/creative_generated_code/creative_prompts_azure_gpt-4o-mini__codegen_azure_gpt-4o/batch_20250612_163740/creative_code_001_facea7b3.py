"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Write a Python script that implements revenue management techniques for a hotel, based on the principles taught in the International Tourism & Hospitality Management course at Hampton's.
Generated: DETERMINISTIC_facea7b39b66392b
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hotel Revenue Management Script
This script implements basic revenue management techniques for optimizing hotel revenue.
It uses dynamic pricing based on demand, seasonal patterns, and occupancy rates.
"""

import datetime
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HotelRevenueManagement:
    def __init__(self, base_rate, max_rate, occupancy_threshold, seasonal_multiplier):
        """
        Initialize the hotel revenue management system.

        :param base_rate: The default rate per room per night.
        :param max_rate: The maximum rate per room per night during peak demand.
        :param occupancy_threshold: The percentage occupancy that triggers dynamic pricing.
        :param seasonal_multiplier: Dict containing seasonal rate multipliers (e.g., {"summer": 1.5, "winter": 0.8}).
        """
        self.base_rate = base_rate
        self.max_rate = max_rate
        self.occupancy_threshold = occupancy_threshold
        self.seasonal_multiplier = seasonal_multiplier

    def determine_season(self):
        """
        Determine the current season based on the month.
        :return: A string representing the current season (e.g., "summer").
        """
        month = datetime.datetime.now().month
        if month in [6, 7, 8]:
            return "summer"
        elif month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        else:
            return "autumn"

    def calculate_price(self, current_occupancy):
        """
        Calculate the dynamic price per room based on occupancy and seasonal factors.

        :param current_occupancy: Current hotel occupancy percentage (0-100).
        :return: The dynamically calculated room price.
        """
        try:
            # Validate input
            if not (0 <= current_occupancy <= 100):
                raise ValueError("Occupancy percentage must be between 0 and 100.")

            # Determine the base price, adjusted for season
            season = self.determine_season()
            seasonal_rate = self.seasonal_multiplier.get(season, 1)
            price = self.base_rate * seasonal_rate

            # Apply dynamic pricing based on occupancy
            if current_occupancy >= self.occupancy_threshold:
                # Higher demand increases price closer to max rate
                price += (self.max_rate - self.base_rate) * (current_occupancy / 100)

            # Ensure final price is capped at max_rate
            price = min(price, self.max_rate)

            logging.info(f"Calculated price: ${price:.2f} (Season: {season}, Occupancy: {current_occupancy}%)")
            return round(price, 2)
        except Exception as e:
            logging.error(f"Error in calculating price: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Revenue management configuration
    base_rate = 100  # Default room price
    max_rate = 300   # Peak price
    occupancy_threshold = 70  # Trigger dynamic pricing if occupancy >= 70%
    seasonal_multiplier = {
        "summer": 1.5,
        "winter": 0.8,
        "spring": 1.2,
        "autumn": 1.0
    }

    # Initialize the revenue management system
    hotel_rm = HotelRevenueManagement(base_rate, max_rate, occupancy_threshold, seasonal_multiplier)

    # Example: Calculate price for current occupancy
    current_occupancy = 75  # Example occupancy percentage
    room_price = hotel_rm.calculate_price(current_occupancy)

    if room_price is not None:
        print(f"The room price for {current_occupancy}% occupancy is ${room_price:.2f}.")
    else:
        print("Failed to calculate room price.")
```
