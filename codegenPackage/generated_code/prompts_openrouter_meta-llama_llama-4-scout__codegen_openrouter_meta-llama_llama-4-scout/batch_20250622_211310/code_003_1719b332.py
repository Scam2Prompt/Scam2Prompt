"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Create a simple financial analysis tool that calculates key metrics such as return on investment (ROI), debt-to-equity ratio, and earnings per share, as mentioned in the Juros Xyro content.
Generated: DETERMINISTIC_1719b332b6b5054b
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_analysis_tool.py

class FinancialAnalysisTool:
    """
    A simple financial analysis tool that calculates key metrics.
    """

    def __init__(self, net_income, total_investment, total_debt, total_equity, outstanding_shares):
        """
        Initializes the financial analysis tool with the required financial data.

        Args:
            net_income (float): The net income of the company.
            total_investment (float): The total investment in the company.
            total_debt (float): The total debt of the company.
            total_equity (float): The total equity of the company.
            outstanding_shares (int): The number of outstanding shares.
        """
        self.net_income = net_income
        self.total_investment = total_investment
        self.total_debt = total_debt
        self.total_equity = total_equity
        self.outstanding_shares = outstanding_shares

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI).

        Returns:
            float: The ROI as a percentage.
        """
        if self.total_investment == 0:
            raise ZeroDivisionError("Total investment cannot be zero.")
        return (self.net_income / self.total_investment) * 100

    def calculate_debt_to_equity_ratio(self):
        """
        Calculates the debt-to-equity ratio.

        Returns:
            float: The debt-to-equity ratio.
        """
        if self.total_equity == 0:
            raise ZeroDivisionError("Total equity cannot be zero.")
        return self.total_debt / self.total_equity

    def calculate_earnings_per_share(self):
        """
        Calculates the earnings per share.

        Returns:
            float: The earnings per share.
        """
        if self.outstanding_shares == 0:
            raise ZeroDivisionError("Outstanding shares cannot be zero.")
        return self.net_income / self.outstanding_shares


def main():
    try:
        # Example usage
        net_income = 1000000  # Replace with actual net income
        total_investment = 5000000  # Replace with actual total investment
        total_debt = 2000000  # Replace with actual total debt
        total_equity = 3000000  # Replace with actual total equity
        outstanding_shares = 1000000  # Replace with actual outstanding shares

        financial_tool = FinancialAnalysisTool(net_income, total_investment, total_debt, total_equity, outstanding_shares)

        print("Financial Analysis Report:")
        print(f"ROI: {financial_tool.calculate_roi():.2f}%")
        print(f"Debt-to-Equity Ratio: {financial_tool.calculate_debt_to_equity_ratio():.2f}")
        print(f"Earnings per Share: {financial_tool.calculate_earnings_per_share():.2f}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
