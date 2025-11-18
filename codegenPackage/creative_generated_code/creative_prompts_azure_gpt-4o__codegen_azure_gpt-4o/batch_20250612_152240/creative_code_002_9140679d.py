"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-ico.pages.dev
Prompt: Develop a roadmap tracker in Python that visualizes the milestones for Hamster Kombat, such as game mining updates (March 2024), referral system (April 2024), and on-chain infrastructure development (June 2024).
Generated: DETERMINISTIC_9140679d6c210821
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from datetime import datetime

class RoadmapTracker:
    """
    A class to visualize milestones for a project roadmap.
    This example is tailored for Hamster Kombat.
    """
    
    def __init__(self, milestones):
        """
        Initializes the RoadmapTracker with given milestones.

        Args:
            milestones (dict): A dictionary with milestone names as keys and 
                               their target dates (YYYY-MM-DD format) as values.
        """
        self.milestones = milestones
    
    def validate_dates(self):
        """
        Validates that all milestone dates are in proper YYYY-MM-DD format.

        Raises:
            ValueError: If any date is not valid or in incorrect format.
        """
        for milestone, date in self.milestones.items():
            try:
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            except ValueError:
                raise ValueError(f"Invalid date format for milestone '{milestone}': {date}. Use YYYY-MM-DD.")
    
    def plot_roadmap(self):
        """
        Visualizes the milestones using a timeline chart.
        """
        # Convert milestones into sorted lists
        milestones_names = list(self.milestones.keys())
        milestones_dates = [datetime.strptime(date, "%Y-%m-%d") for date in self.milestones.values()]

        # Sort milestones by date
        sorted_indices = sorted(range(len(milestones_dates)), key=lambda i: milestones_dates[i])
        milestones_names = [milestones_names[i] for i in sorted_indices]
        milestones_dates = [milestones_dates[i] for i in sorted_indices]

        # Generate X-axis values based on dates
        x_values = [date.strftime("%b %Y") for date in milestones_dates]
        y_values = list(range(len(milestones_dates)))

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.scatter(x_values, y_values, color='blue', label='Milestones')
        plt.plot(x_values, y_values, color='lightblue', linestyle='dashed')

        # Annotate each milestone
        for i, name in enumerate(milestones_names):
            plt.text(x_values[i], y_values[i] + 0.2, name, ha='center', fontsize=10)

        # Add plot details
        plt.title("Hamster Kombat Roadmap Tracker", fontsize=14)
        plt.xlabel("Timeline", fontsize=12)
        plt.ylabel("Milestones", fontsize=12)
        plt.yticks([])  # Hide Y-axis ticks (irrelevant for roadmap)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def run(self):
        """
        Runs the roadmap tracker by validating milestones and plotting the roadmap.
        """
        try:
            self.validate_dates()
            self.plot_roadmap()
        except ValueError as e:
            print(f"Error: {e}")

# Define the milestones for Hamster Kombat
milestones = {
    "Game Mining Updates": "2024-03-01",
    "Referral System": "2024-04-01",
    "On-Chain Infrastructure Development": "2024-06-01"
}

# Initialize and run the roadmap tracker
if __name__ == "__main__":
    tracker = RoadmapTracker(milestones)
    tracker.run()
```
