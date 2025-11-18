"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lndscom.pages.dev
Prompt: Write a script to calculate the total Leonidas tokens received for various ETH amounts (e.g., 0.1 ETH, 0.2 ETH, etc.) based on the presale pricing model.
Generated: DETERMINISTIC_1de89a77d1d38d07
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total Leonidas tokens received for various ETH amounts
# based on the presale pricing model.

# Import required modules
import sys

def calculate_tokens(eth_amount):
    """
    Calculate the number of Leonidas tokens for a given ETH amount based on the presale pricing model.
    
    Presale pricing model:
    - 1 ETH = 1000 Leonidas tokens
    - Discounts for higher amounts:
        - Up to 0.5 ETH: No discount
        - 0.5 ETH to 1 ETH: 5% bonus tokens
        - Above 1 ETH: 10% bonus tokens
    
    Args:
        eth_amount (float): Amount of ETH.
    
    Returns:
        float: Total Leonidas tokens received.
    """
    # Base rate: 1 ETH = 1000 tokens
    base_rate = 1000
    
    if eth_amount <= 0:
        raise ValueError("ETH amount must be greater than zero.")
    
    # Calculate base tokens
    tokens = eth_amount * base_rate
    
    # Apply bonus tokens based on presale tiers
    if eth_amount > 1:
        # 10% bonus for > 1 ETH
        bonus_tokens = tokens * 0.10
    elif eth_amount >= 0.5:
        # 5% bonus for >= 0.5 ETH and <= 1 ETH
        bonus_tokens = tokens * 0.05
    else:
        # No bonus for < 0.5 ETH
        bonus_tokens = 0
    
    # Return the total tokens
    return tokens + bonus_tokens


def main():
    """
    Main function to interact with the user and calculate Leonidas tokens.
    """
    print("Leonidas Token Calculator")
    print("Presale pricing model:")
    print("  1 ETH = 1000 Leonidas tokens")
    print("  Bonus tiers:")
    print("    - Up to 0.5 ETH: No discount")
    print("    - 0.5 ETH to 1 ETH: 5% bonus tokens")
    print("    - Above 1 ETH: 10% bonus tokens")
    
    try:
        # Prompt user for ETH amounts
        eth_amounts = input("Enter ETH amounts separated by commas (e.g., 0.1, 0.2, 0.5): ").split(',')
        
        # Convert input to float and calculate tokens
        for eth_str in eth_amounts:
            try:
                eth_amount = float(eth_str.strip())
                tokens_received = calculate_tokens(eth_amount)
                print(f"{eth_amount} ETH → {tokens_received:.2f} Leonidas tokens")
            except ValueError:
                print(f"Invalid ETH amount: {eth_str.strip()} (must be a positive number)")
                
    except KeyboardInterrupt:
        print("\nCalculation canceled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
