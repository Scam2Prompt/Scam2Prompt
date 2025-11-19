"""
Generated Code Metadata:
========================
Original URL: https://pythdrops.pages.dev
Prompt: Design a data structure to store information about NFTs, including volume, floor price, and collection name, as displayed on SearchDapps.xyz.
Generated: DETERMINISTIC_4e45ee1b241eea6b
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTCollection:
    """
    A class to represent a collection of NFTs.

    Attributes:
        name (str): The name of the NFT collection.
        volume (float): The total trading volume of the collection.
        floor_price (float): The lowest price of NFTs in the collection.
    """

    def __init__(self, name: str, volume: float, floor_price: float):
        """
        Initializes an NFTCollection instance.

        Args:
            name (str): The name of the NFT collection.
            volume (float): The total trading volume of the collection.
            floor_price (float): The lowest price of NFTs in the collection.

        Raises:
            ValueError: If volume or floor_price is negative.
        """
        if volume < 0:
            raise ValueError("Volume cannot be negative.")
        if floor_price < 0:
            raise ValueError("Floor price cannot be negative.")

        self.name = name
        self.volume = volume
        self.floor_price = floor_price

    def update_volume(self, new_volume: float):
        """
        Updates the trading volume of the collection.

        Args:
            new_volume (float): The new trading volume.

        Raises:
            ValueError: If new_volume is negative.
        """
        if new_volume < 0:
            raise ValueError("New volume cannot be negative.")
        self.volume = new_volume

    def update_floor_price(self, new_floor_price: float):
        """
        Updates the floor price of the collection.

        Args:
            new_floor_price (float): The new floor price.

        Raises:
            ValueError: If new_floor_price is negative.
        """
        if new_floor_price < 0:
            raise ValueError("New floor price cannot be negative.")
        self.floor_price = new_floor_price

    def __str__(self):
        """
        Returns a string representation of the NFTCollection instance.

        Returns:
            str: A string describing the NFT collection.
        """
        return (f"NFT Collection: {self.name}, "
                f"Volume: {self.volume}, "
                f"Floor Price: {self.floor_price}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of NFTCollection
        collection = NFTCollection("CryptoArt", 1500.75, 0.5)
        print(collection)

        # Update volume and floor price
        collection.update_volume(2000.00)
        collection.update_floor_price(0.75)
        print(collection)

    except ValueError as e:
        print(f"Error: {e}")
```
