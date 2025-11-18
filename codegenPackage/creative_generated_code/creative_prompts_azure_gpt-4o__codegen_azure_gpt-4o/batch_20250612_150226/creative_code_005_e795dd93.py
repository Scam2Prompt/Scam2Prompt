"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a Python script to visualize the faction distribution (Masterminds, Warriors, Renegades) on the R-Planet map using matplotlib.
Generated: DETERMINISTIC_e795dd93e1c2fe54
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_faction_distribution():
    """
    Visualizes the faction distribution on the R-Planet map.

    Factions:
      - Masterminds: Represented in blue
      - Warriors: Represented in red
      - Renegades: Represented in green
    """
    try:
        # Define the faction names and their respective counts (example data).
        factions = ['Masterminds', 'Warriors', 'Renegades']
        counts = [120, 200, 80]  # Example numbers for each faction

        # Validate that the data is consistent
        if len(factions) != len(counts):
            raise ValueError("Mismatch between factions and counts data length.")

        # Create a bar chart for faction distribution
        colors = ['blue', 'red', 'green']  # Colors representing each faction
        x_positions = np.arange(len(factions))  # X-axis positions for bars

        plt.figure(figsize=(8, 6))  # Set the size of the plot
        plt.bar(x_positions, counts, color=colors, tick_label=factions)

        # Add labels, a title, and grid for better visualization
        plt.xlabel("Factions", fontsize=12)
        plt.ylabel("Number of Units", fontsize=12)
        plt.title("Faction Distribution on R-Planet Map", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Horizontal grid lines for clarity

        # Save the plot as an image and display it
        plt.tight_layout()
        plt.savefig("faction_distribution.png")  # Save as an image file
        plt.show()

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred while visualizing faction distribution: {e}")

# Entry point for the script
if __name__ == "__main__":
    visualize_faction_distribution()
```
