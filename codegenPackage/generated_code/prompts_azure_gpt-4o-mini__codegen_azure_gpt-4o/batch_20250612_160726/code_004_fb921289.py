"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: Create a function that calculates potential returns on investments in a prediction market, taking inspiration from Zenafex’s trading model.
Generated: DETERMINISTIC_fb9212890e4fc730
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_potential_returns(investment_amount, market_odds, probability_estimate):
    """
    Calculate potential returns on investments in a prediction market.

    Parameters:
    - investment_amount (float): The amount of money invested.
    - market_odds (float): The market odds expressed as a decimal (e.g., 2.5 for 150% return).
    - probability_estimate (float): The trader's estimated probability of the event occurring (0 to 1).

    Returns:
    - dict: A dictionary containing:
        - 'expected_return' (float): The expected monetary return based on the trader's probability estimate.
        - 'risk_factor' (float): The risk factor based on the difference between market odds and probability estimate.
    """
    try:
        # Validate inputs
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not (0 < market_odds):
            raise ValueError("Market odds must be greater than zero.")
        if not (0 <= probability_estimate <= 1):
            raise ValueError("Probability estimate must be between 0 and 1.")

        # Calculate expected return
        expected_return = investment_amount * market_odds * probability_estimate

        # Calculate risk factor (difference between market odds and probability estimate)
        risk_factor = abs(market_odds - (1 / probability_estimate)) if probability_estimate > 0 else math.inf

        # Return results as a dictionary
        return {
            'expected_return': round(expected_return, 2),
            'risk_factor': round(risk_factor, 2)
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Example inputs
    investment = 100.0  # $100 investment
    odds = 2.5          # Market odds (150% return)
    probability = 0.6   # Trader's estimated probability (60%)

    # Calculate potential returns
    result = calculate_potential_returns(investment, odds, probability)
    print(result)
```
