"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Create a function that calculates potential royalties for artists selling NFTs, based on the features discussed on SuperRare.fr.
Generated: DETERMINISTIC_baf3037f5688b30d
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_nft_royalties(
    initial_sale_price: float,
    resale_price: float,
    total_resales: int,
    artist_royalty_percentage: float = 10.0,
    platform_fee_percentage: float = 3.0,
    minimum_royalty: float = 0.0
) -> dict:
    """
    Calculate NFT royalties for artists based on SuperRare-like features.
    
    Args:
        initial_sale_price: Price of the first sale (in any currency)
        resale_price: Price of each subsequent resale (in same currency)
        total_resales: Number of resales that occurred
        artist_royalty_percentage: Percentage royalty for artist on resales (default 10%)
        platform_fee_percentage: Percentage fee taken by platform (default 3%)
        minimum_royalty: Minimum royalty amount to ensure artist gets something (default 0)
        
    Returns:
        Dictionary containing:
        - initial_sale_artist_cut: Artist's earnings from initial sale
        - initial_sale_platform_cut: Platform's earnings from initial sale
        - total_resale_royalties: Total royalties from all resales
        - total_platform_fees: Total platform fees from resales
        - total_artist_earnings: Sum of initial and resale earnings
        - total_platform_earnings: Sum of platform fees
        
    Raises:
        ValueError: If any numeric parameter is negative
    """
    
    # Validate input parameters
    if any(val < 0 for val in [
        initial_sale_price,
        resale_price,
        total_resales,
        artist_royalty_percentage,
        platform_fee_percentage,
        minimum_royalty
    ]):
        raise ValueError("All numeric parameters must be non-negative")
    
    # Calculate initial sale splits (artist gets 85%, platform 15% as per SuperRare)
    initial_sale_artist_cut = initial_sale_price * 0.85
    initial_sale_platform_cut = initial_sale_price * 0.15
    
    # Calculate resale royalties and fees
    resale_royalty_per_item = max(
        resale_price * (artist_royalty_percentage / 100),
        minimum_royalty
    )
    platform_fee_per_item = resale_price * (platform_fee_percentage / 100)
    
    total_resale_royalties = resale_royalty_per_item * total_resales
    total_platform_fees = platform_fee_per_item * total_resales
    
    # Calculate totals
    total_artist_earnings = initial_sale_artist_cut + total_resale_royalties
    total_platform_earnings = initial_sale_platform_cut + total_platform_fees
    
    return {
        "initial_sale_artist_cut": round(initial_sale_artist_cut, 2),
        "initial_sale_platform_cut": round(initial_sale_platform_cut, 2),
        "total_resale_royalties": round(total_resale_royalties, 2),
        "total_platform_fees": round(total_platform_fees, 2),
        "total_artist_earnings": round(total_artist_earnings, 2),
        "total_platform_earnings": round(total_platform_earnings, 2),
    }
```
