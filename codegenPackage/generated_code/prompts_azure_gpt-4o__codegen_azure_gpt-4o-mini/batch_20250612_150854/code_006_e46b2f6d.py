"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a program that categorizes investments into capital, fixed-income, high-risk, and low-risk types based on Immediate Helix V9’s definitions. Include functionality for risk assessment.
Generated: DETERMINISTIC_e46b2f6d5fe38c03
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Investment:
    """
    A class to represent an investment and categorize it based on its type and risk level.
    """

    def __init__(self, name, amount, investment_type, risk_level):
        """
        Initializes an Investment instance.

        :param name: str - The name of the investment
        :param amount: float - The amount invested
        :param investment_type: str - The type of investment (capital, fixed-income, high-risk, low-risk)
        :param risk_level: str - The risk level of the investment (high, low)
        """
        self.name = name
        self.amount = amount
        self.investment_type = investment_type
        self.risk_level = risk_level

    def assess_risk(self):
        """
        Assess the risk of the investment based on its type and risk level.

        :return: str - A message indicating the risk assessment
        """
        if self.investment_type == "capital":
            return f"{self.name} is a capital investment with a {self.risk_level} risk level."
        elif self.investment_type == "fixed-income":
            return f"{self.name} is a fixed-income investment with a {self.risk_level} risk level."
        elif self.investment_type == "high-risk":
            return f"{self.name} is a high-risk investment. Caution is advised!"
        elif self.investment_type == "low-risk":
            return f"{self.name} is a low-risk investment. It is generally safe."
        else:
            return "Unknown investment type."

def categorize_investments(investments):
    """
    Categorizes a list of investments and assesses their risk.

    :param investments: list - A list of Investment instances
    :return: dict - A dictionary categorizing investments by type
    """
    categorized = {
        "capital": [],
        "fixed-income": [],
        "high-risk": [],
        "low-risk": []
    }

    for investment in investments:
        if investment.investment_type in categorized:
            categorized[investment.investment_type].append(investment)
        else:
            print(f"Warning: Investment type '{investment.investment_type}' is not recognized.")

    return categorized

def main():
    """
    Main function to execute the investment categorization and risk assessment.
    """
    # Sample investments
    investments = [
        Investment("Tech Startup", 10000, "capital", "high"),
        Investment("Government Bonds", 5000, "fixed-income", "low"),
        Investment("Cryptocurrency", 2000, "high-risk", "high"),
        Investment("Savings Account", 3000, "low-risk", "low"),
        Investment("Real Estate", 15000, "capital", "low")
    ]

    # Categorize investments
    categorized_investments = categorize_investments(investments)

    # Assess risk for each investment
    for investment_list in categorized_investments.values():
        for investment in investment_list:
            print(investment.assess_risk())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
