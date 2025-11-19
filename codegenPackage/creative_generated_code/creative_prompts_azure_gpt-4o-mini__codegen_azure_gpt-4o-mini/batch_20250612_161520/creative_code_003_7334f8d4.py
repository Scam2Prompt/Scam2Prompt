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
def calculate_staking_earnings(staked_amount, annual_return_percentage, years):
    """
    Calculate the potential earnings from staking MGLS tokens.

    Parameters:
    staked_amount (float): The amount of MGLS tokens being staked.
    annual_return_percentage (float): The expected annual return percentage (e.g., 5 for 5%).
    years (int): The number of years the tokens will be staked.

    Returns:
    float: The total value of the staked amount after the specified number of years, including earnings.
    float: The total earnings from staking.
    
    Raises:
    ValueError: If staked_amount, annual_return_percentage, or years are negative or staked_amount is zero.
    """

    # Input validation
    if staked_amount <= 0:
        raise ValueError("Staked amount must be greater than zero.")
    if annual_return_percentage < 0:
        raise ValueError("Annual return percentage cannot be negative.")
    if years < 0:
        raise ValueError("Number of years cannot be negative.")

    # Calculate total value after staking
    total_value = staked_amount * ((1 + (annual_return_percentage / 100)) ** years)
    
    # Calculate earnings
    earnings = total_value - staked_amount
    
    return total_value, earnings


# Example usage
if __name__ == "__main__":
    try:
        staked_amount = 1000.0  # Amount of MGLS tokens
        annual_return_percentage = 5.0  # Expected annual return in percentage
        years = 3  # Number of years to stake
        
        total_value, earnings = calculate_staking_earnings(staked_amount, annual_return_percentage, years)
        
        print(f"Total value after {years} years: ${total_value:.2f}")
        print(f"Total earnings after {years} years: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
