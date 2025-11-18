"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befetoken.pages.dev
Prompt: Create a Python script to calculate the distribution of BEFE tokens based on the tokenomics provided (80% Fair Launch - LP, 20% Airdrop).
Generated: DETERMINISTIC_0ee5e19ce91bcc63
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the distribution of BEFE tokens based on tokenomics.

# Importing required libraries
import sys

def calculate_token_distribution(total_supply):
    """
    Calculate token distribution based on tokenomics.
    
    Parameters:
        total_supply (int): Total supply of BEFE tokens.
    
    Returns:
        dict: Distribution of tokens (LP and Airdrop).
    """
    try:
        # Validate total_supply
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        # Tokenomics percentages
        fair_launch_percentage = 80  # 80% for LP (Fair Launch)
        airdrop_percentage = 20      # 20% for Airdrop

        # Calculate distribution
        fair_launch_tokens = (fair_launch_percentage / 100) * total_supply
        airdrop_tokens = (airdrop_percentage / 100) * total_supply

        # Return distribution as a dictionary
        return {
            "Fair Launch (LP)": round(fair_launch_tokens),
            "Airdrop": round(airdrop_tokens)
        }
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example Usage:
    try:
        # Prompting user for total supply input
        total_supply = int(input("Enter the total supply of BEFE tokens: "))
        
        # Calculate and display distribution
        distribution = calculate_token_distribution(total_supply)
        print("\nToken Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens} tokens")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
