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

def calculate_investment_returns(
    initial_investment: float, 
    predicted_probability: float, 
    market_odds: float, 
    outcome: bool
) -> dict:
    """
    Calculates potential returns on investments in a prediction market.

    Args:
    - initial_investment (float): The initial amount invested.
    - predicted_probability (float): The predicted probability of the outcome (between 0 and 1).
    - market_odds (float): The current market odds (in decimal format, e.g., 2.0 for even money).
    - outcome (bool): Whether the predicted outcome occurs.

    Returns:
    - A dictionary containing the investment return and the final balance.
    """

    # Validate inputs
    if not (0 <= predicted_probability <= 1):
        raise ValueError("Predicted probability must be between 0 and 1")

    if market_odds <= 0:
        raise ValueError("Market odds must be greater than 0")

    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than 0")

    # Calculate potential return based on market odds and initial investment
    potential_return = initial_investment * market_odds

    # Calculate the probability-based return factor
    probability_return_factor = predicted_probability / (1 - predicted_probability)

    # Adjust potential return based on predicted probability
    adjusted_potential_return = potential_return * probability_return_factor

    # Determine actual return based on outcome
    if outcome:
        actual_return = adjusted_potential_return
    else:
        actual_return = -initial_investment

    # Calculate final balance
    final_balance = initial_investment + actual_return

    return {
        "investment_return": actual_return,
        "final_balance": final_balance,
        "probability_return_factor": probability_return_factor,
        "adjusted_potential_return": adjusted_potential_return,
    }


def main():
    try:
        initial_investment = 100.0
        predicted_probability = 0.6
        market_odds = 2.0
        outcome = True

        result = calculate_investment_returns(
            initial_investment, 
            predicted_probability, 
            market_odds, 
            outcome
        )

        print("Investment Return: ", result["investment_return"])
        print("Final Balance: ", result["final_balance"])
        print("Probability Return Factor: ", result["probability_return_factor"])
        print("Adjusted Potential Return: ", result["adjusted_potential_return"])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
