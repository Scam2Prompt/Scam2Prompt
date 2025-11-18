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
class RentalService:
    """
    A class to handle the rental of police uniforms and armor services,
    including the calculation of late fees and extended hire charges.
    """

    def __init__(self, daily_rate, late_fee_rate, max_late_days):
        """
        Initializes the RentalService with the following parameters:
        
        :param daily_rate: Daily rental rate for the item
        :param late_fee_rate: Daily late fee rate
        :param max_late_days: Maximum number of days for which late fees can be charged
        """
        self.daily_rate = daily_rate
        self.late_fee_rate = late_fee_rate
        self.max_late_days = max_late_days

    def calculate_total_due(self, days_rented, days_late):
        """
        Calculates the total amount due based on rental days and late days.

        :param days_rented: Total number of days the item was rented
        :param days_late: Number of days the item is returned late
        :return: Total amount due
        :raises ValueError: If days_rented or days_late are negative
        """
        if days_rented < 0 or days_late < 0:
            raise ValueError("Days rented and late cannot be negative.")

        total_rental = days_rented * self.daily_rate
        
        # Calculate late fees
        late_days_charged = min(days_late, self.max_late_days)
        total_late_fees = late_days_charged * self.late_fee_rate
        
        total_due = total_rental + total_late_fees
        return total_due

def main():
    """
    Main function to demonstrate the usage of the RentalService class.
    You can modify the rates and durations to test different scenarios.
    """
    # Example rates
    daily_rate = 50.00  # Daily hire charge
    late_fee_rate = 20.00  # Daily late fee
    max_late_days = 10  # Maximum late days for fee calculation

    # Create an instance of RentalService
    rental_service = RentalService(daily_rate, late_fee_rate, max_late_days)

    # Example rental data
    days_rented = 5  # Number of days the item was rented
    days_late = 12  # Number of days the item was returned late

    try:
        total_due = rental_service.calculate_total_due(days_rented, days_late)
        print(f"Total amount due: ${total_due:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
