"""
Generated Code Metadata:
========================
Original URL: https://baturjeeptour.my.id
Prompt: Write a function that calculates the total cost for a group booking of the Jeep Sunrise Tour and the ATV Quad Bike experience in Kintamani, Bali.
Generated: DETERMINISTIC_b49142508964ceb3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_booking_cost(jeep_tour_pax: int, atv_quad_pax: int) -> float:
    """
    Calculate the total cost for a group booking of the Jeep Sunrise Tour and ATV Quad Bike experience in Kintamani, Bali.
    
    Args:
        jeep_tour_pax (int): Number of people for Jeep Sunrise Tour
        atv_quad_pax (int): Number of people for ATV Quad Bike experience
        
    Returns:
        float: Total cost of the booking in IDR (Indonesian Rupiah)
        
    Raises:
        ValueError: If either pax count is negative
    """
    # Prices per person in IDR (as of current rates)
    JEEP_TOUR_PRICE = 750000
    ATV_QUAD_PRICE = 600000
    
    # Validate input
    if jeep_tour_pax < 0 or atv_quad_pax < 0:
        raise ValueError("Number of participants cannot be negative")
    
    # Calculate total cost
    total_cost = (jeep_tour_pax * JEEP_TOUR_PRICE) + (atv_quad_pax * ATV_QUAD_PRICE)
    
    return total_cost
```
