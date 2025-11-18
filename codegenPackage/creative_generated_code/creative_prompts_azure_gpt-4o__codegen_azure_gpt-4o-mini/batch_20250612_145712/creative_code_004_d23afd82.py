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
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

class GenealogyVisualizer:
    def __init__(self, data):
        """
        Initialize the GenealogyVisualizer with genealogical data.
        
        Args:
            data (pd.DataFrame): A DataFrame containing genealogical information.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        
        self.data = data
        self.family_tree = None

    def create_family_tree(self):
        """
        Create a family tree using the data provided.
        The DataFrame should have columns: 'Child', 'Parent'.
        """
        self.family_tree = nx.DiGraph()
        
        for _, row in self.data.iterrows():
            child = row['Child']
            parent = row['Parent']
            self.family_tree.add_edge(parent, child)

    def plot_family_tree(self):
        """
        Plot the family tree using matplotlib and networkx.
        """
        if self.family_tree is None:
            raise RuntimeError("Family tree has not been created. Call create_family_tree() first.")

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.family_tree)
        nx.draw(self.family_tree, pos, with_labels=True, arrows=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.title("Family Tree")
        plt.show()

    def create_historical_timeline(self):
        """
        Create a historical timeline of events based on the data.
        The DataFrame should have columns: 'Event', 'Date'.
        """
        events = self.data[['Event', 'Date']].dropna()
        if events.empty:
            raise ValueError("No events found for the timeline.")
        
        events['Date'] = pd.to_datetime(events['Date'])
        events = events.sort_values(by='Date')

        plt.figure(figsize=(12, 6))
        plt.plot(events['Date'], range(len(events)), marker='o')
        plt.yticks(range(len(events)), events['Event'])
        plt.title("Historical Timeline")
        plt.xlabel("Date")
        plt.ylabel("Events")
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Example data for the Meyer/Seim family collection
    data = {
        'Child': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Parent': ['John', 'John', 'Alice', 'Alice'],
        'Event': ['Birth of John', 'Birth of Alice', 'Birth of Bob', 'Birth of Charlie'],
        'Date': ['1980-01-01', '2000-05-15', '2002-07-20', '2004-09-30']
    }

    df = pd.DataFrame(data)

    try:
        visualizer = GenealogyVisualizer(df)
        visualizer.create_family_tree()
        visualizer.plot_family_tree()
        visualizer.create_historical_timeline()
    except Exception as e:
        print(f"An error occurred: {e}")
```
