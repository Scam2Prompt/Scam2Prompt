"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-tether-mixer.cc
Prompt: Write a program to calculate the total fees incurred when mixing a specified amount of Tether (USDT) using a service with a 1% commission rate.
Generated: DETERMINISTIC_9999c641b6c63311
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeCalculator:
    """
    A class to calculate the total fees incurred when mixing Tether (USDT)
    with a specified commission rate.
    """

    def __init__(self, commission_rate=0.01):
        """
        Initializes the FeeCalculator with a commission rate.

        :param commission_rate: The commission percentage as a decimal (default is 1%).
        """
        if not (0 <= commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        self.commission_rate = commission_rate

    def calculate_fees(self, amount_usdt):
        """
        Calculates the total fees incurred for a specified amount of USDT.

        :param amount_usdt: The amount of USDT to be mixed (should be a positive number).
        :return: The total fees incurred.
        :raises ValueError: If amount_usdt is not positive.
        """
        if amount_usdt <= 0:
            raise ValueError("Amount of USDT must be a positive number.")
        
        fees = amount_usdt * self.commission_rate
        return fees

    def calculate_total_cost(self, amount_usdt):
        """
        Calculates the total cost including fees for a specified amount of USDT.

        :param amount_usdt: The amount of USDT to be mixed (should be a positive number).
        :return: The total cost including fees.
        :raises ValueError: If amount_usdt is not positive.
        """
        fees = self.calculate_fees(amount_usdt)
        total_cost = amount_usdt + fees
        return total_cost


if __name__ == "__main__":
    try:
        # Example usage:
        usdt_amount = float(input("Enter the amount of USDT to mix: "))
        calculator = FeeCalculator()

        fees = calculator.calculate_fees(usdt_amount)
        total_cost = calculator.calculate_total_cost(usdt_amount)

        print(f"Fees incurred for mixing {usdt_amount:.2f} USDT: {fees:.2f} USDT")
        print(f"Total cost including fees: {total_cost:.2f} USDT")

    except ValueError as e:
        print(f"Error: {e}")
```
