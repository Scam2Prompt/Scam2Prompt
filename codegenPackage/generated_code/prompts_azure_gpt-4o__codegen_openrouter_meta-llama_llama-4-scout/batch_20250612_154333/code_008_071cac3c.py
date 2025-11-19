"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: Develop a portfolio management tool for smart investment growth, incorporating mutual funds and SIPs features from Exytrade's offerings.
Generated: DETERMINISTIC_071cac3c48455785
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_management_tool.py

import datetime
import json

class MutualFund:
    """Represents a mutual fund investment."""

    def __init__(self, fund_name, investment_amount):
        """
        Initializes a MutualFund object.

        Args:
            fund_name (str): Name of the mutual fund.
            investment_amount (float): Initial investment amount.
        """
        self.fund_name = fund_name
        self.investment_amount = investment_amount
        self.current_value = investment_amount

    def update_value(self, new_value):
        """
        Updates the current value of the mutual fund.

        Args:
            new_value (float): New value of the mutual fund.
        """
        self.current_value = new_value

    def get_details(self):
        """
        Returns a dictionary with mutual fund details.

        Returns:
            dict: Mutual fund details.
        """
        return {
            "fund_name": self.fund_name,
            "investment_amount": self.investment_amount,
            "current_value": self.current_value,
        }


class SIP:
    """Represents a Systematic Investment Plan (SIP) investment."""

    def __init__(self, sip_name, investment_amount, frequency):
        """
        Initializes an SIP object.

        Args:
            sip_name (str): Name of the SIP.
            investment_amount (float): Investment amount per installment.
            frequency (str): Frequency of investments (e.g., monthly, quarterly).
        """
        self.sip_name = sip_name
        self.investment_amount = investment_amount
        self.frequency = frequency
        self.investment_history = []

    def add_investment(self, investment_date, amount):
        """
        Adds a new investment to the SIP.

        Args:
            investment_date (datetime.date): Date of investment.
            amount (float): Amount invested.
        """
        self.investment_history.append((investment_date, amount))

    def get_details(self):
        """
        Returns a dictionary with SIP details.

        Returns:
            dict: SIP details.
        """
        return {
            "sip_name": self.sip_name,
            "investment_amount": self.investment_amount,
            "frequency": self.frequency,
            "investment_history": self.investment_history,
        }


class Portfolio:
    """Represents a portfolio of investments."""

    def __init__(self):
        """
        Initializes a Portfolio object.
        """
        self.mutual_funds = []
        self.sips = []

    def add_mutual_fund(self, mutual_fund):
        """
        Adds a mutual fund to the portfolio.

        Args:
            mutual_fund (MutualFund): Mutual fund to add.
        """
        self.mutual_funds.append(mutual_fund)

    def add_sip(self, sip):
        """
        Adds an SIP to the portfolio.

        Args:
            sip (SIP): SIP to add.
        """
        self.sips.append(sip)

    def get_portfolio_value(self):
        """
        Returns the total value of the portfolio.

        Returns:
            float: Total portfolio value.
        """
        total_value = 0
        for mutual_fund in self.mutual_funds:
            total_value += mutual_fund.current_value
        for sip in self.sips:
            # For simplicity, assume SIP value is the sum of all investments
            total_value += sum(amount for _, amount in sip.investment_history)
        return total_value

    def get_details(self):
        """
        Returns a dictionary with portfolio details.

        Returns:
            dict: Portfolio details.
        """
        portfolio_details = {
            "mutual_funds": [mutual_fund.get_details() for mutual_fund in self.mutual_funds],
            "sips": [sip.get_details() for sip in self.sips],
            "total_portfolio_value": self.get_portfolio_value(),
        }
        return portfolio_details


def load_portfolio_from_json(file_path):
    """
    Loads a portfolio from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Portfolio: Loaded portfolio.

    Raises:
        json.JSONDecodeError: If the JSON file is invalid.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            portfolio = Portfolio()
            for mutual_fund_data in data.get("mutual_funds", []):
                mutual_fund = MutualFund(
                    mutual_fund_data["fund_name"],
                    mutual_fund_data["investment_amount"],
                )
                mutual_fund.update_value(mutual_fund_data["current_value"])
                portfolio.add_mutual_fund(mutual_fund)
            for sip_data in data.get("sips", []):
                sip = SIP(
                    sip_data["sip_name"],
                    sip_data["investment_amount"],
                    sip_data["frequency"],
                )
                for investment_date, amount in sip_data.get("investment_history", []):
                    sip.add_investment(
                        datetime.datetime.strptime(investment_date, "%Y-%m-%d").date(),
                        amount,
                    )
                portfolio.add_sip(sip)
            return portfolio
    except json.JSONDecodeError as e:
        print(f"Error loading portfolio from JSON: {e}")
        return None


def save_portfolio_to_json(portfolio, file_path):
    """
    Saves a portfolio to a JSON file.

    Args:
        portfolio (Portfolio): Portfolio to save.
        file_path (str): Path to the JSON file.

    Raises:
        Exception: If an error occurs while saving the portfolio.
    """
    try:
        data = portfolio.get_details()
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving portfolio to JSON: {e}")


# Example usage:
if __name__ == "__main__":
    portfolio = Portfolio()

    mutual_fund1 = MutualFund("Fund 1", 10000)
    mutual_fund1.update_value(12000)
    portfolio.add_mutual_fund(mutual_fund1)

    sip1 = SIP("SIP 1", 500, "monthly")
    sip1.add_investment(datetime.date(2022, 1, 1), 500)
    sip1.add_investment(datetime.date(2022, 2, 1), 500)
    portfolio.add_sip(sip1)

    print("Portfolio Details:")
    print(json.dumps(portfolio.get_details(), indent=4))

    save_portfolio_to_json(portfolio, "portfolio.json")

    loaded_portfolio = load_portfolio_from_json("portfolio.json")
    if loaded_portfolio:
        print("Loaded Portfolio Details:")
        print(json.dumps(loaded_portfolio.get_details(), indent=4))
```
