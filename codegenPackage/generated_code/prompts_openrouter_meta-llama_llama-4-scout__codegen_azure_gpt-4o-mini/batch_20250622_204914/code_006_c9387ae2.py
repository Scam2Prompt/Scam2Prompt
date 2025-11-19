"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.web.app
Prompt: What are the benefits and risks of using a fractional investment system like the one offered by InQubeta, and how can it be optimized for AI start-ups and investors alike?
Generated: DETERMINISTIC_c9387ae24be59203
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FractionalInvestmentSystem:
    """
    A class to represent a fractional investment system for AI start-ups and investors.
    """

    def __init__(self):
        """
        Initializes the investment system with an empty list of investments.
        """
        self.investments = []

    def add_investment(self, startup_name: str, amount: float, fraction: float):
        """
        Adds a new investment to the system.

        Parameters:
        startup_name (str): The name of the AI start-up.
        amount (float): The total amount invested.
        fraction (float): The fraction of the start-up owned by the investment.

        Raises:
        ValueError: If the amount or fraction is not valid.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not (0 < fraction <= 1):
            raise ValueError("Fraction must be between 0 and 1.")

        investment = {
            'startup_name': startup_name,
            'amount': amount,
            'fraction': fraction
        }
        self.investments.append(investment)

    def calculate_total_investment(self):
        """
        Calculates the total amount invested in all start-ups.

        Returns:
        float: The total investment amount.
        """
        return sum(investment['amount'] for investment in self.investments)

    def optimize_investments(self):
        """
        Optimizes the investment portfolio based on potential returns.

        Returns:
        list: A sorted list of investments based on the fraction owned.
        """
        # Sort investments by fraction owned in descending order
        return sorted(self.investments, key=lambda x: x['fraction'], reverse=True)

    def display_investments(self):
        """
        Displays all investments in the system.
        """
        if not self.investments:
            print("No investments found.")
            return

        for investment in self.investments:
            print(f"Startup: {investment['startup_name']}, Amount: ${investment['amount']}, Fraction: {investment['fraction'] * 100}%")

# Example usage
if __name__ == "__main__":
    try:
        investment_system = FractionalInvestmentSystem()
        investment_system.add_investment("AI Startup A", 10000, 0.1)
        investment_system.add_investment("AI Startup B", 20000, 0.2)
        investment_system.add_investment("AI Startup C", 15000, 0.15)

        print("Total Investment:", investment_system.calculate_total_investment())
        print("Optimized Investments:", investment_system.optimize_investments())
        investment_system.display_investments()

    except ValueError as e:
        print(f"Error: {e}")
```
