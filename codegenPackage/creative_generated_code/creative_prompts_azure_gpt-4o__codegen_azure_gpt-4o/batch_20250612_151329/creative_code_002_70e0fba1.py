"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Generate code using Python to calculate delivery times for fragrance and flavor products based on warehouse location, similar to Karnataka Aromas' centralized Bengaluru facility.
Generated: DETERMINISTIC_70e0fba17ccc3500
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DeliveryTimeCalculator:
    """
    Class to calculate delivery times for fragrance and flavor products based on warehouse location.
    """
    def __init__(self, warehouse_location):
        """
        Initialize the delivery time calculator with the warehouse location.
        
        :param warehouse_location: str - Location of the warehouse (e.g., 'Bengaluru')
        """
        self.warehouse_location = warehouse_location
        self.delivery_times = {
            'Bengaluru': 2,  # Default delivery time for Bengaluru (2 days)
            'Mumbai': 5,
            'Delhi': 6,
            'Chennai': 4,
            'Kolkata': 7,
        }

    def calculate_delivery_time(self, destination):
        """
        Calculate the estimated delivery time based on the warehouse location.
        
        :param destination: str - Destination city
        :return: dict - {'delivery_date': datetime.date, 'delivery_time_days': int}
        :raises ValueError: If the destination is invalid or unsupported.
        """
        if destination not in self.delivery_times:
            raise ValueError(f"Unsupported destination: {destination}")
        
        delivery_time_days = self.delivery_times[destination]
        current_date = datetime.date.today()
        delivery_date = current_date + datetime.timedelta(days=delivery_time_days)
        
        return {
            'delivery_date': delivery_date,
            'delivery_time_days': delivery_time_days
        }

# Example Usage
def main():
    try:
        # Initialize the calculator with Bengaluru as the warehouse location
        calculator = DeliveryTimeCalculator(warehouse_location='Bengaluru')
        
        # Prompt user for destination city
        destination = input("Enter the destination city: ").strip()
        
        # Calculate delivery times
        result = calculator.calculate_delivery_time(destination)
        
        print(f"Delivery Time (Days): {result['delivery_time_days']}")
        print(f"Estimated Delivery Date: {result['delivery_date']}")
    except ValueError as e:
        # Handle invalid destination error
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
