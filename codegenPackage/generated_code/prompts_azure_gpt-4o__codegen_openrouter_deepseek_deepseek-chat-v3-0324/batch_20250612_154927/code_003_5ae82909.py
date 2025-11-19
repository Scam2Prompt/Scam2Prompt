"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Provide a Python function that calculates the cost estimate for installing retractable window screens based on user-provided dimensions and screen type (e.g., motorized or standard).
Generated: DETERMINISTIC_5ae829096e828301
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_screen_installation_cost(width: float, height: float, screen_type: str) -> float:
    """
    Calculate the cost estimate for installing retractable window screens.
    
    Args:
        width (float): Width of the window in feet.
        height (float): Height of the window in feet.
        screen_type (str): Type of screen ('standard' or 'motorized').
        
    Returns:
        float: Total installation cost in USD.
        
    Raises:
        ValueError: If dimensions are non-positive or screen type is invalid.
    """
    # Validate input parameters
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    
    screen_type = screen_type.lower()
    if screen_type not in ['standard', 'motorized']:
        raise ValueError("Invalid screen type. Must be 'standard' or 'motorized'.")
    
    # Base prices per square foot
    STANDARD_PRICE_PER_SQFT = 12.50
    MOTORIZED_PRICE_PER_SQFT = 25.75
    
    # Installation fees
    STANDARD_INSTALLATION_FEE = 75.00
    MOTORIZED_INSTALLATION_FEE = 150.00
    
    # Calculate area
    area = width * height
    
    # Calculate material cost based on screen type
    if screen_type == 'standard':
        material_cost = area * STANDARD_PRICE_PER_SQFT
        installation_fee = STANDARD_INSTALLATION_FEE
    else:
        material_cost = area * MOTORIZED_PRICE_PER_SQFT
        installation_fee = MOTORIZED_INSTALLATION_FEE
    
    # Calculate total cost
    total_cost = material_cost + installation_fee
    
    # Apply bulk discount for large windows (over 40 sqft)
    if area > 40:
        total_cost *= 0.9  # 10% discount
    
    return round(total_cost, 2)
```
