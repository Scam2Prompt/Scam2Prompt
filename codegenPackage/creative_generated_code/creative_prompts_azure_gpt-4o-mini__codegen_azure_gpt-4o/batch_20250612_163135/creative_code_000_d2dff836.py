"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.lu
Prompt: Generate a wiring diagram for installing an LED dimmer switch, including key components and connections.
Generated: DETERMINISTIC_d2dff8363bb83642
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code to generate a wiring diagram for installing an LED dimmer switch. The diagram is created as an image file using the `matplotlib` library.

```python
import matplotlib.pyplot as plt

def generate_wiring_diagram(output_file="wiring_diagram.png"):
    """
    Generates a wiring diagram for installing an LED dimmer switch.
    
    Args:
        output_file (str): Filename for saving the generated diagram image.
    """
    try:
        # Initialize the diagram
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")  # Turn off axes for a cleaner diagram
        
        # Draw components
        # 1. AC Power Source
        ax.text(1, 8, "AC Power Source", fontsize=10, fontweight="bold", color="black")
        ax.plot([1, 2], [8, 6], color="black", linewidth=2, label="Power Line")  # Power wire to dimmer switch

        # 2. Dimmer switch
        ax.text(4, 6, "Dimmer Switch", fontsize=10, fontweight="bold", color="black")
        ax.add_patch(plt.Rectangle((3.8, 5.5), 1.5, 1, edgecolor="black", facecolor="lightgray", label="Dimmer"))
        ax.plot([2, 4], [6, 6], color="black", linewidth=2)  # Wire from power source to dimmer switch

        # 3. LED Light
        ax.text(7, 8, "LED Light", fontsize=10, fontweight="bold", color="black")
        ax.plot([5, 7], [6, 8], color="black", linewidth=2, label="Power to LED Light")  # Power wire to LED

        # Draw ground wire
        ax.text(1, 2, "Ground", fontsize=10, fontweight="bold", color="green")
        ax.plot([1, 7], [2, 2], color="green", linestyle="--", linewidth=2, label="Ground Wire")  # Ground wire across components

        # Connect dimmer switch to ground
        ax.plot([4, 4], [5.5, 2], color="green", linestyle="--", linewidth=1.5)  # Dimmer grounded

        # Legend and labels
        ax.legend(["Power Line", "Ground Wire"], loc="lower left", fontsize=8)
        ax.text(4, 3, "Wiring Diagram: LED Dimmer Switch", fontsize=12, fontweight="bold", ha="center")

        # Save the diagram
        plt.savefig(output_file, dpi=300)
        print(f"Wiring diagram saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the wiring diagram: {e}")

# Call the function to generate the wiring diagram
generate_wiring_diagram()
```
