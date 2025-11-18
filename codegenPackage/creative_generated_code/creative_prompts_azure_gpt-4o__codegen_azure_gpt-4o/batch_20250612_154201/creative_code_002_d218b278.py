"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodelyai-web3.pages.dev
Prompt: Create a function to calculate the variable APR based on the total percentage of $NODE tokens staked, as described in the Nodely AI documentation.
Generated: DETERMINISTIC_d218b278705d8004
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_variable_apr(tokens_staked_percentage: float) -> float:
    """
    Calculate the variable Annual Percentage Rate (APR) based on the percentage of $NODE tokens staked.

    Args:
        tokens_staked_percentage (float): The percentage of $NODE tokens staked (0-100).

    Returns:
        float: The calculated APR as a percentage.

    Raises:
        ValueError: If the input percentage is not within the valid range (0-100).
    """

    # Validate input
    if tokens_staked_percentage < 0 or tokens_staked_percentage > 100:
        raise ValueError("tokens_staked_percentage must be between 0 and 100 inclusive.")

    # Define APR calculation rules based on documentation
    if tokens_staked_percentage < 20:
        apr = 50.0  # High reward for low staking participation
    elif 20 <= tokens_staked_percentage <= 50:
        apr = 35.0  # Moderate reward for balanced staking
    elif 50 < tokens_staked_percentage <= 80:
        apr = 20.0  # Lower reward as more nodes are staked
    else:  # tokens_staked_percentage > 80
        apr = 10.0  # Minimal reward for high staking participation

    return apr


# Example usage:
if __name__ == "__main__":
    try:
        percentage_staked = 45.0  # Replace this value with user input or real data
        apr = calculate_variable_apr(percentage_staked)
        print(f"Variable APR for {percentage_staked}% staked: {apr}%")
    except ValueError as e:
        print(f"Error: {e}")
```
