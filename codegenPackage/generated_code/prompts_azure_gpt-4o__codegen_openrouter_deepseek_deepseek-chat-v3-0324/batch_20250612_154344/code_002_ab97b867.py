"""
Generated Code Metadata:
========================
Original URL: https://jpegsfun.pages.dev
Prompt: Develop a function to calculate trading fees (1%) and royalties for secondary market trades based on the jpegs.fun NFT trading model.
Generated: DETERMINISTIC_ab97b867ee660c4a
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_trading_fees_and_royalties(
    sale_price: float, 
    is_secondary_market: bool, 
    royalty_percentage: float = 0.1
) -> dict:
    """
    Calculate trading fees and royalties for NFT trades based on jpegs.fun model.
    
    Args:
        sale_price (float): The sale price of the NFT in the base currency
        is_secondary_market (bool): True if this is a secondary market sale
        royalty_percentage (float, optional): Royalty percentage (0-1). Defaults to 0.1 (10%).
    
    Returns:
        dict: Dictionary containing:
            - 'platform_fee': The 1% platform fee
            - 'royalty_fee': The royalty fee (0 for primary sales)
            - 'seller_proceeds': Amount seller receives after fees
            - 'total_fees': Sum of all fees
    
    Raises:
        ValueError: If sale_price is negative or royalty_percentage is not between 0-1
    """
    # Input validation
    if sale_price < 0:
        raise ValueError("Sale price cannot be negative")
    if not 0 <= royalty_percentage <= 1:
        raise ValueError("Royalty percentage must be between 0 and 1")
    
    # Calculate platform fee (1%)
    platform_fee = sale_price * 0.01
    
    # Calculate royalty fee (only for secondary market)
    royalty_fee = sale_price * royalty_percentage if is_secondary_market else 0
    
    # Calculate total fees and seller proceeds
    total_fees = platform_fee + royalty_fee
    seller_proceeds = sale_price - total_fees
    
    return {
        'platform_fee': round(platform_fee, 6),
        'royalty_fee': round(royalty_fee, 6),
        'seller_proceeds': round(seller_proceeds, 6),
        'total_fees': round(total_fees, 6)
    }
```
