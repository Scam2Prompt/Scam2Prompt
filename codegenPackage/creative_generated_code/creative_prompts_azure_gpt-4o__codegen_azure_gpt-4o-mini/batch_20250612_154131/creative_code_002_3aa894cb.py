"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Generate Python code to model the YTD return calculation for the ARK Venture Fund, using the fund's inception date and current NAV.
Generated: DETERMINISTIC_3aa894cb7d55f90c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FundReturnCalculator:
    def __init__(self, inception_date: str, current_nav: float):
        """
        Initializes the FundReturnCalculator with inception date and current NAV.

        :param inception_date: The inception date of the fund in 'YYYY-MM-DD' format.
        :param current_nav: The current Net Asset Value (NAV) of the fund.
        """
        self.inception_date = self._parse_date(inception_date)
        self.current_nav = self._validate_nav(current_nav)

    @staticmethod
    def _parse_date(date_string: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        :param date_string: The date string to parse.
        :return: A datetime.date object.
        :raises ValueError: If the date_string is not in the correct format.
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD.") from e

    @staticmethod
    def _validate_nav(nav: float) -> float:
        """
        Validates the NAV input.

        :param nav: The NAV to validate.
        :return: The validated NAV.
        :raises ValueError: If the NAV is not a positive number.
        """
        if nav <= 0:
            raise ValueError("NAV must be a positive number.")
        return nav

    def calculate_ytd_return(self, previous_nav: float) -> float:
        """
        Calculates the Year-To-Date (YTD) return for the fund.

        :param previous_nav: The NAV at the start of the year.
        :return: The YTD return as a percentage.
        :raises ValueError: If the previous_nav is not a positive number.
        """
        previous_nav = self._validate_nav(previous_nav)
        
        if previous_nav == 0:
            raise ValueError("Previous NAV cannot be zero.")
        
        # Calculate YTD return
        ytd_return = ((self.current_nav - previous_nav) / previous_nav) * 100
        return ytd_return

    def get_fund_age_in_years(self) -> float:
        """
        Calculates the age of the fund in years from inception date to current date.

        :return: The age of the fund in years.
        """
        today = datetime.date.today()
        age = today.year - self.inception_date.year - ((today.month, today.day) < (self.inception_date.month, self.inception_date.day))
        return age

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the FundReturnCalculator with inception date and current NAV
        fund_calculator = FundReturnCalculator('2021-01-01', 150.50)
        
        # Calculate YTD return based on previous NAV
        previous_nav = 100.00  # Example previous NAV
        ytd_return = fund_calculator.calculate_ytd_return(previous_nav)
        print(f"YTD Return: {ytd_return:.2f}%")

        # Get fund age in years
        fund_age = fund_calculator.get_fund_age_in_years()
        print(f"Fund Age: {fund_age:.2f} years")

    except ValueError as e:
        print(f"Error: {e}")
```
