"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Generate code to calculate the potential returns for a high-risk savings plan with an average rate of 24.56% (2023), as mentioned in the "Sur-Mesure" formula on pipelinefinanceconseil.com. Include options for adjusting risk levels dynamically.
Generated: DETERMINISTIC_c626acf5dfe0617d
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_returns(principal, duration_years, rate_of_return):
    """
    Calculates the potential returns for a savings plan.

    Args:
        principal (float): Initial investment amount.
        duration_years (int): Investment duration in years.
        rate_of_return (float): Average annual percentage rate of return.

    Returns:
        float: Total amount after the investment duration, including returns.
    """

    try:
        # Ensure all inputs are valid numbers and duration is positive.
        if principal <= 0 or duration_years <= 0 or rate_of_return <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Apply the compound interest formula: A = P * (1 + r)^t
        total_amount = principal * (1 + rate_of_return / 100) ** duration_years
        return total_amount
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def adjust_risk_level(base_rate, risk_level="moderate"):
    """
    Adjusts the rate of return based on risk level.

    Args:
        base_rate (float): Base average rate of return (e.g., 24.56%).
        risk_level (str): Risk level ("low", "moderate", "high").

    Returns:
        float: Adjusted rate of return based on risk level.
    """

    try:
        risk_levels = {
            "low": base_rate - base_rate * 0.2,  # Reduce rate by 20%
            "moderate": base_rate,              # Default average rate
            "high": base_rate + base_rate * 0.3 # Increase rate by 30%
        }

        if risk_level not in risk_levels:
            raise ValueError("Invalid risk level. Choose 'low', 'moderate', or 'high'.")

        return risk_levels[risk_level]
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage:
    try:
        # Get user inputs
        principal = float(input("Enter the principal amount ($): "))
        duration_years = int(input("Enter the duration of the investment (years): "))
        risk_level = input("Enter the risk level (low, moderate, high): ").strip().lower()

        # Base rate as per the 2023 average from "Sur-Mesure" formula
        base_rate = 24.56

        # Adjust the rate based on risk level
        adjusted_rate = adjust_risk_level(base_rate, risk_level)

        # Calculate potential returns
        total_returns = calculate_potential_returns(principal, duration_years, adjusted_rate)

        # Display results
        print(f"\nInvestment Details:")
        print(f"Principal Amount: ${principal:,.2f}")
        print(f"Duration: {duration_years} years")
        print(f"Risk Level: {risk_level.capitalize()}")
        print(f"Adjusted Annual Rate of Return: {adjusted_rate:.2f}%")
        print(f"Total Returns After {duration_years} Years: ${total_returns:,.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal and duration.")
        sys.exit(1)
```
