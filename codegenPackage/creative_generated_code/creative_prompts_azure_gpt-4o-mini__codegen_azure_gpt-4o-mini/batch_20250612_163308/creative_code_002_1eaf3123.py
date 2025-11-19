"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Create a function to display the rarity and expiration date of a claimed Habbo NFT based on user input.
Generated: DETERMINISTIC_1eaf3123e37e0771
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

class HabboNFT:
    """A class to represent a Habbo NFT with rarity and expiration date."""
    
    def __init__(self, rarity: str, expiration_date: str):
        """
        Initialize a new Habbo NFT instance.

        :param rarity: A string representing the rarity of the NFT (e.g., 'Common', 'Rare').
        :param expiration_date: A string representing the expiration date in 'YYYY-MM-DD' format.
        """
        self.rarity = rarity
        self.expiration_date = self._parse_expiration_date(expiration_date)

    @staticmethod
    def _parse_expiration_date(expiration_date: str) -> datetime:
        """
        Parse the expiration date string into a datetime object.

        :param expiration_date: A string representing the expiration date in 'YYYY-MM-DD' format.
        :return: A datetime object representing the expiration date.
        :raises ValueError: If the expiration date is not in the correct format.
        """
        try:
            return datetime.strptime(expiration_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid expiration date format: {expiration_date}. Expected 'YYYY-MM-DD'.") from e

    def display_nft_info(self):
        """Display the rarity and expiration date of the NFT."""
        current_date = datetime.now()
        is_expired = self.expiration_date < current_date
        
        expiration_status = "Expired" if is_expired else "Active"
        
        print(f"NFT Rarity: {self.rarity}")
        print(f"Expiration Date: {self.expiration_date.strftime('%Y-%m-%d')}")
        print(f"Status: {expiration_status}")


def main():
    """Main function to handle user input and display NFT information."""
    try:
        rarity = input("Enter the rarity of your NFT (e.g., 'Common', 'Rare'): ")
        expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")

        # Create an instance of HabboNFT
        nft = HabboNFT(rarity, expiration_date)

        # Display the NFT information
        nft.display_nft_info()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
