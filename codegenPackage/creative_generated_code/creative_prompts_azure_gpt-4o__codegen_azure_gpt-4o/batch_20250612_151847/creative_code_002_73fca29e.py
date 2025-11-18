"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Generate code to calculate the distribution percentages of TOR tokens based on the allocation plan provided (e.g., 25% for Airdrop, 10% for Pre-sale, etc.) using Python.
Generated: DETERMINISTIC_73fca29ebd7f8c15
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List

def calculate_distribution(total_tokens: int, allocation_plan: Dict[str, float]) -> Dict[str, int]:
    """
    Calculate the distribution percentages of tokens based on the allocation plan.

    Args:
        total_tokens (int): The total number of tokens to be distributed.
        allocation_plan (Dict[str, float]): A dictionary containing the allocation plan
            with the percentage for each category. Percentages should sum to 100.

    Returns:
        Dict[str, int]: A dictionary with the number of tokens allocated for each category.

    Raises:
        ValueError: If the percentages in the allocation plan do not sum to 100.
    """
    # Validate that the allocation plan percentages sum to 100%
    total_percentage = sum(allocation_plan.values())
    if not abs(total_percentage - 100.0) < 1e-6:  # Allow for floating-point precision
        raise ValueError("The allocation plan percentages must sum to 100.")

    # Calculate token allocation for each category
    distribution = {}
    for category, percentage in allocation_plan.items():
        # Using floor division to ensure the result is an integer
        distribution[category] = int((percentage / 100) * total_tokens)

    # Adjust for any rounding errors to ensure total distribution matches total_tokens
    distributed_tokens = sum(distribution.values())
    if distributed_tokens != total_tokens:
        # Find the category to adjust (typically the largest percentage category)
        largest_category = max(allocation_plan, key=allocation_plan.get)
        adjustment = total_tokens - distributed_tokens
        distribution[largest_category] += adjustment

    return distribution

if __name__ == "__main__":
    # Example usage
    try:
        # Define the total tokens and allocation plan
        total_tokens = 1000000  # Total number of TOR tokens
        allocation_plan = {
            "Airdrop": 25.0,   # 25%
            "Pre-sale": 10.0,  # 10%
            "Team": 20.0,      # 20%
            "Reserve": 45.0    # 45%
        }

        # Calculate distribution
        token_distribution = calculate_distribution(total_tokens, allocation_plan)

        # Print the resulting distribution
        print("Token Distribution:")
        for category, tokens in token_distribution.items():
            print(f"{category}: {tokens} tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
