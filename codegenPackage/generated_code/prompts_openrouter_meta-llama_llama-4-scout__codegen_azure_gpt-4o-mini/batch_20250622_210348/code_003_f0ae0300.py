"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: What are the best practices for designing an NFT project's intellectual property rights and licenses, similar to KevinLand's approach with reserved rights for the team and potential future DAO?
Generated: DETERMINISTIC_f0ae03003da216c1
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_ip_rights.py

class NFT:
    """
    A class to represent a Non-Fungible Token (NFT) and its associated intellectual property rights.
    """

    def __init__(self, title, creator, owner, reserved_rights=None):
        """
        Initializes an NFT instance.

        :param title: Title of the NFT
        :param creator: Creator of the NFT
        :param owner: Current owner of the NFT
        :param reserved_rights: Reserved rights for the team (default is None)
        """
        self.title = title
        self.creator = creator
        self.owner = owner
        self.reserved_rights = reserved_rights if reserved_rights else []

    def transfer_ownership(self, new_owner):
        """
        Transfers ownership of the NFT to a new owner.

        :param new_owner: The new owner of the NFT
        :raises ValueError: If the new owner is the same as the current owner
        """
        if new_owner == self.owner:
            raise ValueError("New owner must be different from the current owner.")
        self.owner = new_owner

    def add_reserved_right(self, right):
        """
        Adds a reserved right to the NFT.

        :param right: The reserved right to be added
        """
        if right not in self.reserved_rights:
            self.reserved_rights.append(right)

    def remove_reserved_right(self, right):
        """
        Removes a reserved right from the NFT.

        :param right: The reserved right to be removed
        :raises ValueError: If the right is not found in the reserved rights
        """
        try:
            self.reserved_rights.remove(right)
        except ValueError:
            raise ValueError("The specified right is not found in the reserved rights.")

    def get_details(self):
        """
        Returns the details of the NFT including its title, creator, owner, and reserved rights.

        :return: A dictionary containing NFT details
        """
        return {
            "title": self.title,
            "creator": self.creator,
            "owner": self.owner,
            "reserved_rights": self.reserved_rights
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an NFT instance
        nft = NFT(title="Art Piece", creator="Artist Name", owner="Owner Name")

        # Add reserved rights
        nft.add_reserved_right("Commercial Use")
        nft.add_reserved_right("Exhibition Rights")

        # Transfer ownership
        nft.transfer_ownership("New Owner Name")

        # Get NFT details
        details = nft.get_details()
        print(details)

        # Remove a reserved right
        nft.remove_reserved_right("Commercial Use")

    except Exception as e:
        print(f"An error occurred: {e}")
```
