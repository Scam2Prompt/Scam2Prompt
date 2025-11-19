"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Design a potato processing plant with a capacity of 1000 kg/h, including patates yıkama makineleri (potato washing machines), patates kabuğu soyma makineleri (potato peeling machines), and haşlama makineleri (blanching machines).
Generated: DETERMINISTIC_7c6983fc65bec601
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PotatoProcessingPlant:
    """
    A class to represent a potato processing plant with a capacity of 1000 kg/h.
    The plant includes washing, peeling, and blanching machines.
    """

    def __init__(self, capacity_kg_per_hour=1000):
        """
        Initializes the PotatoProcessingPlant with a specified capacity.

        :param capacity_kg_per_hour: The processing capacity of the plant in kg/h.
        """
        self.capacity_kg_per_hour = capacity_kg_per_hour
        self.washing_machine = PotatoWashingMachine()
        self.peeling_machine = PotatoPeelingMachine()
        self.blanching_machine = PotatoBlanchingMachine()

    def process_potatoes(self, weight_kg):
        """
        Processes the given weight of potatoes through the plant.

        :param weight_kg: The weight of potatoes to be processed in kg.
        :raises ValueError: If the weight exceeds the plant's capacity.
        """
        if weight_kg > self.capacity_kg_per_hour:
            raise ValueError(f"Cannot process {weight_kg} kg. Capacity is {self.capacity_kg_per_hour} kg/h.")

        self.washing_machine.wash(weight_kg)
        self.peeling_machine.peel(weight_kg)
        self.blanching_machine.blanch(weight_kg)

        print(f"Processed {weight_kg} kg of potatoes successfully.")

class PotatoWashingMachine:
    """
    A class to represent a potato washing machine.
    """

    def wash(self, weight_kg):
        """
        Washes the given weight of potatoes.

        :param weight_kg: The weight of potatoes to wash in kg.
        """
        print(f"Washing {weight_kg} kg of potatoes... Done.")

class PotatoPeelingMachine:
    """
    A class to represent a potato peeling machine.
    """

    def peel(self, weight_kg):
        """
        Peels the given weight of potatoes.

        :param weight_kg: The weight of potatoes to peel in kg.
        """
        print(f"Peeling {weight_kg} kg of potatoes... Done.")

class PotatoBlanchingMachine:
    """
    A class to represent a potato blanching machine.
    """

    def blanch(self, weight_kg):
        """
        Blanches the given weight of potatoes.

        :param weight_kg: The weight of potatoes to blanch in kg.
        """
        print(f"Blanching {weight_kg} kg of potatoes... Done.")

# Example usage
if __name__ == "__main__":
    try:
        plant = PotatoProcessingPlant()
        plant.process_potatoes(500)  # Example weight to process
    except ValueError as e:
        print(f"Error: {e}")
```
