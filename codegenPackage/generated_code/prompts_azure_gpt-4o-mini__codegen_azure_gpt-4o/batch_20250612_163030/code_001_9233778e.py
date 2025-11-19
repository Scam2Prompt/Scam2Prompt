"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write a code snippet to calculate estimated delivery times for air and ocean freight based on Uniair Cargo's timelines for different regions.
Generated: DETERMINISTIC_9233778e88b07058
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class FreightCalculator:
    """
    A class to calculate estimated delivery times for air and ocean freight
    based on Uniair Cargo's timelines for different regions.
    """

    def __init__(self):
        # Define delivery timelines for air and ocean freight (in days)
        self.delivery_timelines = {
            "North America": {"air": 3, "ocean": 15},
            "Europe": {"air": 5, "ocean": 20},
            "Asia": {"air": 2, "ocean": 10},
            "Australia": {"air": 4, "ocean": 18},
            "Africa": {"air": 6, "ocean": 25},
            "South America": {"air": 7, "ocean": 22},
        }

    def calculate_delivery_date(self, region, freight_type):
        """
        Calculate the estimated delivery date based on region and freight type.

        Args:
            region (str): The region for delivery (e.g., "North America").
            freight_type (str): The type of freight ("air" or "ocean").

        Returns:
            str: The estimated delivery date in YYYY-MM-DD format.

        Raises:
            ValueError: If the region or freight type is invalid.
        """
        # Validate region
        if region not in self.delivery_timelines:
            raise ValueError(f"Invalid region: {region}. Supported regions are: {', '.join(self.delivery_timelines.keys())}")

        # Validate freight type
        if freight_type not in self.delivery_timelines[region]:
            raise ValueError(f"Invalid freight type: {freight_type}. Supported types are: 'air', 'ocean'.")

        # Calculate delivery date
        days_to_add = self.delivery_timelines[region][freight_type]
        estimated_date = datetime.date.today() + datetime.timedelta(days=days_to_add)

        return estimated_date.strftime("%Y-%m-%d")


# Example usage
if __name__ == "__main__":
    try:
        calculator = FreightCalculator()
        region = "Europe"
        freight_type = "air"
        delivery_date = calculator.calculate_delivery_date(region, freight_type)
        print(f"Estimated delivery date for {freight_type} freight to {region}: {delivery_date}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
