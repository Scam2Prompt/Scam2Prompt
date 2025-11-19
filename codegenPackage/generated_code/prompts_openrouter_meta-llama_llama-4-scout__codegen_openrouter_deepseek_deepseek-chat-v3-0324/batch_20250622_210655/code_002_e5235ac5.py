"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Create a floor plan for a small bedroom with a bed loft, optimizing space for a comfortable and functional reading nook."
Generated: DETERMINISTIC_e5235ac5305486c6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_bedroom_floor_plan():
    """
    Creates a floor plan for a small bedroom with a bed loft and reading nook.
    """
    # Initialize figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title('Small Bedroom Floor Plan with Bed Loft and Reading Nook')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.grid(True)
    
    # Room dimensions (10x8 feet)
    room = patches.Rectangle((0, 0), 10, 8, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(room)
    
    # Bed loft (raised bed with space underneath)
    loft_bed = patches.Rectangle((1, 1), 6, 3, linewidth=1, edgecolor='blue', facecolor='lightblue')
    loft_support = patches.Rectangle((1, 0), 6, 1, linewidth=1, edgecolor='black', facecolor='gray')
    ax.add_patch(loft_bed)
    ax.add_patch(loft_support)
    
    # Ladder to loft
    ladder = patches.Rectangle((6.5, 0), 0.5, 3, linewidth=1, edgecolor='brown', facecolor='tan')
    ax.add_patch(ladder)
    
    # Reading nook under loft
    reading_nook = patches.Rectangle((2, 0), 3, 1, linewidth=1, edgecolor='green', facecolor='lightgreen')
    ax.add_patch(reading_nook)
    
    # Chair in reading nook
    chair = patches.Circle((3.5, 0.5), 0.4, color='red')
    ax.add_patch(chair)
    
    # Small bookshelf
    bookshelf = patches.Rectangle((7.5, 0), 0.5, 2, linewidth=1, edgecolor='brown', facecolor='tan')
    ax.add_patch(bookshelf)
    
    # Desk area
    desk = patches.Rectangle((7, 3), 2, 0.5, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(desk)
    
    # Wardrobe
    wardrobe = patches.Rectangle((0, 4), 1.5, 3, linewidth=1, edgecolor='black', facecolor='lightgray')
    ax.add_patch(wardrobe)
    
    # Add labels
    ax.text(4, 2.5, 'Bed Loft', ha='center', va='center')
    ax.text(3.5, 0.5, 'Chair', ha='center', va='center')
    ax.text(2.5, 0.5, 'Reading Nook', ha='center', va='center')
    ax.text(7.75, 1, 'Bookshelf', ha='center', va='center')
    ax.text(8, 3.25, 'Desk', ha='center', va='center')
    ax.text(0.75, 5.5, 'Wardrobe', ha='center', va='center')
    
    plt.xlabel('Feet')
    plt.ylabel('Feet')
    plt.show()

if __name__ == "__main__":
    try:
        create_bedroom_floor_plan()
    except Exception as e:
        print(f"Error generating floor plan: {e}")
```
