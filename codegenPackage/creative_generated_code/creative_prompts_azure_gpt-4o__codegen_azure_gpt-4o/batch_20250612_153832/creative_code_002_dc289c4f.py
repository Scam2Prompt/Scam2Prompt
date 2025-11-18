"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Create a function to calculate the total bonus tokens a user receives during the Sophon Network Stage 2 presale, considering the 15% bonus offer.
Generated: DETERMINISTIC_dc289c4fca0f79b8
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonus_tokens(purchased_tokens: float, bonus_percentage: float = 15.0) -> float:
    """
    Calculate the total bonus tokens a user receives during the Sophon Network Stage 2 presale.

    Args:
        purchased_tokens (float): The number of tokens purchased by the user.
        bonus_percentage (float): The percentage of bonus tokens offered during the presale. Default is 15%.

    Returns:
        float: The total bonus tokens the user receives.

    Raises:
        ValueError: If purchased_tokens is negative or zero.
    """
    # Validate the input
    if purchased_tokens <= 0:
        raise ValueError("Purchased tokens must be greater than zero.")

    # Calculate the bonus tokens
    bonus_tokens = purchased_tokens * (bonus_percentage / 100)

    return bonus_tokens


# Example usage:
if __name__ == "__main__":
    try:
        # Tokens purchased by the user
        tokens_purchased = 1000

        # Calculate bonus tokens
        bonus = calculate_bonus_tokens(tokens_purchased)
        
        print(f"Purchased Tokens: {tokens_purchased}, Bonus Tokens: {bonus}")
    except ValueError as e:
        print(f"Error: {e}")
```
