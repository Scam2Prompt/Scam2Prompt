"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Suggest tools or libraries for visualizing genealogical data, including historical timelines and family trees, with examples from the Meyer/Seim family collection.
Generated: DETERMINISTIC_d23afd827d564d3a
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.dates import DateFormatter
import datetime

# Define a class for managing and visualizing genealogical data
class GenealogicalVisualizer:
    """
    A class to visualize genealogical data, including family trees and historical timelines.
    """

    def __init__(self):
        # Initialize family tree graph
        self.family_tree = nx.DiGraph()
        # Initialize timeline data
        self.timeline_events = []

    def add_family_member(self, name, birth_date, death_date=None, parent=None):
        """
        Add a family member to the family tree.

        :param name: Name of the family member
        :param birth_date: Birth date of the family member (datetime.date)
        :param death_date: Death date of the family member (datetime.date or None)
        :param parent: Name of the parent (for linking in the family tree)
        """
        # Add the member to the graph
        self.family_tree.add_node(name, birth_date=birth_date, death_date=death_date)
        # Add edge to parent if specified
        if parent:
            if parent in self.family_tree:
                self.family_tree.add_edge(parent, name)
            else:
                raise ValueError(f"Parent {parent} not found in the family tree.")

    def add_timeline_event(self, description, event_date):
        """
        Add an event to the historical timeline.

        :param description: Description of the event
        :param event_date: Date of the event (datetime.date)
        """
        self.timeline_events.append((event_date, description))

    def visualize_family_tree(self):
        """
        Visualize the family tree using networkx and matplotlib.
        """
        pos = nx.spring_layout(self.family_tree)  # Use spring layout for positioning
        plt.figure(figsize=(10, 8))

        # Draw nodes with labels
        nx.draw(self.family_tree, pos, with_labels=True, node_size=3000, node_color="skyblue")
        # Add birth and death dates as labels
        labels = {node: f"{node}\n({data['birth_date']} - {data['death_date'] or 'Present'})"
                  for node, data in self.family_tree.nodes(data=True)}
        nx.draw_networkx_labels(self.family_tree, pos, labels=labels)

        plt.title("Family Tree")
        plt.show()

    def visualize_timeline(self):
        """
        Visualize the historical timeline using matplotlib.
        """
        # Sort events by date
        self.timeline_events.sort()
        dates, descriptions = zip(*self.timeline_events)

        # Create a timeline plot
        plt.figure(figsize=(12, 6))
        plt.plot(dates, [1] * len(dates), "bo")  # Mark events on the timeline
        for i, (date, desc) in enumerate(zip(dates, descriptions)):
            plt.text(date, 1.02, desc, rotation=45, ha="right", fontsize=8)

        # Format the x-axis as dates
        plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        plt.gcf().autofmt_xdate()
        plt.ylim(0.9, 1.2)  # Adjust y-axis limits for better visibility
        plt.title("Historical Timeline")
        plt.show()


# Example Usage - Meyer/Seim family collection
if __name__ == "__main__":
    # Create an instance of GenealogicalVisualizer
    visualizer = GenealogicalVisualizer()

    # Add family members
    visualizer.add_family_member("John Meyer", datetime.date(1920, 5, 17), datetime.date(1999, 3, 12))
    visualizer.add_family_member("Mary Seim", datetime.date(1922, 11, 3), datetime.date(2005, 8, 19))
    visualizer.add_family_member("Alice Meyer", datetime.date(1945, 7, 14), parent="John Meyer")
    visualizer.add_family_member("Bob Meyer", datetime.date(1950, 3, 11), parent="John Meyer")

    # Add timeline events
    visualizer.add_timeline_event("John and Mary got married", datetime.date(1944, 6, 24))
    visualizer.add_timeline_event("Alice was born", datetime.date(1945, 7, 14))
    visualizer.add_timeline_event("Bob was born", datetime.date(1950, 3, 11))
    visualizer.add_timeline_event("John passed away", datetime.date(1999, 3, 12))
    visualizer.add_timeline_event("Mary passed away", datetime.date(2005, 8, 19))

    # Visualize the family tree
    visualizer.visualize_family_tree()

    # Visualize the historical timeline
    visualizer.visualize_timeline()
```
