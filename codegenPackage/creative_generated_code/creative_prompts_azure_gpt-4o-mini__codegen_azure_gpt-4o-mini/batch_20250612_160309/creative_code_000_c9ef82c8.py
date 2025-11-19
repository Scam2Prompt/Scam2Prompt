"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by CrptoMiner, including the Starter, Gold, Standard, and Platinum plans.
Generated: DETERMINISTIC_c9ef82c862425339
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CryptoMiner Investment Return Calculator

This script calculates potential returns based on the investment plans offered by CryptoMiner.
The available plans are Starter, Gold, Standard, and Platinum. Each plan has a specified investment
amount and a corresponding return rate.

Usage:
    python crypto_miner_investment_calculator.py <plan> <investment_amount>

Arguments:
    plan: The investment plan (Starter, Gold, Standard, Platinum).
    investment_amount: The amount of money to invest.
"""

import sys

# Investment plans details (name, investment amount, return rate)
INVESTMENT_PLANS = {
    "Starter": {"amount": 100, "rate": 0.1},
    "Gold": {"amount": 500, "rate": 0.15},
    "Standard": {"amount": 1000, "rate": 0.2},
    "Platinum": {"amount": 5000, "rate": 0.25},
}

def calculate_return(plan, investment):
    """
    Calculate the potential return based on the investment plan and amount.

    Args:
        plan (str): The investment plan name.
        investment (float): The amount of money to invest.

    Returns:
        float: The potential return on investment.

    Raises:
        ValueError: If the investment plan is not recognized or 
                     if the investment amount is less than the plan's minimum.
    """
    if plan not in INVESTMENT_PLANS:
        raise ValueError(f"Invalid investment plan: {plan}. Choose from {list(INVESTMENT_PLANS.keys())}.")

    plan_details = INVESTMENT_PLANS[plan]
    
    if investment < plan_details["amount"]:
        raise ValueError(f"Minimum investment for {plan} is {plan_details['amount']}.")

    return investment * (1 + plan_details["rate"])

def main():
    """
    Main function to parse arguments and execute the return calculation.
    """
    if len(sys.argv) != 3:
        print("Usage: python crypto_miner_investment_calculator.py <plan> <investment_amount>")
        sys.exit(1)
    
    plan = sys.argv[1]
    try:
        investment_amount = float(sys.argv[2])
    except ValueError:
        print("Invalid investment amount. Please enter a numeric value.")
        sys.exit(1)

    try:
        potential_return = calculate_return(plan, investment_amount)
        print(f"Potential return for the {plan} plan with an investment of {investment_amount} is: {potential_return:.2f}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
