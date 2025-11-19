"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Write a Python function that calculates the total cost for a stay at The Balcone Suites & Resort, taking into account room type, number of nights, and any applicable offers.
Generated: DETERMINISTIC_1b1de1e8bbc72631
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RoomType:
    """Enumeration of room types and their respective nightly rates."""
    STANDARD = 100.0
    DELUXE = 150.0
    SUITE = 200.0

def calculate_total_cost(room_type, number_of_nights, discount_rate=0):
    """
    Calculate the total cost for a stay at The Balcone Suites & Resort.

    Parameters:
    room_type (str): The type of room ('standard', 'deluxe', 'suite').
    number_of_nights (int): The number of nights for the stay.
    discount_rate (float): A discount rate to apply (0 to 1). Default is 0 (no discount).

    Returns:
    float: The total cost for the stay after applying the discount.

    Raises:
    ValueError: If an invalid room type is provided or if number_of_nights is negative.
    """
    
    # Validate room type
    room_rates = {
        'standard': RoomType.STANDARD,
        'deluxe': RoomType.DELUXE,
        'suite': RoomType.SUITE
    }
    
    if room_type.lower() not in room_rates:
        raise ValueError(f"Invalid room type: {room_type}. Choose from {list(room_rates.keys())}.")
    
    if number_of_nights < 0:
        raise ValueError("Number of nights cannot be negative.")

    # Calculate the base cost
    base_cost = room_rates[room_type.lower()] * number_of_nights

    # Apply discount if applicable
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1.")
    
    total_cost = base_cost * (1 - discount_rate)

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        total = calculate_total_cost('deluxe', 3, 0.1)
        print(f"The total cost for your stay is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
