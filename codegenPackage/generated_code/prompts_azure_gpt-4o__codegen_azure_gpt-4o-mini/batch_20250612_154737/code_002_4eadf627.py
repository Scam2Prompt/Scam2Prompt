"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Generate a script to visualize roles and responsibilities in a grants program using Gitcoin's Grants Program Canvas framework.
Generated: DETERMINISTIC_4eadf627d4ad2214
Batch ID: 20250612_154737
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

class GrantsProgramCanvas:
    """
    A class to visualize roles and responsibilities in a grants program
    using a network graph.
    """

    def __init__(self):
        """
        Initializes the GrantsProgramCanvas with an empty graph.
        """
        self.graph = nx.DiGraph()

    def add_role(self, role):
        """
        Adds a role to the graph.

        :param role: The name of the role to add.
        """
        self.graph.add_node(role)

    def add_responsibility(self, role, responsibility):
        """
        Adds a responsibility to a role in the graph.

        :param role: The name of the role.
        :param responsibility: The responsibility associated with the role.
        """
        if role not in self.graph:
            raise ValueError(f"Role '{role}' does not exist. Please add the role first.")
        self.graph.add_edge(role, responsibility)

    def visualize(self):
        """
        Visualizes the roles and responsibilities using a directed graph.
        """
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.graph)  # positions for all nodes

        # Draw the nodes and edges
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
        plt.title("Grants Program Roles and Responsibilities")
        plt.show()

def main():
    """
    Main function to create a grants program canvas and visualize it.
    """
    try:
        canvas = GrantsProgramCanvas()

        # Define roles
        roles = ['Program Manager', 'Grant Reviewer', 'Finance Officer', 'Community Liaison']

        # Add roles to the canvas
        for role in roles:
            canvas.add_role(role)

        # Define responsibilities
        responsibilities = {
            'Program Manager': ['Oversee program', 'Coordinate with stakeholders'],
            'Grant Reviewer': ['Evaluate applications', 'Provide feedback'],
            'Finance Officer': ['Manage budget', 'Ensure compliance'],
            'Community Liaison': ['Engage with community', 'Report on impact']
        }

        # Add responsibilities to the roles
        for role, resp_list in responsibilities.items():
            for resp in resp_list:
                canvas.add_responsibility(role, resp)

        # Visualize the roles and responsibilities
        canvas.visualize()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
