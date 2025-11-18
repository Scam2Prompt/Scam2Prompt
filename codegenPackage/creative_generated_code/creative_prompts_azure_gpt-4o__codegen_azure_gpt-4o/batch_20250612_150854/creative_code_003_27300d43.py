"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefrontier.app
Prompt: Create a program that simulates cryptocurrency portfolio management, incorporating Immediate Frontier's structured learning approach to risk assessment and diversification.
Generated: DETERMINISTIC_27300d43f215dfca
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal


class CryptoPortfolioManager:
    """
    A class to simulate cryptocurrency portfolio management.
    This includes risk assessment and diversification following structured learning principles.
    """
    def __init__(self):
        self.portfolio = {}
        self.total_investment = Decimal("0.00")

    def add_asset(self, name, amount, price_per_unit, risk_score):
        """
        Add a cryptocurrency asset to the portfolio.

        :param name: Name of the cryptocurrency (e.g., 'Bitcoin').
        :param amount: Amount of the asset held.
        :param price_per_unit: Current price per unit of the asset.
        :param risk_score: Risk score for the asset (1 to 10, where 1 is low risk).
        """
        if risk_score < 1 or risk_score > 10:
            raise ValueError("Risk score must be between 1 and 10.")

        if name in self.portfolio:
            raise ValueError(f"The asset '{name}' already exists in the portfolio.")

        self.portfolio[name] = {
            "amount": Decimal(amount),
            "price_per_unit": Decimal(price_per_unit),
            "risk_score": risk_score,
            "value": Decimal(amount) * Decimal(price_per_unit)
        }
        self.total_investment += self.portfolio[name]["value"]

    def remove_asset(self, name):
        """
        Remove a cryptocurrency asset from the portfolio.

        :param name: Name of the cryptocurrency to be removed.
        """
        if name not in self.portfolio:
            raise ValueError(f"The asset '{name}' does not exist in the portfolio.")

        self.total_investment -= self.portfolio[name]["value"]
        del self.portfolio[name]

    def calculate_diversification(self):
        """
        Calculate the diversification ratio of the portfolio.

        :return: Dictionary showing the percentage of total investment for each asset.
        """
        diversification = {}
        for name, details in self.portfolio.items():
            diversification[name] = (details["value"] / self.total_investment) * 100
        return diversification

    def assess_portfolio_risk(self):
        """
        Assess the overall risk of the portfolio based on the weighted average of risk scores.

        :return: Weighted average risk score of the portfolio.
        """
        total_risk_weighted = Decimal("0.00")
        for details in self.portfolio.values():
            total_risk_weighted += (details["risk_score"] * details["value"])
        weighted_risk = total_risk_weighted / self.total_investment if self.total_investment > 0 else 0
        return round(weighted_risk, 2)

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio including diversification and risk assessment.

        :return: Dictionary summarizing the portfolio.
        """
        summary = {
            "total_investment": self.total_investment,
            "portfolio": self.portfolio,
            "diversification": self.calculate_diversification(),
            "overall_risk_score": self.assess_portfolio_risk()
        }
        return summary

    def save_to_file(self, filename):
        """
        Save the portfolio data to a JSON file.

        :param filename: Name of the file to save the portfolio.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_portfolio_summary(), file, indent=4, default=str)
        except IOError as e:
            print(f"Error saving portfolio to file: {e}")

    def load_from_file(self, filename):
        """
        Load portfolio data from a JSON file.

        :param filename: Name of the file to load the portfolio from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.total_investment = Decimal(data["total_investment"])
                self.portfolio = {
                    name: {
                        "amount": Decimal(details["amount"]),
                        "price_per_unit": Decimal(details["price_per_unit"]),
                        "risk_score": int(details["risk_score"]),
                        "value": Decimal(details["value"])
                    }
                    for name, details in data["portfolio"].items()
                }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading portfolio from file: {e}")


# Example usage of the program
if __name__ == "__main__":
    manager = CryptoPortfolioManager()

    try:
        # Add assets to the portfolio
        manager.add_asset("Bitcoin", 1.5, 45000, 4)
        manager.add_asset("Ethereum", 10, 3000, 6)
        manager.add_asset("Cardano", 1000, 0.4, 8)

        # Display portfolio summary
        print("Portfolio Summary:")
        print(json.dumps(manager.get_portfolio_summary(), indent=4, default=str))

        # Save portfolio to a file
        manager.save_to_file("portfolio.json")

        # Remove an asset and display updated summary
        manager.remove_asset("Cardano")
        print("Updated Portfolio Summary:")
        print(json.dumps(manager.get_portfolio_summary(), indent=4, default=str))

        # Load portfolio from file
        manager.load_from_file("portfolio.json")
        print("Loaded Portfolio Summary:")
        print(json.dumps(manager.get_portfolio_summary(), indent=4, default=str))

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
