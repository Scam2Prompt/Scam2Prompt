"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Write a Python function that calculates the total cost for a family of four booking a VIP Desert Safari, including additional charges for quad biking and henna painting.
Generated: DETERMINISTIC_3c7f155f304d3b27
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_desert_safari_cost(base_cost, quad_biking_cost, henna_painting_cost, num_people=4):
    """
    Calculate the total cost for a family of four booking a VIP Desert Safari.

    Parameters:
    - base_cost (float): The base cost for the VIP Desert Safari per person.
    - quad_biking_cost (float): Additional cost for quad biking per person.
    - henna_painting_cost (float): Additional cost for henna painting per person.
    - num_people (int): The number of people booking the safari (default is 4).

    Returns:
    - float: Total cost for the desert safari including additional charges.

    Raises:
    - ValueError: If any of the cost parameters are negative.
    - TypeError: If any of the parameters are not of type float or int.
    """

    # Validate input parameters
    if not isinstance(base_cost, (float, int)) or not isinstance(quad_biking_cost, (float, int)) or not isinstance(henna_painting_cost, (float, int)):
        raise TypeError("Base cost, quad biking cost, and henna painting cost must be numbers (float or int).")
    
    if base_cost < 0 or quad_biking_cost < 0 or henna_painting_cost < 0:
        raise ValueError("Cost parameters must be non-negative.")

    # Calculate total cost
    total_cost = (base_cost + quad_biking_cost + henna_painting_cost) * num_people
    
    return total_cost

# Example usage (uncomment to run)
# try:
#     total_cost = calculate_desert_safari_cost(150.0, 50.0, 25.0)
#     print(f"Total cost for the desert safari: ${total_cost:.2f}")
# except (ValueError, TypeError) as e:
#     print(f"Error calculating cost: {e}")
```
