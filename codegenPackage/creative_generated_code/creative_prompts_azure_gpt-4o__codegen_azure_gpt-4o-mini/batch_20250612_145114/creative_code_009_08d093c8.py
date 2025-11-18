"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Generate a script to calculate the transferable warranty period for new roof installations, based on King Roofing's 5-year warranty policy.
Generated: DETERMINISTIC_08d093c8922b90d5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class WarrantyPeriodCalculator:
    def __init__(self, installation_date: str):
        """
        Initializes the WarrantyPeriodCalculator with the installation date.

        :param installation_date: The date when the roof was installed in 'YYYY-MM-DD' format
        """
        self.installation_date = self._parse_date(installation_date)
        self.warranty_period_years = 5  # King Roofing's warranty period in years

    def _parse_date(self, date_str: str) -> datetime:
        """
        Parses the installation date from a string to a datetime object.

        :param date_str: The date string in 'YYYY-MM-DD' format
        :return: A datetime object representing the installation date
        :raises ValueError: If the date_str is not in the correct format
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def calculate_transferable_warranty_end_date(self) -> datetime:
        """
        Calculates the end date of the transferable warranty period.

        :return: The end date of the warranty as a datetime object
        """
        return self.installation_date + timedelta(days=self.warranty_period_years * 365)

    def get_warranty_details(self) -> dict:
        """
        Retrieves the warranty details including installation date and warranty end date.

        :return: A dictionary containing installation date and warranty end date
        """
        warranty_end_date = self.calculate_transferable_warranty_end_date()
        return {
            'installation_date': self.installation_date.date(),
            'transferable_warranty_end_date': warranty_end_date.date(),
            'warranty_period_years': self.warranty_period_years
        }

# Example usage:
if __name__ == "__main__":
    try:
        installation_date_input = input("Enter the roof installation date (YYYY-MM-DD): ")
        warranty_calculator = WarrantyPeriodCalculator(installation_date_input)
        warranty_details = warranty_calculator.get_warranty_details()

        print(f"Warranty details: {warranty_details}")
    except Exception as e:
        print(f"Error: {e}")
```
