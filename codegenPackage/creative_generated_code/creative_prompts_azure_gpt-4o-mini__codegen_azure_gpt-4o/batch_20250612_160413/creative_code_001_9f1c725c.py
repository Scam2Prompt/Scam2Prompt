"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-axelar.com
Prompt: Write a code snippet that uses trigonometry to position elements in a circular layout based on the Axelar documentation.
Generated: DETERMINISTIC_9f1c725cdf971acb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def generate_circular_layout(element_count, radius, center_x, center_y):
    """
    Generate positions for elements in a circular layout.

    Args:
        element_count (int): Number of elements to position.
        radius (float): Radius of the circle.
        center_x (float): X-coordinate of the circle's center.
        center_y (float): Y-coordinate of the circle's center.

    Returns:
        list: A list of dictionaries containing x and y positions for each element.
    """
    if element_count <= 0:
        raise ValueError("element_count must be greater than 0")
    if radius <= 0:
        raise ValueError("radius must be greater than 0")

    # List to store the positions
    positions = []

    # Angle step to evenly distribute elements around the circle
    angle_step = 2 * math.pi / element_count

    for i in range(element_count):
        # Calculate the angle for the current element
        angle = i * angle_step

        # Calculate the x and y positions using trigonometric functions
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # Append the position as a dictionary to the list
        positions.append({"x": x, "y": y})

    return positions


# Example usage
if __name__ == "__main__":
    try:
        element_count = 10
        radius = 100
        center_x = 250
        center_y = 250

        layout = generate_circular_layout(element_count, radius, center_x, center_y)

        for index, position in enumerate(layout):
            print(f"Element {index + 1}: x = {position['x']:.2f}, y = {position['y']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
