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

def draw_dental_clinic_layout():
    """
    Draws a dental clinic layout using matplotlib.
    The layout includes reception, waiting area, treatment rooms, and sterilization area.
    """
    # Initialize the figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_title("Dental Clinic Layout - Pahubel Services", fontsize=16)
    ax.set_aspect('equal', adjustable='box')

    # Reception Area
    reception = patches.Rectangle((5, 60), 30, 15, edgecolor='black', facecolor='lightblue', label='Reception')
    ax.add_patch(reception)
    ax.text(20, 67.5, "Reception", ha='center', va='center', fontsize=12)

    # Waiting Area
    waiting_area = patches.Rectangle((5, 40), 30, 15, edgecolor='black', facecolor='lightgreen', label='Waiting Area')
    ax.add_patch(waiting_area)
    ax.text(20, 47.5, "Waiting Area", ha='center', va='center', fontsize=12)

    # Treatment Rooms
    treatment_room_1 = patches.Rectangle((40, 60), 25, 15, edgecolor='black', facecolor='lightcoral', label='Treatment Room 1')
    ax.add_patch(treatment_room_1)
    ax.text(52.5, 67.5, "Treatment Room 1", ha='center', va='center', fontsize=12)

    treatment_room_2 = patches.Rectangle((40, 40), 25, 15, edgecolor='black', facecolor='lightcoral', label='Treatment Room 2')
    ax.add_patch(treatment_room_2)
    ax.text(52.5, 47.5, "Treatment Room 2", ha='center', va='center', fontsize=12)

    # Sterilization Area
    sterilization_area = patches.Rectangle((70, 50), 25, 15, edgecolor='black', facecolor='lightyellow', label='Sterilization Area')
    ax.add_patch(sterilization_area)
    ax.text(82.5, 57.5, "Sterilization Area", ha='center', va='center', fontsize=12)

    # Add legend
    ax.legend(loc='upper right', fontsize=10)

    # Add grid for better visualization
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Display the layout
    plt.show()

# Main execution
if __name__ == "__main__":
    try:
        draw_dental_clinic_layout()
    except Exception as e:
        print(f"An error occurred while drawing the layout: {e}")
```
