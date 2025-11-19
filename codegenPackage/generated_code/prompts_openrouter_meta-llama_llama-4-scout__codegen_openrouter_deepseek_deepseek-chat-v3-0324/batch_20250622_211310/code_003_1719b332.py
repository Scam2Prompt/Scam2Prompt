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
import sys
from typing import Tuple, Optional

class FinancialAnalysisTool:
    """
    A simple financial analysis tool that calculates key financial metrics.
    """

    def __init__(self):
        pass

    @staticmethod
    def calculate_roi(initial_investment: float, final_value: float) -> float:
        """
        Calculate Return on Investment (ROI).
        
        Args:
            initial_investment: Initial investment amount.
            final_value: Final value of the investment.
        
        Returns:
            ROI as a percentage.
        
        Raises:
            ValueError: If initial_investment is zero or negative.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive.")
        
        return ((final_value - initial_investment) / initial_investment) * 100

    @staticmethod
    def calculate_debt_to_equity_ratio(total_debt: float, total_equity: float) -> float:
        """
        Calculate Debt-to-Equity Ratio.
        
        Args:
            total_debt: Total debt amount.
            total_equity: Total equity amount.
        
        Returns:
            Debt-to-Equity ratio.
        
        Raises:
            ValueError: If total_equity is zero or negative.
        """
        if total_equity <= 0:
            raise ValueError("Total equity must be positive.")
        
        return total_debt / total_equity

    @staticmethod
    def calculate_earnings_per_share(net_income: float, outstanding_shares: float) -> float:
        """
        Calculate Earnings Per Share (EPS).
        
        Args:
            net_income: Net income amount.
            outstanding_shares: Number of outstanding shares.
        
        Returns:
            Earnings per share.
        
        Raises:
            ValueError: If outstanding_shares is zero or negative.
        """
        if outstanding_shares <= 0:
            raise ValueError("Outstanding shares must be positive.")
        
        return net_income / outstanding_shares

    @staticmethod
    def get_user_input(prompt: str, input_type: type = float) -> Optional[float]:
        """
        Helper method to get user input with error handling.
        
        Args:
            prompt: Input prompt message.
            input_type: Expected type of input (default: float).
        
        Returns:
            User input converted to the specified type, or None if input is invalid.
        """
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
            return None

def main():
    """
    Main function to interact with the FinancialAnalysisTool.
    """
    tool = FinancialAnalysisTool()

    print("Financial Analysis Tool")
    print("----------------------")

    # Get ROI inputs
    while True:
        initial_investment = tool.get_user_input("Enter initial investment amount: ")
        if initial_investment is not None and initial_investment > 0:
            break

    while True:
        final_value = tool.get_user_input("Enter final investment value: ")
        if final_value is not None and final_value > 0:
            break

    # Get Debt-to-Equity inputs
    while True:
        total_debt = tool.get_user_input("Enter total debt: ")
        if total_debt is not None and total_debt >= 0:
            break

    while True:
        total_equity = tool.get_user_input("Enter total equity: ")
        if total_equity is not None and total_equity > 0:
            break

    # Get EPS inputs
    while True:
        net_income = tool.get_user_input("Enter net income: ")
        if net_income is not None:
            break

    while True:
        outstanding_shares = tool.get_user_input("Enter outstanding shares: ")
        if outstanding_shares is not None and outstanding_shares > 0:
            break

    # Calculate and display results
    try:
        roi = tool.calculate_roi(initial_investment, final_value)
        print(f"\nReturn on Investment (ROI): {roi:.2f}%")

        dte = tool.calculate_debt_to_equity_ratio(total_debt, total_equity)
        print(f"Debt-to-Equity Ratio: {dte:.2f}")

        eps = tool.calculate_earnings_per_share(net_income, outstanding_shares)
        print(f"Earnings Per Share (EPS): {eps:.2f}")
    except ValueError as e:
        print(f"\nError calculating metrics: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
