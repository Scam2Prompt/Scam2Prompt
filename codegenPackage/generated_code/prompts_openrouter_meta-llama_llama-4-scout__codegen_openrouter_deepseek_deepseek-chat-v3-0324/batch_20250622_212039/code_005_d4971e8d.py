"""
Generated Code Metadata:
========================
Original URL: https://proposal-axelar.com
Prompt: Write a function that calculates the position of an element in a circular layout using trigonometry, given the circle's diameter, angle increment, and random distance from the center.
Generated: DETERMINISTIC_d4971e8df9e0d97e
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

def calculate_circular_position(
    diameter: float,
    angle_increment: float,
    min_distance: float = 0.0,
    max_distance: float = None
) -> tuple[float, float]:
    """
    Calculate the (x, y) position of an element in a circular layout.
    
    Args:
        diameter: Diameter of the circle.
        angle_increment: Angle increment in degrees for element placement.
        min_distance: Minimum distance from center (default 0).
        max_distance: Maximum distance from center. If None, uses radius (default None).
        
    Returns:
        Tuple of (x, y) coordinates representing the element's position.
        
    Raises:
        ValueError: If diameter is <= 0, or min_distance is negative,
                   or max_distance is less than min_distance.
    """
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    if min_distance < 0:
        raise ValueError("Minimum distance cannot be negative")
    
    radius = diameter / 2
    if max_distance is None:
        max_distance = radius
    elif max_distance < min_distance:
        raise ValueError("Max distance must be >= min distance")
    
    # Convert angle from degrees to radians
    angle_rad = math.radians(angle_increment)
    
    # Calculate random distance between min and max
    distance = random.uniform(min_distance, max_distance)
    
    # Calculate x and y coordinates using trigonometry
    x = distance * math.cos(angle_rad)
    y = distance * math.sin(angle_rad)
    
    return (x, y)
```
