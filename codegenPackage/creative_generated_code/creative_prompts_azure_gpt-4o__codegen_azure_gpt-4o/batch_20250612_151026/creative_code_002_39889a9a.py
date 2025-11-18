"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claynosaurz-nft.web.app
Prompt: Generate code to display remaining NFT availability (e.g., "Remaining 1483 / 2023") and update it dynamically during the minting process.
Generated: DETERMINISTIC_39889a9a0ad62a7d
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time

# Class to manage NFT inventory
class NFTInventory:
    def __init__(self, total_nfts):
        """
        Initialize the inventory with the total number of NFTs.
        :param total_nfts: Total NFTs available for minting.
        """
        self.total_nfts = total_nfts
        self.remaining_nfts = total_nfts
        self.lock = threading.Lock()  # To ensure thread-safe updates

    def mint_nft(self):
        """
        Simulate the minting process by decrementing the remaining NFTs count.
        Raises an exception if there are no NFTs left to mint.
        """
        with self.lock:  # Ensure thread-safe access to shared resource
            if self.remaining_nfts > 0:
                self.remaining_nfts -= 1  # Mint one NFT
            else:
                raise Exception("No NFTs remaining to mint.")

    def get_remaining(self):
        """
        Get the current count of remaining NFTs.
        :return: Remaining NFTs count.
        """
        with self.lock:  # Ensure thread-safe access to shared resource
            return self.remaining_nfts


def display_nft_availability(inventory):
    """
    Continuously display the remaining NFT availability.
    :param inventory: NFTInventory instance.
    """
    while inventory.get_remaining() > 0:
        print(f"Remaining {inventory.get_remaining()} / {inventory.total_nfts}")
        time.sleep(1)  # Update every second


def simulate_minting(inventory, mint_count, interval=0.2):
    """
    Simulate minting NFTs in a separate thread.
    :param inventory: NFTInventory instance.
    :param mint_count: Number of NFTs to mint.
    :param interval: Time interval between each minting operation (in seconds).
    """
    for _ in range(mint_count):
        try:
            inventory.mint_nft()
            time.sleep(interval)  # Simulate minting delay
        except Exception as e:
            print(f"Minting Error: {e}")
            break  # Stop minting if no NFTs are left


if __name__ == "__main__":
    # Initialize with 2023 NFTs
    total_nfts = 2023
    inventory = NFTInventory(total_nfts)

    # Start display thread to show remaining NFTs
    display_thread = threading.Thread(target=display_nft_availability, args=(inventory,))
    display_thread.daemon = True  # Daemon thread will exit when main program exits
    display_thread.start()

    # Simulate minting process in another thread
    mint_count = 600  # Number of NFTs to mint
    minting_thread = threading.Thread(target=simulate_minting, args=(inventory, mint_count))
    minting_thread.start()

    # Wait for minting thread to finish
    minting_thread.join()

    print("Minting process completed.")
```
