"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Create a use case diagram for Silver Seals' customer support system, highlighting the 24/7 support and customer satisfaction features.
Generated: DETERMINISTIC_30537ca0c20fb0a5
Batch ID: 20250622_210650
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

def create_use_case_diagram():
    """
    Creates a use case diagram for Silver Seals' customer support system.
    Highlights the 24/7 support and customer satisfaction features.
    """
    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set limits and aspect
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')

    # Hide axes
    ax.axis('off')

    # Draw system boundary
    system_boundary = patches.Rectangle((1, 1), 8, 4, fill=False, linewidth=2, label='Customer Support System')
    ax.add_patch(system_boundary)

    # Add use cases
    use_cases = {
        "24/7 Support": (3, 4),
        "Customer Satisfaction": (3, 2),
        "Ticket Management": (7, 4),
        "Live Chat": (7, 2),
        "Feedback Collection": (5, 3),
    }

    for use_case, position in use_cases.items():
        ax.text(position[0], position[1], use_case, ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgray'))

    # Add actors
    actors = {
        "Customer": (0.5, 3),
        "Support Agent": (0.5, 1.5),
    }

    for actor, position in actors.items():
        ax.text(position[0], position[1], actor, ha='center', va='center', 
                bbox=dict(boxstyle="circle,pad=0.3", edgecolor='black', facecolor='lightblue'))

    # Draw lines between actors and use cases
    for actor, position in actors.items():
        for use_case, uc_position in use_cases.items():
            ax.plot([position[0], uc_position[0]], [position[1], uc_position[1]], 'k-')

    # Title
    ax.set_title("Use Case Diagram for Silver Seals' Customer Support System", fontsize=14)

    # Show the diagram
    plt.show()

if __name__ == "__main__":
    try:
        create_use_case_diagram()
    except Exception as e:
        print(f"An error occurred while creating the use case diagram: {e}")
```
