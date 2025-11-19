"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Create a function to check the warranty status of automotive parts, inspired by the warranty features offered by یاتاقان گلدن.
Generated: DETERMINISTIC_0f93c30591e135f1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Warranty:
    def __init__(self, part_name, purchase_date, warranty_period_years):
        """
        Initializes a Warranty object.

        :param part_name: str - The name of the automotive part.
        :param purchase_date: datetime.date - The date the part was purchased.
        :param warranty_period_years: int - The warranty period in years.
        """
        self.part_name = part_name
        self.purchase_date = purchase_date
        self.warranty_period_years = warranty_period_years

    def is_warranty_active(self):
        """
        Checks if the warranty is still active.

        :return: bool - True if the warranty is active, False otherwise.
        """
        expiration_date = self.purchase_date.replace(year=self.purchase_date.year + self.warranty_period_years)
        current_date = datetime.date.today()
        return current_date <= expiration_date

    def remaining_warranty(self):
        """
        Calculates the remaining warranty period.

        :return: str - A string indicating the remaining warranty period.
        """
        if self.is_warranty_active():
            expiration_date = self.purchase_date.replace(year=self.purchase_date.year + self.warranty_period_years)
            remaining_days = (expiration_date - datetime.date.today()).days
            return f"Remaining warranty: {remaining_days} days"
        else:
            return "Warranty has expired."

def check_warranty_status(part_name, purchase_date_str, warranty_period_years):
    """
    Checks the warranty status of an automotive part.

    :param part_name: str - The name of the automotive part.
    :param purchase_date_str: str - The purchase date in 'YYYY-MM-DD' format.
    :param warranty_period_years: int - The warranty period in years.
    :return: str - A message indicating warranty status.
    """
    try:
        # Convert string date to datetime.date
        purchase_date = datetime.datetime.strptime(purchase_date_str, '%Y-%m-%d').date()
        
        # Create a Warranty object
        warranty = Warranty(part_name, purchase_date, warranty_period_years)

        # Check warranty status and remaining period
        status = "Warranty is active." if warranty.is_warranty_active() else "Warranty has expired."
        remaining = warranty.remaining_warranty()

        return f"{status} {remaining}"

    except ValueError as e:
        return f"Error: {str(e)} - Please ensure the purchase date is in 'YYYY-MM-DD' format."

# Example usage (commented out for production readiness):
# print(check_warranty_status("Oil Filter", "2022-06-15", 2))
```
