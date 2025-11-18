"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-mantanetwork-8pv.pages.dev
Prompt: Create a script to track the burning of Mystical Manta NFTs and their conversion into Golden Treasure Shovel NFTs, ensuring accurate record-keeping.
Generated: DETERMINISTIC_103150ed351581c1
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NFTTracker:
    """
    A class to track the burning of Mystical Manta NFTs and their conversion into Golden Treasure Shovel NFTs.
    """

    def __init__(self):
        self.mystical_manta_burned: List[Dict] = []  # List to hold burned Mystical Manta NFTs
        self.golden_shovels_created: List[Dict] = []  # List to hold created Golden Treasure Shovel NFTs

    def burn_mystical_manta(self, manta_id: str, owner: str) -> None:
        """
        Track the burning of a Mystical Manta NFT.
        
        :param manta_id: Unique identifier for the Mystical Manta NFT.
        :param owner: Owner of the Mystical Manta NFT.
        """
        try:
            entry = {
                'manta_id': manta_id,
                'owner': owner,
                'burned_at': datetime.now().isoformat()
            }
            self.mystical_manta_burned.append(entry)
            logging.info(f'Mystical Manta NFT burned: {entry}')
        except Exception as e:
            logging.error(f'Error burning Mystical Manta NFT: {e}')

    def create_golden_shovel(self, shovel_id: str, owner: str) -> None:
        """
        Track the creation of a Golden Treasure Shovel NFT.
        
        :param shovel_id: Unique identifier for the Golden Treasure Shovel NFT.
        :param owner: Owner of the Golden Treasure Shovel NFT.
        """
        try:
            entry = {
                'shovel_id': shovel_id,
                'owner': owner,
                'created_at': datetime.now().isoformat()
            }
            self.golden_shovels_created.append(entry)
            logging.info(f'Golden Treasure Shovel NFT created: {entry}')
        except Exception as e:
            logging.error(f'Error creating Golden Treasure Shovel NFT: {e}')

    def get_burned_mantas(self) -> List[Dict]:
        """
        Retrieve the list of burned Mystical Manta NFTs.
        
        :return: List of burned Mystical Manta NFTs.
        """
        return self.mystical_manta_burned

    def get_created_shovels(self) -> List[Dict]:
        """
        Retrieve the list of created Golden Treasure Shovel NFTs.
        
        :return: List of created Golden Treasure Shovel NFTs.
        """
        return self.golden_shovels_created

# Example usage
if __name__ == "__main__":
    tracker = NFTTracker()
    
    # Burn a Mystical Manta NFT
    tracker.burn_mystical_manta("Manta123", "UserA")
    
    # Create a Golden Treasure Shovel NFT
    tracker.create_golden_shovel("Shovel456", "UserA")
    
    # Output the records
    logging.info("Burned Mystical Manta NFTs: %s", tracker.get_burned_mantas())
    logging.info("Created Golden Treasure Shovel NFTs: %s", tracker.get_created_shovels())
```
