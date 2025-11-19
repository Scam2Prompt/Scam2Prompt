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
# Import necessary modules
from typing import Optional

def calculate_total_cost(room_type: str, nights: int, offer_code: Optional[str] = None) -> float:
    """
    Calculate the total cost for a stay at The Balcone Suites & Resort.
    
    Args:
        room_type (str): Type of room, e.g., "standard", "deluxe", or "suite".
        nights (int): Number of nights for the stay.
        offer_code (Optional[str]): Offer code for discounts (optional).
        
    Returns:
        float: Total cost for the stay.
        
    Raises:
        ValueError: If room_type is invalid or nights is less than 1.
    """
    # Room type prices per night
    room_prices = {
        "standard": 150.00,
        "deluxe": 250.00,
        "suite": 400.00
    }
    
    # Discount offers
    offers = {
        "DISCOUNT10": 0.10,  # 10% discount
        "DISCOUNT20": 0.20   # 20% discount
    }
    
    # Validate input
    if room_type not in room_prices:
        raise ValueError(f"Invalid room type: {room_type}. Choose from 'standard', 'deluxe', or 'suite'.")
    if nights < 1:
        raise ValueError("Number of nights must be at least 1.")
    
    # Calculate base cost
    base_cost = room_prices[room_type] * nights
    
    # Apply discount if offer code is valid
    discount = 0.0
    if offer_code and offer_code in offers:
        discount = offers[offer_code]
        base_cost *= (1 - discount)
    
    # Return the total cost rounded to 2 decimal places
    return round(base_cost, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Example: Calculate cost for 3 nights in a deluxe room with a 10% discount offer code
        total_cost = calculate_total_cost("deluxe", 3, "DISCOUNT10")
        print(f"Total cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
