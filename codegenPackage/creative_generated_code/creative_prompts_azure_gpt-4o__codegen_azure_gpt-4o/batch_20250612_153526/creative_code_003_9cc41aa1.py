"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-coolcoinwtf.pages.dev
Prompt: Create a function that calculates the $COOL token allocation per NFT holder based on the Coolman's Universe (3,750 tokens) and Babies By Coolman (1,250 tokens) collections.
Generated: DETERMINISTIC_9cc41aa11580fed2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates $COOL token allocations for NFT holders based on the 
Coolman’s Universe and Babies by Coolman collections. 

Coolman's Universe holders: 3,750 tokens
Babies By Coolman holders: 1,250 tokens
"""

# Import necessary libraries
from typing import Dict

def calculate_token_allocation(nft_holdings: Dict[str, int]) -> Dict[str, float]:
    """
    Calculate the $COOL token allocation for NFT holders.

    Parameters:
        nft_holdings (Dict[str, int]): A dictionary where keys are wallet addresses
                                       and values are the number of NFTs held by each wallet.

    Returns:
        Dict[str, float]: A dictionary where keys are wallet addresses and values are the
                          $COOL token allocations for each wallet.
    """
    try:
        # Constants for token allocations per NFT
        COOLMAN_UNIVERSE_TOKENS = 3750
        BABIES_BY_COOLMAN_TOKENS = 1250

        # Initialize total allocation dictionary
        token_allocations = {}

        # Calculate token allocations for each wallet
        for wallet, nft_count in nft_holdings.items():
            # Allocation per wallet = [NFTs * Coolman's Universe Tokens] + [NFTs * Babies Tokens]
            allocation = (nft_count * COOLMAN_UNIVERSE_TOKENS) + (nft_count * BABIES_BY_COOLMAN_TOKENS)
            token_allocations[wallet] = allocation

        return token_allocations

    except Exception as e:
        # Handle errors gracefully and provide an error message
        print(f"Error during calculation: {str(e)}")
        return {}

# Example usage
if __name__ == "__main__":
    # Example input: NFT holdings by wallet
    example_nft_holdings = {
        "0xABC123": 2,  # Wallet with 2 NFTs
        "0xDEF456": 5,  # Wallet with 5 NFTs
        "0xGHI789": 1   # Wallet with 1 NFT
    }

    # Calculate allocations
    allocations = calculate_token_allocation(example_nft_holdings)
    
    # Print allocations
    print("Token Allocations:")
    for wallet, allocation in allocations.items():
        print(f"Wallet: {wallet}, Allocation: {allocation} $COOL")
```
