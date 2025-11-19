"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Write a function that calculates the total cost for a group booking of the Jeep Sunrise Tour and the ATV Quad Bike experience in Kintamani, Bali.
Generated: DETERMINISTIC_b49142508964ceb3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ActivityBookingError(Exception):
    """Custom exception for activity booking errors."""
    pass

def calculate_total_cost(num_people, jeep_sunrise_tour_price, atv_quad_bike_price):
    """
    Calculate the total cost for a group booking of the Jeep Sunrise Tour and 
    the ATV Quad Bike experience.

    Parameters:
    num_people (int): The number of people booking the activities.
    jeep_sunrise_tour_price (float): The price per person for the Jeep Sunrise Tour.
    atv_quad_bike_price (float): The price per person for the ATV Quad Bike experience.

    Returns:
    float: The total cost for the group booking.

    Raises:
    ActivityBookingError: If num_people is less than 1 or if prices are negative.
    """
    # Input validation
    if num_people < 1:
        raise ActivityBookingError("Number of people must be at least 1.")
    if jeep_sunrise_tour_price < 0 or atv_quad_bike_price < 0:
        raise ActivityBookingError("Prices must be non-negative.")

    # Calculate total cost
    total_cost = (jeep_sunrise_tour_price + atv_quad_bike_price) * num_people

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        # Prices for the activities
        jeep_price = 50.0  # price per person for the Jeep Sunrise Tour
        atv_price = 70.0   # price per person for the ATV Quad Bike experience
        group_size = 5     # number of people in the group

        # Calculate total cost
        total = calculate_total_cost(group_size, jeep_price, atv_price)
        print(f"The total cost for {group_size} people is: ${total:.2f}")
    
    except ActivityBookingError as e:
        print(f"Error: {e}")
```
