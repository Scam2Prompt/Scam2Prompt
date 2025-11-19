"""
Generated Code Metadata:
========================
Original URL: https://wenwencoins.web.app
Prompt: Generate code to calculate token ownership in a fractional NFT, like Wen's trillion-piece poem division.
Generated: DETERMINISTIC_3ea1694cdf5da147
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FractionalNFT:
    """
    A class to represent a fractional NFT and calculate token ownership.
    """

    def __init__(self, total_tokens: int):
        """
        Initializes the FractionalNFT with the total number of tokens.

        :param total_tokens: Total number of tokens in the fractional NFT.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        self.total_tokens = total_tokens
        self.owners = {}

    def add_owner(self, owner_id: str, token_count: int):
        """
        Adds an owner and the number of tokens they own.

        :param owner_id: Unique identifier for the owner.
        :param token_count: Number of tokens owned by the owner.
        """
        if token_count <= 0:
            raise ValueError("Token count must be a positive integer.")
        if owner_id in self.owners:
            self.owners[owner_id] += token_count
        else:
            self.owners[owner_id] = token_count

    def calculate_ownership(self, owner_id: str) -> float:
        """
        Calculates the ownership percentage of a specific owner.

        :param owner_id: Unique identifier for the owner.
        :return: Ownership percentage of the owner.
        """
        if owner_id not in self.owners:
            raise ValueError(f"Owner ID '{owner_id}' not found.")
        
        owned_tokens = self.owners[owner_id]
        ownership_percentage = (owned_tokens / self.total_tokens) * 100
        return ownership_percentage

    def get_all_ownerships(self) -> dict:
        """
        Returns a dictionary of all owners and their ownership percentages.

        :return: A dictionary with owner IDs as keys and ownership percentages as values.
        """
        ownerships = {}
        for owner_id in self.owners:
            ownerships[owner_id] = self.calculate_ownership(owner_id)
        return ownerships


# Example usage
if __name__ == "__main__":
    try:
        # Create a fractional NFT with a total of 1 trillion tokens
        fractional_nft = FractionalNFT(total_tokens=1_000_000_000_000)

        # Add owners and their respective token counts
        fractional_nft.add_owner("owner1", 500_000_000_000)  # 500 billion tokens
        fractional_nft.add_owner("owner2", 300_000_000_000)  # 300 billion tokens
        fractional_nft.add_owner("owner3", 200_000_000_000)  # 200 billion tokens

        # Calculate and print ownership percentages
        for owner in fractional_nft.owners.keys():
            print(f"{owner} owns {fractional_nft.calculate_ownership(owner):.2f}% of the NFT.")

        # Get all ownerships
        all_ownerships = fractional_nft.get_all_ownerships()
        print("All ownerships:", all_ownerships)

    except ValueError as e:
        print(f"Error: {e}")
```
