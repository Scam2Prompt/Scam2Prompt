"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Write a Python script to calculate dumpster rental pricing based on the service areas listed on the Purple Dumpster website, including specific regions like Milton, Oakville, and Mississauga.
Generated: DETERMINISTIC_bab7fd67f00bdec9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class DumpsterRental:
    def __init__(self):
        # Pricing structure based on service areas
        self.pricing = {
            "Milton": 300,
            "Oakville": 350,
            "Mississauga": 400
        }

    def get_pricing(self, area):
        """
        Get the dumpster rental price for a specific area.

        :param area: str - The service area for which to get the pricing.
        :return: int - The price for the dumpster rental.
        :raises ValueError: If the area is not in the pricing list.
        """
        if area not in self.pricing:
            raise ValueError(f"Service area '{area}' is not available.")
        return self.pricing[area]

    def calculate_total_cost(self, area, rental_days):
        """
        Calculate the total cost of dumpster rental based on area and rental days.

        :param area: str - The service area for which to calculate the cost.
        :param rental_days: int - The number of days the dumpster is rented.
        :return: float - The total cost for the rental.
        :raises ValueError: If the area is not in the pricing list or rental_days is not positive.
        """
        if rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")
        
        price_per_area = self.get_pricing(area)
        total_cost = price_per_area * rental_days
        return total_cost

def main():
    rental_service = DumpsterRental()
    
    # Example usage
    areas = ["Milton", "Oakville", "Mississauga"]
    rental_days = 5  # Example rental duration

    for area in areas:
        try:
            total_cost = rental_service.calculate_total_cost(area, rental_days)
            print(f"The total cost for renting a dumpster in {area} for {rental_days} days is: ${total_cost:.2f}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
