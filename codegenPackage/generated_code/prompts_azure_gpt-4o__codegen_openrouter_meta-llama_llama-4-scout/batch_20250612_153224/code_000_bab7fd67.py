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
# dumpster_rental_pricing.py

class DumpsterRentalPricing:
    def __init__(self):
        # Define service areas and their respective pricing
        self.service_areas = {
            "Milton": {"small": 350, "medium": 450, "large": 550},
            "Oakville": {"small": 400, "medium": 500, "large": 600},
            "Mississauga": {"small": 450, "medium": 550, "large": 650},
            # Add more service areas as needed
        }

    def calculate_pricing(self, area, dumpster_size, rental_days):
        """
        Calculate dumpster rental pricing based on service area, dumpster size, and rental days.

        Args:
            area (str): Service area (e.g., Milton, Oakville, Mississauga)
            dumpster_size (str): Dumpster size (e.g., small, medium, large)
            rental_days (int): Number of rental days

        Returns:
            float: Total rental pricing

        Raises:
            ValueError: If service area or dumpster size is invalid
        """
        if area not in self.service_areas:
            raise ValueError(f"Invalid service area: {area}")
        if dumpster_size not in self.service_areas[area]:
            raise ValueError(f"Invalid dumpster size: {dumpster_size} for area {area}")

        base_price = self.service_areas[area][dumpster_size]
        daily_rate = 50  # Daily rate for additional days
        if rental_days <= 7:
            return base_price
        else:
            return base_price + (rental_days - 7) * daily_rate

    def get_service_areas(self):
        """
        Get a list of available service areas.

        Returns:
            list: List of service areas
        """
        return list(self.service_areas.keys())

    def get_dumpster_sizes(self, area):
        """
        Get a list of available dumpster sizes for a given service area.

        Args:
            area (str): Service area

        Returns:
            list: List of dumpster sizes

        Raises:
            ValueError: If service area is invalid
        """
        if area not in self.service_areas:
            raise ValueError(f"Invalid service area: {area}")
        return list(self.service_areas[area].keys())


def main():
    try:
        pricing = DumpsterRentalPricing()
        print("Service Areas:")
        for area in pricing.get_service_areas():
            print(area)

        area = input("Enter service area: ")
        dumpster_size = input("Enter dumpster size (small, medium, large): ")
        rental_days = int(input("Enter rental days: "))

        total_price = pricing.calculate_pricing(area, dumpster_size, rental_days)
        print(f"Total Rental Pricing: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
