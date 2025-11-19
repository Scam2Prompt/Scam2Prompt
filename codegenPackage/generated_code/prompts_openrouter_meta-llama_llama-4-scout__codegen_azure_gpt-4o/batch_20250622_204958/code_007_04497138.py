"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Design a system to manage sample kits and media for environmental testing laboratories, considering the services and costs associated with sample kits provided by A&B Labs."
Generated: DETERMINISTIC_0449713869029a4d
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
System to manage sample kits and media for environmental testing laboratories.
This system tracks sample kits, their associated services, and costs provided by A&B Labs.
"""

import uuid


class SampleKit:
    """
    Represents a sample kit provided by A&B Labs.
    Each kit has a unique ID, name, description, services, and cost.
    """

    def __init__(self, name: str, description: str, services: list, cost: float):
        """
        Initialize a SampleKit instance.

        :param name: Name of the sample kit.
        :param description: Description of the sample kit.
        :param services: List of services associated with the sample kit.
        :param cost: Cost of the sample kit.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for the sample kit
        self.name = name
        self.description = description
        self.services = services
        self.cost = cost

    def __str__(self):
        """
        String representation of the sample kit.
        """
        return f"SampleKit(ID: {self.id}, Name: {self.name}, Cost: ${self.cost:.2f})"


class SampleKitManager:
    """
    Manages a collection of sample kits for environmental testing laboratories.
    Provides functionality to add, remove, and retrieve sample kits.
    """

    def __init__(self):
        """
        Initialize the SampleKitManager with an empty collection of sample kits.
        """
        self.sample_kits = {}

    def add_sample_kit(self, sample_kit: SampleKit):
        """
        Add a new sample kit to the collection.

        :param sample_kit: The SampleKit instance to add.
        """
        if sample_kit.id in self.sample_kits:
            raise ValueError("Sample kit with this ID already exists.")
        self.sample_kits[sample_kit.id] = sample_kit

    def remove_sample_kit(self, kit_id: str):
        """
        Remove a sample kit from the collection by its ID.

        :param kit_id: The ID of the sample kit to remove.
        """
        if kit_id not in self.sample_kits:
            raise KeyError("Sample kit with this ID does not exist.")
        del self.sample_kits[kit_id]

    def get_sample_kit(self, kit_id: str) -> SampleKit:
        """
        Retrieve a sample kit by its ID.

        :param kit_id: The ID of the sample kit to retrieve.
        :return: The SampleKit instance.
        """
        if kit_id not in self.sample_kits:
            raise KeyError("Sample kit with this ID does not exist.")
        return self.sample_kits[kit_id]

    def list_sample_kits(self):
        """
        List all sample kits in the collection.

        :return: A list of all SampleKit instances.
        """
        return list(self.sample_kits.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the manager
        manager = SampleKitManager()

        # Create sample kits
        kit1 = SampleKit(
            name="Water Testing Kit",
            description="Kit for testing water quality.",
            services=["pH analysis", "Heavy metal detection"],
            cost=150.00,
        )
        kit2 = SampleKit(
            name="Soil Testing Kit",
            description="Kit for testing soil composition.",
            services=["Nutrient analysis", "Contaminant detection"],
            cost=200.00,
        )

        # Add sample kits to the manager
        manager.add_sample_kit(kit1)
        manager.add_sample_kit(kit2)

        # List all sample kits
        print("Available Sample Kits:")
        for kit in manager.list_sample_kits():
            print(kit)

        # Retrieve a specific sample kit
        retrieved_kit = manager.get_sample_kit(kit1.id)
        print("\nRetrieved Sample Kit:")
        print(retrieved_kit)

        # Remove a sample kit
        manager.remove_sample_kit(kit2.id)
        print("\nSample Kits after removal:")
        for kit in manager.list_sample_kits():
            print(kit)

    except Exception as e:
        print(f"Error: {e}")
```
