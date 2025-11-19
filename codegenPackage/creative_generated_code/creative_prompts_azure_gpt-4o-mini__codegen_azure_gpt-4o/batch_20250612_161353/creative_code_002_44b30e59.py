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
# hotel_cost_calculator.py

def calculate_total_cost(room_type: str, nights: int) -> float:
    """
    Calculate the total cost of a hotel stay based on the room type and number of nights.

    Parameters:
        room_type (str): The type of room ("standard", "deluxe", "suite").
        nights (int): The number of nights staying at the hotel.

    Returns:
        float: The total cost of the stay.

    Raises:
        ValueError: If an invalid room type is provided.
        ValueError: If the number of nights is less than 1.
    """
    # Define room prices per night (example pricing based on Hostal Koltin Suchitoto)
    room_prices = {
        "standard": 50.0,  # Price per night for a standard room in dollars
        "deluxe": 75.0,    # Price per night for a deluxe room in dollars
        "suite": 120.0     # Price per night for a suite in dollars
    }
    
    # Validate room type
    if room_type not in room_prices:
        raise ValueError(f"Invalid room type '{room_type}'. Valid options are: {', '.join(room_prices.keys())}")
    
    # Validate number of nights
    if nights < 1:
        raise ValueError("Number of nights must be at least 1.")
    
    # Calculate total cost
    total_cost = room_prices[room_type] * nights
    
    return total_cost


# Example usage (uncomment the lines below to test the function)
# try:
#     room_type = "deluxe"
#     nights = 3
#     cost = calculate_total_cost(room_type, nights)
#     print(f"The total cost for {nights} nights in a {room_type} room is ${cost:.2f}.")
# except ValueError as e:
#     print(f"Error: {e}")
```
