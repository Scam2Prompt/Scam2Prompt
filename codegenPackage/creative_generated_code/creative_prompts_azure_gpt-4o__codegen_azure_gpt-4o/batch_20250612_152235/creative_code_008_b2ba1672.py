"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-playpixiz-io.pages.dev
Prompt: Create a function to calculate and display Yetiz bonus allocation for NFT holders, referencing the Pixiz Mint platform.
Generated: DETERMINISTIC_b2ba1672d190adea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_and_display_bonus(nft_holders, total_bonus_pool):
    """
    Calculate and display the bonus allocation for NFT holders.

    :param nft_holders: List of dictionaries representing NFT holders. 
                        Each dictionary should have 'name' and 'nft_count' keys.
    :param total_bonus_pool: Total amount of bonus pool to be distributed.
    :return: None
    """
    try:
        # Validate inputs
        if not isinstance(nft_holders, list) or not all(isinstance(holder, dict) for holder in nft_holders):
            raise ValueError("Invalid format for NFT holders. Expected a list of dictionaries.")
        if not isinstance(total_bonus_pool, (int, float)) or total_bonus_pool <= 0:
            raise ValueError("Total bonus pool must be a positive number.")
        
        # Calculate the total number of NFTs
        total_nfts = sum(holder.get('nft_count', 0) for holder in nft_holders)
        if total_nfts == 0:
            raise ValueError("Total NFT count is zero. Cannot allocate bonuses.")
        
        # Calculate bonus per NFT
        bonus_per_nft = total_bonus_pool / total_nfts
        logging.info(f"Total NFTs: {total_nfts}, Bonus per NFT: {bonus_per_nft:.2f}")

        # Allocate and display bonuses for each holder
        for holder in nft_holders:
            name = holder.get('name', 'Unknown')
            nft_count = holder.get('nft_count', 0)
            holder_bonus = nft_count * bonus_per_nft
            logging.info(f"Holder: {name}, NFTs: {nft_count}, Bonus: {holder_bonus:.2f}")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Example Usage
if __name__ == "__main__":
    # List of NFT holders
    nft_holders = [
        {'name': 'Alice', 'nft_count': 5},
        {'name': 'Bob', 'nft_count': 3},
        {'name': 'Charlie', 'nft_count': 2}
    ]
    
    # Total bonus pool
    total_bonus_pool = 1000.0
    
    # Calculate and display the bonus allocation
    calculate_and_display_bonus(nft_holders, total_bonus_pool)
```
