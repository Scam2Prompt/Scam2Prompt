"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Generate a code snippet for calculating the total supply and allocation percentages for Doge2014 tokens based on the provided tokenomics.
Generated: DETERMINISTIC_fde70b67acde8c79
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_allocation():
    """
    Calculate the total supply and allocation percentages for Doge2014 tokens.
    Returns a dictionary with allocation details.
    """
    # Tokenomics parameters
    total_supply = 420_690_000_000_000  # Total supply in tokens
    
    allocation = {
        'presale': 0.30,       # 30%
        'liquidity': 0.25,     # 25%
        'development': 0.15,   # 15%
        'marketing': 0.10,     # 10%
        'team': 0.10,          # 10%
        'community': 0.10      # 10%
    }
    
    # Validate allocation sums to 100%
    if not round(sum(allocation.values()), 2) == 1.00:
        raise ValueError("Allocation percentages do not sum to 100%")
    
    # Calculate token amounts for each category
    token_allocation = {
        category: {
            'percentage': f"{percentage * 100:.2f}%",
            'tokens': int(total_supply * percentage)
        }
        for category, percentage in allocation.items()
    }
    
    return {
        'total_supply': total_supply,
        'allocations': token_allocation
    }


if __name__ == "__main__":
    try:
        token_data = calculate_token_allocation()
        print("Token Allocation Details:")
        print(f"Total Supply: {token_data['total_supply']:,} DOGE2014")
        print("\nBreakdown:")
        for category, details in token_data['allocations'].items():
            print(f"{category.capitalize()}: {details['percentage']} ({details['tokens']:,} tokens)")
    except ValueError as e:
        print(f"Error: {e}")
```
