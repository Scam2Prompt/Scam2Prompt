"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Design a custom tile work pattern using Python and matplotlib, inspired by the handcrafted stone and tile work services offered by Winger R&R.
Generated: DETERMINISTIC_83bfb7489bba913b
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from matplotlib.collections import PatchCollection
import random

def generate_tile_pattern(width=10, height=10, tile_size=1, pattern_type='mosaic'):
    """
    Generate a custom tile pattern with various designs.
    
    Parameters:
    - width: Number of tiles horizontally
    - height: Number of tiles vertically
    - tile_size: Size of each tile
    - pattern_type: Type of pattern ('mosaic', 'herringbone', 'chevron', 'random')
    
    Returns:
    - fig: matplotlib figure object
    """
    
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(0, width * tile_size)
    ax.set_ylim(0, height * tile_size)
    ax.set_aspect('equal')
    ax.axis('off')
    
    patches = []
    colors = []
    
    # Define a palette inspired by natural stone and tile
    palette = [
        '#8B7355', '#C4A484', '#D8B991',  # Earth tones
        '#6B8E23', '#556B2F',             # Greens
        '#B22222', '#CD5C5C',             # Reds
        '#4682B4', '#5F9EA0',             # Blues
        '#DAA520', '#F5DEB3'              # Golds
    ]
    
    for i in range(width):
        for j in range(height):
            x = i * tile_size
            y = j * tile_size
            
            if pattern_type == 'mosaic':
                # Create mosaic pattern with small squares
                for sub_i in range(2):
                    for sub_j in range(2):
                        sub_x = x + sub_i * tile_size/2
                        sub_y = y + sub_j * tile_size/2
                        patches.append(Rectangle((sub_x, sub_y), tile_size/2, tile_size/2))
                        colors.append(random.choice(palette))
            
            elif pattern_type == 'herringbone':
                # Create herringbone pattern
                if (i + j) % 2 == 0:
                    patches.append(Polygon([
                        (x, y),
                        (x + tile_size, y),
                        (x + tile_size/2, y + tile_size)
                    ]))
                    patches.append(Polygon([
                        (x, y + tile_size),
                        (x + tile_size, y + tile_size),
                        (x + tile_size/2, y)
                    ]))
                colors.extend([random.choice(palette), random.choice(palette)])
            
            elif pattern_type == 'chevron':
                # Create chevron pattern
                if j % 2 == 0:
                    patches.append(Polygon([
                        (x, y),
                        (x + tile_size/2, y + tile_size),
                        (x + tile_size, y)
                    ]))
                else:
                    patches.append(Polygon([
                        (x, y + tile_size),
                        (x + tile_size/2, y),
                        (x + tile_size, y + tile_size)
                    ]))
                colors.append(random.choice(palette))
            
            else:  # random pattern
                shape_type = random.choice(['square', 'triangle', 'hexagon'])
                
                if shape_type == 'square':
                    patches.append(Rectangle((x, y), tile_size, tile_size))
                elif shape_type == 'triangle':
                    patches.append(Polygon([
                        (x, y),
                        (x + tile_size, y),
                        (x + tile_size/2, y + tile_size)
                    ]))
                else:  # hexagon
                    patches.append(Polygon([
                        (x + tile_size/4, y),
                        (x + 3*tile_size/4, y),
                        (x + tile_size, y + tile_size/2),
                        (x + 3*tile_size/4, y + tile_size),
                        (x + tile_size/4, y + tile_size),
                        (x, y + tile_size/2)
                    ]))
                colors.append(random.choice(palette))
    
    # Add all patches to the plot
    collection = PatchCollection(patches, alpha=0.9, edgecolor='#333333', linewidth=0.5)
    collection.set_facecolor(colors)
    ax.add_collection(collection)
    
    # Add title
    title = f"Winger R&R Inspired {pattern_type.capitalize()} Tile Pattern"
    plt.title(title, fontsize=16, pad=20)
    
    return fig

# Example usage
if __name__ == "__main__":
    patterns = ['mosaic', 'herringbone', 'chevron', 'random']
    
    for pattern in patterns:
        fig = generate_tile_pattern(width=8, height=8, tile_size=1, pattern_type=pattern)
        plt.tight_layout()
        plt.savefig(f'{pattern}_tile_pattern.png', dpi=300, bbox_inches='tight')
        plt.close()
```
