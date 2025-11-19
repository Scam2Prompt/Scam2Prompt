"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Generate Python code to model the YTD return calculation for the ARK Venture Fund, using the fund's inception date and current NAV.
Generated: DETERMINISTIC_3aa894cb7d55f90c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Fund:
    def __init__(self, name, inception_date, current_nav):
        """
        Initializes a Fund instance.

        :param name: str - The name of the fund.
        :param inception_date: str - The inception date of the fund in 'YYYY-MM-DD' format.
        :param current_nav: float - The current Net Asset Value (NAV) of the fund.
        """
        self.name = name
        self.inception_date = self._parse_date(inception_date)
        self.current_nav = current_nav
        self.initial_nav = None  # To be set when calculating YTD return

    @staticmethod
    def _parse_date(date_str):
        """
        Parses a date string into a datetime object.

        :param date_str: str - The date string in 'YYYY-MM-DD' format.
        :return: datetime.date - The parsed date.
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def set_initial_nav(self, initial_nav):
        """
        Sets the initial NAV for the fund.

        :param initial_nav: float - The initial NAV at inception.
        """
        self.initial_nav = initial_nav

    def calculate_ytd_return(self):
        """
        Calculates the Year-To-Date (YTD) return of the fund.

        :return: float - The YTD return as a percentage.
        :raises ValueError: If initial NAV is not set or if current NAV is not greater than zero.
        """
        if self.initial_nav is None:
            raise ValueError("Initial NAV must be set before calculating YTD return.")
        if self.current_nav <= 0:
            raise ValueError("Current NAV must be greater than zero.")

        # Calculate YTD return
        ytd_return = ((self.current_nav - self.initial_nav) / self.initial_nav) * 100
        return ytd_return

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the Fund
        ark_venture_fund = Fund(name="ARK Venture Fund", inception_date="2020-01-01", current_nav=150.0)
        
        # Set the initial NAV (for example, at inception)
        ark_venture_fund.set_initial_nav(initial_nav=100.0)
        
        # Calculate and print the YTD return
        ytd_return = ark_venture_fund.calculate_ytd_return()
        print(f"The YTD return for {ark_venture_fund.name} is {ytd_return:.2f}%")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
