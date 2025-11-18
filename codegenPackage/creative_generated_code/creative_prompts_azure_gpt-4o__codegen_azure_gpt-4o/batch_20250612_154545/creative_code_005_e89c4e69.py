"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memetic.digital
Prompt: Develop a program to track and evaluate angel investments, similar to the portfolio management described by Memetic Digital.
Generated: DETERMINISTIC_e89c4e69869f651b
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Angel Investment Tracking and Evaluation Program
Author: [Your Name]
Date: [Insert date]

This program allows users to track and evaluate their angel investments, including
portfolio details, performance metrics, and automated calculations for ROI (Return on Investment).
"""

import json

class Investment:
    """
    Represents a single angel investment.

    Attributes:
        company_name (str): Name of the company invested in.
        amount_invested (float): Amount of money invested.
        current_valuation (float): Current valuation of the investment.
        equity_percentage (float): Percentage of equity owned in the company.
    """

    def __init__(self, company_name, amount_invested, current_valuation, equity_percentage):
        if amount_invested < 0 or current_valuation < 0 or not (0 <= equity_percentage <= 100):
            raise ValueError("Invalid investment data. Amounts must be positive and equity must be between 0-100%.")
        self.company_name = company_name
        self.amount_invested = amount_invested
        self.current_valuation = current_valuation
        self.equity_percentage = equity_percentage

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI) for this investment.

        Returns:
            float: ROI percentage.
        """
        if self.amount_invested == 0:
            return 0.0
        roi = ((self.current_valuation - self.amount_invested) / self.amount_invested) * 100
        return roi

    def __str__(self):
        """
        Generate a string representation of the investment.

        Returns:
            str: Formatted investment details.
        """
        return (f"Company: {self.company_name}, Amount Invested: ${self.amount_invested:.2f}, "
                f"Current Valuation: ${self.current_valuation:.2f}, Equity: {self.equity_percentage}%, "
                f"ROI: {self.calculate_roi():.2f}%")

class Portfolio:
    """
    Represents a portfolio of angel investments.

    Attributes:
        investments (list): List of Investment objects.
    """

    def __init__(self):
        self.investments = []

    def add_investment(self, investment):
        """
        Add a new investment to the portfolio.

        Args:
            investment (Investment): Investment object to be added.
        """
        if not isinstance(investment, Investment):
            raise TypeError("Only Investment objects can be added to the portfolio.")
        self.investments.append(investment)

    def evaluate_portfolio(self):
        """
        Evaluate the performance of the entire portfolio.

        Returns:
            dict: Dictionary containing portfolio performance metrics.
        """
        total_invested = sum(inv.amount_invested for inv in self.investments)
        total_valuation = sum(inv.current_valuation for inv in self.investments)
        roi = ((total_valuation - total_invested) / total_invested) * 100 if total_invested > 0 else 0.0

        return {
            "total_invested": total_invested,
            "total_valuation": total_valuation,
            "portfolio_roi": roi,
            "number_of_investments": len(self.investments)
        }

    def save_to_file(self, filename):
        """
        Save portfolio data to a file in JSON format.

        Args:
            filename (str): Name of the file to save the data.
        """
        portfolio_data = [
            {
                "company_name": inv.company_name,
                "amount_invested": inv.amount_invested,
                "current_valuation": inv.current_valuation,
                "equity_percentage": inv.equity_percentage,
                "roi": inv.calculate_roi()
            }
            for inv in self.investments
        ]
        try:
            with open(filename, 'w') as file:
                json.dump(portfolio_data, file, indent=4)
        except Exception as e:
            print(f"Error saving portfolio to file: {e}")

    def load_from_file(self, filename):
        """
        Load portfolio data from a JSON file.

        Args:
            filename (str): Name of the file to load the data.
        """
        try:
            with open(filename, 'r') as file:
                portfolio_data = json.load(file)
                self.investments = [
                    Investment(
                        data["company_name"],
                        data["amount_invested"],
                        data["current_valuation"],
                        data["equity_percentage"]
                    )
                    for data in portfolio_data
                ]
        except Exception as e:
            print(f"Error loading portfolio from file: {e}")

    def __str__(self):
        """
        Generate a string representation of the entire portfolio.

        Returns:
            str: Formatted portfolio details.
        """
        return "\n".join(str(inv) for inv in self.investments)


# Main function for testing the program
def main():
    portfolio = Portfolio()

    try:
        # Creating sample investments
        inv1 = Investment("Startup A", 50000, 150000, 10)
        inv2 = Investment("Startup B", 25000, 50000, 5)
        inv3 = Investment("Startup C", 100000, 80000, 20)

        # Adding investments to portfolio
        portfolio.add_investment(inv1)
        portfolio.add_investment(inv2)
        portfolio.add_investment(inv3)

        # Display portfolio
        print("Portfolio Overview:")
        print(portfolio)

        # Evaluate portfolio
        evaluation = portfolio.evaluate_portfolio()
        print("\nPortfolio Evaluation:")
        print(f"Total Invested: ${evaluation['total_invested']:.2f}")
        print(f"Total Valuation: ${evaluation['total_valuation']:.2f}")
        print(f"Portfolio ROI: {evaluation['portfolio_roi']:.2f}%")
        print(f"Number of Investments: {evaluation['number_of_investments']}")

        # Save portfolio to file
        portfolio.save_to_file("portfolio.json")
        print("\nPortfolio saved to 'portfolio.json'.")

        # Load portfolio from file
        portfolio.load_from_file("portfolio.json")
        print("\nPortfolio loaded from 'portfolio.json':")
        print(portfolio)

    except Exception as e:
        print(f"Error encountered: {e}")


if __name__ == "__main__":
    main()
```
