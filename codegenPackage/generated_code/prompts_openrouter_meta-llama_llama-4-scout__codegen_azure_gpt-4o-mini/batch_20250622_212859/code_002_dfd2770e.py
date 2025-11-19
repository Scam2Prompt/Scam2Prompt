"""
Generated Code Metadata:
========================
Original URL: https://createra-genesis-land.netlify.app
Prompt: Generate a code snippet to display the minting progress of Createra Genesis Land NFTs, showing 589 out of 777 minted, along with a percentage completion.
Generated: DETERMINISTIC_dfd2770e945f334c
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class MintingProgress:
    def __init__(self, total_nfts: int):
        """
        Initializes the MintingProgress with the total number of NFTs.

        :param total_nfts: Total number of NFTs to be minted.
        """
        if total_nfts <= 0:
            raise ValueError("Total NFTs must be a positive integer.")
        self.total_nfts = total_nfts
        self.minted_nfts = 0

    def update_minted_nfts(self, minted: int):
        """
        Updates the number of minted NFTs and displays the progress.

        :param minted: Number of NFTs minted.
        """
        if minted < 0:
            raise ValueError("Minted NFTs cannot be negative.")
        if minted > self.total_nfts:
            raise ValueError("Minted NFTs cannot exceed total NFTs.")
        
        self.minted_nfts = minted
        self.display_progress()

    def display_progress(self):
        """
        Displays the current minting progress.
        """
        percentage = (self.minted_nfts / self.total_nfts) * 100
        print(f"Minting Progress: {self.minted_nfts} out of {self.total_nfts} minted.")
        print(f"Completion: {percentage:.2f}%")

def main():
    try:
        total_nfts = 777
        minted_nfts = 589
        
        # Create a MintingProgress instance
        progress = MintingProgress(total_nfts)
        
        # Update the minted NFTs
        progress.update_minted_nfts(minted_nfts)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
