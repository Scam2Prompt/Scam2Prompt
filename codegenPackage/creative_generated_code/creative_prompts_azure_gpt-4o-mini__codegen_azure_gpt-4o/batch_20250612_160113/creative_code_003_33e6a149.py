"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: Create a function to handle the minting process for a limited number of Mystery Box NFTs, specifically for a total of 150 mints.
Generated: DETERMINISTIC_33e6a1493604c035
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MysteryBoxNFTMinting:
    def __init__(self, max_mints=150):
        """
        Initializes the MysteryBoxNFTMinting class.
        :param max_mints: Maximum number of NFTs that can be minted. Default is 150.
        """
        self.max_mints = max_mints
        self.minted_count = 0
        self.minted_boxes = set()

    def mint_nft(self, user_id):
        """
        Handles the minting process for a Mystery Box NFT.
        :param user_id: A unique identifier for the user requesting the mint.
        :return: A dictionary with the status of the minting process and minted box ID, if successful.
        """
        try:
            # Check if the maximum minting limit is reached
            if self.minted_count >= self.max_mints:
                return {"success": False, "message": "Minting limit reached. No NFTs available."}

            # Generate a unique Mystery Box ID
            box_id = self._generate_unique_box_id()

            # Add the box ID to the minted list and increment the counter
            self.minted_boxes.add(box_id)
            self.minted_count += 1

            return {
                "success": True,
                "message": "Minted successfully.",
                "box_id": box_id,
                "user_id": user_id
            }
        except Exception as e:
            # Handle unexpected errors during minting
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def _generate_unique_box_id(self):
        """
        Generates a unique Mystery Box ID.
        :return: A unique Mystery Box ID.
        """
        while True:
            # Generate a random ID for the Mystery Box
            box_id = f"BOX-{random.randint(100000, 999999)}"
            # Ensure the box ID is unique
            if box_id not in self.minted_boxes:
                return box_id

# Example usage:
if __name__ == "__main__":
    nft_minter = MysteryBoxNFTMinting(max_mints=150)

    # Simulate minting NFTs for users
    for user_id in range(1, 155):  # Attempt 155 mints to test the limit
        result = nft_minter.mint_nft(user_id=user_id)
        print(result)
```
