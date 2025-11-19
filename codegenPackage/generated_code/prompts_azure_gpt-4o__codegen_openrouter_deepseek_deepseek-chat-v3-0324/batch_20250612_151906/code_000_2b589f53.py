"""
Generated Code Metadata:
========================
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Write a Python script to calculate the token distribution of BEFE based on its total supply (100,000,000,000) and the percentages provided (80% for fair launch LP and 20% for airdrop).
Generated: DETERMINISTIC_2b589f533a50964d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_distribution(total_supply, fair_launch_percentage, airdrop_percentage):
    """
    Calculate the token distribution based on given percentages.
    
    Args:
        total_supply (int): Total supply of tokens
        fair_launch_percentage (float): Percentage for fair launch LP (0-100)
        airdrop_percentage (float): Percentage for airdrop (0-100)
    
    Returns:
        dict: Dictionary containing distribution amounts
    """
    try:
        # Validate input percentages sum to 100
        if abs((fair_launch_percentage + airdrop_percentage) - 100) > 0.001:
            raise ValueError("Percentages must sum to 100")
            
        # Calculate distribution amounts
        fair_launch_tokens = (total_supply * fair_launch_percentage) / 100
        airdrop_tokens = (total_supply * airdrop_percentage) / 100
        
        return {
            "total_supply": total_supply,
            "fair_launch_lp": {
                "percentage": fair_launch_percentage,
                "tokens": int(fair_launch_tokens)
            },
            "airdrop": {
                "percentage": airdrop_percentage,
                "tokens": int(airdrop_tokens)
            }
        }
        
    except Exception as e:
        print(f"Error calculating token distribution: {e}")
        return None

if __name__ == "__main__":
    # Token distribution parameters
    TOTAL_SUPPLY = 100_000_000_000
    FAIR_LAUNCH_PERCENTAGE = 80.0
    AIRDROP_PERCENTAGE = 20.0
    
    # Calculate distribution
    distribution = calculate_token_distribution(
        TOTAL_SUPPLY,
        FAIR_LAUNCH_PERCENTAGE,
        AIRDROP_PERCENTAGE
    )
    
    if distribution:
        print("Token Distribution:")
        print(f"Total Supply: {distribution['total_supply']:,}")
        print(f"Fair Launch LP: {distribution['fair_launch_lp']['tokens']:,} ({distribution['fair_launch_lp']['percentage']}%)")
        print(f"Airdrop: {distribution['airdrop']['tokens']:,} ({distribution['airdrop']['percentage']}%)")
```
