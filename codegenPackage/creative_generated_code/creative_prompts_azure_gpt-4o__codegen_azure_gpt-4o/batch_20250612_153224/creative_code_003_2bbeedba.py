"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Write a function to optimize the layout for tlakovanje (paving) surfaces using predefined dimensions and patterns.
Generated: DETERMINISTIC_2bbeedba4ee89d59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def optimize_paving_layout(surface_width, surface_height, tile_width, tile_height):
    """
    Optimizes the paving layout for a given surface using predefined tile dimensions.

    Args:
        surface_width (float): The width of the surface to be paved (in meters).
        surface_height (float): The height of the surface to be paved (in meters).
        tile_width (float): The width of a single tile (in meters).
        tile_height (float): The height of a single tile (in meters).

    Returns:
        dict: A dictionary containing the optimal number of tiles and wasted area.
    """
    try:
        # Validate input parameters
        if surface_width <= 0 or surface_height <= 0 or tile_width <= 0 or tile_height <= 0:
            raise ValueError("All dimensions must be positive numbers.")

        # Calculate the number of tiles that fit in both dimensions
        tiles_across_width = math.ceil(surface_width / tile_width)
        tiles_across_height = math.ceil(surface_height / tile_height)

        # Total tiles needed
        total_tiles = tiles_across_width * tiles_across_height

        # Calculate the paved area using tiles
        paved_area = tiles_across_width * tile_width * tiles_across_height * tile_height

        # Calculate wasted area (surface area minus actual paved area)
        surface_area = surface_width * surface_height
        wasted_area = paved_area - surface_area

        # Return the optimization results
        return {
            "total_tiles": total_tiles,
            "wasted_area": wasted_area,
            "tiles_across_width": tiles_across_width,
            "tiles_across_height": tiles_across_height,
        }

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}


# Example usage (you can remove this in production code):
if __name__ == "__main__":
    surface_width = 5.5  # in meters
    surface_height = 3.2  # in meters
    tile_width = 0.3  # in meters
    tile_height = 0.3  # in meters

    result = optimize_paving_layout(surface_width, surface_height, tile_width, tile_height)
    print("Optimization Result:", result)
```
