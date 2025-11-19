"""
Generated Code Metadata:
========================
Original URL: https://portal-coln.pages.dev
Prompt: Using the $PORTAL tokenomics breakdown, write a Python function to calculate the percentage of tokens allocated to "Early Contributors" and "Community Reserve" based on the total supply of 1,000,000,000 tokens.
Generated: DETERMINISTIC_f1268d486ddfeed2
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_allocation(total_supply: int, early_contributors: int, community_reserve: int) -> dict:
    """
    Calculate the percentage of tokens allocated to Early Contributors and Community Reserve.

    Parameters:
    total_supply (int): The total supply of tokens.
    early_contributors (int): The number of tokens allocated to Early Contributors.
    community_reserve (int): The number of tokens allocated to Community Reserve.

    Returns:
    dict: A dictionary containing the percentage allocations for Early Contributors and Community Reserve.
    """
    # Validate input values
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    if early_contributors < 0 or community_reserve < 0:
        raise ValueError("Token allocations must be non-negative.")

    # Calculate percentages
    early_contributors_percentage = (early_contributors / total_supply) * 100
    community_reserve_percentage = (community_reserve / total_supply) * 100

    # Return the results in a dictionary
    return {
        "Early Contributors Percentage": early_contributors_percentage,
        "Community Reserve Percentage": community_reserve_percentage
    }

# Example usage
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # Total supply of tokens
    EARLY_CONTRIBUTORS = 150_000_000  # Example allocation for Early Contributors
    COMMUNITY_RESERVE = 100_000_000  # Example allocation for Community Reserve

    try:
        allocation = calculate_token_allocation(TOTAL_SUPPLY, EARLY_CONTRIBUTORS, COMMUNITY_RESERVE)
        print(allocation)
    except ValueError as e:
        print(f"Error: {e}")
```
