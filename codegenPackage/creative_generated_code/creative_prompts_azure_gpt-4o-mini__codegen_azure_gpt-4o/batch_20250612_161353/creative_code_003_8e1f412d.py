"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Create a code snippet that calculates the total cost for minting multiple PIF NFTs at the price of 0.25 BNB each.
Generated: DETERMINISTIC_8e1f412d3d1a729d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the total cost for minting multiple PIF NFTs
def calculate_total_cost(num_nfts, price_per_nft):
    """
    Calculates the total cost for minting a given number of NFTs.

    Args:
        num_nfts (int): Number of NFTs to mint.
        price_per_nft (float): Price of a single NFT in BNB.

    Returns:
        float: Total cost of minting the NFTs in BNB.
    """
    try:
        # Validate input
        if not isinstance(num_nfts, int) or num_nfts < 0:
            raise ValueError("Number of NFTs must be a non-negative integer")
        if not isinstance(price_per_nft, (int, float)) or price_per_nft <= 0:
            raise ValueError("Price per NFT must be a positive number")

        # Calculate total cost
        total_cost = num_nfts * price_per_nft
        return total_cost
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Price of a single PIF NFT
    PRICE_PER_PIF_NFT = 0.25  # BNB

    # Number of NFTs to mint
    num_nfts_to_mint = 10

    # Calculate the total cost
    total_cost = calculate_total_cost(num_nfts_to_mint, PRICE_PER_PIF_NFT)

    if total_cost is not None:
        print(f"The total cost of minting {num_nfts_to_mint} PIF NFTs at {PRICE_PER_PIF_NFT} BNB each is {total_cost:.2f} BNB.")
```
