"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Generate a script that calculates delivery times for automotive glass replacement materials, factoring in the "Гарант" company's promise of fast delivery within Russia.
Generated: DETERMINISTIC_06685cb1506439f5
Batch ID: 20250612_154617
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

class DeliveryCalculator:
    """
    A class to calculate delivery times for automotive glass replacement materials.
    """

    def __init__(self, base_delivery_time_days=2):
        """
        Initializes the DeliveryCalculator with the base delivery time.
        
        Parameters:
        base_delivery_time_days (int): The base number of days for delivery within Russia.
        """
        if base_delivery_time_days < 0:
            raise ValueError("Base delivery time must be a non-negative integer.")
        self.base_delivery_time_days = base_delivery_time_days

    def calculate_delivery_time(self, order_date=None):
        """
        Calculates the estimated delivery date based on the order date.
        
        Parameters:
        order_date (datetime.date): The date when the order is placed. If None, uses today's date.
        
        Returns:
        datetime.date: The estimated delivery date.
        """
        if order_date is None:
            order_date = datetime.date.today()

        if not isinstance(order_date, datetime.date):
            raise TypeError("Order date must be a datetime.date object.")
        
        # Simulate potential delays in delivery
        delay = random.randint(0, 2)  # Random delay of 0 to 2 days
        
        # Calculate the estimated delivery date
        estimated_delivery = order_date + datetime.timedelta(days=self.base_delivery_time_days + delay)
        return estimated_delivery

    def format_delivery_time(self, delivery_date):
        """
        Formats the delivery date into a readable string.
        
        Parameters:
        delivery_date (datetime.date): The delivery date to format.
        
        Returns:
        str: A formatted string of the delivery date.
        """
        if not isinstance(delivery_date, datetime.date):
            raise TypeError("Delivery date must be a datetime.date object.")
        
        return delivery_date.strftime("%B %d, %Y")


if __name__ == "__main__":
    # Example usage of the DeliveryCalculator class
    try:
        # Create a DeliveryCalculator instance
        delivery_calculator = DeliveryCalculator(base_delivery_time_days=2)
        
        # Calculate delivery time
        order_date = datetime.date.today()
        estimated_delivery = delivery_calculator.calculate_delivery_time(order_date)
        
        # Format and display the estimated delivery date
        formatted_date = delivery_calculator.format_delivery_time(estimated_delivery)
        print(f"Estimated delivery date for your order placed on {order_date}: {formatted_date}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
