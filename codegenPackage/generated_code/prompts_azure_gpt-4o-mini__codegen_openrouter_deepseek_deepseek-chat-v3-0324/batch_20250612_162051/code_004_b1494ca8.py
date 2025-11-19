"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Construct a library function that calculates the total cost for installing a شیشه دوش حمام based on user input for dimensions and selected color options.
Generated: DETERMINISTIC_b1494ca896a6561b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_shower_glass_cost(width, height, color_option):
    """
    Calculate the total cost for installing a shower glass based on dimensions and color options.
    
    Args:
        width (float): Width of the shower glass in meters.
        height (float): Height of the shower glass in meters.
        color_option (str): Color option for the glass. Valid options: 'clear', 'bronze', 'grey', 'blue'.
        
    Returns:
        float: Total cost of the shower glass installation.
        
    Raises:
        ValueError: If dimensions are not positive or color option is invalid.
    """
    # Validate input dimensions
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    
    # Base price per square meter
    BASE_PRICE_PER_SQM = 150.0
    
    # Color premium multipliers
    COLOR_PRICES = {
        'clear': 1.0,
        'bronze': 1.2,
        'grey': 1.15,
        'blue': 1.1
    }
    
    # Validate color option
    if color_option.lower() not in COLOR_PRICES:
        raise ValueError(f"Invalid color option. Valid options are: {list(COLOR_PRICES.keys())}")
    
    # Calculate area
    area = width * height
    
    # Calculate base cost
    base_cost = area * BASE_PRICE_PER_SQM
    
    # Apply color premium
    color_multiplier = COLOR_PRICES[color_option.lower()]
    total_cost = base_cost * color_multiplier
    
    # Round to 2 decimal places for currency
    return round(total_cost, 2)
```
