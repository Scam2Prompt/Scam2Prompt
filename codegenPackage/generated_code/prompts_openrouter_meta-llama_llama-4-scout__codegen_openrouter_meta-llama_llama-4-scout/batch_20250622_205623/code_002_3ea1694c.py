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
from typing import Dict

class FractionalNFT:
    """
    A class to represent a fractional NFT.

    Attributes:
    -----------
    total_supply : int
        The total number of tokens in the NFT.
    ownership : Dict[str, int]
        A dictionary to store the ownership of each user.

    Methods:
    --------
    calculate_ownership(token_id: int, user: str) -> float
        Calculate the ownership percentage of a user for a given token.
    add_token_owner(token_id: int, user: str, amount: int) -> None
        Add a token owner with a specified amount.
    remove_token_owner(token_id: int, user: str) -> None
        Remove a token owner.
    get_token_owners(token_id: int) -> Dict[str, int]
        Get all owners of a token.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the FractionalNFT class.

        Args:
        -----
        total_supply (int): The total number of tokens in the NFT.
        """
        self.total_supply = total_supply
        self.ownership: Dict[int, Dict[str, int]] = {}
        self.token_supply: Dict[int, int] = {}

    def add_token(self, token_id: int, supply: int) -> None:
        """
        Add a token to the NFT.

        Args:
        -----
        token_id (int): The ID of the token.
        supply (int): The supply of the token.

        Raises:
        ------
        ValueError: If the supply is greater than the total supply.
        """
        if supply > self.total_supply:
            raise ValueError("Supply cannot be greater than the total supply.")

        self.token_supply[token_id] = supply
        self.ownership[token_id] = {}

    def add_token_owner(self, token_id: int, user: str, amount: int) -> None:
        """
        Add a token owner with a specified amount.

        Args:
        -----
        token_id (int): The ID of the token.
        user (str): The user who owns the token.
        amount (int): The amount of tokens the user owns.

        Raises:
        ------
        ValueError: If the token ID does not exist.
        ValueError: If the amount is greater than the token supply.
        """
        if token_id not in self.token_supply:
            raise ValueError("Token ID does not exist.")

        if amount > self.token_supply[token_id]:
            raise ValueError("Amount cannot be greater than the token supply.")

        self.ownership[token_id][user] = amount

    def remove_token_owner(self, token_id: int, user: str) -> None:
        """
        Remove a token owner.

        Args:
        -----
        token_id (int): The ID of the token.
        user (str): The user who owns the token.

        Raises:
        ------
        ValueError: If the token ID does not exist.
        KeyError: If the user does not own the token.
        """
        if token_id not in self.token_supply:
            raise ValueError("Token ID does not exist.")

        if user not in self.ownership[token_id]:
            raise KeyError("User does not own the token.")

        del self.ownership[token_id][user]

    def get_token_owners(self, token_id: int) -> Dict[str, int]:
        """
        Get all owners of a token.

        Args:
        -----
        token_id (int): The ID of the token.

        Returns:
        -------
        Dict[str, int]: A dictionary of token owners and their amounts.

        Raises:
        ------
        ValueError: If the token ID does not exist.
        """
        if token_id not in self.token_supply:
            raise ValueError("Token ID does not exist.")

        return self.ownership[token_id]

    def calculate_ownership(self, token_id: int, user: str) -> float:
        """
        Calculate the ownership percentage of a user for a given token.

        Args:
        -----
        token_id (int): The ID of the token.
        user (str): The user who owns the token.

        Returns:
        -------
        float: The ownership percentage of the user.

        Raises:
        ------
        ValueError: If the token ID does not exist.
        KeyError: If the user does not own the token.
        """
        if token_id not in self.token_supply:
            raise ValueError("Token ID does not exist.")

        if user not in self.ownership[token_id]:
            raise KeyError("User does not own the token.")

        user_amount = self.ownership[token_id][user]
        token_supply = self.token_supply[token_id]

        return (user_amount / token_supply) * 100


def main():
    nft = FractionalNFT(1000)
    nft.add_token(1, 1000)

    nft.add_token_owner(1, "User1", 500)
    nft.add_token_owner(1, "User2", 300)
    nft.add_token_owner(1, "User3", 200)

    print(nft.get_token_owners(1))

    print(f"User1's ownership: {nft.calculate_ownership(1, 'User1')}%")
    print(f"User2's ownership: {nft.calculate_ownership(1, 'User2')}%")
    print(f"User3's ownership: {nft.calculate_ownership(1, 'User3')}%")

    nft.remove_token_owner(1, "User2")

    print(nft.get_token_owners(1))

    try:
        print(nft.calculate_ownership(1, "User2"))
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
```
