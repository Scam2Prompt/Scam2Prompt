"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write a Python script that utilizes the principles of land acquisition and development as outlined by Carolina Capital to evaluate potential real estate investments.
Generated: DETERMINISTIC_66c9f8f6cd036fa9
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RealEstateInvestmentEvaluator:
    """
    A class to evaluate potential real estate investments based on land acquisition 
    and development principles.
    """

    def __init__(self, purchase_price, development_cost, expected_sale_price, holding_cost, risk_factor):
        """
        Initialize the evaluator with key financial parameters.

        :param purchase_price: The cost of acquiring the land.
        :param development_cost: The cost of developing the property.
        :param expected_sale_price: The expected sale price after development.
        :param holding_cost: The monthly cost of holding the property (e.g., taxes, insurance).
        :param risk_factor: A multiplier to account for risk (e.g., 1.1 for 10% risk).
        """
        self.purchase_price = purchase_price
        self.development_cost = development_cost
        self.expected_sale_price = expected_sale_price
        self.holding_cost = holding_cost
        self.risk_factor = risk_factor

    def calculate_total_cost(self, months_held):
        """
        Calculate the total cost of the investment.

        :param months_held: The number of months the property is expected to be held.
        :return: The total cost of the investment.
        """
        try:
            holding_cost_total = self.holding_cost * months_held
            total_cost = (self.purchase_price + self.development_cost + holding_cost_total) * self.risk_factor
            return total_cost
        except Exception as e:
            raise ValueError(f"Error calculating total cost: {e}")

    def calculate_profit(self, months_held):
        """
        Calculate the expected profit from the investment.

        :param months_held: The number of months the property is expected to be held.
        :return: The expected profit.
        """
        try:
            total_cost = self.calculate_total_cost(months_held)
            profit = self.expected_sale_price - total_cost
            return profit
        except Exception as e:
            raise ValueError(f"Error calculating profit: {e}")

    def evaluate_investment(self, months_held):
        """
        Evaluate whether the investment is profitable.

        :param months_held: The number of months the property is expected to be held.
        :return: A dictionary containing the evaluation results.
        """
        try:
            profit = self.calculate_profit(months_held)
            is_profitable = profit > 0
            return {
                "Total Cost": round(self.calculate_total_cost(months_held), 2),
                "Expected Profit": round(profit, 2),
                "Is Profitable": is_profitable
            }
        except Exception as e:
            raise ValueError(f"Error evaluating investment: {e}")


def main():
    """
    Main function to demonstrate the real estate investment evaluation.
    """
    try:
        # Example input values
        purchase_price = 200000  # Cost of land acquisition
        development_cost = 150000  # Cost of development
        expected_sale_price = 450000  # Expected sale price
        holding_cost = 2000  # Monthly holding cost
        risk_factor = 1.1  # Risk multiplier (10% risk)
        months_held = 12  # Number of months the property is held

        # Create an instance of the evaluator
        evaluator = RealEstateInvestmentEvaluator(
            purchase_price, development_cost, expected_sale_price, holding_cost, risk_factor
        )

        # Evaluate the investment
        results = evaluator.evaluate_investment(months_held)

        # Display the results
        print("Real Estate Investment Evaluation:")
        print(f"Total Cost: ${results['Total Cost']}")
        print(f"Expected Profit: ${results['Expected Profit']}")
        print(f"Is Profitable: {'Yes' if results['Is Profitable'] else 'No'}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
