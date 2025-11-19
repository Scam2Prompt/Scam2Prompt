"""
Generated Code Metadata:
========================
Original URL: https://fr.habbometa.com
Prompt: Write a code snippet to handle NFT expiration dates, like the one mentioned for the user's reward ("Expire le : 31/05/2025").
Generated: DETERMINISTIC_4dfdc42dd832ffa9
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class NFT:
    def __init__(self, name: str, expiration_date: str):
        """
        Initializes an NFT instance.

        :param name: The name of the NFT.
        :param expiration_date: The expiration date in 'DD/MM/YYYY' format.
        """
        self.name = name
        self.expiration_date = self._parse_expiration_date(expiration_date)

    def _parse_expiration_date(self, expiration_date: str) -> datetime:
        """
        Parses the expiration date from a string to a datetime object.

        :param expiration_date: The expiration date in 'DD/MM/YYYY' format.
        :return: A datetime object representing the expiration date.
        :raises ValueError: If the date format is incorrect.
        """
        try:
            return datetime.strptime(expiration_date, '%d/%m/%Y')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {expiration_date}. Expected format: DD/MM/YYYY.") from e

    def is_expired(self) -> bool:
        """
        Checks if the NFT has expired.

        :return: True if the NFT is expired, False otherwise.
        """
        return datetime.now() > self.expiration_date

    def days_until_expiration(self) -> int:
        """
        Calculates the number of days until the NFT expires.

        :return: The number of days until expiration.
        :raises ValueError: If the NFT is already expired.
        """
        if self.is_expired():
            raise ValueError(f"The NFT '{self.name}' has already expired.")
        return (self.expiration_date - datetime.now()).days

# Example usage
if __name__ == "__main__":
    try:
        nft = NFT("Rare Art Piece", "31/05/2025")
        print(f"NFT Name: {nft.name}")
        print(f"Is Expired: {nft.is_expired()}")
        print(f"Days until expiration: {nft.days_until_expiration()}")
    except ValueError as e:
        print(f"Error: {e}")
```
