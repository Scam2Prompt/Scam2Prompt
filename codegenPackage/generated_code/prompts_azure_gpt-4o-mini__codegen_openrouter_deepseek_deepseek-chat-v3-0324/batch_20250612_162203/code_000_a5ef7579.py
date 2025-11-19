"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Write a code snippet to calculate the total area required for installing raised access flooring in a server room, considering the dimensions of the room and the panel sizes mentioned on Libo Interiors' website.
Generated: DETERMINISTIC_a5ef7579f055f2be
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_raised_floor_area(room_length, room_width, panel_size=600):
    """
    Calculate the total area required for installing raised access flooring in a server room.
    
    Args:
        room_length (float): Length of the room in millimeters.
        room_width (float): Width of the room in millimeters.
        panel_size (int, optional): Size of the flooring panel in millimeters (default is 600mm).
    
    Returns:
        float: Total area required in square meters.
    
    Raises:
        ValueError: If any input is non-positive or panel_size is not a standard size.
    """
    # Standard panel sizes (in mm) as per Libo Interiors' specifications
    STANDARD_PANEL_SIZES = {300, 600, 1200}
    
    # Validate inputs
    if room_length <= 0 or room_width <= 0:
        raise ValueError("Room dimensions must be positive numbers.")
    if panel_size not in STANDARD_PANEL_SIZES:
        raise ValueError(f"Panel size must be one of {STANDARD_PANEL_SIZES} mm.")
    
    # Calculate number of panels needed along length and width
    panels_length = room_length / panel_size
    panels_width = room_width / panel_size
    
    # Round up to nearest whole panel
    panels_length = int(panels_length) if panels_length.is_integer() else int(panels_length) + 1
    panels_width = int(panels_width) if panels_width.is_integer() else int(panels_width) + 1
    
    # Calculate total area in square meters
    total_panels = panels_length * panels_width
    panel_area_sq_m = (panel_size / 1000) ** 2  # Convert mm to m and calculate area
    total_area = total_panels * panel_area_sq_m
    
    return total_area

# Example usage:
# area = calculate_raised_floor_area(5000, 4000)  # 5m x 4m room with default 600mm panels
# print(f"Total area required: {area:.2f} square meters")
```
