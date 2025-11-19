"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenafex.com
Prompt: Create a function that calculates potential returns on investments in a prediction market, taking inspiration from Zenafex’s trading model.
Generated: DETERMINISTIC_fb9212890e4fc730
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate potential returns on investments
# in a prediction market inspired by Zenafex's trading model.

def calculate_potential_returns(investment, probability, payout_multiplier):
    """
    Calculate potential returns on an investment in a prediction market.

    :param investment: float - The amount of money invested.
    :param probability: float - The probability (0.0 to 1.0) of the event occurring.
    :param payout_multiplier: float - The payout multiplier if the event occurs.

    :return: dict - A dictionary containing:
        - 'expected_return': Expected monetary return based on the probabilities.
        - 'break_even_probability': Probability at which the investment breaks even.
    """
    try:
        # Validate inputs
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0.0 and 1.0 (inclusive).")
        if investment <= 0:
            raise ValueError("Investment must be greater than 0.")
        if payout_multiplier <= 0:
            raise ValueError("Payout multiplier must be greater than 0.")

        # Calculate expected return
        expected_return = (probability * payout_multiplier * investment) - investment

        # Calculate break-even probability
        break_even_probability = 1 / payout_multiplier

        # Return results as a dictionary
        return {
            'expected_return': expected_return,
            'break_even_probability': break_even_probability
        }

    except ValueError as e:
        # Handle invalid inputs gracefully
        return {'error': str(e)}

    except Exception as e:
        # Catch unexpected errors
        return {'error': f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # User inputs
    investment_amount = 1000  # Amount invested
    event_probability = 0.7  # Probability of the event occurring
    payout_ratio = 2.5        # Payout multiplier

    # Calculate returns
    result = calculate_potential_returns(investment_amount, event_probability, payout_ratio)
    
    # Display results
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Expected Return: ${result['expected_return']:.2f}")
        print(f"Break-Even Probability: {result['break_even_probability']:.2%}")
```
