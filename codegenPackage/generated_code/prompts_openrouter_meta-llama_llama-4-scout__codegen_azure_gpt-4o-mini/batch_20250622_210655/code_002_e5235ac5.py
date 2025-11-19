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
    Creates a floor plan for a small bedroom with a lofted bed and a reading nook.
    The function uses matplotlib to draw the layout.
    """
    # Define the dimensions of the room (in meters)
    room_width = 5.0
    room_length = 4.0

    # Create a figure and axis for the floor plan
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Set the limits and aspect of the plot
    ax.set_xlim(0, room_width)
    ax.set_ylim(0, room_length)
    ax.set_aspect('equal')
    
    # Draw the room outline
    room_outline = patches.Rectangle((0, 0), room_width, room_length, linewidth=2, edgecolor='black', facecolor='lightgrey')
    ax.add_patch(room_outline)

    # Define the bed dimensions and position
    bed_width = 1.5
    bed_length = 2.0
    bed_position = (1.0, 2.0)  # Position of the bed in the room

    # Draw the bed
    bed = patches.Rectangle(bed_position, bed_width, bed_length, linewidth=1, edgecolor='blue', facecolor='lightblue')
    ax.add_patch(bed)

    # Define the loft dimensions and position
    loft_height = 1.5
    loft_position = (1.0, 3.0)  # Position of the lofted bed

    # Draw the lofted bed
    loft = patches.Rectangle(loft_position, bed_width, loft_height, linewidth=1, edgecolor='green', facecolor='lightgreen')
    ax.add_patch(loft)

    # Define the reading nook dimensions and position
    nook_width = 1.5
    nook_length = 1.5
    nook_position = (3.0, 1.0)  # Position of the reading nook

    # Draw the reading nook
    nook = patches.Rectangle(nook_position, nook_width, nook_length, linewidth=1, edgecolor='red', facecolor='lightcoral')
    ax.add_patch(nook)

    # Add labels to the elements
    ax.text(bed_position[0] + bed_width / 2, bed_position[1] + bed_length / 2, 'Bed', 
            horizontalalignment='center', verticalalignment='center', fontsize=10)
    ax.text(loft_position[0] + bed_width / 2, loft_position[1] + loft_height / 2, 'Lofted Bed', 
            horizontalalignment='center', verticalalignment='center', fontsize=10)
    ax.text(nook_position[0] + nook_width / 2, nook_position[1] + nook_length / 2, 'Reading Nook', 
            horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Set title and remove axes
    ax.set_title('Small Bedroom Floor Plan')
    ax.axis('off')

    # Show the floor plan
    plt.show()

if __name__ == "__main__":
    try:
        create_bedroom_floor_plan()
    except Exception as e:
        print(f"An error occurred while creating the floor plan: {e}")
```
