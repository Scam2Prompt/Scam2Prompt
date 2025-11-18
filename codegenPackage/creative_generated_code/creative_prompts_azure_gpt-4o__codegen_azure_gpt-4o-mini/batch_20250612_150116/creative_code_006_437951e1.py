"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Create a Python function to calculate the cost of asset finance for acquiring business tools, factoring in rental payments instead of upfront purchases, as outlined on Maestro Finance.
Generated: DETERMINISTIC_437951e1dfa6c2eb
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AssetFinanceCalculator:
    """
    A class to calculate the cost of asset finance for acquiring business tools
    by factoring in rental payments instead of upfront purchases.
    """

    def __init__(self, rental_payment: float, lease_term: int, interest_rate: float):
        """
        Initializes the AssetFinanceCalculator with rental payment, lease term, and interest rate.

        :param rental_payment: Monthly rental payment for the asset (in currency units)
        :param lease_term: Lease term in months
        :param interest_rate: Annual interest rate as a percentage (e.g., 5 for 5%)
        """
        self.rental_payment = rental_payment
        self.lease_term = lease_term
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of asset finance over the lease term.

        :return: Total cost (in currency units) over the entire lease term
        """
        try:
            total_cost = self.rental_payment * self.lease_term
            return total_cost

        except Exception as e:
            raise RuntimeError("An error occurred while calculating the total cost") from e

    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest paid over the lease term.

        :return: Total interest (in currency units) over the entire lease term
        """
        try:
            total_cost = self.calculate_total_cost()
            total_interest = total_cost * self.interest_rate * (self.lease_term / 12)  # Simple interest calculation
            return total_interest

        except Exception as e:
            raise RuntimeError("An error occurred while calculating the total interest") from e

    def calculate_grand_total(self) -> float:
        """
        Calculate the grand total cost including interest over the lease term.

        :return: Grand total cost (in currency units) over the entire lease term
        """
        try:
            total_cost = self.calculate_total_cost()
            total_interest = self.calculate_total_interest()
            grand_total = total_cost + total_interest
            return grand_total

        except Exception as e:
            raise RuntimeError("An error occurred while calculating the grand total") from e


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with sample values
        calculator = AssetFinanceCalculator(rental_payment=500, lease_term=36, interest_rate=5)

        # Calculate and print the results
        print(f"Total Cost: {calculator.calculate_total_cost():.2f}")
        print(f"Total Interest: {calculator.calculate_total_interest():.2f}")
        print(f"Grand Total: {calculator.calculate_grand_total():.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
