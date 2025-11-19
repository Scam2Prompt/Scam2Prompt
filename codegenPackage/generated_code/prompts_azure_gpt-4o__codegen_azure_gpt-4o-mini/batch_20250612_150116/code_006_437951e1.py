"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Create a Python function to calculate the cost of asset finance for acquiring business tools, factoring in rental payments instead of upfront purchases, as outlined on Maestro Finance.
Generated: DETERMINISTIC_437951e1dfa6c2eb
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AssetFinanceCalculator:
    """
    A class to calculate the cost of asset finance for acquiring business tools.
    This class considers rental payments instead of upfront purchases.
    """

    def __init__(self, rental_payment: float, lease_term_months: int, interest_rate: float):
        """
        Initializes the AssetFinanceCalculator with rental payment, lease term, and interest rate.

        :param rental_payment: Monthly rental payment for the asset
        :param lease_term_months: Total lease term in months
        :param interest_rate: Annual interest rate as a percentage
        """
        if rental_payment <= 0:
            raise ValueError("Rental payment must be greater than zero.")
        if lease_term_months <= 0:
            raise ValueError("Lease term must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.rental_payment = rental_payment
        self.lease_term_months = lease_term_months
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of asset finance over the lease term.

        :return: Total cost of asset finance
        """
        total_rental_payments = self.rental_payment * self.lease_term_months
        total_interest = self.calculate_total_interest(total_rental_payments)
        total_cost = total_rental_payments + total_interest
        return total_cost

    def calculate_total_interest(self, total_rental_payments: float) -> float:
        """
        Calculates the total interest incurred over the lease term.

        :param total_rental_payments: Total rental payments over the lease term
        :return: Total interest amount
        """
        # Simple interest calculation for demonstration purposes
        total_interest = total_rental_payments * self.interest_rate * (self.lease_term_months / 12)
        return total_interest

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of AssetFinanceCalculator
        calculator = AssetFinanceCalculator(rental_payment=500, lease_term_months=36, interest_rate=5)
        
        # Calculate the total cost of asset finance
        total_cost = calculator.calculate_total_cost()
        
        # Print the result
        print(f"Total cost of asset finance: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
