"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write a Python function to calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count, using the pricing details provided on the website.
Generated: DETERMINISTIC_3c40a3f78a080490
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_workbench_price(width_cm, depth_cm, height_cm, drawer_count):
    """
    Calculate the total price of a Karma Çalışma Tezgahı based on dimensions and drawer count.
    
    Args:
        width_cm (float): Width of the workbench in centimeters (60-200 cm)
        depth_cm (float): Depth of the workbench in centimeters (60-100 cm)
        height_cm (float): Height of the workbench in centimeters (70-90 cm)
        drawer_count (int): Number of drawers (0-4)
    
    Returns:
        float: Total price in TRY
    
    Raises:
        ValueError: If any dimension or drawer count is out of valid range
    """
    # Validate input ranges
    if not (60 <= width_cm <= 200):
        raise ValueError("Width must be between 60-200 cm")
    if not (60 <= depth_cm <= 100):
        raise ValueError("Depth must be between 60-100 cm")
    if not (70 <= height_cm <= 90):
        raise ValueError("Height must be between 70-90 cm")
    if not (0 <= drawer_count <= 4):
        raise ValueError("Drawer count must be between 0-4")
    
    # Base price per square cm (example pricing - adjust according to actual rates)
    BASE_PRICE_PER_SQ_CM = 0.15  # TRY
    
    # Drawer prices (example pricing - adjust according to actual rates)
    DRAWER_PRICES = {
        0: 0,
        1: 250,
        2: 450,
        3: 600,
        4: 700
    }
    
    # Calculate surface area (width * depth)
    surface_area = width_cm * depth_cm
    
    # Calculate base price
    base_price = surface_area * BASE_PRICE_PER_SQ_CM
    
    # Add height adjustment (example: 10% increase for non-standard heights)
    if height_cm != 80:  # Assuming 80cm is standard
        base_price *= 1.1
    
    # Add drawer costs
    total_price = base_price + DRAWER_PRICES[drawer_count]
    
    return round(total_price, 2)

def calculate_total_price(workbenches):
    """
    Calculate total price for multiple workbenches.
    
    Args:
        workbenches (list): List of dictionaries containing workbench specs
            Each dict should have: width_cm, depth_cm, height_cm, drawer_count
    
    Returns:
        float: Total price for all workbenches
    
    Raises:
        ValueError: If any workbench has invalid specs
    """
    total = 0.0
    for bench in workbenches:
        try:
            price = calculate_workbench_price(
                bench['width_cm'],
                bench['depth_cm'],
                bench['height_cm'],
                bench['drawer_count']
            )
            total += price
        except KeyError as e:
            raise ValueError(f"Missing required specification: {e}")
    
    return round(total, 2)
```
