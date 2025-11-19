"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Create a function to check the warranty status of automotive parts, inspired by the warranty features offered by یاتاقان گلدن.
Generated: DETERMINISTIC_0f93c30591e135f1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Warranty:
    def __init__(self, part_name, purchase_date, warranty_period_years):
        """
        Initializes a Warranty object.

        :param part_name: Name of the automotive part
        :param purchase_date: Date of purchase (YYYY-MM-DD)
        :param warranty_period_years: Warranty period in years
        """
        self.part_name = part_name
        self.purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d").date()
        self.warranty_period_years = warranty_period_years

    def is_warranty_valid(self):
        """
        Checks if the warranty is still valid.

        :return: True if warranty is valid, False otherwise
        """
        current_date = datetime.date.today()
        warranty_expiration_date = self.purchase_date.replace(year=self.purchase_date.year + self.warranty_period_years)
        return current_date <= warranty_expiration_date

    def warranty_status(self):
        """
        Returns the warranty status of the part.

        :return: A string indicating the warranty status
        """
        if self.is_warranty_valid():
            return f"The warranty for '{self.part_name}' is still valid."
        else:
            return f"The warranty for '{self.part_name}' has expired."

def main():
    """
    Main function to demonstrate the warranty checking functionality.
    """
    try:
        # Example usage
        part_name = "Engine Oil Filter"
        purchase_date = "2022-05-15"
        warranty_period_years = 2

        # Create a Warranty object
        warranty = Warranty(part_name, purchase_date, warranty_period_years)

        # Check and print the warranty status
        print(warranty.warranty_status())

    except ValueError as e:
        print(f"Error: {e}. Please ensure the purchase date is in YYYY-MM-DD format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
