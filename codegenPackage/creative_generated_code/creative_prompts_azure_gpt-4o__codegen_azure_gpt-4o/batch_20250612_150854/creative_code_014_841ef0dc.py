"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Develop a Python program to calculate the potential risks and rewards of different investment types, as categorized by Immediate Peak.
Generated: DETERMINISTIC_841ef0dc195024f3
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_analysis.py

import math


class InvestmentType:
    """
    A class to represent an investment type with its associated attributes.
    """

    def __init__(self, name, average_return, volatility, risk_factor):
        """
        Initialize an investment type.

        Args:
            name (str): The name of the investment type.
            average_return (float): The expected average return (as a percentage).
            volatility (float): The standard deviation representing the volatility (as a percentage).
            risk_factor (float): A custom risk multiplier to reflect risk severity.
        """
        self.name = name
        self.average_return = average_return
        self.volatility = volatility
        self.risk_factor = risk_factor


def calculate_reward(risk_factor, average_return):
    """
    Calculates the expected reward based on risk factor and average return.

    Args:
        risk_factor (float): A custom multiplier for risk severity.
        average_return (float): Expected average return (as a percentage).

    Returns:
        float: The calculated reward.
    """
    try:
        # Reward increases proportionally with the average return and inversely with risk factor.
        return average_return / math.sqrt(risk_factor)
    except ZeroDivisionError:
        # Handle the case where risk_factor is 0 to avoid division by zero.
        print("Error: Risk factor cannot be zero.")
        return 0.0


def calculate_risk(volatility, risk_factor):
    """
    Calculates the risk of an investment based on volatility and risk factor.

    Args:
        volatility (float): The standard deviation representing market volatility (as a percentage).
        risk_factor (float): A custom multiplier for risk severity.

    Returns:
        float: The calculated risk.
    """
    try:
        # Risk increases proportionally with volatility and risk factor.
        return volatility * risk_factor
    except Exception as e:
        # Catch any unforeseen errors.
        print(f"Error calculating risk: {e}")
        return float('inf')


def main():
    """
    Main function to calculate and display the risks and rewards of different investment types.
    """
    # Define a list of investment types with their attributes.
    investments = [
        InvestmentType(name="Stocks", average_return=10.0, volatility=20.0, risk_factor=1.5),
        InvestmentType(name="Bonds", average_return=5.0, volatility=5.0, risk_factor=0.8),
        InvestmentType(name="Real Estate", average_return=7.0, volatility=10.0, risk_factor=1.2),
        InvestmentType(name="Cryptocurrency", average_return=15.0, volatility=50.0, risk_factor=2.5),
    ]

    print("Investment Risk and Reward Analysis")
    print("=" * 40)

    # Iterate through each investment type and calculate risks and rewards.
    for investment in investments:
        reward = calculate_reward(investment.risk_factor, investment.average_return)
        risk = calculate_risk(investment.volatility, investment.risk_factor)

        # Display the results.
        print(f"Investment Type: {investment.name}")
        print(f"  Average Return: {investment.average_return}%")
        print(f"  Volatility: {investment.volatility}%")
        print(f"  Risk Factor: {investment.risk_factor}")
        print(f"  Calculated Reward: {reward:.2f}")
        print(f"  Calculated Risk: {risk:.2f}")
        print("-" * 40)


# Entry point for the program.
if __name__ == "__main__":
    main()
```
