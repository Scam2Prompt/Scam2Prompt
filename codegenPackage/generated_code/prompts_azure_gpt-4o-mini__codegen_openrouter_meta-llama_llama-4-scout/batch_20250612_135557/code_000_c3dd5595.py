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
import networkx as nx
import matplotlib.pyplot as plt

class Person:
    """Represents an individual in the family tree."""
    
    def __init__(self, name, birth=None, death=None):
        """
        Initializes a Person object.

        Args:
            name (str): The person's name.
            birth (str, optional): The person's birth date. Defaults to None.
            death (str, optional): The person's death date. Defaults to None.
        """
        self.name = name
        self.birth = birth
        self.death = death
        self.spouse = None
        self.children = []

    def add_spouse(self, spouse):
        """Adds a spouse to the person."""
        self.spouse = spouse

    def add_child(self, child):
        """Adds a child to the person."""
        self.children.append(child)


class FamilyTree:
    """Represents a family tree."""
    
    def __init__(self):
        """Initializes a FamilyTree object."""
        self.people = {}

    def add_person(self, name, birth=None, death=None):
        """
        Adds a person to the family tree.

        Args:
            name (str): The person's name.
            birth (str, optional): The person's birth date. Defaults to None.
            death (str, optional): The person's death date. Defaults to None.

        Returns:
            Person: The added person.
        """
        if name not in self.people:
            self.people[name] = Person(name, birth, death)
        return self.people[name]

    def add_relationship(self, parent1, parent2, child):
        """
        Adds a relationship between two parents and a child.

        Args:
            parent1 (str): The first parent's name.
            parent2 (str): The second parent's name.
            child (str): The child's name.
        """
        parent1_obj = self.add_person(parent1)
        parent2_obj = self.add_person(parent2)
        child_obj = self.add_person(child)

        parent1_obj.add_child(child_obj)
        parent2_obj.add_child(child_obj)

        if not parent1_obj.spouse:
            parent1_obj.add_spouse(parent2_obj)
        if not parent2_obj.spouse:
            parent2_obj.add_spouse(parent1_obj)

    def visualize(self):
        """Visualizes the family tree using NetworkX and Matplotlib."""
        G = nx.DiGraph()

        for person in self.people.values():
            G.add_node(person.name)
            if person.spouse:
                G.add_edge(person.name, person.spouse.name, type="spouse")
            for child in person.children:
                G.add_edge(person.name, child.name, type="parent")

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='gray')
        plt.show()


def main():
    try:
        tree = FamilyTree()

        # Example usage:
        tree.add_relationship("John", "Jane", "Alice")
        tree.add_relationship("John", "Jane", "Bob")
        tree.add_person("John", "1990-01-01")
        tree.add_person("Jane", "1992-01-01")
        tree.add_person("Alice", "2010-01-01")
        tree.add_person("Bob", "2012-01-01")

        tree.visualize()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
