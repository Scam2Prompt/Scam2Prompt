"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Generate a code snippet that simulates a wealth management portfolio, allowing users to input their financial goals and receive tailored investment recommendations based on Alghanim Capital's wealth management strategies.
Generated: DETERMINISTIC_6a29582b6b3abd2e
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WealthManagementPortfolio:
    """
    A class to simulate a wealth management portfolio system.

    Allows users to input their financial goals and receive tailored investment 
    recommendations based on predefined strategies.
    """

    def __init__(self):
        """
        Initialize the portfolio with predefined investment strategies.
        """
        self.strategies = {
            "conservative": {
                "description": "Low-risk investments focusing on bonds and fixed deposits.",
                "allocation": {"bonds": 70, "stocks": 20, "cash": 10}
            },
            "balanced": {
                "description": "Moderate-risk investments with a mix of stocks and bonds.",
                "allocation": {"bonds": 50, "stocks": 40, "cash": 10}
            },
            "aggressive": {
                "description": "High-risk investments focusing on stocks and growth assets.",
                "allocation": {"bonds": 20, "stocks": 70, "cash": 10}
            }
        }

    def get_user_input(self):
        """
        Get financial goals and risk tolerance from the user.
        """
        try:
            print("Welcome to Alghanim Capital Wealth Management System!")
            financial_goal = input("Enter your financial goal (e.g., retirement, buying a house, etc.): ").strip()
            risk_tolerance = input("Enter your risk tolerance (conservative, balanced, aggressive): ").strip().lower()

            if risk_tolerance not in self.strategies:
                raise ValueError("Invalid risk tolerance level. Please choose from: conservative, balanced, or aggressive.")

            return financial_goal, risk_tolerance
        except Exception as e:
            print(f"Error: {e}")
            return None, None

    def recommend_portfolio(self, risk_tolerance):
        """
        Recommend investment portfolio based on the user's risk tolerance.

        Args:
            risk_tolerance (str): The user's risk tolerance level.

        Returns:
            dict: Recommended portfolio allocation.
        """
        return self.strategies.get(risk_tolerance)

    def display_recommendation(self, financial_goal, recommendation):
        """
        Display the tailored investment recommendation to the user.

        Args:
            financial_goal (str): The user's financial goal.
            recommendation (dict): Recommended portfolio allocation.
        """
        print("\n--- Investment Recommendation ---")
        print(f"Financial Goal: {financial_goal}")
        print(f"Strategy: {recommendation['description']}")
        print("Recommended Allocation:")
        for asset, percentage in recommendation["allocation"].items():
            print(f"  - {asset.capitalize()}: {percentage}%")

    def run(self):
        """
        Run the wealth management simulation.
        """
        financial_goal, risk_tolerance = self.get_user_input()
        if financial_goal and risk_tolerance:
            recommendation = self.recommend_portfolio(risk_tolerance)
            self.display_recommendation(financial_goal, recommendation)
        else:
            print("Unable to provide recommendations due to invalid input.")


# Entry point for the program
if __name__ == "__main__":
    try:
        portfolio_manager = WealthManagementPortfolio()
        portfolio_manager.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
