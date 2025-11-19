"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Develop a function that calculates the distribution of PUNDU tokens based on the provided tokenomics percentages.
Generated: DETERMINISTIC_c9b0d26b627c934f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_token_distribution(total_tokens: int, tokenomics_percentages: Dict[str, float]) -> Dict[str, int]:
    """
    Calculate the distribution of PUNDU tokens based on the provided tokenomics percentages.

    Args:
    - total_tokens (int): The total number of PUNDU tokens.
    - tokenomics_percentages (Dict[str, float]): A dictionary containing the tokenomics percentages.

    Returns:
    - Dict[str, int]: A dictionary containing the distribution of PUNDU tokens.

    Raises:
    - ValueError: If the total tokens is less than or equal to 0.
    - ValueError: If the tokenomics percentages do not add up to 100.
    """

    # Check if total tokens is valid
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than 0")

    # Check if tokenomics percentages add up to 100
    if abs(sum(tokenomics_percentages.values()) - 100) > 1e-6:
        raise ValueError("Tokenomics percentages must add up to 100")

    # Initialize token distribution dictionary
    token_distribution = {}

    # Calculate token distribution
    remaining_tokens = total_tokens
    for category, percentage in tokenomics_percentages.items():
        # Calculate tokens for current category
        tokens = int((percentage / 100) * total_tokens)
        
        # Update remaining tokens
        remaining_tokens -= tokens

        # Store token distribution
        token_distribution[category] = tokens

    # Distribute remaining tokens to categories to avoid rounding errors
    if remaining_tokens > 0:
        categories = list(tokenomics_percentages.keys())
        for i in range(remaining_tokens):
            token_distribution[categories[i % len(categories)]] += 1

    return token_distribution


# Example usage:
if __name__ == "__main__":
    total_tokens = 1000000
    tokenomics_percentages = {
        "team": 20,
        "advisors": 10,
        "community": 30,
        "reserve": 40
    }

    try:
        token_distribution = calculate_token_distribution(total_tokens, tokenomics_percentages)
        print("Token Distribution:")
        for category, tokens in token_distribution.items():
            print(f"{category.capitalize()}: {tokens}")
    except ValueError as e:
        print(f"Error: {e}")
```
