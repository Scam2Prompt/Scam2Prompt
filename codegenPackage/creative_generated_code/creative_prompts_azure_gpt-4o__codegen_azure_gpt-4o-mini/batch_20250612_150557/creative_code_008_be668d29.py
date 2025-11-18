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
def calculate_total_mint_percentage(nft_data):
    """
    Calculate the total mint percentage for a list of NFTs based on their individual mint percentages.

    Args:
        nft_data (list of dict): A list of dictionaries where each dictionary contains the
                                  'mint_percentage' key representing the mint percentage
                                  of an NFT.

    Returns:
        float: The total mint percentage for all NFTs combined.
    
    Raises:
        ValueError: If nft_data is not a list or if any dictionary in the list does not contain
                    a valid 'mint_percentage' key with a float value.
    """
    
    # Validate input data type
    if not isinstance(nft_data, list):
        raise ValueError("Input must be a list of NFT data.")

    total_percentage = 0.0

    # Iterate over each NFT data entry
    for nft in nft_data:
        # Validate that each entry is a dictionary
        if not isinstance(nft, dict):
            raise ValueError("Each NFT data entry must be a dictionary.")
        
        # Validate that 'mint_percentage' exists and is a float
        if 'mint_percentage' not in nft or not isinstance(nft['mint_percentage'], (float, int)):
            raise ValueError("Each NFT must contain a 'mint_percentage' key with a numeric value.")

        # Accumulate the mint percentage
        total_percentage += float(nft['mint_percentage'])

    return total_percentage

# Example usage (uncomment to run):
# nft_list = [
#     {'mint_percentage': 0.25},
#     {'mint_percentage': 0.75},
#     {'mint_percentage': 0.50}
# ]
# try:
#     total = calculate_total_mint_percentage(nft_list)
#     print(f"Total Mint Percentage: {total:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
