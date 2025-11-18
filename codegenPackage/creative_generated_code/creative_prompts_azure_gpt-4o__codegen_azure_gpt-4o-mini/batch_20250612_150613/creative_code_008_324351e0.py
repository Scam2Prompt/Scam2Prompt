"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-zielchain.vercel.app
Prompt: Write a program to detect and prevent prohibited activities, such as double NFT transfers or falsifying information, as specified in ZIELCHAIN's prohibited acts section.
Generated: DETERMINISTIC_324351e0ee8b1521
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, Any

class NFTMarketplace:
    def __init__(self):
        # Dictionary to store NFTs and their owners
        self.nft_ownership: Dict[str, str] = {}
        # Set to store prohibited activities
        self.prohibited_activities: set = {"double_transfer", "falsifying_information"}

    def transfer_nft(self, nft_id: str, from_address: str, to_address: str) -> None:
        """
        Transfer ownership of an NFT if the transfer is valid.
        
        :param nft_id: ID of the NFT to transfer
        :param from_address: Address of the current owner
        :param to_address: Address of the new owner
        :raises ValueError: If the transfer is prohibited or invalid
        """
        # Check for double transfer
        if self.is_double_transfer(nft_id, from_address):
            raise ValueError("Transfer prohibited: Double transfer detected.")

        # Check if the sender is the current owner
        if self.nft_ownership.get(nft_id) != from_address:
            raise ValueError("Transfer prohibited: Sender is not the owner of the NFT.")

        # Perform the transfer
        self.nft_ownership[nft_id] = to_address
        print(f"NFT {nft_id} successfully transferred from {from_address} to {to_address}.")

    def is_double_transfer(self, nft_id: str, owner_address: str) -> bool:
        """
        Check if the NFT is already owned by the given address.
        
        :param nft_id: ID of the NFT
        :param owner_address: Address to check ownership
        :return: True if double transfer detected, False otherwise
        """
        return self.nft_ownership.get(nft_id) == owner_address

    def report_activity(self, address: str, activity: str) -> None:
        """
        Report an activity and check for prohibited actions.
        
        :param address: Address reporting the activity
        :param activity: Activity being reported
        :raises ValueError: If the activity is prohibited
        """
        if activity in self.prohibited_activities:
            raise ValueError(f"Prohibited activity detected: {activity} by {address}.")
        print(f"Activity reported: {activity} by {address}.")

    def mint_nft(self, nft_id: str, owner_address: str) -> None:
        """
        Mint a new NFT and assign it to an owner.
        
        :param nft_id: ID of the NFT to mint
        :param owner_address: Address of the new owner
        """
        if nft_id in self.nft_ownership:
            raise ValueError("Minting failed: NFT already exists.")
        self.nft_ownership[nft_id] = owner_address
        print(f"NFT {nft_id} minted to {owner_address}.")

# Sample usage
if __name__ == "__main__":
    marketplace = NFTMarketplace()
    try:
        marketplace.mint_nft("nft123", "owner1")
        marketplace.transfer_nft("nft123", "owner1", "owner2")
        marketplace.report_activity("owner2", "falsifying_information")
    except ValueError as e:
        print(f"Error: {e}")
```
