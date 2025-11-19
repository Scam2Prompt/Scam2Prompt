"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of coat racks with pricing and special offers, similar to those found on Shahkar Industry's product page.
Generated: DETERMINISTIC_8cd2199e94bb7f14
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coat_rack.py

class CoatRack:
    def __init__(self, id, name, price, special_offer=None):
        """
        Initialize a CoatRack object.

        Args:
            id (int): Unique identifier for the coat rack.
            name (str): Name of the coat rack.
            price (float): Price of the coat rack.
            special_offer (str, optional): Special offer for the coat rack. Defaults to None.
        """
        self.id = id
        self.name = name
        self.price = price
        self.special_offer = special_offer

    def __str__(self):
        """
        Return a string representation of the CoatRack object.

        Returns:
            str: String representation of the CoatRack object.
        """
        offer = f" - Special Offer: {self.special_offer}" if self.special_offer else ""
        return f"{self.name}: ${self.price:.2f}{offer}"


class CoatRackRepository:
    def __init__(self):
        """
        Initialize a CoatRackRepository object.
        """
        self.coat_racks = []

    def add_coat_rack(self, coat_rack):
        """
        Add a coat rack to the repository.

        Args:
            coat_rack (CoatRack): CoatRack object to add.
        """
        self.coat_racks.append(coat_rack)

    def get_coat_racks(self):
        """
        Get a list of all coat racks in the repository.

        Returns:
            list: List of CoatRack objects.
        """
        return self.coat_racks


class ECommerceWebsite:
    def __init__(self, repository):
        """
        Initialize an ECommerceWebsite object.

        Args:
            repository (CoatRackRepository): CoatRackRepository object.
        """
        self.repository = repository

    def display_coat_racks(self):
        """
        Display a list of coat racks with pricing and special offers.
        """
        try:
            coat_racks = self.repository.get_coat_racks()
            if not coat_racks:
                print("No coat racks available.")
                return

            print("Coat Racks:")
            for coat_rack in coat_racks:
                print(coat_rack)

        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    # Create coat racks
    coat_rack1 = CoatRack(1, "Wooden Coat Rack", 49.99)
    coat_rack2 = CoatRack(2, "Metal Coat Rack", 29.99, "10% off")
    coat_rack3 = CoatRack(3, "Velvet Coat Rack", 79.99)

    # Create repository and add coat racks
    repository = CoatRackRepository()
    repository.add_coat_rack(coat_rack1)
    repository.add_coat_rack(coat_rack2)
    repository.add_coat_rack(coat_rack3)

    # Create e-commerce website and display coat racks
    website = ECommerceWebsite(repository)
    website.display_coat_racks()


if __name__ == "__main__":
    main()
```
