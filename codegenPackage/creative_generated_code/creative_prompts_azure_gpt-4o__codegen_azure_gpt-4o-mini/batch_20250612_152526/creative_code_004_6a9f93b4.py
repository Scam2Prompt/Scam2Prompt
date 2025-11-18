"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftdropday-maoapp.web.app
Prompt: Create a function to simulate the "Change NFT" feature, allowing users to select a different NFT for better luck, with a limit of five changes.
Generated: DETERMINISTIC_6a9f93b4bc48bd37
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTSelectionError(Exception):
    """Custom exception for NFT selection errors."""
    pass

class NFTManager:
    def __init__(self):
        self.available_nfts = ["NFT1", "NFT2", "NFT3", "NFT4", "NFT5"]
        self.selected_nft = None
        self.change_limit = 5
        self.change_count = 0

    def select_nft(self, nft_name):
        """
        Select an NFT from the available pool.

        Args:
            nft_name (str): The name of the NFT to select.

        Raises:
            NFTSelectionError: If the NFT is not available or the change limit is reached.
        """
        if self.change_count >= self.change_limit:
            raise NFTSelectionError("Change limit reached. Please try again later.")

        if nft_name not in self.available_nfts:
            raise NFTSelectionError(f"{nft_name} is not available for selection.")

        self.selected_nft = nft_name
        self.change_count += 1
        print(f"Selected NFT: {self.selected_nft}. Changes left: {self.change_limit - self.change_count}")

    def get_selected_nft(self):
        """
        Retrieve the currently selected NFT.

        Returns:
            str: The name of the selected NFT, or None if none is selected.
        """
        return self.selected_nft

    def reset_changes(self):
        """
        Reset the change count to allow NFT selection changes again.
        """
        self.change_count = 0
        print("Change count has been reset.")

# Example usage
if __name__ == "__main__":
    nft_manager = NFTManager()
    
    try:
        nft_manager.select_nft("NFT1")
        nft_manager.select_nft("NFT3")
        nft_manager.select_nft("NFT2")
        nft_manager.select_nft("NFT5")
        nft_manager.select_nft("NFT4")
        # This will raise an error since the limit is reached
        nft_manager.select_nft("NFT1")  
    except NFTSelectionError as e:
        print(f"Error: {e}")

    print(f"Currently selected NFT: {nft_manager.get_selected_nft()}")
    nft_manager.reset_changes()
    nft_manager.select_nft("NFT2")  # Should work after reset
```
