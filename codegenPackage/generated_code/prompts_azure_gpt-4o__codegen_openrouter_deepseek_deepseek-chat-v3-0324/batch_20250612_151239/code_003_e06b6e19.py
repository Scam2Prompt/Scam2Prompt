"""
Generated Code Metadata:
========================
Original URL: https://patekphilippenft.pages.dev
Prompt: Generate code to calculate the total cost in ETH for minting Patek Philippe NFTs, including bonuses for minting 5 or 10 NFTs.
Generated: DETERMINISTIC_e06b6e1943172cdb
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Patek Philippe NFT Minting Cost Calculator

def calculate_minting_cost(num_nfts: int, base_cost_eth: float) -> float:
    """
    Calculate the total cost in ETH for minting Patek Philippe NFTs, including bonuses.
    
    Args:
        num_nfts (int): Number of NFTs to mint (must be positive)
        base_cost_eth (float): Base cost per NFT in ETH (must be positive)
        
    Returns:
        float: Total cost in ETH after applying discounts
        
    Raises:
        ValueError: If input values are invalid
    """
    # Validate inputs
    if not isinstance(num_nfts, int) or num_nfts <= 0:
        raise ValueError("Number of NFTs must be a positive integer")
    if not isinstance(base_cost_eth, (int, float)) or base_cost_eth <= 0:
        raise ValueError("Base cost must be a positive number")
    
    # Calculate base cost
    total_cost = num_nfts * base_cost_eth
    
    # Apply bulk discounts
    if num_nfts >= 10:
        # 15% discount for 10+ NFTs
        total_cost *= 0.85
    elif num_nfts >= 5:
        # 10% discount for 5-9 NFTs
        total_cost *= 0.90
    
    return round(total_cost, 4)  # Round to 4 decimal places for ETH precision


# Example usage
if __name__ == "__main__":
    try:
        nfts_to_mint = 7
        base_price = 0.1  # 0.1 ETH per NFT
        total = calculate_minting_cost(nfts_to_mint, base_price)
        print(f"Total cost for {nfts_to_mint} NFTs: {total} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
