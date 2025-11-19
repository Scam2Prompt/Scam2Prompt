"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: What are the steps to access new Adventure Instances in Big Time, and what unique features do they offer?
Generated: DETERMINISTIC_b5835bdcf911a980
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AdventureInstance:
    """
    A class to represent an Adventure Instance in the game Big Time.
    """

    def __init__(self, instance_id, name, features):
        """
        Initialize a new Adventure Instance.

        :param instance_id: Unique identifier for the adventure instance.
        :param name: Name of the adventure instance.
        :param features: List of unique features offered by the instance.
        """
        self.instance_id = instance_id
        self.name = name
        self.features = features

    def display_info(self):
        """
        Display the information of the adventure instance.
        """
        info = f"Adventure Instance ID: {self.instance_id}\n" \
               f"Name: {self.name}\n" \
               f"Unique Features: {', '.join(self.features)}"
        print(info)

class AdventureManager:
    """
    A class to manage multiple Adventure Instances.
    """

    def __init__(self):
        """Initialize the Adventure Manager with an empty list of instances."""
        self.adventure_instances = []

    def add_instance(self, instance):
        """
        Add a new adventure instance to the manager.

        :param instance: AdventureInstance to add.
        """
        if not isinstance(instance, AdventureInstance):
            raise TypeError("Expected an instance of AdventureInstance.")
        self.adventure_instances.append(instance)

    def get_instance_by_id(self, instance_id):
        """
        Retrieve an Adventure Instance by its ID.

        :param instance_id: The ID of the Adventure Instance to retrieve.
        :return: AdventureInstance object if found, else raises ValueError.
        """
        for instance in self.adventure_instances:
            if instance.instance_id == instance_id:
                return instance
        raise ValueError(f"Adventure Instance with ID {instance_id} not found.")

# Example usage:
if __name__ == "__main__":
    # Create instance manager
    manager = AdventureManager()

    # Create new Adventure Instances
    instance1 = AdventureInstance(1, "The Lost Cavern", ["Puzzle Solving", "Treasure Hunt"])
    instance2 = AdventureInstance(2, "Dragon's Peak", ["Combat Challenges", "Rare Loot"])
    
    # Add instances to the manager
    try:
        manager.add_instance(instance1)
        manager.add_instance(instance2)

        # Retrieve and display instance information
        adventure = manager.get_instance_by_id(1)
        adventure.display_info()
        
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
```
