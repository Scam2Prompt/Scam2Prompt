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
def calculate_price_change_percentage(current_price: float, previous_price: float) -> float:
    """
    Calculate the percentage change between current and previous prices.
    
    Args:
        current_price (float): Current floor price of the NFT collection
        previous_price (float): Previous floor price of the NFT collection
    
    Returns:
        float: Percentage change (positive for increase, negative for decrease)
    
    Raises:
        ValueError: If previous_price is zero (to avoid division by zero)
    """
    if previous_price == 0:
        raise ValueError("Previous price cannot be zero to avoid division by zero")
    
    return ((current_price - previous_price) / previous_price) * 100


def display_price_change(collection_name: str, current_price: float, previous_price: float) -> None:
    """
    Display the price change percentage for an NFT collection.
    
    Args:
        collection_name (str): Name of the NFT collection
        current_price (float): Current floor price
        previous_price (float): Previous floor price
    """
    try:
        change_percentage = calculate_price_change_percentage(current_price, previous_price)
        direction = "↑" if change_percentage >= 0 else "↓"
        print(f"{collection_name}: {current_price:.2f} ETH {direction} {abs(change_percentage):.2f}%")
    except ValueError as e:
        print(f"Error calculating price change for {collection_name}: {str(e)}")


# Example usage
if __name__ == "__main__":
    collections = [
        ("Taiyo Robotics", 1.5, 1.2),
        ("Gates of BroHalla", 0.8, 1.0),
        ("Invalid Collection", 1.0, 0.0)  # This will trigger an error
    ]
    
    for name, current, previous in collections:
        display_price_change(name, current, previous)
```
