"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a Python script that simulates a world model, incorporating concepts of perception and reality as discussed in the "Das Weltmodell" article on ScienceArtThinking.
Generated: DETERMINISTIC_a696ff3df3b924fa
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulates a world model incorporating concepts of perception and reality.

Inspired by the "Das Weltmodell" article on ScienceArtThinking.
"""

import random

class Entity:
    """Represents an entity in the world model."""
    def __init__(self, name, properties):
        """
        Initializes an entity with a name and properties.

        Args:
            name (str): The name of the entity.
            properties (dict): A dictionary of entity properties.
        """
        self.name = name
        self.properties = properties

    def __str__(self):
        return f"{self.name}: {self.properties}"


class Perception:
    """Represents a perception of an entity in the world model."""
    def __init__(self, entity, observer):
        """
        Initializes a perception of an entity from an observer's perspective.

        Args:
            entity (Entity): The entity being perceived.
            observer (Entity): The observer perceiving the entity.
        """
        self.entity = entity
        self.observer = observer
        self.perceived_properties = self._perceive_properties()

    def _perceive_properties(self):
        """
        Simulates the observer's perception of the entity's properties.

        Returns:
            dict: A dictionary of perceived properties.
        """
        perceived_properties = {}
        for property_name, property_value in self.entity.properties.items():
            # Simulate perception error with 10% chance
            if random.random() < 0.1:
                perceived_properties[property_name] = random.random() * 100
            else:
                perceived_properties[property_name] = property_value
        return perceived_properties

    def __str__(self):
        return f"{self.observer.name}'s perception of {self.entity.name}: {self.perceived_properties}"


class WorldModel:
    """Represents the world model."""
    def __init__(self):
        """
        Initializes the world model with entities.
        """
        self.entities = []

    def add_entity(self, entity):
        """
        Adds an entity to the world model.

        Args:
            entity (Entity): The entity to add.
        """
        self.entities.append(entity)

    def get_entity(self, name):
        """
        Retrieves an entity by name.

        Args:
            name (str): The name of the entity.

        Returns:
            Entity: The entity with the given name, or None if not found.
        """
        for entity in self.entities:
            if entity.name == name:
                return entity
        return None

    def simulate_perception(self, observer, entity_name):
        """
        Simulates an observer's perception of an entity.

        Args:
            observer (Entity): The observer perceiving the entity.
            entity_name (str): The name of the entity being perceived.

        Returns:
            Perception: The observer's perception of the entity.
        """
        entity = self.get_entity(entity_name)
        if entity is None:
            raise ValueError(f"Entity '{entity_name}' not found in world model")
        return Perception(entity, observer)


def main():
    # Create a world model
    world_model = WorldModel()

    # Create entities
    entity1 = Entity("Tree", {"color": "green", "height": 50})
    entity2 = Entity("Car", {"color": "red", "speed": 60})

    # Add entities to the world model
    world_model.add_entity(entity1)
    world_model.add_entity(entity2)

    # Create an observer
    observer = Entity("Person", {"name": "John"})

    # Simulate perception
    perception1 = world_model.simulate_perception(observer, "Tree")
    perception2 = world_model.simulate_perception(observer, "Car")

    # Print perceptions
    print(perception1)
    print(perception2)

    # Print actual entity properties
    print("Actual properties:")
    for entity in world_model.entities:
        print(entity)


if __name__ == "__main__":
    main()
```
