"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write code to calculate token allocations for presale, staking, marketing, rewards, and liquidity, based on the $FROP tokenomics percentages.
Generated: DETERMINISTIC_c83701e2c6ead63e
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate $FROP token allocations based on tokenomics percentages

def calculate_token_allocations(total_supply, allocations):
    """
    Calculate token allocations based on the $FROP tokenomics percentages.

    Args:
        total_supply (int): The total supply of tokens.
        allocations (dict): A dictionary of allocation categories and their respective percentages.
    
    Returns:
        dict: A dictionary with allocation categories and their respective token amounts.
    """
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than 0")
    
    if not allocations or not isinstance(allocations, dict):
        raise ValueError("Allocations must be a non-empty dictionary")
    
    # Ensure percentages sum up to 100
    total_percentage = sum(allocations.values())
    if total_percentage != 100:
        raise ValueError("Allocation percentages must sum up to 100")

    # Calculate token allocations
    token_allocations = {}
    for category, percentage in allocations.items():
        token_allocations[category] = (total_supply * percentage) // 100  # Use floor division for integer results

    return token_allocations


# Example usage
if __name__ == "__main__":
    try:
        # Define total supply of $FROP tokens
        total_supply = 1000000  # Example: 1,000,000 tokens

        # Define $FROP tokenomics percentages
        tokenomics_percentages = {
            "Presale": 40,  # 40%
            "Staking": 20,  # 20%
            "Marketing": 15,  # 15%
            "Rewards": 15,  # 15%
            "Liquidity": 10  # 10%
        }

        # Calculate allocations
        allocations = calculate_token_allocations(total_supply, tokenomics_percentages)

        # Print allocation results
        print("Token Allocations:")
        for category, amount in allocations.items():
            print(f"{category}: {amount} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
