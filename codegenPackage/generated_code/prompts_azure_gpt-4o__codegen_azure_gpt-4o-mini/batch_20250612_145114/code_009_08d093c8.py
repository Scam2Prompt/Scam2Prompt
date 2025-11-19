"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Generate a script to calculate the transferable warranty period for new roof installations, based on King Roofing's 5-year warranty policy.
Generated: DETERMINISTIC_08d093c8922b90d5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class RoofWarranty:
    """
    A class to represent the warranty period for new roof installations.
    """

    def __init__(self, installation_date: str):
        """
        Initializes the RoofWarranty instance.

        :param installation_date: The date of roof installation in 'YYYY-MM-DD' format.
        """
        self.installation_date = self._validate_date(installation_date)
        self.warranty_period = timedelta(days=5 * 365)  # 5 years warranty period

    def _validate_date(self, date_str: str) -> datetime:
        """
        Validates the installation date format and converts it to a datetime object.

        :param date_str: The date string to validate.
        :return: A datetime object representing the installation date.
        :raises ValueError: If the date format is incorrect.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.") from e

    def calculate_transferable_warranty(self) -> str:
        """
        Calculates the end date of the transferable warranty period.

        :return: A string representing the end date of the warranty period.
        """
        warranty_end_date = self.installation_date + self.warranty_period
        return warranty_end_date.strftime('%Y-%m-%d')

def main():
    """
    Main function to execute the warranty calculation.
    """
    installation_date = input("Enter the roof installation date (YYYY-MM-DD): ")
    
    try:
        roof_warranty = RoofWarranty(installation_date)
        warranty_end_date = roof_warranty.calculate_transferable_warranty()
        print(f"The transferable warranty period ends on: {warranty_end_date}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
