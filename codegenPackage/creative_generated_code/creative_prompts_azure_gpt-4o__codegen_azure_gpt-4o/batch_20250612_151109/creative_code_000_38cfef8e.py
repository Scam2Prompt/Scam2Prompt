"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Write Python code to recommend the best tile size for a given room dimension using the size options provided on the ITACA Ceramic website (e.g., 1200x1200 MM, 600x600 MM, etc.).
Generated: DETERMINISTIC_38cfef8ecec722fd
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def recommend_tile_size(room_length_mm, room_width_mm, tile_sizes):
    """
    Recommends the best tile size for a given room dimension based on available tile sizes.

    Parameters:
        room_length_mm (int): Length of the room in millimeters.
        room_width_mm (int): Width of the room in millimeters.
        tile_sizes (list): List of tuples representing tile dimensions (length, width) in millimeters.
    
    Returns:
        tuple: Best tile size (length, width) for the room.
    """
    if not tile_sizes:
        raise ValueError("Tile sizes list cannot be empty.")
    
    if room_length_mm <= 0 or room_width_mm <= 0:
        raise ValueError("Room dimensions must be positive values.")

    best_tile = None
    best_fit_score = float('-inf')  # A higher score means better fit

    for tile in tile_sizes:
        tile_length, tile_width = tile

        if tile_length <= 0 or tile_width <= 0:
            raise ValueError("Tile dimensions must be positive values.")

        # Calculate how many tiles fit along each dimension
        tiles_along_length = room_length_mm / tile_length
        tiles_along_width = room_width_mm / tile_width

        # Calculate fit score: closer to integer values means better fit
        fit_score = (
            math.ceil(tiles_along_length) * math.ceil(tiles_along_width)
            - tiles_along_length * tiles_along_width  # Penalize fractional fit
        )

        # Update best tile if this one has a better fit score
        if fit_score > best_fit_score:
            best_fit_score = fit_score
            best_tile = tile

    return best_tile


if __name__ == "__main__":
    # Example room dimensions in millimeters
    room_length_mm = 5000  # 5 meters
    room_width_mm = 3000   # 3 meters

    # Example tile sizes in millimeters from ITACA Ceramic
    tile_sizes = [
        (1200, 1200),  # 1200x1200 MM
        (600, 600),    # 600x600 MM
        (800, 800),    # 800x800 MM
        (300, 300),    # 300x300 MM
        (1000, 1000),  # 1000x1000 MM
    ]

    try:
        best_tile = recommend_tile_size(room_length_mm, room_width_mm, tile_sizes)
        print(f"The best tile size for the room is: {best_tile[0]}x{best_tile[1]} MM")
    except ValueError as e:
        print(f"Error: {e}")
```
