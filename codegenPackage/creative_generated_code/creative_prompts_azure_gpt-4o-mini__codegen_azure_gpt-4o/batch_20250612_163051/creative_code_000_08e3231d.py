"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimimart.com
Prompt: Generate a code snippet for implementing a 30-day return policy for an e-commerce website similar to ChicEuroTrendz.
Generated: DETERMINISTIC_08e3231d7abbc318
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class ReturnPolicy:
    """
    A class representing the 30-day return policy for an e-commerce website.
    """
    def __init__(self):
        """
        Initialize the return policy class.
        """
        self.return_window_days = 30

    def is_return_eligible(self, purchase_date):
        """
        Check if a product is eligible for return based on the purchase date.

        :param purchase_date: str - The purchase date in 'YYYY-MM-DD' format.
        :return: bool - True if eligible for return, False otherwise.
        """
        try:
            # Parse the input date string into a datetime object
            purchase_date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
            
            # Calculate the return deadline
            return_deadline = purchase_date_obj + timedelta(days=self.return_window_days)
            
            # Compare return deadline with today's date
            if datetime.now() < return_deadline:
                return True
            else:
                return False
        except ValueError:
            # Handle invalid date format
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
            return False


# Example usage
if __name__ == "__main__":
    # Instantiate the ReturnPolicy
    policy = ReturnPolicy()
    
    # Example purchase date
    purchase_date = "2023-09-15"
    
    # Check eligibility for return
    if policy.is_return_eligible(purchase_date):
        print("The product is eligible for return.")
    else:
        print("The product is NOT eligible for return.")
```
