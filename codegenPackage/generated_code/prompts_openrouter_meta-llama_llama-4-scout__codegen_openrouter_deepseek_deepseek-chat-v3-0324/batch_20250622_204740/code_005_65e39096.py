"""
Generated Code Metadata:
========================
Original URL: https://www.insectshieldzoro.com
Prompt: "Design a warranty policy for insect screen products, considering a 5-year warranty period, and create a Python code to calculate warranty expiration dates."
Generated: DETERMINISTIC_65e39096ee00cd5c
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Optional

class WarrantyPolicy:
    """
    A class to represent a warranty policy for insect screen products.
    
    Attributes:
        warranty_period_years (int): The warranty period in years (default is 5).
    """
    
    def __init__(self, warranty_period_years: int = 5):
        """
        Initialize the WarrantyPolicy with the given warranty period.
        
        Args:
            warranty_period_years (int): The warranty period in years (default is 5).
            
        Raises:
            ValueError: If warranty_period_years is not a positive integer.
        """
        if not isinstance(warranty_period_years, int) or warranty_period_years <= 0:
            raise ValueError("Warranty period must be a positive integer.")
        self.warranty_period_years = warranty_period_years
    
    def calculate_expiration_date(self, purchase_date: str) -> Optional[str]:
        """
        Calculate the warranty expiration date based on the purchase date.
        
        Args:
            purchase_date (str): The purchase date in 'YYYY-MM-DD' format.
            
        Returns:
            Optional[str]: The expiration date in 'YYYY-MM-DD' format, or None if input is invalid.
        """
        try:
            purchase_date_obj = datetime.strptime(purchase_date, "%Y-%m-%d").date()
            expiration_date = purchase_date_obj + timedelta(days=self.warranty_period_years * 365)
            return expiration_date.strftime("%Y-%m-%d")
        except ValueError:
            return None

def main():
    """Demonstrate the usage of the WarrantyPolicy class."""
    warranty = WarrantyPolicy()
    
    while True:
        print("\nInsect Screen Warranty Calculator")
        print("1. Calculate warranty expiration date")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            expiration_date = warranty.calculate_expiration_date(purchase_date)
            
            if expiration_date:
                print(f"Warranty expires on: {expiration_date}")
            else:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
```
