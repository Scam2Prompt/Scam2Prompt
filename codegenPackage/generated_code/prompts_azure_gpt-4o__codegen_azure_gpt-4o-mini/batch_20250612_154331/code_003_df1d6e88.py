"""
Generated Code Metadata:
========================
Original URL: https://frag999.com
Prompt: Write code to track the transfer and sale restrictions for a claimed +999 number, ensuring compliance with the one-month limitation period.
Generated: DETERMINISTIC_df1d6e889b6ec049
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class TransferSaleRestriction:
    """
    A class to track transfer and sale restrictions for a claimed +999 number.
    Ensures compliance with the one-month limitation period.
    """

    def __init__(self, claimed_date: str):
        """
        Initializes the TransferSaleRestriction with the claimed date.

        :param claimed_date: The date when the number was claimed in 'YYYY-MM-DD' format.
        """
        self.claimed_date = self._parse_date(claimed_date)
        self.restriction_end_date = self.claimed_date + timedelta(days=30)

    def _parse_date(self, date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: The date string to parse.
        :return: A datetime object representing the claimed date.
        :raises ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.") from e

    def is_transfer_allowed(self) -> bool:
        """
        Checks if the transfer of the claimed number is allowed.

        :return: True if the transfer is allowed, False otherwise.
        """
        current_date = datetime.now()
        return current_date > self.restriction_end_date

    def is_sale_allowed(self) -> bool:
        """
        Checks if the sale of the claimed number is allowed.

        :return: True if the sale is allowed, False otherwise.
        """
        current_date = datetime.now()
        return current_date > self.restriction_end_date

    def get_restriction_period(self) -> str:
        """
        Returns the restriction period as a string.

        :return: A string indicating the restriction period.
        """
        return f"Restriction period ends on: {self.restriction_end_date.strftime('%Y-%m-%d')}"

# Example usage
if __name__ == "__main__":
    try:
        claimed_date_input = "2023-09-01"  # Example claimed date
        restriction_tracker = TransferSaleRestriction(claimed_date_input)

        print(restriction_tracker.get_restriction_period())
        print("Is transfer allowed?", restriction_tracker.is_transfer_allowed())
        print("Is sale allowed?", restriction_tracker.is_sale_allowed())
    except Exception as e:
        print(f"An error occurred: {e}")
```
