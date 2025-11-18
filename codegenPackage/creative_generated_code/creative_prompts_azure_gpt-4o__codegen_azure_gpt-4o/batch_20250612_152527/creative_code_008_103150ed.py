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
import csv
import os
from datetime import datetime

# Constants for file paths
NFT_BURN_LOG_FILE = 'burn_log.csv'
NFT_CONVERSION_LOG_FILE = 'conversion_log.csv'

# Ensure log files exist or create them
def initialize_logs():
    if not os.path.exists(NFT_BURN_LOG_FILE):
        with open(NFT_BURN_LOG_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Burn ID', 'Mystical Manta ID', 'Timestamp'])  # Header row

    if not os.path.exists(NFT_CONVERSION_LOG_FILE):
        with open(NFT_CONVERSION_LOG_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Conversion ID', 'Mystical Manta ID', 'Golden Treasure Shovel ID', 'Timestamp'])  # Header row

# Burn a Mystical Manta NFT and log the event
def burn_nft(mystical_manta_id):
    try:
        burn_id = generate_unique_id()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log the burning event
        with open(NFT_BURN_LOG_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([burn_id, mystical_manta_id, timestamp])

        print(f"Mystical Manta NFT with ID {mystical_manta_id} burned successfully!")
        return burn_id
    except Exception as e:
        print(f"Error during NFT burning: {e}")
        return None

# Convert a burned Mystical Manta NFT into a Golden Treasure Shovel NFT
def convert_nft(mystical_manta_id, golden_treasure_shovel_id):
    try:
        conversion_id = generate_unique_id()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log the conversion event
        with open(NFT_CONVERSION_LOG_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([conversion_id, mystical_manta_id, golden_treasure_shovel_id, timestamp])

        print(f"Mystical Manta NFT with ID {mystical_manta_id} converted to Golden Treasure Shovel NFT with ID {golden_treasure_shovel_id} successfully!")
        return conversion_id
    except Exception as e:
        print(f"Error during NFT conversion: {e}")
        return None

# Generate a unique ID for logging purposes
def generate_unique_id():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')

# Main function to demonstrate burning and conversion of NFTs
def main():
    initialize_logs()

    # Example: Burn and convert NFTs
    mystical_manta_id = "MM12345"
    golden_treasure_shovel_id = "GTS67890"

    burn_id = burn_nft(mystical_manta_id)
    if burn_id:
        convert_nft(mystical_manta_id, golden_treasure_shovel_id)

if __name__ == "__main__":
    main()
```
