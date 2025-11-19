"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superrare.fr
Prompt: Create a function that calculates potential royalties for artists selling NFTs, based on the features discussed on SuperRare.fr.
Generated: DETERMINISTIC_baf3037f5688b30d
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_nft_royalties(sale_price, royalty_percentage):
    """
    Calculate royalties for artists selling NFTs.

    Parameters:
        sale_price (float): The price at which the NFT was sold (e.g., in ETH or USD).
        royalty_percentage (float): The percentage of royalties the artist is entitled to.

    Returns:
        float: The royalty amount owed to the artist.

    Raises:
        ValueError: If the sale_price or royalty_percentage is negative.
        TypeError: If the inputs are not of type float or int.
    """

    # Ensure sale_price and royalty_percentage are of the correct type
    if not isinstance(sale_price, (float, int)) or not isinstance(royalty_percentage, (float, int)):
        raise TypeError("Both sale_price and royalty_percentage must be numeric (int or float).")

    # Ensure sale_price and royalty_percentage are valid values
    if sale_price < 0:
        raise ValueError("Sale price cannot be negative.")
    if royalty_percentage < 0 or royalty_percentage > 100:
        raise ValueError("Royalty percentage must be between 0 and 100.")

    # Use Decimal for precise calculations
    sale_price = decimal.Decimal(sale_price)
    royalty_percentage = decimal.Decimal(royalty_percentage)

    # Calculate the royalty amount
    royalty_amount = (sale_price * royalty_percentage) / 100

    # Return result as a float
    return float(royalty_amount)

# Example usage
try:
    sale_price = 1000.0  # Example sale price (e.g., $1000 or 1 ETH)
    royalty_percentage = 10.0  # Example royalty percentage (e.g., 10%)
    royalties = calculate_nft_royalties(sale_price, royalty_percentage)
    print(f"Artist royalties: ${royalties:.2f}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```
