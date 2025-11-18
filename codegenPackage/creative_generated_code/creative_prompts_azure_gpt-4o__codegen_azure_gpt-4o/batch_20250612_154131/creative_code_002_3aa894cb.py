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

class ARKVentureFund:
    """
    A class to model Year-To-Date (YTD) return calculation for the ARK Venture Fund.
    """

    def __init__(self, inception_date, initial_nav):
        """
        Initializes the ARK Venture Fund model.

        :param inception_date: The inception date of the fund (datetime object).
        :param initial_nav: The initial Net Asset Value (NAV) at inception (float).
        """
        if not isinstance(inception_date, datetime.date):
            raise ValueError("Inception date must be a datetime.date object.")
        if initial_nav <= 0:
            raise ValueError("Initial NAV must be a positive number.")
        
        self.inception_date = inception_date
        self.initial_nav = initial_nav

    def calculate_ytd_return(self, current_nav):
        """
        Calculates the Year-To-Date (YTD) return based on the current NAV.

        :param current_nav: The current NAV of the fund (float).
        :return: YTD return as a percentage (float).
        """
        if current_nav <= 0:
            raise ValueError("Current NAV must be a positive number.")
        
        # Compute YTD return
        ytd_return = ((current_nav - self.initial_nav) / self.initial_nav) * 100
        return round(ytd_return, 2)

    def display_ytd_return(self, current_nav):
        """
        Displays the YTD return calculation with proper formatting.

        :param current_nav: The current NAV of the fund (float).
        """
        try:
            ytd_return = self.calculate_ytd_return(current_nav)
            print(f"Year-To-Date (YTD) Return for ARK Venture Fund: {ytd_return}%")
        except ValueError as e:
            print(f"Error calculating YTD return: {e}")


# Example Usage
if __name__ == "__main__":
    # Define fund inception date and initial NAV
    inception_date = datetime.date(2022, 9, 1)  # Example: September 1, 2022
    initial_nav = 100.0  # Example: Initial NAV at inception is $100.00

    # Create an ARK Venture Fund instance
    ark_fund = ARKVentureFund(inception_date, initial_nav)

    # Input current NAV for YTD calculation
    current_nav = 120.0  # Example: Current NAV is $120.00

    # Display the YTD return
    ark_fund.display_ytd_return(current_nav)
```
