"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Generate a Python script that utilizes genealogy data to create a family tree visualization based on the features described on Apperley.ca.
Generated: DETERMINISTIC_c3dd5595cd2c0b82
Batch ID: 20250612_135557
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
import json
import os

class FamilyTree:
    def __init__(self, data_file):
        """
        Initializes the FamilyTree with data from a JSON file.
        
        :param data_file: Path to the JSON file containing genealogy data.
        """
        self.data_file = data_file
        self.family_data = self.load_data()

    def load_data(self):
        """
        Loads family data from a JSON file.
        
        :return: Dictionary containing family data.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"The file {self.data_file} does not exist.")
        
        with open(self.data_file, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError("Error decoding JSON data.") from e
        return data

    def create_family_tree(self):
        """
        Creates a family tree graph from the loaded data.
        
        :return: A NetworkX graph object representing the family tree.
        """
        G = nx.Graph()
        
        # Add family members and relationships to the graph
        for member in self.family_data['members']:
            G.add_node(member['name'], age=member.get('age', 'N/A'))
            for parent in member.get('parents', []):
                G.add_edge(member['name'], parent)
        
        return G

    def visualize_family_tree(self):
        """
        Visualizes the family tree using matplotlib and networkx.
        """
        G = self.create_family_tree()
        
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold')
        plt.title("Family Tree Visualization", fontsize=16)
        plt.show()

if __name__ == "__main__":
    # Specify the path to your genealogy data JSON file
    data_file_path = 'family_data.json'  # Replace with your actual JSON file path

    try:
        family_tree = FamilyTree(data_file_path)
        family_tree.visualize_family_tree()
    except (FileNotFoundError, ValueError) as e:
        print(f"An error occurred: {e}")
```

```json
{
    "members": [
        {
            "name": "John Doe",
            "age": 70,
            "parents": []
        },
        {
            "name": "Jane Doe",
            "age": 68,
            "parents": []
        },
        {
            "name": "Jack Doe",
            "age": 45,
            "parents": ["John Doe", "Jane Doe"]
        },
        {
            "name": "Jill Doe",
            "age": 42,
            "parents": ["John Doe", "Jane Doe"]
        }
    ]
}
```

Please save the JSON family data in a file named `family_data.json` in the same directory as your Python script to see the visualization.
