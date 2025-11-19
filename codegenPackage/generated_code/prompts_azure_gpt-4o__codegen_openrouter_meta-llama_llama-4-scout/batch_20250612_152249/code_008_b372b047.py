"""
Generated Code Metadata:
========================
Original URL: https://bafybeia3lvdsyprhe2r3uvhlzhwyb7ptexvhhd2ccobtmsiyr3fpvfak6a.ipfs.dweb.link
Prompt: Create a function to compute and display the price of packs on the FantasyTop Pack platform, referencing the unique details provided on the webpage.
Generated: DETERMINISTIC_b372b047e2553e04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fantasy_top_pack.py

class FantasyTopPack:
    """
    A class to compute and display the price of packs on the FantasyTop Pack platform.
    """

    def __init__(self, pack_details):
        """
        Initialize the FantasyTopPack class.

        Args:
            pack_details (dict): A dictionary containing the unique details of the pack.
                It should have the following keys:
                    - 'name' (str): The name of the pack.
                    - 'price_eth' (float): The price of the pack in Ether.
                    - 'pack_size' (int): The number of items in the pack.
                    - 'item_rarity_distribution' (dict): A dictionary containing the rarity distribution of items in the pack.
                        It should have the following keys:
                            - 'common' (int): The number of common items.
                            - 'uncommon' (int): The number of uncommon items.
                            - 'rare' (int): The number of rare items.
                            - 'epic' (int): The number of epic items.
                            - 'legendary' (int): The number of legendary items.
        """
        self.pack_details = pack_details

    def calculate_pack_value(self, eth_to_usd_exchange_rate):
        """
        Calculate the value of the pack in USD.

        Args:
            eth_to_usd_exchange_rate (float): The current exchange rate of Ether to USD.

        Returns:
            float: The value of the pack in USD.
        """
        try:
            pack_price_eth = self.pack_details['price_eth']
            pack_value_usd = pack_price_eth * eth_to_usd_exchange_rate
            return pack_value_usd
        except KeyError as e:
            print(f"Error: Missing key {e} in pack details.")
            return None

    def display_pack_details(self):
        """
        Display the details of the pack.
        """
        try:
            pack_name = self.pack_details['name']
            pack_price_eth = self.pack_details['price_eth']
            pack_size = self.pack_details['pack_size']
            item_rarity_distribution = self.pack_details['item_rarity_distribution']

            print(f"Pack Name: {pack_name}")
            print(f"Pack Price (ETH): {pack_price_eth}")
            print(f"Pack Size: {pack_size}")
            print("Item Rarity Distribution:")
            for rarity, count in item_rarity_distribution.items():
                print(f"  - {rarity.capitalize()}: {count}")
        except KeyError as e:
            print(f"Error: Missing key {e} in pack details.")

    def display_pack_value(self, eth_to_usd_exchange_rate):
        """
        Display the value of the pack in USD.

        Args:
            eth_to_usd_exchange_rate (float): The current exchange rate of Ether to USD.
        """
        pack_value_usd = self.calculate_pack_value(eth_to_usd_exchange_rate)
        if pack_value_usd is not None:
            print(f"Pack Value (USD): {pack_value_usd:.2f}")


def main():
    pack_details = {
        'name': 'Starter Pack',
        'price_eth': 0.1,
        'pack_size': 10,
        'item_rarity_distribution': {
            'common': 5,
            'uncommon': 3,
            'rare': 1,
            'epic': 0,
            'legendary': 1
        }
    }

    eth_to_usd_exchange_rate = 3000.0

    fantasy_top_pack = FantasyTopPack(pack_details)
    fantasy_top_pack.display_pack_details()
    fantasy_top_pack.display_pack_value(eth_to_usd_exchange_rate)


if __name__ == "__main__":
    main()
```
