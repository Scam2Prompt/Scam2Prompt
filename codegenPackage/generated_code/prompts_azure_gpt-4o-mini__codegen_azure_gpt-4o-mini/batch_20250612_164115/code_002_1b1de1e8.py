"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Write a Python function that calculates the total cost for a stay at The Balcone Suites & Resort, taking into account room type, number of nights, and any applicable offers.
Generated: DETERMINISTIC_1b1de1e8bbc72631
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RoomType:
    """Enum for room types with their respective nightly rates."""
    STANDARD = 100
    DELUXE = 150
    SUITE = 200

class Offer:
    """Enum for available offers."""
    NONE = 1.0
    DISCOUNT_10 = 0.9  # 10% discount
    DISCOUNT_20 = 0.8  # 20% discount

def calculate_total_cost(room_type: str, number_of_nights: int, offer: str) -> float:
    """
    Calculate the total cost for a stay at The Balcone Suites & Resort.

    Parameters:
    room_type (str): The type of room ('standard', 'deluxe', 'suite').
    number_of_nights (int): The number of nights for the stay.
    offer (str): The applicable offer ('none', 'discount_10', 'discount_20').

    Returns:
    float: The total cost for the stay.

    Raises:
    ValueError: If the room type or offer is invalid, or if the number of nights is less than 1.
    """
    
    # Validate input parameters
    if number_of_nights < 1:
        raise ValueError("Number of nights must be at least 1.")
    
    room_rates = {
        'standard': RoomType.STANDARD,
        'deluxe': RoomType.DELUXE,
        'suite': RoomType.SUITE
    }
    
    offers = {
        'none': Offer.NONE,
        'discount_10': Offer.DISCOUNT_10,
        'discount_20': Offer.DISCOUNT_20
    }
    
    # Get the nightly rate for the selected room type
    if room_type.lower() not in room_rates:
        raise ValueError("Invalid room type. Choose from 'standard', 'deluxe', or 'suite'.")
    
    nightly_rate = room_rates[room_type.lower()]
    
    # Get the discount multiplier for the selected offer
    if offer.lower() not in offers:
        raise ValueError("Invalid offer. Choose from 'none', 'discount_10', or 'discount_20'.")
    
    discount_multiplier = offers[offer.lower()]
    
    # Calculate total cost
    total_cost = nightly_rate * number_of_nights * discount_multiplier
    
    return total_cost

# Example usage (uncomment to test):
# try:
#     total = calculate_total_cost('deluxe', 3, 'discount_10')
#     print(f"Total cost for the stay: ${total:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
