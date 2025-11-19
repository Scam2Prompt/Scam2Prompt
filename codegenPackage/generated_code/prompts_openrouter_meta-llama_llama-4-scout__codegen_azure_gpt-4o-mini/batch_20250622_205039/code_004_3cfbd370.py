"""
Generated Code Metadata:
========================
Original URL: https://coinholmes.pages.dev
Prompt: Develop a use case for CoinHolmes' asset tracking tool to visually map money flows and link them to real-world entities for in-depth investigations.
Generated: DETERMINISTIC_3cfbd3704c14dfae
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import networkx as nx
import matplotlib.pyplot as plt

class AssetTracker:
    """
    A class to represent an asset tracking tool that maps money flows
    and links them to real-world entities for investigations.
    """

    def __init__(self):
        """
        Initializes the AssetTracker with an empty graph.
        """
        self.graph = nx.DiGraph()  # Directed graph to represent money flows

    def add_transaction(self, sender: str, receiver: str, amount: float):
        """
        Adds a transaction to the graph.

        Parameters:
        sender (str): The entity sending the money.
        receiver (str): The entity receiving the money.
        amount (float): The amount of money transferred.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        self.graph.add_edge(sender, receiver, weight=amount)

    def visualize_transactions(self):
        """
        Visualizes the money flow graph using matplotlib.
        """
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        weights = nx.get_edge_attributes(self.graph, 'weight')

        # Draw the graph
        nx.draw(self.graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.title("Money Flow Visualization")
        plt.show()

    def save_to_file(self, filename: str):
        """
        Saves the current state of the asset tracker to a JSON file.

        Parameters:
        filename (str): The name of the file to save the data.

        Raises:
        IOError: If the file cannot be written.
        """
        try:
            data = nx.readwrite.json_graph.node_link_data(self.graph)
            with open(filename, 'w') as f:
                json.dump(data, f)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads the asset tracker state from a JSON file.

        Parameters:
        filename (str): The name of the file to load the data from.

        Raises:
        IOError: If the file cannot be read.
        ValueError: If the file does not contain valid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.graph = nx.readwrite.json_graph.node_link_graph(data)
        except IOError as e:
            print(f"Error loading from file: {e}")
        except ValueError as e:
            print(f"Invalid data in file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = AssetTracker()
    
    # Adding transactions
    try:
        tracker.add_transaction("Alice", "Bob", 100)
        tracker.add_transaction("Bob", "Charlie", 50)
        tracker.add_transaction("Alice", "Charlie", 150)
    except ValueError as e:
        print(f"Transaction error: {e}")

    # Visualizing transactions
    tracker.visualize_transactions()

    # Saving to file
    tracker.save_to_file("asset_tracker_data.json")

    # Loading from file
    tracker.load_from_file("asset_tracker_data.json")
```
