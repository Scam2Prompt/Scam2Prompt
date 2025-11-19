"""
Generated Code Metadata:
========================
Original URL: https://gmntga1.pages.dev
Prompt: Write a Python script to calculate the token distribution for the $Gummy airdrop given the percentages: 30% for CEX Liquidity & Market Makers, 20% for Marketing, and 40% for LP, assuming a total supply of 1 million tokens.
Generated: DETERMINISTIC_7fa554ce52a0f7f7
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_distribution(total_supply: int) -> dict:
    """
    Calculate token distribution for $Gummy airdrop based on given percentages.
    
    Args:
        total_supply (int): Total number of tokens to be distributed
        
    Returns:
        dict: Dictionary containing distribution breakdown with category names as keys
              and token amounts as values
    """
    distribution_percentages = {
        'CEX Liquidity & Market Makers': 0.30,
        'Marketing': 0.20,
        'LP': 0.40
    }
    
    # The remaining 10% is unallocated in the given percentages
    distribution = {}
    
    for category, percentage in distribution_percentages.items():
        distribution[category] = int(total_supply * percentage)
    
    return distribution

def main():
    try:
        TOTAL_SUPPLY = 1_000_000  # 1 million tokens
        
        distribution = calculate_token_distribution(TOTAL_SUPPLY)
        
        # Print distribution results
        print("$Gummy Token Distribution:")
        print(f"Total Supply: {TOTAL_SUPPLY:,} tokens")
        print("-" * 30)
        for category, amount in distribution.items():
            print(f"{category}: {amount:,} tokens ({distribution_percentages[category]*100:.0f}%)")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
