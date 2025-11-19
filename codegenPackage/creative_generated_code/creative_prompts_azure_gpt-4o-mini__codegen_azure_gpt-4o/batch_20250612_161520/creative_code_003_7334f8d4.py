"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Create a function that calculates potential earnings from staking $MGLS tokens based on different annual return percentages.
Generated: DETERMINISTIC_7334f8d46492cf9c
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This Python script calculates potential earnings from staking $MGLS tokens 
# based on different annual return percentages.

def calculate_staking_earnings(principal: float, annual_returns: list, years: int) -> dict:
    """
    Calculate potential earnings for staking $MGLS tokens.

    :param principal: Initial amount of $MGLS tokens staked.
    :param annual_returns: A list of annual return percentages (e.g., [5, 10, 15]).
    :param years: Number of years the tokens will be staked.
    :return: A dictionary where keys are annual return percentages and values are the total earnings after staking.
    """
    
    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if years <= 0:
        raise ValueError("Number of years must be greater than zero.")
    if not annual_returns or not all(isinstance(rate, (int, float)) and rate > 0 for rate in annual_returns):
        raise ValueError("Annual returns must be a list of positive numbers.")

    # Dictionary to store earnings for each return percentage
    earnings = {}

    for rate in annual_returns:
        # Convert percentage to a decimal for calculation
        decimal_rate = rate / 100
        # Compound formula to calculate total amount after staking
        total_amount = principal * ((1 + decimal_rate) ** years)
        # Calculate earnings (total amount - principal)
        earnings[rate] = round(total_amount - principal, 2)

    return earnings


# Example usage:
if __name__ == "__main__":
    try:
        # User inputs
        principal_amount = 1000  # Initial amount of $MGLS tokens
        annual_percentage_returns = [5, 10, 15]  # Annual return percentages
        staking_duration = 3  # Number of years

        # Calculate potential earnings
        potential_earnings = calculate_staking_earnings(principal_amount, annual_percentage_returns, staking_duration)
        
        # Display results
        print(f"Potential earnings after {staking_duration} years of staking:")
        for rate, earnings in potential_earnings.items():
            print(f"  {rate}% annual return: ${earnings}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
