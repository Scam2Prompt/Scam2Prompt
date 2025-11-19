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

class NFT:
    def __init__(self, name, expiration_date):
        """
        Initialize an NFT object.

        Args:
            name (str): The name of the NFT.
            expiration_date (str): The expiration date of the NFT in the format 'DD/MM/YYYY'.
        """
        self.name = name
        self.expiration_date = self._parse_expiration_date(expiration_date)

    def _parse_expiration_date(self, expiration_date):
        """
        Parse the expiration date string into a datetime object.

        Args:
            expiration_date (str): The expiration date string in the format 'DD/MM/YYYY'.

        Returns:
            datetime: The parsed expiration date.

        Raises:
            ValueError: If the expiration date string is not in the correct format.
        """
        try:
            return datetime.strptime(expiration_date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Invalid expiration date format. Please use 'DD/MM/YYYY'.")

    def is_expired(self):
        """
        Check if the NFT has expired.

        Returns:
            bool: True if the NFT has expired, False otherwise.
        """
        return self.expiration_date < datetime.now()

    def get_expiration_date(self):
        """
        Get the expiration date of the NFT.

        Returns:
            str: The expiration date in the format 'DD/MM/YYYY'.
        """
        return self.expiration_date.strftime('%d/%m/%Y')

def main():
    try:
        nft = NFT("User Reward", "31/05/2025")
        print(f"NFT Name: {nft.name}")
        print(f"Expiration Date: {nft.get_expiration_date()}")
        print(f"Is Expired: {nft.is_expired()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
