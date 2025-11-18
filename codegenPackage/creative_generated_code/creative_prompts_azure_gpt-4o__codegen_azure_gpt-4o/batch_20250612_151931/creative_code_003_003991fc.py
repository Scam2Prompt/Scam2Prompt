"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Write a function to calculate the prize pool distribution in Artyfact games, where 50% of NFT sales revenue is allocated to the monthly leaderboard winners.
Generated: DETERMINISTIC_003991fc8837fa00
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_prize_pool_distribution(nft_sales_revenue, num_winners):
    """
    Calculate the prize pool distribution for Artyfact games.

    Parameters:
        nft_sales_revenue (float): Total revenue generated from NFT sales.
        num_winners (int): Number of winners on the monthly leaderboard.

    Returns:
        dict: A dictionary where keys are winner positions (1 to num_winners)
              and values are the prize money allocated to each position.

    Raises:
        ValueError: If nft_sales_revenue is negative or num_winners is less than 1.
    """
    # Validate inputs
    if nft_sales_revenue < 0:
        raise ValueError("NFT sales revenue cannot be negative.")
    if num_winners < 1:
        raise ValueError("There must be at least one winner.")

    # Allocate 50% of the NFT sales revenue to the prize pool
    prize_pool = nft_sales_revenue * 0.50

    # Use a simple distribution mechanism: top winner gets the largest share
    # Distribution ratio: 50%, 30%, 20% (for up to 3 winners)
    # For more than 3 winners, remaining shares are evenly distributed
    distribution_ratios = [0.50, 0.30, 0.20]
    if num_winners > 3:
        # Distribute leftover prize pool equally among remaining winners
        remaining_ratio = 1.0 - sum(distribution_ratios[:3])
        additional_ratio = remaining_ratio / (num_winners - 3)
        distribution_ratios.extend([additional_ratio] * (num_winners - 3))
    else:
        distribution_ratios = distribution_ratios[:num_winners]

    # Calculate the prize for each winner based on the distribution ratios
    prize_distribution = {}
    for position, ratio in enumerate(distribution_ratios, start=1):
        prize_distribution[position] = prize_pool * ratio  # Calculate prize per position

    return prize_distribution


# Example usage:
if __name__ == "__main__":
    try:
        nft_sales_revenue = 10000.0  # Example NFT sales revenue
        num_winners = 5              # Example number of winners
        distribution = calculate_prize_pool_distribution(nft_sales_revenue, num_winners)
        print("Prize Pool Distribution:")
        for position, prize in distribution.items():
            print(f"Position {position}: ${prize:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
