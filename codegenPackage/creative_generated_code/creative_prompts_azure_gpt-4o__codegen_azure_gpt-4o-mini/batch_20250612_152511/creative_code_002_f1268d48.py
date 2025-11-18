"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Using the $PORTAL tokenomics breakdown, write a Python function to calculate the percentage of tokens allocated to "Early Contributors" and "Community Reserve" based on the total supply of 1,000,000,000 tokens.
Generated: DETERMINISTIC_f1268d486ddfeed2
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_token_allocation(total_supply=1_000_000_000):
    """
    Calculate the percentage of tokens allocated to 'Early Contributors' and 'Community Reserve'.
    
    Parameters:
    total_supply (int): The total supply of tokens. Default is 1,000,000,000.
    
    Returns:
    dict: A dictionary containing the percentages for 'Early Contributors' and 'Community Reserve'.
    
    Raises:
    ValueError: If total_supply is less than or equal to zero.
    """
    
    # Validate the total supply value
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")

    # Token allocation values based on the $PORTAL tokenomics breakdown
    early_contributors_allocated = 150_000_000  # Example allocation for early contributors
    community_reserve_allocated = 100_000_000    # Example allocation for community reserve

    # Calculate percentages
    early_contributors_percentage = (early_contributors_allocated / total_supply) * 100
    community_reserve_percentage = (community_reserve_allocated / total_supply) * 100

    # Prepare the result dictionary
    allocation_percentages = {
        "Early Contributors": early_contributors_percentage,
        "Community Reserve": community_reserve_percentage
    }

    return allocation_percentages

# Example usage
if __name__ == "__main__":
    try:
        allocations = calculate_token_allocation()
        print("Token Allocation Percentages:")
        for category, percentage in allocations.items():
            print(f"{category}: {percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
