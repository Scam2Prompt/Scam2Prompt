"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-incinerator.pages.dev
Prompt: Generate a function that calculates the reclaimed TON based on the type of NFT burned using the Ton Incinerator.
Generated: DETERMINISTIC_44c61878252a6435
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate reclaimed TON based on the type of NFT burned
def calculate_reclaimed_ton(nft_type: str, quantity: int) -> float:
    """
    Calculate the amount of TON reclaimed based on the type of NFT burned.
    
    Args:
        nft_type (str): The type of NFT burned. Valid types are "common", "rare", "legendary".
        quantity (int): The number of NFTs burned.
    
    Returns:
        float: The total amount of TON reclaimed.
    
    Raises:
        ValueError: If the NFT type is invalid or quantity is not positive.
    """
    # Define TON reclaim values per NFT type
    ton_values = {
        "common": 0.1,    # 0.1 TON reclaimed per common NFT
        "rare": 0.5,      # 0.5 TON reclaimed per rare NFT
        "legendary": 2.0  # 2.0 TON reclaimed per legendary NFT
    }

    # Validate input
    if nft_type not in ton_values:
        raise ValueError(f"Invalid NFT type: {nft_type}. Valid types are: {', '.join(ton_values.keys())}")
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    # Calculate reclaimed TON
    reclaimed_ton = ton_values[nft_type] * quantity

    return reclaimed_ton


# Example usage
try:
    nft_type = "rare"
    quantity = 3
    reclaimed_ton = calculate_reclaimed_ton(nft_type, quantity)
    print(f"Reclaimed TON for burning {quantity} '{nft_type}' NFTs: {reclaimed_ton} TON")
except ValueError as e:
    print(f"Error: {e}")
```
