"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Develop a roadmap visualization tool in Python that tracks the progress of an AI and NFT project, similar to the phases outlined in the Cyber Lama roadmap.
Generated: DETERMINISTIC_48e75920c293e68b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd

class RoadmapVisualizer:
    """
    A class to visualize the roadmap of an AI and NFT project.
    """

    def __init__(self):
        """
        Initializes the RoadmapVisualizer with an empty dataframe.
        """
        self.phases = pd.DataFrame(columns=['Phase', 'Start Date', 'End Date', 'Progress'])

    def add_phase(self, phase, start_date, end_date, progress=0):
        """
        Adds a new phase to the roadmap.

        Parameters:
            phase (str): The name of the phase.
            start_date (str): The start date of the phase (YYYY-MM-DD).
            end_date (str): The end date of the phase (YYYY-MM-DD).
            progress (int): The completion percentage of the phase (0-100).
        """
        # Validate progress input
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")

        # Append the new phase to the dataframe
        new_phase = pd.DataFrame([[phase, start_date, end_date, progress]],
                                  columns=self.phases.columns)
        self.phases = pd.concat([self.phases, new_phase], ignore_index=True)

    def visualize(self):
        """
        Creates a Gantt chart to visualize the roadmap phases and their progress.
        """
        # Validate that there are phases to display
        if self.phases.empty:
            raise ValueError("No phases to visualize. Please add phases first.")

        # Convert dates to datetime for proper plotting
        self.phases['Start Date'] = pd.to_datetime(self.phases['Start Date'])
        self.phases['End Date'] = pd.to_datetime(self.phases['End Date'])

        # Prepare the figure for the Gantt chart
        plt.figure(figsize=(12, 7))

        # Create a bar for each phase
        for idx, row in self.phases.iterrows():
            plt.barh(row['Phase'], (row['End Date'] - row['Start Date']).days,
                     left=(row['Start Date'] - self.phases['Start Date'].min()).days,
                     color=self._get_color_based_on_progress(row['Progress']))

            # Add progress label
            plt.text((row['Start Date'] - self.phases['Start Date'].min()).days + 
                      (row['End Date'] - row['Start Date']).days / 2,
                      idx, f"{row['Progress']}%", 
                      va='center', ha='center', fontsize=10, color='white')

        # Formatting the plot
        plt.title('Project Roadmap Visualization', fontsize=16)
        plt.xlabel('Time (Days)', fontsize=12)
        plt.ylabel('Phases', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='x')
        plt.tight_layout()

        # Show the plot
        plt.show()

    def _get_color_based_on_progress(self, progress):
        """
        Returns a color based on the progress of the phase.

        Parameters:
            progress (int): The completion percentage of the phase (0-100).

        Returns:
            str: Color code for the phase.
        """
        if progress == 100:
            return 'green'
        elif progress >= 50:
            return 'orange'
        else:
            return 'red'


if __name__ == "__main__":
    # Example usage of the RoadmapVisualizer
    try:
        roadmap = RoadmapVisualizer()
        roadmap.add_phase('Phase 1: Concept Development', '2023-01-01', '2023-03-01', 100)
        roadmap.add_phase('Phase 2: Prototype Development', '2023-03-02', '2023-05-01', 70)
        roadmap.add_phase('Phase 3: Alpha Release', '2023-05-02', '2023-07-01', 30)
        roadmap.add_phase('Phase 4: Public Launch', '2023-07-02', '2023-09-01', 0)
        
        roadmap.visualize()
    except Exception as e:
        print(f"An error occurred: {e}")
```
