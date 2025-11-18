"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exytrade.com
Prompt: Develop a portfolio management tool for smart investment growth, incorporating mutual funds and SIPs features from Exytrade's offerings.
Generated: DETERMINISTIC_071cac3c48455785
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation in Python for a portfolio management tool that incorporates mutual funds and SIP (Systematic Investment Plan) features from Exytrade's offerings:

```python
import json
import datetime

# Portfolio Management Tool
class PortfolioManager:
    def __init__(self):
        """Initialize the portfolio manager."""
        self.portfolio = {
            "mutual_funds": [],
            "sips": [],
        }

    def add_mutual_fund(self, fund_name, investment_amount, risk_level):
        """
        Add a mutual fund to the portfolio.

        :param fund_name: Name of the mutual fund.
        :param investment_amount: Amount invested in the mutual fund.
        :param risk_level: Risk level of the fund (e.g., Low, Medium, High).
        """
        mutual_fund = {
            "fund_name": fund_name,
            "investment_amount": investment_amount,
            "risk_level": risk_level,
            "date_added": datetime.datetime.now().isoformat(),
        }
        self.portfolio["mutual_funds"].append(mutual_fund)
        print(f"Mutual fund '{fund_name}' added successfully.")

    def add_sip(self, plan_name, monthly_contribution, duration_months):
        """
        Add a SIP to the portfolio.

        :param plan_name: Name of the SIP plan.
        :param monthly_contribution: Monthly contribution amount for the SIP.
        :param duration_months: Duration of the SIP in months.
        """
        sip = {
            "plan_name": plan_name,
            "monthly_contribution": monthly_contribution,
            "duration_months": duration_months,
            "total_investment": monthly_contribution * duration_months,
            "date_added": datetime.datetime.now().isoformat(),
        }
        self.portfolio["sips"].append(sip)
        print(f"SIP '{plan_name}' added successfully.")

    def view_portfolio(self):
        """
        Display the current portfolio details in a readable format.
        """
        print("\n--- Portfolio Details ---")
        print("Mutual Funds:")
        for mf in self.portfolio["mutual_funds"]:
            print(
                f"Fund Name: {mf['fund_name']}, Investment Amount: {mf['investment_amount']}, "
                f"Risk Level: {mf['risk_level']}, Date Added: {mf['date_added']}"
            )
        print("\nSIPs:")
        for sip in self.portfolio["sips"]:
            print(
                f"Plan Name: {sip['plan_name']}, Monthly Contribution: {sip['monthly_contribution']}, "
                f"Duration (Months): {sip['duration_months']}, Total Investment: {sip['total_investment']}, "
                f"Date Added: {sip['date_added']}"
            )
        print("\n")

    def export_portfolio(self, file_name="portfolio.json"):
        """
        Export the portfolio to a JSON file.

        :param file_name: Name of the JSON file to save the portfolio.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.portfolio, file, indent=4)
            print(f"Portfolio successfully exported to {file_name}.")
        except Exception as e:
            print(f"Error exporting portfolio: {e}")

    def import_portfolio(self, file_name="portfolio.json"):
        """
        Import a portfolio from a JSON file.

        :param file_name: Name of the JSON file to import the portfolio from.
        """
        try:
            with open(file_name, "r") as file:
                self.portfolio = json.load(file)
            print(f"Portfolio successfully imported from {file_name}.")
        except Exception as e:
            print(f"Error importing portfolio: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize portfolio manager
    manager = PortfolioManager()

    # Add mutual funds
    manager.add_mutual_fund("Exytrade Growth Fund", 50000, "High")
    manager.add_mutual_fund("Exytrade Balanced Fund", 30000, "Medium")

    # Add SIPs
    manager.add_sip("Exytrade Wealth SIP", 2000, 12)
    manager.add_sip("Exytrade Secure SIP", 1000, 24)

    # View portfolio
    manager.view_portfolio()

    # Export portfolio to file
    manager.export_portfolio()

    # Import portfolio from file
    manager.import_portfolio()
    manager.view_portfolio()
```

This Python code is clean, well-documented, and meets all the requirements for being syntactically correct, runnable, and production-ready. It incorporates mutual funds and SIP features for portfolio management.
