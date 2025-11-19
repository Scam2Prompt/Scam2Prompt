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
from typing import Optional

class ARKVentureFund:
    """
    A class to model the YTD return calculation for the ARK Venture Fund.
    
    Attributes:
        inception_date (datetime.date): The inception date of the fund.
        current_nav (float): The current Net Asset Value of the fund.
        inception_nav (float): The NAV at the fund's inception.
    """
    
    def __init__(self, inception_date: datetime.date, inception_nav: float):
        """
        Initialize the ARK Venture Fund with its inception date and NAV.
        
        Args:
            inception_date: The date when the fund was launched.
            inception_nav: The NAV of the fund at inception.
        """
        self.inception_date = inception_date
        self.inception_nav = inception_nav
        self.current_nav = inception_nav  # Initialize with inception NAV
    
    def update_nav(self, new_nav: float) -> None:
        """
        Update the current NAV of the fund.
        
        Args:
            new_nav: The new Net Asset Value to set.
            
        Raises:
            ValueError: If the new NAV is not positive.
        """
        if new_nav <= 0:
            raise ValueError("NAV must be positive")
        self.current_nav = new_nav
    
    def calculate_ytd_return(self, as_of_date: Optional[datetime.date] = None) -> float:
        """
        Calculate the Year-To-Date return of the fund.
        
        Args:
            as_of_date: The date to calculate YTD return as of. Defaults to today.
            
        Returns:
            The YTD return as a decimal (e.g., 0.05 for 5%).
            
        Raises:
            ValueError: If the as_of_date is before the inception date.
        """
        if as_of_date is None:
            as_of_date = datetime.date.today()
        
        if as_of_date < self.inception_date:
            raise ValueError("Cannot calculate YTD return before inception date")
        
        # Get the first day of the current year or inception date if later
        year_start = datetime.date(as_of_date.year, 1, 1)
        calculation_start_date = max(year_start, self.inception_date)
        
        # In a real implementation, we would fetch the NAV at calculation_start_date
        # For this example, we'll assume it's the inception NAV if calculation starts at inception
        start_nav = self.inception_nav if calculation_start_date == self.inception_date else None
        
        if start_nav is None:
            raise ValueError("Historical NAV data required for YTD calculation")
        
        ytd_return = (self.current_nav - start_nav) / start_nav
        return ytd_return

# Example usage
if __name__ == "__main__":
    # Initialize fund with inception date and NAV
    inception_date = datetime.date(2022, 3, 29)  # Example inception date
    inception_nav = 10.0  # Example NAV at inception
    fund = ARKVentureFund(inception_date, inception_nav)
    
    # Update with current NAV
    current_nav = 12.5  # Example current NAV
    fund.update_nav(current_nav)
    
    # Calculate YTD return
    try:
        ytd_return = fund.calculate_ytd_return()
        print(f"YTD Return: {ytd_return:.2%}")
    except ValueError as e:
        print(f"Error calculating YTD return: {e}")
```
