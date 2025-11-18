"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Write a program to calculate delivery timelines for shipments based on the "on-time delivery" commitment of Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_dbd18440adc14417
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DeliveryCalculator:
    """
    A class to calculate delivery timelines based on 'on-time delivery' commitments.
    """

    def __init__(self, commitment_days):
        """
        Initializes the DeliveryCalculator with the company's 'on-time delivery' commitment.
        
        :param commitment_days: int - The number of days within which delivery is promised.
        """
        if commitment_days <= 0:
            raise ValueError("Commitment days must be a positive integer.")
        self.commitment_days = commitment_days

    def calculate_delivery_date(self, order_date):
        """
        Calculates the expected delivery date based on the order date and commitment days.
        
        :param order_date: str - The order date in the format 'YYYY-MM-DD'.
        :return: str - The expected delivery date in the format 'YYYY-MM-DD'.
        """
        try:
            # Parse the order date
            order_date_obj = datetime.datetime.strptime(order_date, "%Y-%m-%d").date()
            
            # Calculate the delivery date
            delivery_date_obj = order_date_obj + datetime.timedelta(days=self.commitment_days)
            
            return delivery_date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid order date format: {e}")

def main():
    """
    Main function to interact with the DeliveryCalculator.
    """
    try:
        # Input: Company's on-time delivery commitment in days
        commitment_days = int(input("Enter the company's 'on-time delivery' commitment in days: "))
        
        # Create an instance of DeliveryCalculator
        delivery_calculator = DeliveryCalculator(commitment_days)
        
        # Input: Order Date
        order_date = input("Enter the order date (YYYY-MM-DD): ")
        
        # Calculate and print the delivery date
        delivery_date = delivery_calculator.calculate_delivery_date(order_date)
        print(f"Expected delivery date: {delivery_date}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
