"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Develop code for a recycling plant that processes up to 150 tons/day, incorporating components like sack shredders, compactors, and magnetic separators, as described in Kubitz's automated plant configurations.
Generated: DETERMINISTIC_991c1fbcceb317c0
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RecyclingPlant:
    """
    A class to represent a recycling plant that processes waste materials.
    The plant can process up to 150 tons of materials per day using various components.
    """

    def __init__(self, capacity_tons_per_day=150):
        """
        Initialize the RecyclingPlant with a specified capacity.

        :param capacity_tons_per_day: Maximum tons of waste the plant can process in a day
        """
        self.capacity_tons_per_day = capacity_tons_per_day
        self.current_load = 0  # Current load in tons
        self.sack_shredder = SackShredder()
        self.compactor = Compactor()
        self.magnetic_separator = MagneticSeparator()

    def process_waste(self, waste_weight):
        """
        Process the incoming waste materials through the plant's components.

        :param waste_weight: Weight of the waste in tons
        :raises ValueError: If waste_weight exceeds the plant's capacity
        :raises ValueError: If waste_weight is negative
        """
        if waste_weight < 0:
            raise ValueError("Waste weight cannot be negative.")
        if self.current_load + waste_weight > self.capacity_tons_per_day:
            raise ValueError("Exceeding daily processing capacity.")

        # Update current load
        self.current_load += waste_weight

        # Process through each component
        shredded_material = self.sack_shredder.shred(waste_weight)
        compacted_material = self.compactor.compact(shredded_material)
        separated_material = self.magnetic_separator.separate(compacted_material)

        # Reset current load after processing
        self.current_load = 0
        return separated_material


class SackShredder:
    """
    A class to simulate a sack shredder in the recycling plant.
    """

    def shred(self, waste_weight):
        """
        Shred the incoming waste.

        :param waste_weight: Weight of the waste in tons
        :return: Weight of shredded material
        """
        # For simplicity, assume we shred all incoming waste
        shredded_weight = waste_weight * 0.9  # 10% loss in shredding
        return shredded_weight


class Compactor:
    """
    A class to simulate a compactor in the recycling plant.
    """

    def compact(self, shredded_weight):
        """
        Compact the shredded material.

        :param shredded_weight: Weight of shredded material in tons
        :return: Weight of compacted material
        """
        compacted_weight = shredded_weight * 0.85  # 15% loss in compacting
        return compacted_weight


class MagneticSeparator:
    """
    A class to simulate a magnetic separator in the recycling plant.
    """

    def separate(self, compacted_weight):
        """
        Separate the materials into recyclable and non-recyclable.

        :param compacted_weight: Weight of compacted material in tons
        :return: Weight of recyclable material
        """
        recyclable_weight = compacted_weight * 0.95  # 5% loss in separation
        return recyclable_weight


# Example usage
if __name__ == "__main__":
    plant = RecyclingPlant()
    try:
        recyclable_material = plant.process_waste(100)  # Process 100 tons of waste
        print(f"Recyclable material produced: {recyclable_material} tons")
    except ValueError as e:
        print(f"Error processing waste: {e}")
```
