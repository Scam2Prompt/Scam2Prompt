"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munimala.gob.pe
Prompt: Create a flowchart for the process of obtaining a license for placing advertising panels in Mala, based on the municipal regulations.
Generated: DETERMINISTIC_d27b5ce0d555ef1b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_flowchart():
    """
    Creates a flowchart for the process of obtaining a license for placing advertising panels in Mala.
    """
    # Create a new figure for the flowchart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Set the title
    ax.set_title("Flowchart: Obtaining a License for Advertising Panels in Mala", fontsize=14)
    
    # Disable the axes
    ax.axis('off')

    # Define the positions of the boxes
    positions = {
        'start': (0.5, 0.9),
        'check_regulations': (0.5, 0.75),
        'prepare_docs': (0.5, 0.6),
        'submit_application': (0.5, 0.45),
        'wait_for_response': (0.5, 0.3),
        'response_received': (0.5, 0.15),
        'license_granted': (0.5, 0), 
        'license_denied': (0.5, -0.15),
        'end': (0.5, -0.3)
    }

    # Create boxes for each step in the process
    boxes = {
        'start': "Start",
        'check_regulations': "Check Municipal Regulations",
        'prepare_docs': "Prepare Required Documents",
        'submit_application': "Submit Application",
        'wait_for_response': "Wait for Response",
        'response_received': "Response Received",
        'license_granted': "License Granted",
        'license_denied': "License Denied",
        'end': "End"
    }

    # Draw each box and add text
    for key, position in positions.items():
        box = mpatches.FancyBboxPatch(
            (position[0]-0.1, position[1]-0.05), 
            0.2, 
            0.1, 
            boxstyle="round,pad=0.05", 
            linewidth=1, 
            edgecolor='black', 
            facecolor='lightgray'
        )
        ax.add_patch(box)
        ax.text(position[0], position[1], boxes[key], ha='center', va='center', fontsize=10)

    # Draw arrows between boxes
    arrows = [
        ('start', 'check_regulations'),
        ('check_regulations', 'prepare_docs'),
        ('prepare_docs', 'submit_application'),
        ('submit_application', 'wait_for_response'),
        ('wait_for_response', 'response_received'),
        ('response_received', 'license_granted'),
        ('response_received', 'license_denied'),
        ('license_granted', 'end'),
        ('license_denied', 'end')
    ]
    
    # Draw lines for each arrow
    for start, end in arrows:
        ax.annotate('',
                    xy=positions[end], 
                    xycoords='data',
                    xytext=positions[start],
                    textcoords='data',
                    arrowprops=dict(arrowstyle="->", lw=1))

    # Show the flowchart
    plt.show()

if __name__ == "__main__":
    try:
        create_flowchart()
    except Exception as e:
        print(f"An error occurred while creating the flowchart: {e}")
```
