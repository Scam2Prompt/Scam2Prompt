"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy-b3j.pages.dev
Prompt: Write a program to simulate the distribution of "$Gummy" tokens based on the tokenomics percentages provided (e.g., 30% LP burnt, 10% CEX liquidity, 20% market makers, 40% marketing).
Generated: DETERMINISTIC_3bfa5fee68788e5f
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def distribute_tokens(total_tokens, distribution_percentages):
    """
    Distributes tokens based on given percentages.

    Parameters:
        total_tokens (int): Total number of $Gummy tokens to distribute.
        distribution_percentages (dict): A dictionary of allocation percentages 
                                          (key: allocation name, value: percentage).

    Returns:
        dict: A dictionary with the calculated token distribution per allocation.
    """
    # Validate inputs
    if not isinstance(total_tokens, int) or total_tokens <= 0:
        raise ValueError("Total tokens must be a positive integer.")
    if not isinstance(distribution_percentages, dict) or not distribution_percentages:
        raise ValueError("Distribution percentages must be a non-empty dictionary.")

    # Check if the percentages sum up to 100
    total_percentage = sum(distribution_percentages.values())
    if total_percentage != 100:
        raise ValueError("Distribution percentages must sum up to 100.")

    # Calculate token allocation
    allocation = {}
    for allocation_name, percentage in distribution_percentages.items():
        # Calculate the number of tokens for each allocation
        allocation[allocation_name] = (total_tokens * percentage) // 100

    return allocation

def main():
    try:
        # Total number of $Gummy tokens
        total_tokens = 1000000  # Example: 1,000,000 tokens

        # Token distribution percentages
        distribution_percentages = {
            "LP burnt": 30,       # 30% of tokens for LP burnt
            "CEX liquidity": 10,  # 10% of tokens for CEX liquidity
            "Market makers": 20,  # 20% of tokens for market makers
            "Marketing": 40       # 40% of tokens for marketing
        }

        # Distribute tokens
        allocation = distribute_tokens(total_tokens, distribution_percentages)

        # Print the results
        print("Token Distribution:")
        for allocation_name, token_count in allocation.items():
            print(f"{allocation_name}: {token_count} tokens")

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
