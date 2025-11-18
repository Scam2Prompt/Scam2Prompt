"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Generate code to calculate the token distribution percentages for Simon’s Cat Token based on the provided tokenomics, ensuring the values sum to 100%.
Generated: DETERMINISTIC_540ecc6cab32ccab
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# simons_cat_tokenomics.py

"""
This script calculates the token distribution percentages for Simon's Cat Token based 
on the provided tokenomics, ensuring the values sum to 100%.
"""

def calculate_token_distribution(tokenomics):
    """
    Calculates the percentage distribution of tokens based on tokenomics.

    Args:
        tokenomics (dict): A dictionary where keys are token categories (e.g., "Marketing", "Development")
                           and values are the number of tokens allocated to each category.

    Returns:
        dict: A dictionary where keys are token categories and values are the percentage distribution.
    """
    try:
        # Validate input
        if not isinstance(tokenomics, dict):
            raise TypeError("Tokenomics must be a dictionary with categories and token allocations.")
        
        total_tokens = sum(tokenomics.values())
        
        # Ensure total tokens is greater than zero to avoid division by zero
        if total_tokens <= 0:
            raise ValueError("Total token allocation must be greater than zero.")
        
        # Calculate percentage distribution
        distribution_percentages = {
            category: (tokens / total_tokens) * 100
            for category, tokens in tokenomics.items()
        }

        # Validate percentages sum up to 100 (accounting for floating-point imprecision)
        if not (99.99 <= sum(distribution_percentages.values()) <= 100.01):
            raise ValueError("Calculated percentages do not sum up to 100.")
        
        return distribution_percentages

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    # Example tokenomics input
    tokenomics = {
        "Marketing": 2000000,
        "Development": 1500000,
        "Liquidity": 1000000,
        "Community Rewards": 500000,
        "Reserve": 500000,
    }

    try:
        # Calculate distribution
        distribution = calculate_token_distribution(tokenomics)

        # Display the results
        print("Token Distribution Percentages:")
        for category, percentage in distribution.items():
            print(f"{category}: {percentage:.2f}%")
    except Exception as e:
        print("Failed to calculate token distribution.")
```
