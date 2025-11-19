"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to calculate late fees or extended hire charges for police uniforms or armourer services, based on the terms outlined by Powered Production Film Services.
Generated: DETERMINISTIC_bc012f740ff8dd5e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class LateFeeCalculator:
    """
    Calculates late fees or extended hire charges for police uniforms or armourer services.
    """

    def __init__(self, daily_rate, weekly_rate, daily_fee, weekly_fee):
        """
        Initializes the LateFeeCalculator with the given rates.

        Args:
            daily_rate (float): Daily rate for the item.
            weekly_rate (float): Weekly rate for the item.
            daily_fee (float): Daily late fee.
            weekly_fee (float): Weekly late fee.
        """
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate
        self.daily_fee = daily_fee
        self.weekly_fee = weekly_fee

    def calculate_late_fee(self, rental_start_date, rental_end_date, return_date):
        """
        Calculates the late fee based on the rental and return dates.

        Args:
            rental_start_date (datetime): Date the item was rented.
            rental_end_date (datetime): Date the item was due to be returned.
            return_date (datetime): Date the item was actually returned.

        Returns:
            float: The late fee.
        """
        if return_date <= rental_end_date:
            return 0.0

        days_late = (return_date - rental_end_date).days
        weeks_late = days_late // 7
        remaining_days = days_late % 7

        late_fee = weeks_late * self.weekly_fee + remaining_days * self.daily_fee
        return late_fee

    def calculate_extended_hire_charge(self, rental_start_date, return_date):
        """
        Calculates the extended hire charge based on the rental and return dates.

        Args:
            rental_start_date (datetime): Date the item was rented.
            return_date (datetime): Date the item was actually returned.

        Returns:
            float: The extended hire charge.
        """
        days_rented = (return_date - rental_start_date).days
        weeks_rented = days_rented // 7
        remaining_days = days_rented % 7

        extended_hire_charge = weeks_rented * self.weekly_rate + remaining_days * self.daily_rate
        return extended_hire_charge


def main():
    try:
        daily_rate = 100.0
        weekly_rate = 600.0
        daily_fee = 50.0
        weekly_fee = 200.0

        calculator = LateFeeCalculator(daily_rate, weekly_rate, daily_fee, weekly_fee)

        rental_start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
        rental_end_date = datetime.strptime('2024-01-08', '%Y-%m-%d')
        return_date = datetime.strptime('2024-01-15', '%Y-%m-%d')

        late_fee = calculator.calculate_late_fee(rental_start_date, rental_end_date, return_date)
        extended_hire_charge = calculator.calculate_extended_hire_charge(rental_start_date, return_date)

        print(f"Late Fee: ${late_fee:.2f}")
        print(f"Extended Hire Charge: ${extended_hire_charge:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
