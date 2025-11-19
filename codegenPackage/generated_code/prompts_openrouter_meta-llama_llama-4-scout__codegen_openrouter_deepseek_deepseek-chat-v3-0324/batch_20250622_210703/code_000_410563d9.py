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
from matplotlib.text import Text

# Constants for room dimensions and spacing
ROOM_WIDTH = 4
ROOM_HEIGHT = 3
HALLWAY_WIDTH = 2
MARGIN = 1

def create_clinic_layout():
    """Create a dental clinic layout visualization."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 20)
    ax.set_title('Pahubel Dental Clinic Layout', fontsize=16, pad=20)
    ax.axis('off')
    
    # Main clinic area
    main_clinic = patches.Rectangle((MARGIN, MARGIN), 25, 15, 
                                   linewidth=2, edgecolor='black', 
                                   facecolor='lightgray', alpha=0.3)
    ax.add_patch(main_clinic)
    
    # Reception area
    reception = patches.Rectangle((MARGIN + 2, MARGIN + 12), 6, 3, 
                                 linewidth=1, edgecolor='black', 
                                 facecolor='lightblue', alpha=0.5)
    ax.add_patch(reception)
    ax.text(MARGIN + 5, MARGIN + 13.5, 'Reception', ha='center', va='center')
    
    # Waiting area
    waiting = patches.Rectangle((MARGIN + 9, MARGIN + 12), 6, 3, 
                               linewidth=1, edgecolor='black', 
                               facecolor='lightgreen', alpha=0.5)
    ax.add_patch(waiting)
    ax.text(MARGIN + 12, MARGIN + 13.5, 'Waiting Area', ha='center', va='center')
    
    # Hallway
    hallway = patches.Rectangle((MARGIN + 2, MARGIN + 2), 21, HALLWAY_WIDTH, 
                               linewidth=1, edgecolor='black', 
                               facecolor='white', alpha=0.5)
    ax.add_patch(hallway)
    ax.text(MARGIN + 12.5, MARGIN + 3, 'Hallway', ha='center', va='center')
    
    # Treatment rooms
    rooms = [
        ('General Dentistry', MARGIN + 2, MARGIN + 5),
        ('Pediatric Dentistry', MARGIN + 8, MARGIN + 5),
        ('Orthodontics', MARGIN + 14, MARGIN + 5),
        ('Oral Surgery', MARGIN + 20, MARGIN + 5),
        ('Endodontics', MARGIN + 2, MARGIN + 9),
        ('Periodontics', MARGIN + 8, MARGIN + 9),
        ('Prosthodontics', MARGIN + 14, MARGIN + 9),
        ('Radiology', MARGIN + 20, MARGIN + 9)
    ]
    
    for name, x, y in rooms:
        room = patches.Rectangle((x, y), ROOM_WIDTH, ROOM_HEIGHT, 
                                linewidth=1, edgecolor='black', 
                                facecolor='salmon', alpha=0.5)
        ax.add_patch(room)
        ax.text(x + ROOM_WIDTH/2, y + ROOM_HEIGHT/2, name, 
                ha='center', va='center', fontsize=9)
    
    # Staff areas
    staff_rooms = [
        ('Staff Lounge', MARGIN + 18, MARGIN + 12),
        ('Sterilization', MARGIN + 22, MARGIN + 12)
    ]
    
    for name, x, y in staff_rooms:
        room = patches.Rectangle((x, y), ROOM_WIDTH, ROOM_HEIGHT, 
                                linewidth=1, edgecolor='black', 
                                facecolor='lightyellow', alpha=0.5)
        ax.add_patch(room)
        ax.text(x + ROOM_WIDTH/2, y + ROOM_HEIGHT/2, name, 
                ha='center', va='center', fontsize=9)
    
    # Restroom
    restroom = patches.Rectangle((MARGIN + 2, MARGIN + 2 + HALLWAY_WIDTH + ROOM_HEIGHT + 1), 
                                ROOM_WIDTH, ROOM_HEIGHT, 
                                linewidth=1, edgecolor='black', 
                                facecolor='lavender', alpha=0.5)
    ax.add_patch(restroom)
    ax.text(MARGIN + 4, MARGIN + 6.5, 'Restroom', ha='center', va='center')
    
    # Legend
    legend_elements = [
        patches.Patch(facecolor='lightblue', edgecolor='black', label='Reception'),
        patches.Patch(facecolor='lightgreen', edgecolor='black', label='Waiting Area'),
        patches.Patch(facecolor='salmon', edgecolor='black', label='Treatment Rooms'),
        patches.Patch(facecolor='lightyellow', edgecolor='black', label='Staff Areas'),
        patches.Patch(facecolor='lavender', edgecolor='black', label='Restroom')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1))
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    create_clinic_layout()
```
