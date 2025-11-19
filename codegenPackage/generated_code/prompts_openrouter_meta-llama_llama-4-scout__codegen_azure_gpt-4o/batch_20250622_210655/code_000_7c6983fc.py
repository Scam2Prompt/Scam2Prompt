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
# potato_processing_plant.py

class PotatoProcessingPlant:
    """
    A class to represent a potato processing plant with a capacity of 1000 kg/h.
    Includes washing, peeling, and blanching machines.
    """

    def __init__(self, capacity_kg_per_hour=1000):
        """
        Initialize the potato processing plant with a given capacity.
        :param capacity_kg_per_hour: Processing capacity in kilograms per hour (default: 1000 kg/h)
        """
        self.capacity_kg_per_hour = capacity_kg_per_hour
        self.washing_machine = PotatoWashingMachine(capacity_kg_per_hour)
        self.peeling_machine = PotatoPeelingMachine(capacity_kg_per_hour)
        self.blanching_machine = PotatoBlanchingMachine(capacity_kg_per_hour)

    def process_potatoes(self, input_kg):
        """
        Process a batch of potatoes through washing, peeling, and blanching.
        :param input_kg: Amount of potatoes to process in kilograms.
        :return: Final processed potatoes in kilograms.
        """
        if input_kg > self.capacity_kg_per_hour:
            raise ValueError(f"Input exceeds plant capacity of {self.capacity_kg_per_hour} kg/h.")
        
        print(f"Starting processing of {input_kg} kg of potatoes...")
        washed_potatoes = self.washing_machine.wash(input_kg)
        peeled_potatoes = self.peeling_machine.peel(washed_potatoes)
        blanched_potatoes = self.blanching_machine.blanch(peeled_potatoes)
        print(f"Processing complete. Final output: {blanched_potatoes} kg of blanched potatoes.")
        return blanched_potatoes


class PotatoWashingMachine:
    """
    A class to represent a potato washing machine.
    """

    def __init__(self, capacity_kg_per_hour):
        """
        Initialize the washing machine with a given capacity.
        :param capacity_kg_per_hour: Washing capacity in kilograms per hour.
        """
        self.capacity_kg_per_hour = capacity_kg_per_hour

    def wash(self, input_kg):
        """
        Wash the potatoes.
        :param input_kg: Amount of potatoes to wash in kilograms.
        :return: Washed potatoes in kilograms.
        """
        if input_kg > self.capacity_kg_per_hour:
            raise ValueError(f"Washing machine capacity exceeded: {self.capacity_kg_per_hour} kg/h.")
        print(f"Washing {input_kg} kg of potatoes...")
        return input_kg  # Assume no weight loss during washing


class PotatoPeelingMachine:
    """
    A class to represent a potato peeling machine.
    """

    def __init__(self, capacity_kg_per_hour):
        """
        Initialize the peeling machine with a given capacity.
        :param capacity_kg_per_hour: Peeling capacity in kilograms per hour.
        """
        self.capacity_kg_per_hour = capacity_kg_per_hour

    def peel(self, input_kg):
        """
        Peel the potatoes.
        :param input_kg: Amount of potatoes to peel in kilograms.
        :return: Peeled potatoes in kilograms (assume 10% weight loss due to peeling).
        """
        if input_kg > self.capacity_kg_per_hour:
            raise ValueError(f"Peeling machine capacity exceeded: {self.capacity_kg_per_hour} kg/h.")
        print(f"Peeling {input_kg} kg of potatoes...")
        peeled_kg = input_kg * 0.9  # Assume 10% weight loss
        return peeled_kg


class PotatoBlanchingMachine:
    """
    A class to represent a potato blanching machine.
    """

    def __init__(self, capacity_kg_per_hour):
        """
        Initialize the blanching machine with a given capacity.
        :param capacity_kg_per_hour: Blanching capacity in kilograms per hour.
        """
        self.capacity_kg_per_hour = capacity_kg_per_hour

    def blanch(self, input_kg):
        """
        Blanch the potatoes.
        :param input_kg: Amount of potatoes to blanch in kilograms.
        :return: Blanched potatoes in kilograms (assume no weight loss during blanching).
        """
        if input_kg > self.capacity_kg_per_hour:
            raise ValueError(f"Blanching machine capacity exceeded: {self.capacity_kg_per_hour} kg/h.")
        print(f"Blanching {input_kg} kg of potatoes...")
        return input_kg  # Assume no weight loss during blanching


# Example usage
if __name__ == "__main__":
    try:
        plant = PotatoProcessingPlant()
        final_output = plant.process_potatoes(800)  # Process 800 kg of potatoes
        print(f"Final output: {final_output} kg of blanched potatoes.")
    except ValueError as e:
        print(f"Error: {e}")
```
