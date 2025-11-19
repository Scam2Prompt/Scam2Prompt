"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Generate a Python script that utilizes genealogy data to create a family tree visualization based on the features described on Apperley.ca.
Generated: DETERMINISTIC_c3dd5595cd2c0b82
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

class FamilyTree:
    def __init__(self, data):
        """
        Initializes the FamilyTree with genealogy data.

        :param data: A pandas DataFrame containing genealogy data with columns ['Person', 'Parent']
        """
        self.data = data
        self.graph = nx.DiGraph()  # Directed graph to represent family relationships

    def build_tree(self):
        """
        Builds the family tree graph from the provided data.
        """
        for _, row in self.data.iterrows():
            person = row['Person']
            parent = row['Parent']
            if pd.notna(parent):  # Check if parent is not NaN
                self.graph.add_edge(parent, person)

    def draw_tree(self):
        """
        Draws the family tree using matplotlib and networkx.
        """
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)  # Positioning the nodes
        nx.draw(self.graph, pos, with_labels=True, arrows=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        plt.title("Family Tree Visualization")
        plt.show()

def load_data(file_path):
    """
    Loads genealogy data from a CSV file.

    :param file_path: Path to the CSV file containing genealogy data
    :return: A pandas DataFrame containing the data
    """
    try:
        data = pd.read_csv(file_path)
        if 'Person' not in data.columns or 'Parent' not in data.columns:
            raise ValueError("CSV must contain 'Person' and 'Parent' columns.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        raise

def main():
    """
    Main function to execute the family tree visualization.
    """
    file_path = 'genealogy_data.csv'  # Path to the genealogy data CSV file
    try:
        data = load_data(file_path)
        family_tree = FamilyTree(data)
        family_tree.build_tree()
        family_tree.draw_tree()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `genealogy_data.csv` with the appropriate structure (columns 'Person' and 'Parent') in the same directory as this script for it to run successfully.
