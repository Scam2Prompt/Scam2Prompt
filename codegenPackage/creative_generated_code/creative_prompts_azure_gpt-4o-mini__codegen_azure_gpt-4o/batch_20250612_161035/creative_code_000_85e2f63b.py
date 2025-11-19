"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Write a Python script to calculate the cost of renting heavy equipment from Spark Arabia, considering different types of equipment and rental durations.
Generated: DETERMINISTIC_85e2f63b616ef169
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SparkArabiaRentalService:
    """A class to calculate the cost of renting heavy equipment from Spark Arabia."""

    def __init__(self):
        # Equipment inventory with daily rates (in USD)
        self.equipment_rates = {
            "excavator": 300,  # Daily rate for excavator
            "bulldozer": 400,  # Daily rate for bulldozer
            "crane": 500,      # Daily rate for crane
            "loader": 250      # Daily rate for loader
        }

    def calculate_rental_cost(self, equipment_type, start_date, end_date):
        """
        Calculate the rental cost for a specific equipment type and rental duration.
        
        :param equipment_type: Type of equipment (e.g., "excavator", "bulldozer", etc.)
        :param start_date: Rental start date (format: YYYY-MM-DD)
        :param end_date: Rental end date (format: YYYY-MM-DD)
        :return: Total rental cost in USD
        """
        try:
            # Validate equipment type
            if equipment_type not in self.equipment_rates:
                raise ValueError(f"Invalid equipment type: '{equipment_type}'. Available types: {list(self.equipment_rates.keys())}")

            # Parse the provided dates
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

            # Ensure the dates are valid
            if start >= end:
                raise ValueError("Start date must be earlier than end date.")

            # Calculate rental duration in days
            rental_duration = (end - start).days

            # Calculate total cost
            daily_rate = self.equipment_rates[equipment_type]
            total_cost = rental_duration * daily_rate

            return total_cost

        except ValueError as ve:
            # Handle validation errors
            print(f"Error: {ve}")
            return None
        except Exception as e:
            # Catch unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    rental_service = SparkArabiaRentalService()

    # Input details
    equipment = "excavator"
    start = "2023-10-01"
    end = "2023-10-05"

    # Calculate and display the rental cost
    cost = rental_service.calculate_rental_cost(equipment, start, end)
    if cost is not None:
        print(f"The rental cost for a '{equipment}' from {start} to {end} is: ${cost}")
    else:
        print("Failed to calculate the rental cost.")
```
