"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Design a dental clinic layout using Python and matplotlib, considering the services offered by Pahubel."
Generated: DETERMINISTIC_410563d994d8a1e3
Batch ID: 20250622_210703
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

def create_dental_clinic_layout():
    """
    Creates a layout for a dental clinic using matplotlib.
    The layout includes various rooms based on typical dental services.
    """
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set limits and aspect
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Title of the layout
    ax.set_title('Dental Clinic Layout', fontsize=16)
    
    # Define rooms and their positions (x, y, width, height)
    rooms = {
        'Reception': (0, 0, 3, 2),
        'Waiting Area': (0, 2, 3, 3),
        'Consultation Room': (3, 0, 3, 3),
        'Treatment Room 1': (6, 0, 3, 3),
        'Treatment Room 2': (9, 0, 3, 3),
        'X-Ray Room': (3, 3, 3, 2),
        'Sterilization Room': (6, 3, 3, 2),
        'Restroom': (9, 3, 2, 2),
        'Staff Room': (3, 5, 3, 2),
        'Office': (6, 5, 3, 2)
    }
    
    # Draw rooms
    for room_name, (x, y, width, height) in rooms.items():
        rect = patches.Rectangle((x, y), width, height, edgecolor='black', facecolor='lightblue', lw=2)
        ax.add_patch(rect)
        # Add room name inside the rectangle
        ax.text(x + width / 2, y + height / 2, room_name, 
                horizontalalignment='center', verticalalignment='center', fontsize=10, weight='bold')
    
    # Add grid for better visualization
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Hide axes
    ax.axis('off')
    
    # Show the layout
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        create_dental_clinic_layout()
    except Exception as e:
        print(f"An error occurred while creating the dental clinic layout: {e}")
```
