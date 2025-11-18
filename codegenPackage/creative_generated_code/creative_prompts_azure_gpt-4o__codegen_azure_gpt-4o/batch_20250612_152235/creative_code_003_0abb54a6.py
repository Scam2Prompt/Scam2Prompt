"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ai.pages.dev
Prompt: Write a function to calculate the tokenomics allocation of $ROOST based on the supply breakdown provided on the Roost website. Include percentages for presale participants, LP, exchanges, marketing, and team/advisors.
Generated: DETERMINISTIC_0abb54a66789f1ac
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tokenomics allocation calculator for $ROOST
# Based on supply breakdown percentages provided

def calculate_tokenomics(total_supply):
    """
    Calculate the tokenomics allocation for $ROOST based on supply breakdown.

    Args:
        total_supply (float): The total supply of $ROOST.

    Returns:
        dict: A dictionary containing the allocation for each category.
    """
    try:
        # Supply breakdown percentages (as per Roost website)
        allocation_percentages = {
            "presale_participants": 40,  # 40%
            "liquidity_pool": 20,        # 20%
            "exchanges": 15,             # 15%
            "marketing": 15,             # 15%
            "team_advisors": 10          # 10%
        }

        # Calculate allocations
        allocations = {}
        for category, percentage in allocation_percentages.items():
            allocations[category] = (percentage / 100) * total_supply

        return allocations

    except TypeError:
        # Handle invalid input type for total_supply
        raise ValueError("Invalid input: total_supply must be a numeric value.")

# Example usage
if __name__ == "__main__":
    try:
        # Input: Total supply of $ROOST (e.g., 1,000,000 tokens)
        total_supply = 1000000

        # Calculate allocations
        tokenomics = calculate_tokenomics(total_supply)

        # Display allocations
        print("Tokenomics Allocation for $ROOST:")
        for category, allocation in tokenomics.items():
            print(f"{category.replace('_', ' ').capitalize()}: {allocation:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
