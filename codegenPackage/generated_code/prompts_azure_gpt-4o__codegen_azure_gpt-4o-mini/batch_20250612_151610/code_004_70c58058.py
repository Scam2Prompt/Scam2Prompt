"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Suggest a method to visualize family trees using data exported from "Family Historian" software and display it on a genealogy website.
Generated: DETERMINISTIC_70c58058055e736c
Batch ID: 20250612_151610
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

class FamilyTreeVisualizer:
    """
    A class to visualize family trees using data exported from Family Historian software.
    """

    def __init__(self, data_file):
        """
        Initializes the FamilyTreeVisualizer with the given data file.

        :param data_file: Path to the JSON file containing family data.
        """
        self.data_file = data_file
        self.family_data = self.load_data()

    def load_data(self):
        """
        Loads family data from a JSON file.

        :return: A dictionary containing family data.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the data file.")

    def build_family_tree(self):
        """
        Builds a directed graph representing the family tree.

        :return: A NetworkX DiGraph representing the family relationships.
        """
        family_tree = nx.DiGraph()
        for person in self.family_data.get('individuals', []):
            person_id = person['id']
            family_tree.add_node(person_id, name=person['name'])
            for parent in person.get('parents', []):
                family_tree.add_edge(parent, person_id)
        return family_tree

    def visualize_tree(self):
        """
        Visualizes the family tree using Matplotlib.

        :return: None
        """
        family_tree = self.build_family_tree()
        pos = nx.spring_layout(family_tree)  # positions for all nodes
        nx.draw(family_tree, pos, with_labels=True, labels=nx.get_node_attributes(family_tree, 'name'))
        plt.title("Family Tree Visualization")
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        visualizer = FamilyTreeVisualizer('family_data.json')
        visualizer.visualize_tree()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to have the required libraries installed:
```bash
pip install networkx matplotlib
```

This code assumes that the JSON data structure from Family Historian contains an "individuals" list, where each individual has an "id", "name", and a list of "parents". Adjust the data structure as necessary based on your actual data format.
