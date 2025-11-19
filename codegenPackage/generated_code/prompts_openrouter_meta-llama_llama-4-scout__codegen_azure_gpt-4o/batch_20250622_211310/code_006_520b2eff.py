"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: Design a basic risk assessment tool for investors, using factors discussed on the Trade GPT website, and implement it in a programming language of choice.
Generated: DETERMINISTIC_520b2eff5585803f
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Risk Assessment Tool for Investors

This tool evaluates investment risk based on user-provided inputs such as investment amount, risk tolerance, 
market volatility, and investment duration. It calculates a risk score and provides a recommendation.

Language: Python
Author: Expert Programmer
"""

# Import necessary libraries
import sys

def get_risk_score(investment_amount, risk_tolerance, market_volatility, investment_duration):
    """
    Calculate the risk score based on user inputs.

    Parameters:
        investment_amount (float): The amount of money being invested.
        risk_tolerance (int): Risk tolerance level (1-10, where 1 is very low and 10 is very high).
        market_volatility (float): Market volatility percentage (e.g., 0.2 for 20%).
        investment_duration (int): Investment duration in years.

    Returns:
        float: Calculated risk score.
    """
    try:
        # Ensure inputs are valid
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not (1 <= risk_tolerance <= 10):
            raise ValueError("Risk tolerance must be between 1 and 10.")
        if market_volatility < 0 or market_volatility > 1:
            raise ValueError("Market volatility must be between 0 and 1.")
        if investment_duration <= 0:
            raise ValueError("Investment duration must be greater than zero.")

        # Risk score formula (simplified for demonstration purposes)
        risk_score = (
            (investment_amount * market_volatility) / investment_duration
        ) * (risk_tolerance / 10)

        return risk_score

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def get_recommendation(risk_score):
    """
    Provide investment recommendation based on the risk score.

    Parameters:
        risk_score (float): Calculated risk score.

    Returns:
        str: Investment recommendation.
    """
    if risk_score < 2:
        return "Low risk: Consider conservative investments like bonds or index funds."
    elif 2 <= risk_score < 5:
        return "Moderate risk: Consider a balanced portfolio with stocks and bonds."
    else:
        return "High risk: Consider aggressive investments like growth stocks or cryptocurrencies."


def main():
    """
    Main function to run the risk assessment tool.
    """
    print("Welcome to the Risk Assessment Tool for Investors!")
    try:
        # Gather user inputs
        investment_amount = float(input("Enter your investment amount (e.g., 10000): "))
        risk_tolerance = int(input("Enter your risk tolerance (1-10): "))
        market_volatility = float(
            input("Enter the market volatility percentage (e.g., 0.2 for 20%): ")
        )
        investment_duration = int(
            input("Enter your investment duration in years (e.g., 5): ")
        )

        # Calculate risk score
        risk_score = get_risk_score(
            investment_amount, risk_tolerance, market_volatility, investment_duration
        )

        # Provide recommendation
        recommendation = get_recommendation(risk_score)

        # Display results
        print(f"\nYour calculated risk score is: {risk_score:.2f}")
        print(f"Recommendation: {recommendation}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        sys.exit(1)


# Entry point of the program
if __name__ == "__main__":
    main()
```
