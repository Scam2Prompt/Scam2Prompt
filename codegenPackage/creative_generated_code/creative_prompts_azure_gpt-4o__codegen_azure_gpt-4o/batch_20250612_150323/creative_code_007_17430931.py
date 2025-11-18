"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strki.com
Prompt: Develop a program to maximize rental income using dynamic pricing algorithms, similar to the strategies offered by strki.com.
Generated: DETERMINISTIC_174309311cc7b6bf
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class RentalProperty:
    def __init__(self, base_price, occupancy_rate, seasonality_factor):
        """
        Initializes the RentalProperty instance

        :param base_price: Base price per night for the property
        :param occupancy_rate: Historical occupancy rate (0-1)
        :param seasonality_factor: A multiplier for seasonal adjustments
        """
        self.base_price = base_price
        self.occupancy_rate = occupancy_rate
        self.seasonality_factor = seasonality_factor

    def calculate_dynamic_price(self, demand_factor):
        """
        Calculates the dynamic price for the property based on various factors

        :param demand_factor: A factor representing current demand (0-2)
        :return: The dynamically calculated price
        """
        # Formula to dynamically adjust price
        dynamic_price = (self.base_price *
                         self.occupancy_rate *
                         self.seasonality_factor *
                         demand_factor)
        # Ensure the price is rounded to 2 decimal places for currency presentation
        return round(dynamic_price, 2)


class DynamicPricingManager:
    def __init__(self, properties):
        """
        Initializes the DynamicPricingManager with a list of rental properties

        :param properties: A list of RentalProperty instances
        """
        self.properties = properties

    def get_seasonality_factor(self, date):
        """
        Determines the seasonality factor based on the given date

        :param date: The current date
        :return: A seasonal multiplier (e.g., higher for holidays)
        """
        # Adjust seasonality factor based on month or specific holidays
        if date.month in [6, 7, 8]:  # Summer peak season
            return 1.5
        elif date.month in [12, 1]:  # Winter holidays
            return 1.8
        elif date.weekday() in [4, 5]:  # Weekends
            return 1.2
        else:
            return 1.0

    def get_demand_factor(self):
        """
        Simulates the demand factor based on market trends, last-minute bookings, etc.

        :return: A demand multiplier (random for simplicity)
        """
        return round(random.uniform(0.8, 1.5), 2)

    def optimize_prices(self, date):
        """
        Optimizes rental prices for all properties

        :param date: The current date
        :return: A dictionary of property prices (property index -> price)
        """
        optimized_prices = {}
        seasonality_factor = self.get_seasonality_factor(date)

        for i, property in enumerate(self.properties):
            # Assign seasonal factor dynamically to the property
            property.seasonality_factor = seasonality_factor

            demand_factor = self.get_demand_factor()
            optimized_price = property.calculate_dynamic_price(demand_factor)

            optimized_prices[f'Property_{i+1}'] = optimized_price

        return optimized_prices


def main():
    """
    Entry point for the program
    """
    # Example: List of rental properties with base prices and occupancy rates
    properties = [
        RentalProperty(base_price=100, occupancy_rate=0.85, seasonality_factor=1.0),
        RentalProperty(base_price=150, occupancy_rate=0.90, seasonality_factor=1.0),
        RentalProperty(base_price=200, occupancy_rate=0.80, seasonality_factor=1.0)
    ]

    # Initialize dynamic pricing manager
    pricing_manager = DynamicPricingManager(properties)

    # Get the current date
    current_date = datetime.date.today()

    try:
        # Optimize prices for the current date
        optimized_prices = pricing_manager.optimize_prices(current_date)

        # Print optimized prices
        print("Optimized Rental Prices:")
        for property_name, price in optimized_prices.items():
            print(f"{property_name}: ${price}")
    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
