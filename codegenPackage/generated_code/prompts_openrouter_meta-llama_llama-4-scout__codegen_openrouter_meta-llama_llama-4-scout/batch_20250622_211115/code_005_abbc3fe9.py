"""
Generated Code Metadata:
========================
Original URL: https://nft-air.web.app
Prompt: "Create a code snippet to calculate and display the price change percentage for NFT collections like 'Taiyo Robotics' and 'Gates of BroHalla' given their current and previous floor prices."
Generated: DETERMINISTIC_abbc3fe95d2e8d21
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_price_change_percentage(current_price, previous_price):
    """
    Calculate the price change percentage.

    Args:
        current_price (float): The current floor price of the NFT collection.
        previous_price (float): The previous floor price of the NFT collection.

    Returns:
        float: The price change percentage.

    Raises:
        ValueError: If the previous price is zero.
    """
    if previous_price == 0:
        raise ValueError("Previous price cannot be zero.")

    price_change = current_price - previous_price
    price_change_percentage = (price_change / previous_price) * 100
    return price_change_percentage


def display_nft_collection_price_change(collection_name, current_price, previous_price):
    """
    Display the price change percentage for an NFT collection.

    Args:
        collection_name (str): The name of the NFT collection.
        current_price (float): The current floor price of the NFT collection.
        previous_price (float): The previous floor price of the NFT collection.

    Raises:
        ValueError: If the previous price is zero.
    """
    try:
        price_change_percentage = calculate_price_change_percentage(current_price, previous_price)
        print(f"Collection: {collection_name}")
        print(f"Current Floor Price: {current_price}")
        print(f"Previous Floor Price: {previous_price}")
        print(f"Price Change Percentage: {price_change_percentage:.2f}%")
        if price_change_percentage > 0:
            print("Price is up.\n")
        elif price_change_percentage < 0:
            print("Price is down.\n")
        else:
            print("Price is stable.\n")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    nft_collections = {
        "Taiyo Robotics": {"current_price": 1.23, "previous_price": 1.15},
        "Gates of BroHalla": {"current_price": 5.67, "previous_price": 6.00},
    }

    for collection_name, prices in nft_collections.items():
        display_nft_collection_price_change(collection_name, prices["current_price"], prices["previous_price"])


if __name__ == "__main__":
    main()
```
