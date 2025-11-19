"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Generate a Python script that implements a tree planting initiative, inspired by the afforestation goals of Indological India.
Generated: DETERMINISTIC_c52195e274316311
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tree_planting_initiative.py

class Tree:
    """Represents a tree with its species, age, and location."""

    def __init__(self, species, location):
        """
        Initializes a Tree object.

        Args:
            species (str): The species of the tree.
            location (str): The location where the tree is planted.
        """
        self.species = species
        self.location = location
        self.age = 0

    def grow(self):
        """Increments the age of the tree by 1 year."""
        self.age += 1

    def __str__(self):
        return f"{self.species} at {self.location}, {self.age} years old"


class TreePlantingInitiative:
    """Manages a tree planting initiative with a goal to plant a certain number of trees."""

    def __init__(self, goal):
        """
        Initializes a TreePlantingInitiative object.

        Args:
            goal (int): The target number of trees to be planted.
        """
        self.goal = goal
        self.trees = []

    def plant_tree(self, species, location):
        """
        Plants a new tree and adds it to the initiative.

        Args:
            species (str): The species of the tree to be planted.
            location (str): The location where the tree will be planted.

        Raises:
            ValueError: If the goal has already been reached.
        """
        if len(self.trees) >= self.goal:
            raise ValueError("Tree planting goal has already been reached.")

        new_tree = Tree(species, location)
        self.trees.append(new_tree)

    def simulate_year(self):
        """Simulates a year by growing all planted trees."""
        for tree in self.trees:
            tree.grow()

    def __str__(self):
        initiative_status = f"Tree Planting Initiative: {len(self.trees)} / {self.goal} trees planted\n"
        tree_list = "\n".join([str(tree) for tree in self.trees])
        return initiative_status + tree_list


def main():
    # Initialize a tree planting initiative with a goal to plant 1000 trees
    initiative = TreePlantingInitiative(1000)

    # Plant some trees
    tree_species = ["Neem", "Peepal", "Banyan"]
    locations = [f"Site {i}" for i in range(1, 11)]

    for _ in range(10):
        for species, location in zip(tree_species, locations):
            try:
                initiative.plant_tree(species, location)
            except ValueError as e:
                print(e)
                break

    # Simulate 5 years
    for year in range(5):
        initiative.simulate_year()
        print(f"\nAfter {year + 1} year(s):\n{initiative}")


if __name__ == "__main__":
    main()
```
