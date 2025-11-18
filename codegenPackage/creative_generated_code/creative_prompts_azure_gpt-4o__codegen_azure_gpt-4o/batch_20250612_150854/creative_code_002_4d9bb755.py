"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Generate code to analyze financial metrics such as ROI, EPS, and P/E ratio for investment decision-making, referencing Immediate Crest V2's educational goals.
Generated: DETERMINISTIC_4d9bb755c221eb9a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financial Metrics Analyzer

This script calculates key financial metrics such as ROI, EPS, and P/E ratio
to help with investment decision-making. It is designed to be clean, efficient,
and well-documented. Error handling is included to ensure robustness for production use.

Educational Alignment: This code serves as an example for Immediate Crest V2's 
educational goal of teaching financial analytics via programming.
"""

def calculate_roi(initial_investment, net_profit):
    """
    Calculate Return on Investment (ROI).

    Formula: ROI = (Net Profit / Initial Investment) * 100

    :param initial_investment: Amount initially invested (float).
    :param net_profit: Net profit from the investment (float).
    :return: ROI percentage (float).
    """
    try:
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        roi = (net_profit / initial_investment) * 100
        return round(roi, 2)
    except ZeroDivisionError:
        raise ValueError("Initial investment cannot be zero.")
    except TypeError:
        raise ValueError("Inputs must be numerical values.")

def calculate_eps(net_income, total_shares_outstanding):
    """
    Calculate Earnings Per Share (EPS).

    Formula: EPS = Net Income / Total Shares Outstanding

    :param net_income: Company's net income (float).
    :param total_shares_outstanding: Total number of shares outstanding (float).
    :return: EPS value (float).
    """
    try:
        if total_shares_outstanding <= 0:
            raise ValueError("Total shares outstanding must be greater than zero.")
        eps = net_income / total_shares_outstanding
        return round(eps, 2)
    except ZeroDivisionError:
        raise ValueError("Total shares outstanding cannot be zero.")
    except TypeError:
        raise ValueError("Inputs must be numerical values.")

def calculate_pe_ratio(current_stock_price, eps):
    """
    Calculate Price-to-Earnings (P/E) Ratio.

    Formula: P/E Ratio = Current Stock Price / EPS

    :param current_stock_price: Current price of the stock (float).
    :param eps: Earnings per Share (float).
    :return: P/E ratio value (float).
    """
    try:
        if eps <= 0:
            raise ValueError("EPS must be greater than zero.")
        pe_ratio = current_stock_price / eps
        return round(pe_ratio, 2)
    except ZeroDivisionError:
        raise ValueError("EPS cannot be zero.")
    except TypeError:
        raise ValueError("Inputs must be numerical values.")

def main():
    """
    Main function to interact with the user and analyze financial metrics.
    """
    print("Welcome to the Financial Metrics Analyzer.")
    
    try:
        # Gather inputs for ROI calculation
        initial_investment = float(input("Enter the initial investment amount ($): "))
        net_profit = float(input("Enter the net profit ($): "))
        roi = calculate_roi(initial_investment, net_profit)
        print(f"Return on Investment (ROI): {roi}%")

        # Gather inputs for EPS calculation
        net_income = float(input("Enter the company's net income ($): "))
        total_shares_outstanding = float(input("Enter the total shares outstanding: "))
        eps = calculate_eps(net_income, total_shares_outstanding)
        print(f"Earnings Per Share (EPS): ${eps}")

        # Gather inputs for P/E Ratio calculation
        current_stock_price = float(input("Enter the current stock price ($): "))
        pe_ratio = calculate_pe_ratio(current_stock_price, eps)
        print(f"Price-to-Earnings (P/E) Ratio: {pe_ratio}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
