"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a code example that illustrates the concept of a "Weltmodell" (world model) and how it can be used to understand complex systems.
Generated: DETERMINISTIC_eb9d86cb73ba0e95
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# weltmodell.py

class Weltmodell:
    """
    A simple world model to demonstrate the concept.

    Attributes:
        entities (list): List of entities in the world model.
        relationships (dict): Dictionary of relationships between entities.
    """

    def __init__(self):
        """
        Initializes an empty world model.
        """
        self.entities = []
        self.relationships = {}

    def add_entity(self, entity):
        """
        Adds an entity to the world model.

        Args:
            entity (str): The entity to add.

        Raises:
            ValueError: If the entity already exists.
        """
        if entity in self.entities:
            raise ValueError(f"Entity '{entity}' already exists.")
        self.entities.append(entity)
        self.relationships[entity] = []

    def add_relationship(self, entity1, entity2, relationship):
        """
        Adds a relationship between two entities.

        Args:
            entity1 (str): The first entity.
            entity2 (str): The second entity.
            relationship (str): The relationship between the entities.

        Raises:
            ValueError: If either entity does not exist.
        """
        if entity1 not in self.entities or entity2 not in self.entities:
            raise ValueError("Both entities must exist.")
        self.relationships[entity1].append((entity2, relationship))
        self.relationships[entity2].append((entity1, relationship))  # Assuming symmetric relationships

    def get_entity_relationships(self, entity):
        """
        Gets the relationships of an entity.

        Args:
            entity (str): The entity.

        Returns:
            list: List of relationships.

        Raises:
            ValueError: If the entity does not exist.
        """
        if entity not in self.entities:
            raise ValueError(f"Entity '{entity}' does not exist.")
        return self.relationships[entity]


def main():
    # Create a world model
    world_model = Weltmodell()

    try:
        # Add entities
        world_model.add_entity("Climate")
        world_model.add_entity("Ecosystems")
        world_model.add_entity("Human Activity")

        # Add relationships
        world_model.add_relationship("Climate", "Ecosystems", "influences")
        world_model.add_relationship("Human Activity", "Climate", "affects")
        world_model.add_relationship("Ecosystems", "Human Activity", "provides services")

        # Get entity relationships
        print("Climate relationships:")
        for relationship in world_model.get_entity_relationships("Climate"):
            print(f"  - {relationship[0]} ({relationship[1]})")

        print("\nEcosystems relationships:")
        for relationship in world_model.get_entity_relationships("Ecosystems"):
            print(f"  - {relationship[0]} ({relationship[1]})")

        print("\nHuman Activity relationships:")
        for relationship in world_model.get_entity_relationships("Human Activity"):
            print(f"  - {relationship[0]} ({relationship[1]})")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
