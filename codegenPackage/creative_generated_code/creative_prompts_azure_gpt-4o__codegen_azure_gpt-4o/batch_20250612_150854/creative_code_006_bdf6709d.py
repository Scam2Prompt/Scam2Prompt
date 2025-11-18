"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.io
Prompt: Create a Python script for calculating risk tolerance based on financial standing and investment goals, inspired by Immediate Peak's risk management strategies.
Generated: DETERMINISTIC_bdf6709d91a19482
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
Script to calculate risk tolerance based on financial standing and investment goals.
Inspired by Immediate Peak's risk management strategies.

Risk tolerance is calculated using:
- Annual Income
- Savings
- Debt
- Investment Horizon
- Risk Appetite (scale: Low, Medium, High)
"""

def calculate_risk_tolerance(income, savings, debt, investment_horizon, risk_appetite):
    """
    Calculate risk tolerance based on financial metrics and investment goals.

    Parameters:
        income (float): Annual income in USD.
        savings (float): Total savings in USD.
        debt (float): Total debt in USD.
        investment_horizon (int): Investment horizon in years.
        risk_appetite (str): Risk appetite ('Low', 'Medium', 'High').

    Returns:
        str: Risk tolerance level ('Conservative', 'Moderate', 'Aggressive').
    """
    try:
        # Validate inputs
        if income < 0 or savings < 0 or debt < 0 or investment_horizon <= 0:
            raise ValueError("Income, savings, and debt must be non-negative. Investment horizon must be positive.")
        if risk_appetite not in ['Low', 'Medium', 'High']:
            raise ValueError("Risk appetite must be 'Low', 'Medium', or 'High'.")

        # Financial Stability Score: Higher savings, lower debt, higher score
        financial_stability = (savings - debt) / (income if income > 0 else 1)

        # Horizon Factor: Longer investment horizon allows for higher risk
        horizon_factor = investment_horizon / 10  # Normalize horizon (10+ years being ideal)

        # Risk Appetite Factor: Translate risk appetite to numerical scale
        risk_appetite_factor = {'Low': 0.5, 'Medium': 1.0, 'High': 1.5}[risk_appetite]

        # Combined risk score
        risk_score = financial_stability + horizon_factor * risk_appetite_factor

        # Determine risk tolerance based on risk score
        if risk_score < 1:
            return 'Conservative'
        elif 1 <= risk_score < 2:
            return 'Moderate'
        else:
            return 'Aggressive'

    except Exception as e:
        # Handle errors and return meaningful messages
        return f"Error while calculating risk tolerance: {str(e)}"

def main():
    """
    Main function to interact with the user and compute risk tolerance.
    """
    print("Welcome to the Risk Tolerance Calculator!")
    try:
        # Collect user input
        income = float(input("Enter your annual income (USD): "))
        savings = float(input("Enter your total savings (USD): "))
        debt = float(input("Enter your total debt (USD): "))
        investment_horizon = int(input("Enter your investment horizon (years): "))
        risk_appetite = input("Enter your risk appetite (Low, Medium, High): ").strip().capitalize()

        # Calculate risk tolerance
        risk_tolerance = calculate_risk_tolerance(income, savings, debt, investment_horizon, risk_appetite)
        print(f"Your calculated risk tolerance is: {risk_tolerance}")

    except ValueError:
        print("Invalid input. Please enter numeric values for income, savings, debt, and investment horizon.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
