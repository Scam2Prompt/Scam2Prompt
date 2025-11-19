"""
Generated Code Metadata:
========================
Original URL: https://claim-babywif-io.pages.dev
Prompt: Generate code to calculate the token distribution percentages for Baby WIF ($BIF) based on the given tokenomics: 95% for Presale+Liquidity and 5% for CEX Listing. Use Python for the implementation.
Generated: DETERMINISTIC_c41dbde311b4dfc8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_distribution(total_supply):
    """
    Calculate token distribution percentages for Baby WIF ($BIF) based on tokenomics.
    
    Args:
        total_supply (int): Total supply of tokens to be distributed
        
    Returns:
        dict: Dictionary containing distribution amounts and percentages
    """
    try:
        if not isinstance(total_supply, (int, float)) or total_supply <= 0:
            raise ValueError("Total supply must be a positive number")
            
        # Calculate distribution amounts
        presale_liquidity_percent = 0.95  # 95%
        cex_listing_percent = 0.05       # 5%
        
        presale_liquidity_amount = total_supply * presale_liquidity_percent
        cex_listing_amount = total_supply * cex_listing_percent
        
        # Round to nearest integer for token counts
        presale_liquidity_amount = round(presale_liquidity_amount)
        cex_listing_amount = round(cex_listing_amount)
        
        # Adjust for rounding errors to ensure total matches
        total_after_rounding = presale_liquidity_amount + cex_listing_amount
        if total_after_rounding != total_supply:
            presale_liquidity_amount += (total_supply - total_after_rounding)
        
        return {
            'total_supply': total_supply,
            'presale_liquidity': {
                'percentage': presale_liquidity_percent * 100,
                'amount': presale_liquidity_amount
            },
            'cex_listing': {
                'percentage': cex_listing_percent * 100,
                'amount': cex_listing_amount
            }
        }
        
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    total_supply = 1000000  # Example total supply
    distribution = calculate_token_distribution(total_supply)
    
    if distribution:
        print("Token Distribution for Baby WIF ($BIF):")
        print(f"Total Supply: {distribution['total_supply']}")
        print(f"Presale + Liquidity: {distribution['presale_liquidity']['amount']} tokens ({distribution['presale_liquidity']['percentage']}%)")
        print(f"CEX Listing: {distribution['cex_listing']['amount']} tokens ({distribution['cex_listing']['percentage']}%)")
```
