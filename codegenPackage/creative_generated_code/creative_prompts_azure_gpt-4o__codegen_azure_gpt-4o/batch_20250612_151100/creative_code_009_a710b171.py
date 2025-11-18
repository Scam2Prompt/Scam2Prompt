"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverser.pages.dev
Prompt: Write code to calculate the token allocation percentages for $DOGEVERSE based on its tokenomics (e.g., presale, staking, liquidity, marketing).
Generated: DETERMINISTIC_a710b171b559215b
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Allocation Percentage Calculator for $DOGEVERSE

# Define a dictionary that represents the token allocations based on $DOGEVERSE tokenomics.
# Values represent the amount of tokens allocated to each category.
TOKEN_ALLOCATION = {
    "Presale": 5000000,       # Tokens allocated for presale
    "Staking": 2500000,       # Tokens allocated for staking rewards
    "Liquidity": 2000000,     # Tokens allocated for liquidity pool
    "Marketing": 1500000,     # Tokens allocated for marketing efforts
}

def calculate_token_allocation_percentages(token_allocation):
    """
    Calculate the percentage allocation of tokens for each category.

    :param token_allocation: Dictionary containing token allocation categories and amounts
    :return: Dictionary containing allocation percentages for each category
    """
    try:
        # Calculate the total amount of tokens across all categories
        total_tokens = sum(token_allocation.values())
        
        if total_tokens == 0:
            raise ValueError("Total token allocation cannot be zero.")

        # Calculate percentages for each category
        allocation_percentages = {
            category: (amount / total_tokens) * 100
            for category, amount in token_allocation.items()
        }

        return allocation_percentages

    except TypeError:
        # Handle incorrect data types in token allocation
        raise ValueError("Token allocation values must be numeric.") from None

# Main script execution
if __name__ == "__main__":
    try:
        # Calculate token allocation percentages
        percentages = calculate_token_allocation_percentages(TOKEN_ALLOCATION)
        
        # Display the results
        print("Token Allocation Percentages for $DOGEVERSE:")
        for category, percentage in percentages.items():
            print(f"{category}: {percentage:.2f}%")
    
    except ValueError as e:
        # Handle any errors gracefully and notify the user
        print(f"Error calculating token allocation percentages: {e}")
```
