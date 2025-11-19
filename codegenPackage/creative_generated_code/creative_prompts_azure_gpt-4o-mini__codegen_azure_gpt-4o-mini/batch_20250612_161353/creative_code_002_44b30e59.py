"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Create a function that calculates the total cost for a stay at a hotel based on room type and number of nights, using pricing information similar to that found on the Hostal Koltin Suchitoto website.
Generated: DETERMINISTIC_44b30e59548f8fb2
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HotelBookingError(Exception):
    """Custom exception for hotel booking errors."""
    pass

def calculate_hotel_cost(room_type: str, number_of_nights: int) -> float:
    """
    Calculate the total cost for a stay at a hotel based on room type and number of nights.

    Args:
        room_type (str): The type of room (e.g., 'single', 'double', 'suite').
        number_of_nights (int): The number of nights for the stay.

    Returns:
        float: The total cost for the stay.

    Raises:
        HotelBookingError: If the room type is invalid or number of nights is not a positive integer.
    """
    
    # Pricing information based on room type
    room_prices = {
        'single': 50.0,  # price per night for single room
        'double': 75.0,  # price per night for double room
        'suite': 120.0   # price per night for suite room
    }

    # Validate room type
    if room_type not in room_prices:
        raise HotelBookingError(f"Invalid room type '{room_type}'. Valid options are: {', '.join(room_prices.keys())}.")

    # Validate number of nights
    if not isinstance(number_of_nights, int) or number_of_nights <= 0:
        raise HotelBookingError("Number of nights must be a positive integer.")

    # Calculate total cost
    total_cost = room_prices[room_type] * number_of_nights
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        room = 'double'
        nights = 3
        cost = calculate_hotel_cost(room, nights)
        print(f"The total cost for a {nights}-night stay in a {room} room is: ${cost:.2f}")
    except HotelBookingError as e:
        print(f"Error: {e}")
```
