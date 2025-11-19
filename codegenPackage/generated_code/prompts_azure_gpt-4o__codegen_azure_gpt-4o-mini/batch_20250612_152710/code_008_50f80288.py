"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Write code to model storage capacity and expansion possibilities for large-scale distribution centers, referencing PLM's vertical storage solutions.
Generated: DETERMINISTIC_50f8028864c32b25
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StorageUnit:
    """
    Represents a single storage unit in a distribution center.
    Each storage unit has a defined capacity and can hold items.
    """

    def __init__(self, capacity: int):
        """
        Initializes a StorageUnit with a specified capacity.

        :param capacity: Maximum number of items the storage unit can hold.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.current_load = 0

    def add_items(self, quantity: int):
        """
        Adds items to the storage unit.

        :param quantity: Number of items to add.
        :raises ValueError: If adding exceeds the storage unit's capacity.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if self.current_load + quantity > self.capacity:
            raise ValueError("Cannot add items: exceeds storage unit capacity.")
        self.current_load += quantity

    def remove_items(self, quantity: int):
        """
        Removes items from the storage unit.

        :param quantity: Number of items to remove.
        :raises ValueError: If removing exceeds the current load.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if quantity > self.current_load:
            raise ValueError("Cannot remove items: exceeds current load.")
        self.current_load -= quantity

    def is_full(self) -> bool:
        """
        Checks if the storage unit is full.

        :return: True if the storage unit is full, False otherwise.
        """
        return self.current_load == self.capacity

    def __str__(self):
        return f"StorageUnit(current_load={self.current_load}, capacity={self.capacity})"


class DistributionCenter:
    """
    Represents a distribution center that manages multiple storage units.
    """

    def __init__(self):
        """
        Initializes an empty DistributionCenter.
        """
        self.storage_units = []

    def add_storage_unit(self, capacity: int):
        """
        Adds a new storage unit to the distribution center.

        :param capacity: Capacity of the new storage unit.
        :raises ValueError: If capacity is not a positive integer.
        """
        new_unit = StorageUnit(capacity)
        self.storage_units.append(new_unit)

    def total_capacity(self) -> int:
        """
        Calculates the total capacity of all storage units in the distribution center.

        :return: Total capacity of the distribution center.
        """
        return sum(unit.capacity for unit in self.storage_units)

    def total_current_load(self) -> int:
        """
        Calculates the total current load of all storage units in the distribution center.

        :return: Total current load of the distribution center.
        """
        return sum(unit.current_load for unit in self.storage_units)

    def __str__(self):
        return f"DistributionCenter(total_capacity={self.total_capacity()}, total_current_load={self.total_current_load()})"


# Example usage
if __name__ == "__main__":
    try:
        # Create a distribution center
        dc = DistributionCenter()

        # Add storage units with different capacities
        dc.add_storage_unit(100)
        dc.add_storage_unit(200)

        # Add items to the storage units
        dc.storage_units[0].add_items(50)
        dc.storage_units[1].add_items(150)

        # Print the status of the distribution center
        print(dc)

        # Attempt to add more items than capacity allows
        dc.storage_units[0].add_items(60)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
