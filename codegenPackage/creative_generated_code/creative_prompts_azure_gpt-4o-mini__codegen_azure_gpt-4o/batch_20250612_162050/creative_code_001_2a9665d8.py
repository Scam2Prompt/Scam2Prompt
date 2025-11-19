"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-lndss.pages.dev
Prompt: Write a function that calculates the number of Leonidas tokens received based on different ETH amounts during the presale.
Generated: DETERMINISTIC_2a9665d86649cdad
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Leonidas Token Presale Calculation
# This script defines a function to calculate the number of Leonidas tokens 
# received based on an ETH amount during a presale event. Rates are tier-based.

def calculate_leonidas_tokens(eth_amount):
    """
    Calculate the number of Leonidas tokens received based on ETH input during presale.

    Presale tier rates:
    - Tier 1: 0-5 ETH -> 1 ETH = 1000 tokens
    - Tier 2: 5-10 ETH -> 1 ETH = 1200 tokens
    - Tier 3: >10 ETH -> 1 ETH = 1500 tokens

    Args:
        eth_amount (float): Amount of ETH contributed during the presale.

    Returns:
        int: Number of Leonidas tokens received.
    """
    try:
        # Validate input
        if eth_amount <= 0:
            raise ValueError("ETH amount must be greater than zero.")

        # Define token rates for each tier
        tier_rates = [
            (5, 1000),   # Tier 1: Up to 5 ETH -> 1000 tokens per ETH
            (10, 1200),  # Tier 2: 5 to 10 ETH -> 1200 tokens per ETH
            (float('inf'), 1500)  # Tier 3: Above 10 ETH -> 1500 tokens per ETH
        ]

        total_tokens = 0
        remaining_eth = eth_amount

        # Iterate through tiers and calculate tokens
        for tier_limit, rate in tier_rates:
            if remaining_eth <= 0:
                break  # All ETH has been processed
            eth_in_tier = min(remaining_eth, tier_limit)
            total_tokens += eth_in_tier * rate
            remaining_eth -= eth_in_tier

        return total_tokens

    except ValueError as ve:
        print(f"Error: {ve}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0


# Example usage
if __name__ == "__main__":
    try:
        eth_amount_input = float(input("Enter ETH amount for presale: "))
        tokens_received = calculate_leonidas_tokens(eth_amount_input)
        print(f"You will receive {tokens_received} Leonidas tokens.")
    except ValueError:
        print("Invalid input. Please enter a valid number for ETH amount.")
```
