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
    A simple financial analysis tool to calculate key financial metrics:
    - Return on Investment (ROI)
    - Debt-to-Equity Ratio
    - Earnings Per Share (EPS)
    """

    @staticmethod
    def calculate_roi(gain_from_investment: float, cost_of_investment: float) -> float:
        """
        Calculate Return on Investment (ROI).
        
        Formula: ROI = (Gain from Investment - Cost of Investment) / Cost of Investment
        
        :param gain_from_investment: Total gain from the investment
        :param cost_of_investment: Total cost of the investment
        :return: ROI as a percentage
        """
        if cost_of_investment == 0:
            raise ValueError("Cost of investment cannot be zero.")
        roi = (gain_from_investment - cost_of_investment) / cost_of_investment * 100
        return round(roi, 2)

    @staticmethod
    def calculate_debt_to_equity(total_liabilities: float, shareholder_equity: float) -> float:
        """
        Calculate Debt-to-Equity Ratio.
        
        Formula: Debt-to-Equity Ratio = Total Liabilities / Shareholder Equity
        
        :param total_liabilities: Total liabilities of the company
        :param shareholder_equity: Total shareholder equity of the company
        :return: Debt-to-Equity Ratio
        """
        if shareholder_equity == 0:
            raise ValueError("Shareholder equity cannot be zero.")
        debt_to_equity = total_liabilities / shareholder_equity
        return round(debt_to_equity, 2)

    @staticmethod
    def calculate_eps(net_income: float, total_shares_outstanding: int) -> float:
        """
        Calculate Earnings Per Share (EPS).
        
        Formula: EPS = Net Income / Total Shares Outstanding
        
        :param net_income: Net income of the company
        :param total_shares_outstanding: Total number of shares outstanding
        :return: EPS value
        """
        if total_shares_outstanding == 0:
            raise ValueError("Total shares outstanding cannot be zero.")
        eps = net_income / total_shares_outstanding
        return round(eps, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Example data
        gain_from_investment = 15000.0
        cost_of_investment = 10000.0
        total_liabilities = 50000.0
        shareholder_equity = 25000.0
        net_income = 120000.0
        total_shares_outstanding = 10000

        # Create an instance of the tool
        tool = FinancialAnalysisTool()

        # Calculate metrics
        roi = tool.calculate_roi(gain_from_investment, cost_of_investment)
        debt_to_equity = tool.calculate_debt_to_equity(total_liabilities, shareholder_equity)
        eps = tool.calculate_eps(net_income, total_shares_outstanding)

        # Print results
        print(f"Return on Investment (ROI): {roi}%")
        print(f"Debt-to-Equity Ratio: {debt_to_equity}")
        print(f"Earnings Per Share (EPS): ${eps}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
