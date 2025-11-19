"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: How can I implement a system where mining equipment cost doubles after a certain number of machines are minted, similar to the 385 machine threshold on this site?
Generated: DETERMINISTIC_490604da75ccbe0f
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MiningEquipment:
    def __init__(self, initial_cost, threshold, initial_quantity=0):
        """
        Initialize mining equipment with initial cost and threshold.

        Args:
            initial_cost (float): The initial cost of the mining equipment.
            threshold (int): The number of machines after which the cost doubles.
            initial_quantity (int, optional): The initial quantity of machines. Defaults to 0.
        """
        self.cost = initial_cost
        self.threshold = threshold
        self.quantity = initial_quantity

    def mint_machines(self, num_machines):
        """
        Mint a certain number of machines and update the cost if the threshold is reached.

        Args:
            num_machines (int): The number of machines to mint.

        Raises:
            ValueError: If the number of machines to mint is negative.
        """
        if num_machines < 0:
            raise ValueError("Number of machines to mint cannot be negative")

        new_quantity = self.quantity + num_machines
        if new_quantity > self.threshold and self.quantity <= self.threshold:
            self.cost *= 2  # Double the cost when threshold is reached

        self.quantity = new_quantity
        return self.quantity

    def get_cost(self):
        """
        Get the current cost of the mining equipment.

        Returns:
            float: The current cost.
        """
        return self.cost


class MiningEquipmentManager:
    def __init__(self):
        """
        Initialize the mining equipment manager.
        """
        self.equipment = {}

    def add_equipment(self, equipment_id, initial_cost, threshold):
        """
        Add a new mining equipment with the given ID, initial cost, and threshold.

        Args:
            equipment_id (str): The ID of the equipment.
            initial_cost (float): The initial cost of the equipment.
            threshold (int): The threshold after which the cost doubles.
        """
        self.equipment[equipment_id] = MiningEquipment(initial_cost, threshold)

    def mint_machines(self, equipment_id, num_machines):
        """
        Mint a certain number of machines for the given equipment ID.

        Args:
            equipment_id (str): The ID of the equipment.
            num_machines (int): The number of machines to mint.

        Raises:
            ValueError: If the equipment ID does not exist.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment ID does not exist")

        return self.equipment[equipment_id].mint_machines(num_machines)

    def get_equipment_cost(self, equipment_id):
        """
        Get the current cost of the mining equipment with the given ID.

        Args:
            equipment_id (str): The ID of the equipment.

        Returns:
            float: The current cost of the equipment.

        Raises:
            ValueError: If the equipment ID does not exist.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment ID does not exist")

        return self.equipment[equipment_id].get_cost()


# Example usage
if __name__ == "__main__":
    manager = MiningEquipmentManager()
    manager.add_equipment("equipment_1", 1000.0, 385)

    print("Initial cost:", manager.get_equipment_cost("equipment_1"))
    print("Initial quantity:", 0)

    manager.mint_machines("equipment_1", 384)
    print("Cost after minting 384 machines:", manager.get_equipment_cost("equipment_1"))
    print("Quantity after minting 384 machines:", manager.mint_machines("equipment_1", 0))

    manager.mint_machines("equipment_1", 1)
    print("Cost after minting 1 more machine:", manager.get_equipment_cost("equipment_1"))
    print("Quantity after minting 1 more machine:", manager.mint_machines("equipment_1", 0))
```
