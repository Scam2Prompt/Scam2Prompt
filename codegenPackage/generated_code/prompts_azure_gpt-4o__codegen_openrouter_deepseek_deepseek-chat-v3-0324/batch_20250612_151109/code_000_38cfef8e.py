"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Write Python code to recommend the best tile size for a given room dimension using the size options provided on the ITACA Ceramic website (e.g., 1200x1200 MM, 600x600 MM, etc.).
Generated: DETERMINISTIC_38cfef8ecec722fd
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def recommend_tile_size(room_length, room_width, tile_options):
    """
    Recommends the best tile size for a given room dimension based on minimal cuts/waste.
    
    Args:
        room_length (float): Length of the room in millimeters.
        room_width (float): Width of the room in millimeters.
        tile_options (list): List of available tile sizes in format [(length, width), ...].
        
    Returns:
        tuple: Best tile size (length, width) and waste percentage.
    """
    if room_length <= 0 or room_width <= 0:
        raise ValueError("Room dimensions must be positive numbers.")
    
    if not tile_options:
        raise ValueError("No tile options provided.")
    
    best_tile = None
    min_waste = float('inf')
    
    for tile in tile_options:
        tile_length, tile_width = tile
        
        if tile_length <= 0 or tile_width <= 0:
            continue
            
        # Calculate number of tiles needed (rounded up)
        tiles_length = math.ceil(room_length / tile_length)
        tiles_width = math.ceil(room_width / tile_width)
        
        # Calculate total area covered by tiles
        covered_area = tiles_length * tile_length * tiles_width * tile_width
        
        # Calculate room area
        room_area = room_length * room_width
        
        # Calculate waste percentage
        waste = ((covered_area - room_area) / room_area) * 100
        
        if waste < min_waste:
            min_waste = waste
            best_tile = tile
    
    return best_tile, min_waste

# Example usage
if __name__ == "__main__":
    # Common ITACA Ceramic tile sizes in millimeters (length x width)
    tile_options = [
        (1200, 1200),
        (600, 600),
        (300, 300),
        (1200, 600),
        (600, 300)
    ]
    
    try:
        room_length = float(input("Enter room length (mm): "))
        room_width = float(input("Enter room width (mm): "))
        
        best_tile, waste = recommend_tile_size(room_length, room_width, tile_options)
        
        if best_tile:
            print(f"Recommended tile size: {best_tile[0]}x{best_tile[1]} mm")
            print(f"Estimated waste: {waste:.2f}%")
        else:
            print("No suitable tile size found.")
            
    except ValueError as e:
        print(f"Error: {e}")
```
