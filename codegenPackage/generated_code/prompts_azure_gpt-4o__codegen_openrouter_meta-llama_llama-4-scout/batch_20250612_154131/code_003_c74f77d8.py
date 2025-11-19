"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Write a script to model the impact of ARK Venture Fund's single 2.75% management fee compared to a traditional "2 and 20" fee structure over a 5-year investment period.
Generated: DETERMINISTIC_c74f77d80c4130bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_traditional_fees(initial_investment, annual_return, years, management_fee, performance_fee):
    """
    Calculate the growth of an investment with a traditional "2 and 20" fee structure.

    Args:
        initial_investment (float): The initial investment amount.
        annual_return (float): The annual return of the investment.
        years (int): The number of years the investment is held.
        management_fee (float): The annual management fee as a decimal.
        performance_fee (float): The performance fee as a decimal.

    Returns:
        float: The final value of the investment.
    """
    balance = initial_investment
    for _ in range(years):
        # Calculate the annual return
        balance *= (1 + annual_return)
        
        # Calculate the management fee
        management_fee_amount = balance * management_fee
        balance -= management_fee_amount
        
        # Calculate the performance fee
        performance_fee_amount = max(0, balance - initial_investment) * performance_fee
        balance -= performance_fee_amount
    
    return balance

def calculate_ark_venture_fees(initial_investment, annual_return, years, management_fee):
    """
    Calculate the growth of an investment with ARK Venture Fund's single 2.75% management fee.

    Args:
        initial_investment (float): The initial investment amount.
        annual_return (float): The annual return of the investment.
        years (int): The number of years the investment is held.
        management_fee (float): The annual management fee as a decimal.

    Returns:
        float: The final value of the investment.
    """
    balance = initial_investment
    for _ in range(years):
        # Calculate the annual return
        balance *= (1 + annual_return)
        
        # Calculate the management fee
        management_fee_amount = balance * management_fee
        balance -= management_fee_amount
    
    return balance

def main():
    # Initial investment and annual return
    initial_investment = 1000000
    annual_return = 0.10

    # Number of years
    years = 5

    # Traditional "2 and 20" fee structure
    traditional_management_fee = 0.02
    traditional_performance_fee = 0.20

    # ARK Venture Fund's single 2.75% management fee
    ark_venture_management_fee = 0.0275

    # Calculate the growth of the investments
    traditional_final_value = calculate_traditional_fees(initial_investment, annual_return, years, traditional_management_fee, traditional_performance_fee)
    ark_venture_final_value = calculate_ark_venture_fees(initial_investment, annual_return, years, ark_venture_management_fee)

    # Print the results
    print(f"Traditional '2 and 20' fee structure: ${traditional_final_value:,.2f}")
    print(f"ARK Venture Fund's single 2.75% management fee: ${ark_venture_final_value:,.2f}")

    # Plot the growth of the investments over time
    traditional_balances = []
    ark_venture_balances = []
    balances = [initial_investment]
    for _ in range(years):
        balances.append(balances[-1] * (1 + annual_return))

    for i, balance in enumerate(balances):
        traditional_balance = balance
        ark_venture_balance = balance

        if i > 0:
            traditional_balance *= (1 - traditional_management_fee)
            if balance > initial_investment:
                traditional_balance -= (balance - initial_investment) * traditional_performance_fee * (1 - traditional_management_fee)
            ark_venture_balance *= (1 - ark_venture_management_fee)

        traditional_balances.append(traditional_balance)
        ark_venture_balances.append(ark_venture_balance)

    plt.plot(traditional_balances, label="Traditional '2 and 20' fee structure")
    plt.plot(ark_venture_balances, label="ARK Venture Fund's single 2.75% management fee")
    plt.xlabel("Years")
    plt.ylabel("Balance ($)")
    plt.title("Growth of Investments Over Time")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
```
