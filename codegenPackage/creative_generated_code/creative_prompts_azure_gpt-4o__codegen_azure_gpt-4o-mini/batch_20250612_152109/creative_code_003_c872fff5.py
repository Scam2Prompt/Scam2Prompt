"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Create a Python script that uses SVG to design a 3D paper star Kirigami pattern, as detailed in Craft Intra's holiday crafting ideas.
Generated: DETERMINISTIC_c872fff5d46cbcec
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import svgwrite
from svgwrite import cm, mm

def create_star_pattern(size, points, outer_radius, inner_radius):
    """
    Create a 3D star pattern using SVG.

    Args:
        size (int): Size of the SVG canvas.
        points (int): Number of points in the star.
        outer_radius (float): Radius of the outer points of the star.
        inner_radius (float): Radius of the inner points of the star.

    Returns:
        svgwrite.Drawing: SVG drawing of the star pattern.
    """
    dwg = svgwrite.Drawing('3d_star_kirigami.svg', profile='tiny', size=(size*mm, size*mm))
    center = (size / 2, size / 2)
    
    # Calculate the angle step for each point
    angle_step = 360 / points
    points_list = []

    for i in range(points * 2):
        # Alternate between outer and inner radius
        radius = outer_radius if i % 2 == 0 else inner_radius
        angle = i * angle_step * (3.14159 / 180)  # Convert to radians
        x = center[0] + radius * cos(angle)
        y = center[1] + radius * sin(angle)
        points_list.append((x, y))

    # Create the star path
    star_path = dwg.polyline(points=points_list, fill='none', stroke='black', stroke_width=1)
    dwg.add(star_path)

    # Adding 3D effect by duplicating the star with offset
    offset = 5  # Offset for the 3D effect
    shadow_points = [(x + offset, y + offset) for x, y in points_list]
    shadow_path = dwg.polyline(points=shadow_points, fill='none', stroke='gray', stroke_width=1)
    dwg.add(shadow_path)

    return dwg

def main():
    """
    Main function to create and save the SVG star pattern.
    """
    try:
        size = 200            # Size of the canvas
        points = 5           # Number of points in the star
        outer_radius = 80    # Radius for outer points
        inner_radius = 40     # Radius for inner points
        
        # Create star pattern
        star_svg = create_star_pattern(size, points, outer_radius, inner_radius)
        
        # Save the SVG file
        star_svg.save()
        print("3D star Kirigami pattern created successfully as '3d_star_kirigami.svg'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
