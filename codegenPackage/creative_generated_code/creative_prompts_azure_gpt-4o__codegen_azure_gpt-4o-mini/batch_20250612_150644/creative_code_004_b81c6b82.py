"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmyevent.com
Prompt: Suggest libraries or tools for creating a timeline visualization of China's major scientific achievements, such as those highlighted on 光明网.
Generated: DETERMINISTIC_b81c6b8258ef9785
Batch ID: 20250612_150644
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
from datetime import datetime

# Define a class for the Timeline Visualization
class TimelineVisualizer:
    def __init__(self):
        """
        Initializes the TimelineVisualizer with an empty DataFrame.
        """
        self.data = pd.DataFrame(columns=["Date", "Event"])

    def add_event(self, date: str, event: str):
        """
        Adds an event to the timeline.

        :param date: The date of the event in 'YYYY-MM-DD' format
        :param event: The description of the event
        """
        try:
            # Convert string date to datetime object
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            # Append the event to the DataFrame
            self.data = self.data.append({"Date": date_obj, "Event": event}, ignore_index=True)
        except ValueError as e:
            print(f"Error adding event: {e}. Please ensure the date is in 'YYYY-MM-DD' format.")

    def plot_timeline(self):
        """
        Plots the timeline of events using Matplotlib.
        """
        if self.data.empty:
            print("No events to display. Please add events before plotting.")
            return
        
        # Sort the DataFrame by Date
        self.data = self.data.sort_values("Date")

        # Create a figure and a set of subplots
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plotting each event
        ax.plot(self.data["Date"], range(len(self.data)), marker="o", linestyle="--", color="b")
        
        # Adding event labels
        for i, event in enumerate(self.data["Event"]):
            ax.text(self.data["Date"].iloc[i], i, event, fontsize=9, ha='right', va='bottom', rotation=45)

        # Formatting the plot
        ax.set_yticks(range(len(self.data)))
        ax.set_yticklabels(self.data["Date"].dt.strftime('%Y-%m-%d'), fontsize=10)
        ax.set_xlabel("Date")
        ax.set_title("Timeline of Major Scientific Achievements in China")
        ax.grid(True)

        # Show plot
        plt.tight_layout()
        plt.show()

# Usage example
if __name__ == "__main__":
    # Create an instance of the TimelineVisualizer
    timeline = TimelineVisualizer()

    # Add events to the timeline (dates and events should be modified as per actual achievements)
    timeline.add_event("1949-10-01", "Establishment of the People's Republic of China")
    timeline.add_event("2000-04-24", "Launch of the first Chinese manned spacecraft, Shenzhou 5")
    timeline.add_event("2016-01-01", "Launch of the Tiangong-2 space laboratory")
    timeline.add_event("2021-05-30", "Mars rover Tianwen-1 successfully lands on Mars")

    # Plot the timeline
    timeline.plot_timeline()
```
