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
from datetime import datetime

class NFTExpirationHandler:
    """
    A class to handle NFT expiration dates.
    """

    def __init__(self, expiration_date_str):
        """
        Initialize the NFTExpirationHandler with an expiration date string.

        :param expiration_date_str: Expiration date in the format "dd/mm/yyyy".
        """
        self.expiration_date_str = expiration_date_str
        self.expiration_date = self._parse_date(expiration_date_str)

    def _parse_date(self, date_str):
        """
        Parse the date string into a datetime object.

        :param date_str: Date string in the format "dd/mm/yyyy".
        :return: A datetime object representing the parsed date.
        :raises ValueError: If the date string is invalid.
        """
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: 'dd/mm/yyyy'.") from e

    def is_expired(self):
        """
        Check if the NFT is expired.

        :return: True if the NFT is expired, False otherwise.
        """
        current_date = datetime.now()
        return current_date > self.expiration_date

    def days_until_expiration(self):
        """
        Calculate the number of days until the NFT expires.

        :return: Number of days until expiration. Returns 0 if already expired.
        """
        if self.is_expired():
            return 0
        delta = self.expiration_date - datetime.now()
        return delta.days

# Example usage:
try:
    nft_handler = NFTExpirationHandler("31/05/2025")
    print(f"Is NFT expired? {nft_handler.is_expired()}")
    print(f"Days until expiration: {nft_handler.days_until_expiration()}")
except ValueError as e:
    print(f"Error: {e}")
```
