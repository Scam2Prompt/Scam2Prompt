"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Write a Python function that takes room dimensions and renovation type as inputs, and returns an estimated cost using Панам's pricing model.
Generated: DETERMINISTIC_7c3a5ce2b9d3ab40
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_renovation_cost(length, width, renovation_type):
    """
    Calculate the estimated cost of room renovation based on dimensions and renovation type.

    Args:
        length (float): The length of the room in meters.
        width (float): The width of the room in meters.
        renovation_type (str): Type of renovation. Options are 'basic', 'standard', or 'premium'.

    Returns:
        float: The estimated cost of renovation.
    Raises:
        ValueError: If length or width is non-positive.
        ValueError: If renovation_type is invalid.
    """
    # Validate room dimensions
    if length <= 0 or width <= 0:
        raise ValueError("Room dimensions must be positive values.")

    # Pricing model (cost per square meter based on renovation type)
    pricing_model = {
        'basic': 50,    # Basic renovation cost per square meter
        'standard': 100,  # Standard renovation cost per square meter
        'premium': 150   # Premium renovation cost per square meter
    }

    # Validate renovation type
    if renovation_type not in pricing_model:
        raise ValueError("Invalid renovation type. Choose from 'basic', 'standard', or 'premium'.")

    # Calculate room area
    room_area = length * width

    # Calculate cost based on chosen renovation type
    cost_per_square_meter = pricing_model[renovation_type]
    estimated_cost = room_area * cost_per_square_meter

    return estimated_cost


# Example Usage:
# try:
#     cost = calculate_renovation_cost(5, 4, 'standard')
#     print(f"Estimated Renovation Cost: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}")
```
