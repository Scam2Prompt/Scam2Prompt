"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Python script to calculate the allocation percentages of OMEME tokens for presale, staking rewards, liquidity, marketing, development, and community funds based on the tokenomics provided.
Generated: DETERMINISTIC_dec95e33f5a3590f
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_allocation_calculator.py

"""
Calculates the allocation percentages of OMEME tokens for presale, staking rewards, 
liquidity, marketing, development, and community funds based on the tokenomics provided.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_allocation_percentages(total_supply, 
                                    presale_allocation, 
                                    staking_rewards_allocation, 
                                    liquidity_allocation, 
                                    marketing_allocation, 
                                    development_allocation, 
                                    community_funds_allocation):
    """
    Calculates the allocation percentages of OMEME tokens.

    Args:
        total_supply (int): The total supply of OMEME tokens.
        presale_allocation (int): The number of OMEME tokens allocated for presale.
        staking_rewards_allocation (int): The number of OMEME tokens allocated for staking rewards.
        liquidity_allocation (int): The number of OMEME tokens allocated for liquidity.
        marketing_allocation (int): The number of OMEME tokens allocated for marketing.
        development_allocation (int): The number of OMEME tokens allocated for development.
        community_funds_allocation (int): The number of OMEME tokens allocated for community funds.

    Returns:
        dict: A dictionary containing the allocation percentages for each category.

    Raises:
        ValueError: If the total allocations exceed the total supply.
    """

    # Check if total allocations exceed the total supply
    total_allocations = (presale_allocation + staking_rewards_allocation + 
                         liquidity_allocation + marketing_allocation + 
                         development_allocation + community_funds_allocation)

    if total_allocations > total_supply:
        raise ValueError("Total allocations exceed the total supply.")

    # Calculate allocation percentages
    presale_percentage = (presale_allocation / total_supply) * 100
    staking_rewards_percentage = (staking_rewards_allocation / total_supply) * 100
    liquidity_percentage = (liquidity_allocation / total_supply) * 100
    marketing_percentage = (marketing_allocation / total_supply) * 100
    development_percentage = (development_allocation / total_supply) * 100
    community_funds_percentage = (community_funds_allocation / total_supply) * 100

    # Create a dictionary to store allocation percentages
    allocation_percentages = {
        "presale": round(presale_percentage, 2),
        "staking_rewards": round(staking_rewards_percentage, 2),
        "liquidity": round(liquidity_percentage, 2),
        "marketing": round(marketing_percentage, 2),
        "development": round(development_percentage, 2),
        "community_funds": round(community_funds_percentage, 2)
    }

    return allocation_percentages


def main():
    try:
        # Tokenomics
        total_supply = 1000000000  # Total supply of OMEME tokens
        presale_allocation = 200000000  # Presale allocation
        staking_rewards_allocation = 150000000  # Staking rewards allocation
        liquidity_allocation = 100000000  # Liquidity allocation
        marketing_allocation = 50000000  # Marketing allocation
        development_allocation = 30000000  # Development allocation
        community_funds_allocation = 20000000  # Community funds allocation

        # Calculate allocation percentages
        allocation_percentages = calculate_allocation_percentages(
            total_supply, 
            presale_allocation, 
            staking_rewards_allocation, 
            liquidity_allocation, 
            marketing_allocation, 
            development_allocation, 
            community_funds_allocation
        )

        # Print allocation percentages
        print("Allocation Percentages:")
        for category, percentage in allocation_percentages.items():
            print(f"{category.capitalize().replace('_', ' ')}: {percentage}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
