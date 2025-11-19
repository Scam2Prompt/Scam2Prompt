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
# Import necessary modules
from typing import Dict

def calculate_token_distribution(total_tokens: int, tokenomics: Dict[str, float]) -> Dict[str, int]:
    """
    Calculate the distribution of PUNDU tokens based on tokenomics percentages.

    Args:
        total_tokens (int): The total number of PUNDU tokens available for distribution.
        tokenomics (Dict[str, float]): A dictionary where keys are categories (e.g., "Team", "Marketing")
                                        and values are the percentage allocation for each category.

    Returns:
        Dict[str, int]: A dictionary where keys are categories and values are the number of tokens allocated.
    
    Raises:
        ValueError: If the sum of percentages in tokenomics does not equal 100.
        ValueError: If any percentage in tokenomics is negative.
    """
    # Validate input percentages
    if not isinstance(total_tokens, int) or total_tokens <= 0:
        raise ValueError("Total tokens must be a positive integer.")
    
    if not isinstance(tokenomics, dict) or not tokenomics:
        raise ValueError("Tokenomics must be a non-empty dictionary.")
    
    total_percentage = sum(tokenomics.values())
    if total_percentage != 100:
        raise ValueError("The sum of tokenomics percentages must equal 100.")
    
    if any(percent < 0 for percent in tokenomics.values()):
        raise ValueError("Tokenomics percentages cannot be negative.")

    # Calculate token distribution
    distribution = {}
    for category, percentage in tokenomics.items():
        # Calculate tokens for each category and round down to the nearest integer
        distribution[category] = int(total_tokens * (percentage / 100))

    # Handle rounding errors to ensure the total distribution matches total_tokens
    distributed_tokens = sum(distribution.values())
    rounding_error = total_tokens - distributed_tokens

    # Adjust rounding error by adding/subtracting tokens to/from the largest category
    if rounding_error != 0:
        largest_category = max(distribution, key=distribution.get)
        distribution[largest_category] += rounding_error

    return distribution

# Example usage
if __name__ == "__main__":
    # Define total tokens and tokenomics percentages
    total_tokens = 1000000  # Total number of PUNDU tokens
    tokenomics = {
        "Team": 40.0,       # 40% for the team
        "Marketing": 30.0,  # 30% for marketing
        "Development": 20.0, # 20% for development
        "Reserve": 10.0     # 10% for reserve
    }

    try:
        # Calculate token distribution
        distribution = calculate_token_distribution(total_tokens, tokenomics)
        print("Token Distribution:", distribution)
    except ValueError as e:
        print("Error:", e)
```
