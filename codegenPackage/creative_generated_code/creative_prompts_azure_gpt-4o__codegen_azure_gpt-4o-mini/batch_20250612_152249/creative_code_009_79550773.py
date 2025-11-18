"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdefi-thedogeverse.pages.dev
Prompt: Create a roadmap visualization tool for the Dogeverse project that dynamically updates based on the phases described (Big Bang, Development, Awareness, Expansion, Cosmic Travel). Include milestones such as DEX/CEX listings and community incentives.
Generated: DETERMINISTIC_795507739e6bbe32
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


class RoadmapVisualizer:
    """
    A class to visualize the roadmap for the Dogeverse project.
    """

    def __init__(self, phases_data):
        """
        Initializes the RoadmapVisualizer with the provided phases data.

        :param phases_data: A dictionary containing the phases and their respective milestones.
        """
        self.phases_data = phases_data

    def draw_roadmap(self):
        """
        Draws the roadmap visualization.
        """
        try:
            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(12, 8))

            # Define colors for each phase
            phase_colors = {
                "Big Bang": 'gold',
                "Development": 'lightblue',
                "Awareness": 'lightgreen',
                "Expansion": 'lightcoral',
                "Cosmic Travel": 'violet'
            }

            # Define positions for each phase
            y_pos = np.arange(len(self.phases_data))

            # Create a bar for each phase with milestones
            for i, (phase, milestones) in enumerate(self.phases_data.items()):
                ax.barh(i, len(milestones), color=phase_colors.get(phase, 'gray'), edgecolor='black')
                for j, milestone in enumerate(milestones):
                    ax.text(len(milestones) - j - 1, i, milestone, ha='center', va='center', color='black')

            # Set y-ticks and labels
            ax.set_yticks(y_pos)
            ax.set_yticklabels(self.phases_data.keys())
            ax.invert_yaxis()  # Invert y-axis to have the first phase at the top

            # Set title and labels
            ax.set_title('Dogeverse Project Roadmap', fontsize=16)
            ax.set_xlabel('Milestones', fontsize=12)
            ax.set_ylabel('Phases', fontsize=12)

            # Show the grid
            ax.grid(axis='x', linestyle='--', alpha=0.7)

            # Show the plot
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Error during roadmap visualization: {e}")


def load_phases_from_json(file_path):
    """
    Loads the phases data from a JSON file.

    :param file_path: The path to the JSON file.
    :return: Dictionary containing phases and milestones.
    """
    try:
        with open(file_path, 'r') as file:
            phases_data = json.load(file)
            return phases_data
    except json.JSONDecodeError:
        print("Error: The JSON file is not properly formatted.")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the JSON file: {e}")
    return {}


if __name__ == "__main__":
    # Example of phases data structure
    phases = {
        "Big Bang": ["Initial Concept", "White Paper Release"],
        "Development": ["Prototype Development", "Alpha Testing", "Beta Testing"],
        "Awareness": ["Community Building", "Marketing Campaign"],
        "Expansion": ["DEX Listing", "CEX Listing", "Partnerships"],
        "Cosmic Travel": ["Global Expansion", "Future Innovations"]
    }

    # Uncomment the following line to load from a JSON file instead
    # phases = load_phases_from_json('dogeverse_phases.json')

    # Create an instance of RoadmapVisualizer
    roadmap_visualizer = RoadmapVisualizer(phases)

    # Draw the roadmap
    roadmap_visualizer.draw_roadmap()
```
