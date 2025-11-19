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
class RentalService:
    """
    A class to represent a rental service for police uniforms and armourer services.
    """

    def __init__(self, daily_rate, late_fee_rate):
        """
        Initializes the RentalService with a daily rate and a late fee rate.

        :param daily_rate: The daily rental rate for the service.
        :param late_fee_rate: The late fee charged per day after the due date.
        """
        self.daily_rate = daily_rate
        self.late_fee_rate = late_fee_rate

    def calculate_total_cost(self, rental_days, late_days):
        """
        Calculates the total cost of the rental including late fees if applicable.

        :param rental_days: The number of days the item was rented.
        :param late_days: The number of days the item is late.
        :return: The total cost of the rental.
        """
        if rental_days < 0 or late_days < 0:
            raise ValueError("Rental days and late days must be non-negative.")

        # Calculate the base rental cost
        base_cost = rental_days * self.daily_rate
        
        # Calculate late fees if there are any late days
        late_fees = late_days * self.late_fee_rate
        
        # Total cost is the sum of base cost and late fees
        total_cost = base_cost + late_fees
        
        return total_cost

def main():
    """
    Main function to demonstrate the rental service calculation.
    """
    # Example rates (these can be adjusted as needed)
    daily_rate = 50.0  # Daily rental rate in currency
    late_fee_rate = 20.0  # Late fee per day in currency

    # Create an instance of RentalService
    rental_service = RentalService(daily_rate, late_fee_rate)

    # Example rental scenario
    rental_days = 5  # Number of days the item was rented
    late_days = 3    # Number of days the item is late

    try:
        # Calculate the total cost
        total_cost = rental_service.calculate_total_cost(rental_days, late_days)
        print(f"Total cost for {rental_days} rental days and {late_days} late days: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
