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
class FinancialAnalysisTool:
    """
    A simple financial analysis tool to calculate key financial metrics.
    """

    def __init__(self, investment: float, gain: float, debt: float, equity: float, earnings: float, shares_outstanding: int):
        """
        Initializes the financial analysis tool with the required parameters.

        :param investment: The initial investment amount.
        :param gain: The total gain from the investment.
        :param debt: The total debt of the company.
        :param equity: The total equity of the company.
        :param earnings: The total earnings of the company.
        :param shares_outstanding: The number of shares outstanding.
        """
        self.investment = investment
        self.gain = gain
        self.debt = debt
        self.equity = equity
        self.earnings = earnings
        self.shares_outstanding = shares_outstanding

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        try:
            roi = (self.gain - self.investment) / self.investment * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Investment cannot be zero for ROI calculation.")

    def calculate_debt_to_equity_ratio(self) -> float:
        """
        Calculates the Debt-to-Equity Ratio.

        :return: Debt-to-Equity Ratio.
        """
        try:
            ratio = self.debt / self.equity
            return ratio
        except ZeroDivisionError:
            raise ValueError("Equity cannot be zero for Debt-to-Equity Ratio calculation.")

    def calculate_earnings_per_share(self) -> float:
        """
        Calculates Earnings Per Share (EPS).

        :return: EPS value.
        """
        try:
            eps = self.earnings / self.shares_outstanding
            return eps
        except ZeroDivisionError:
            raise ValueError("Shares outstanding cannot be zero for EPS calculation.")

    def display_metrics(self):
        """
        Displays the calculated financial metrics.
        """
        try:
            print(f"Return on Investment (ROI): {self.calculate_roi():.2f}%")
            print(f"Debt-to-Equity Ratio: {self.calculate_debt_to_equity_ratio():.2f}")
            print(f"Earnings Per Share (EPS): {self.calculate_earnings_per_share():.2f}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the financial analysis tool with example data
    investment = 10000.0  # Initial investment
    gain = 15000.0        # Total gain from the investment
    debt = 5000.0         # Total debt
    equity = 20000.0      # Total equity
    earnings = 10000.0    # Total earnings
    shares_outstanding = 1000  # Number of shares outstanding

    # Create an instance of the FinancialAnalysisTool
    financial_tool = FinancialAnalysisTool(investment, gain, debt, equity, earnings, shares_outstanding)

    # Display the calculated metrics
    financial_tool.display_metrics()
```
