"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airbox-dao.web.app
Prompt: Write a function to calculate the total mint percentage for NFTs, as described in the Magic Box minting process on the Airbox DAO webpage.
Generated: DETERMINISTIC_be668d2922125f29
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mint_percentage(total_supply, minted_supply):
    """
    Calculate the mint percentage for NFTs based on the Magic Box minting process.

    Parameters:
    total_supply (int): The total number of NFTs available for minting.
    minted_supply (int): The number of NFTs already minted.

    Returns:
    float: The mint percentage (0 to 100).
    
    Raises:
    ValueError: If total_supply is less than or equal to zero.
    ValueError: If minted_supply is negative or greater than total_supply.
    """
    # Validate inputs
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    if minted_supply < 0 or minted_supply > total_supply:
        raise ValueError("Minted supply must be between 0 and the total supply.")

    # Calculate the mint percentage
    mint_percentage = (minted_supply / total_supply) * 100

    # Round to 2 decimal places for clarity
    return round(mint_percentage, 2)


# Example usage:
if __name__ == "__main__":
    try:
        total_supply = 1000  # Total NFTs
        minted_supply = 250  # Already minted NFTs
        result = calculate_mint_percentage(total_supply, minted_supply)
        print(f"Mint Percentage: {result}%")
    except ValueError as e:
        print(f"Error: {e}")
```
