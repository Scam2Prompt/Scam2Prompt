"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Create a Python script that evaluates the risk tolerance of an investor based on their financial goals and investment history.
Generated: DETERMINISTIC_7d352ddd0fb82c32
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def evaluate_risk_tolerance(financial_goals, investment_history):
    """
    Evaluates the risk tolerance of an investor based on their financial goals and investment history.

    Parameters:
    financial_goals (dict): A dictionary containing the investor's financial goals with keys like 'time_horizon' and 'return_expectation'.
    investment_history (list): A list of dictionaries representing past investments with keys like 'amount', 'profit_or_loss', and 'risk_level'.

    Returns:
    str: A risk tolerance category ('Low', 'Moderate', 'High').
    """
    try:
        # Validate input
        if not isinstance(financial_goals, dict) or not isinstance(investment_history, list):
            raise ValueError("Invalid input. 'financial_goals' should be a dictionary and 'investment_history' should be a list.")

        # Extract financial goals
        time_horizon = financial_goals.get('time_horizon', 0)  # in years
        return_expectation = financial_goals.get('return_expectation', 0)  # percentage

        # Safety check on extracted values
        if time_horizon <= 0 or return_expectation <= 0:
            raise ValueError("Invalid financial goals. 'time_horizon' and 'return_expectation' should be positive values.")

        # Analyze investment history
        risk_score = 0
        for investment in investment_history:
            if not isinstance(investment, dict):
                raise ValueError("Invalid investment history. Each investment should be a dictionary.")

            amount = investment.get('amount', 0)
            profit_or_loss = investment.get('profit_or_loss', 0)
            risk_level = investment.get('risk_level', 'Low')

            if amount <= 0 or risk_level not in ['Low', 'Moderate', 'High']:
                raise ValueError("Invalid investment details. Ensure 'amount' is positive and 'risk_level' is valid.")

            # Risk scoring based on risk level
            risk_multiplier = {'Low': 1, 'Moderate': 2, 'High': 3}.get(risk_level, 1)
            risk_score += risk_multiplier * abs(profit_or_loss)

        # Calculate average risk score
        avg_risk_score = risk_score / len(investment_history) if investment_history else 0

        # Determine risk tolerance category
        if avg_risk_score < 50 and time_horizon >= 10 and return_expectation <= 7:
            return "Low"
        elif avg_risk_score < 100 and time_horizon >= 5 and return_expectation <= 15:
            return "Moderate"
        else:
            return "High"

    except ValueError as ve:
        # Handle invalid input errors
        return f"Error evaluating risk tolerance: {ve}"

    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    # Example usage
    financial_goals = {
        "time_horizon": 10,  # years
        "return_expectation": 7  # percentage
    }

    investment_history = [
        {"amount": 10000, "profit_or_loss": -500, "risk_level": "Low"},
        {"amount": 20000, "profit_or_loss": 3000, "risk_level": "Moderate"},
        {"amount": 15000, "profit_or_loss": -2000, "risk_level": "High"}
    ]

    # Evaluate risk tolerance
    risk_tolerance = evaluate_risk_tolerance(financial_goals, investment_history)
    print(f"Investor's Risk Tolerance: {risk_tolerance}")
```
