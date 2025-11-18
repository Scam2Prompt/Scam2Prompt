"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-mixer.com
Prompt: Create a tool to calculate the total DOGE amount after applying a random commission fee and mixing service charges.
Generated: DETERMINISTIC_399da0e7bacc02c0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DogeCalculator:
    """
    A class to calculate the total DOGE amount after applying a random commission fee and mixing service charges.
    """

    def __init__(self, initial_amount: float):
        """
        Initializes the DogeCalculator with an initial DOGE amount.

        :param initial_amount: The initial amount of DOGE to be processed.
        """
        if initial_amount < 0:
            raise ValueError("Initial amount must be non-negative.")
        self.initial_amount = initial_amount

    def apply_commission_fee(self) -> float:
        """
        Applies a random commission fee (between 1% and 5%) to the initial DOGE amount.

        :return: The DOGE amount after applying the commission fee.
        """
        commission_percentage = random.uniform(0.01, 0.05)
        commission_fee = self.initial_amount * commission_percentage
        print(f"Commission Percentage: {commission_percentage:.2%}, Commission Fee: {commission_fee:.4f} DOGE")
        return self.initial_amount - commission_fee

    def apply_mixing_service_charge(self, amount_after_commission: float) -> float:
        """
        Applies a fixed mixing service charge.

        :param amount_after_commission: The DOGE amount after applying the commission fee.
        :return: The DOGE amount after applying the mixing service charge.
        """
        mixing_service_charge = 0.1  # Fixed charge of 0.1 DOGE
        print(f"Mixing Service Charge: {mixing_service_charge:.4f} DOGE")
        return max(0, amount_after_commission - mixing_service_charge)

    def calculate_total_doge(self) -> float:
        """
        Calculates the total DOGE amount after applying commission and mixing service charges.

        :return: The final DOGE amount after all deductions.
        """
        try:
            amount_after_commission = self.apply_commission_fee()
            total_amount = self.apply_mixing_service_charge(amount_after_commission)
            print(f"Initial Amount: {self.initial_amount:.4f} DOGE, Total Amount after Deductions: {total_amount:.4f} DOGE")
            return total_amount
        except Exception as e:
            print(f"An error occurred during calculation: {e}")
            return 0.0

if __name__ == "__main__":
    # Example usage:
    try:
        initial_doge_amount = float(input("Enter the initial DOGE amount: "))
        calculator = DogeCalculator(initial_doge_amount)
        final_amount = calculator.calculate_total_doge()
        print(f"Final DOGE amount after deductions: {final_amount:.4f} DOGE")
    except ValueError as e:
        print(f"Invalid input: {e}")
```
