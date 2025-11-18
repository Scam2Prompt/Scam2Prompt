"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to calculate late fees or extended hire charges for police uniforms or armourer services, based on the terms outlined by Powered Production Film Services.
Generated: DETERMINISTIC_bc012f740ff8dd5e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# late_fee_calculator.py

import datetime

class LateFeeCalculator:
    """
    A class to calculate late fees or extended hire charges for police uniforms 
    or armourer services, based on Powered Production Film Services terms.
    """

    def __init__(self, daily_rate, grace_period_days, late_fee_rate):
        """
        Initialize the calculator with the terms.

        Args:
            daily_rate (float): The daily rental rate for the service.
            grace_period_days (int): Number of days before late fees apply.
            late_fee_rate (float): Additional fee rate (e.g., 0.2 for 20% per day after grace period).
        """
        self.daily_rate = daily_rate
        self.grace_period_days = grace_period_days
        self.late_fee_rate = late_fee_rate

    def calculate_fees(self, hire_date, return_date):
        """
        Calculate the late fees or extended hire charges based on hire and return dates.

        Args:
            hire_date (str): The date the equipment was hired (format: YYYY-MM-DD).
            return_date (str): The date the equipment was returned (format: YYYY-MM-DD).

        Returns:
            dict: A dictionary with total_fee, late_days, and late_fee.
        """
        try:
            # Convert input strings to datetime objects
            hire_dt = datetime.datetime.strptime(hire_date, "%Y-%m-%d")
            return_dt = datetime.datetime.strptime(return_date, "%Y-%m-%d")
            
            if return_dt < hire_dt:
                raise ValueError("Return date cannot be before hire date.")

            # Calculate total days hired
            total_days = (return_dt - hire_dt).days + 1

            # Calculate grace period and late days
            late_days = max(0, total_days - self.grace_period_days)

            # Calculate fees
            base_charge = total_days * self.daily_rate
            late_fee = late_days * self.daily_rate * self.late_fee_rate
            total_fee = base_charge + late_fee

            return {
                "total_fee": round(total_fee, 2),
                "late_days": late_days,
                "late_fee": round(late_fee, 2)
            }

        except ValueError as ve:
            # Handle invalid date formats or logical errors
            return {"error": str(ve)}
        except Exception as e:
            # Catch unexpected errors
            return {"error": f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    # Example usage
    daily_rate = 100.0  # Daily rate for hire
    grace_period_days = 3  # Grace period in days
    late_fee_rate = 0.2  # Late fee rate (20%)

    # Initialize the calculator
    calculator = LateFeeCalculator(daily_rate, grace_period_days, late_fee_rate)

    # Example hire and return dates
    hire_date = "2023-10-01"
    return_date = "2023-10-08"

    # Calculate fees
    result = calculator.calculate_fees(hire_date, return_date)

    # Print the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Total Fee: ${result['total_fee']}")
        print(f"Late Days: {result['late_days']}")
        print(f"Late Fee: ${result['late_fee']}")
```
