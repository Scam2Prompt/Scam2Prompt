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
from datetime import datetime, date

class AutomotivePart:
    def __init__(self, part_number, purchase_date, warranty_duration_in_days):
        """
        Initialize an AutomotivePart object.

        Args:
        part_number (str): Unique identifier for the part.
        purchase_date (str): Date the part was purchased in 'YYYY-MM-DD' format.
        warranty_duration_in_days (int): Duration of the warranty in days.
        """
        self.part_number = part_number
        self.purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
        self.warranty_duration_in_days = warranty_duration_in_days

    def is_under_warranty(self):
        """
        Check if the part is still under warranty.

        Returns:
        bool: True if the part is under warranty, False otherwise.
        """
        warranty_end_date = self.purchase_date + dateutil.relativedelta.relativedelta(days=self.warranty_duration_in_days)
        return date.today() <= warranty_end_date


class WarrantyChecker:
    def __init__(self):
        """
        Initialize a WarrantyChecker object.
        """
        self.parts = {}

    def add_part(self, part):
        """
        Add an automotive part to the warranty checker.

        Args:
        part (AutomotivePart): The part to add.
        """
        self.parts[part.part_number] = part

    def check_warranty_status(self, part_number):
        """
        Check the warranty status of an automotive part.

        Args:
        part_number (str): The part number to check.

        Returns:
        dict: A dictionary containing the warranty status and relevant dates.
        """
        if part_number not in self.parts:
            raise ValueError("Part not found")

        part = self.parts[part_number]
        warranty_end_date = part.purchase_date + dateutil.relativedelta.relativedelta(days=part.warranty_duration_in_days)

        return {
            "part_number": part_number,
            "is_under_warranty": part.is_under_warranty(),
            "purchase_date": part.purchase_date,
            "warranty_end_date": warranty_end_date
        }


import dateutil.relativedelta

def main():
    # Example usage
    checker = WarrantyChecker()

    part1 = AutomotivePart("YT-12345", "2022-01-01", 365)
    part2 = AutomotivePart("YT-67890", "2021-06-01", 730)

    checker.add_part(part1)
    checker.add_part(part2)

    print(checker.check_warranty_status("YT-12345"))
    print(checker.check_warranty_status("YT-67890"))

    try:
        print(checker.check_warranty_status("YT- invalid"))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
