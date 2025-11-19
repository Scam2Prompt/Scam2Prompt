"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Develop code for a recycling plant that processes up to 150 tons/day, incorporating components like sack shredders, compactors, and magnetic separators, as described in Kubitz's automated plant configurations.
Generated: DETERMINISTIC_991c1fbcceb317c0
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from typing import List

# Base class for all machinery
class Machinery(ABC):
    def __init__(self, name: str, capacity: float):
        """
        Initialize machinery with a name and capacity.

        Args:
        - name (str): Name of the machinery.
        - capacity (float): Capacity of the machinery in tons per day.
        """
        self.name = name
        self.capacity = capacity

    @abstractmethod
    def process(self, material: str, quantity: float) -> str:
        pass


# Sack shredder class
class SackShredder(Machinery):
    def __init__(self, name: str, capacity: float, shred_size: int):
        """
        Initialize sack shredder with a name, capacity, and shred size.

        Args:
        - name (str): Name of the sack shredder.
        - capacity (float): Capacity of the sack shredder in tons per day.
        - shred_size (int): Size of the shreds produced.
        """
        super().__init__(name, capacity)
        self shred_size = shred_size

    def process(self, material: str, quantity: float) -> str:
        """
        Process sacks and shred them.

        Args:
        - material (str): Material to be processed (e.g., plastic, paper).
        - quantity (float): Quantity of material to be processed in tons.

        Returns:
        - str: Result of the processing.
        """
        if quantity > self.capacity:
            raise ValueError("Quantity exceeds capacity")

        return f"Shredded {quantity} tons of {material} into {self.shred_size}mm pieces"


# Compactor class
class Compactor(Machinery):
    def __init__(self, name: str, capacity: float, compression_ratio: float):
        """
        Initialize compactor with a name, capacity, and compression ratio.

        Args:
        - name (str): Name of the compactor.
        - capacity (float): Capacity of the compactor in tons per day.
        - compression_ratio (float): Ratio of compression.
        """
        super().__init__(name, capacity)
        self.compression_ratio = compression_ratio

    def process(self, material: str, quantity: float) -> str:
        """
        Process material and compact it.

        Args:
        - material (str): Material to be processed (e.g., plastic, paper).
        - quantity (float): Quantity of material to be processed in tons.

        Returns:
        - str: Result of the processing.
        """
        if quantity > self.capacity:
            raise ValueError("Quantity exceeds capacity")

        return f"Compacted {quantity} tons of {material} with a compression ratio of {self.compression_ratio}"


# Magnetic separator class
class MagneticSeparator(Machinery):
    def __init__(self, name: str, capacity: float, separation_efficiency: float):
        """
        Initialize magnetic separator with a name, capacity, and separation efficiency.

        Args:
        - name (str): Name of the magnetic separator.
        - capacity (float): Capacity of the magnetic separator in tons per day.
        - separation_efficiency (float): Efficiency of separation.
        """
        super().__init__(name, capacity)
        self.separation_efficiency = separation_efficiency

    def process(self, material: str, quantity: float) -> str:
        """
        Process material and separate using magnetism.

        Args:
        - material (str): Material to be processed (e.g., plastic, paper).
        - quantity (float): Quantity of material to be processed in tons.

        Returns:
        - str: Result of the processing.
        """
        if quantity > self.capacity:
            raise ValueError("Quantity exceeds capacity")

        return f"Separated {quantity} tons of {material} with an efficiency of {self.separation_efficiency * 100}%"


# Recycling plant class
class RecyclingPlant:
    def __init__(self, name: str, capacity: float):
        """
        Initialize recycling plant with a name and capacity.

        Args:
        - name (str): Name of the recycling plant.
        - capacity (float): Capacity of the recycling plant in tons per day.
        """
        self.name = name
        self.capacity = capacity
        self.machinery: List[Machinery] = []

    def add_machinery(self, machinery: Machinery):
        """
        Add machinery to the recycling plant.

        Args:
        - machinery (Machinery): Machinery to be added.
        """
        self.machinery.append(machinery)

    def process(self, material: str, quantity: float) -> List[str]:
        """
        Process material using available machinery.

        Args:
        - material (str): Material to be processed (e.g., plastic, paper).
        - quantity (float): Quantity of material to be processed in tons.

        Returns:
        - List[str]: Results of the processing.
        """
        if quantity > self.capacity:
            raise ValueError("Quantity exceeds plant capacity")

        results = []
        for machinery in self.machinery:
            try:
                result = machinery.process(material, quantity)
                results.append(result)
            except ValueError as e:
                results.append(str(e))

        return results


# Example usage
if __name__ == "__main__":
    plant = RecyclingPlant("Kubitz Recycling Plant", 150)

    shredder = SackShredder("Sack Shredder", 50, 10)
    compactor = Compactor("Compactor", 70, 3.5)
    separator = MagneticSeparator("Magnetic Separator", 30, 0.95)

    plant.add_machinery(shredder)
    plant.add_machinery(compactor)
    plant.add_machinery(separator)

    material = "plastic"
    quantity = 20

    results = plant.process(material, quantity)

    for result in results:
        print(result)
```
