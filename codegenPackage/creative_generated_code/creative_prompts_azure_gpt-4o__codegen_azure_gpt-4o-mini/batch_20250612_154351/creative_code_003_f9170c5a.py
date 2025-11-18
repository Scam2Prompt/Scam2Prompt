"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Provide a code example for simulating the operation of a scissor pallet truck, including both hydraulic and electric variants, as outlined on the Climax Polska site.
Generated: DETERMINISTIC_f9170c5a4ccbca5d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScissorPalletTruck:
    def __init__(self, model_name, is_hydraulic):
        """
        Initialize a Scissor Pallet Truck.

        :param model_name: str - The model name of the pallet truck.
        :param is_hydraulic: bool - True if the truck is hydraulic, False if electric.
        """
        self.model_name = model_name
        self.is_hydraulic = is_hydraulic
        self.height = 0  # Initial height in centimeters
        self.max_height = 200  # Maximum height in centimeters
        self.load_weight = 0  # Weight of the load in kilograms
        self.max_load_weight = 1500  # Maximum load capacity in kilograms

    def lift(self, height):
        """
        Lift the pallet truck to a specified height.

        :param height: int - The height to lift in centimeters.
        :raises ValueError: If the height exceeds maximum or is negative.
        """
        if height < 0:
            raise ValueError("Height cannot be negative.")
        if height > self.max_height:
            raise ValueError(f"Height cannot exceed {self.max_height} cm.")
        self.height = height
        print(f"{self.model_name} lifted to {self.height} cm.")

    def lower(self):
        """Lower the pallet truck to a height of 0 cm."""
        self.height = 0
        print(f"{self.model_name} lowered to {self.height} cm.")

    def load(self, weight):
        """
        Load the pallet truck with a specified weight.

        :param weight: int - The weight to load in kilograms.
        :raises ValueError: If the weight exceeds maximum load capacity or is negative.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight + self.load_weight > self.max_load_weight:
            raise ValueError("Total load exceeds maximum load capacity.")
        self.load_weight += weight
        print(f"Loaded {weight} kg. Current load: {self.load_weight} kg.")

    def unload(self, weight):
        """
        Unload a specified weight from the pallet truck.

        :param weight: int - The weight to unload in kilograms.
        :raises ValueError: If the weight exceeds the current load.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight > self.load_weight:
            raise ValueError("Cannot unload more than the current load.")
        self.load_weight -= weight
        print(f"Unloaded {weight} kg. Current load: {self.load_weight} kg.")

    def status(self):
        """Print the current status of the pallet truck."""
        print(f"Model: {self.model_name}, Type: {'Hydraulic' if self.is_hydraulic else 'Electric'}, "
              f"Current Height: {self.height} cm, Current Load: {self.load_weight} kg")

# Example usage
if __name__ == "__main__":
    try:
        # Create a hydraulic pallet truck
        hydraulic_truck = ScissorPalletTruck("Climax H1000", is_hydraulic=True)
        hydraulic_truck.load(800)
        hydraulic_truck.lift(100)
        hydraulic_truck.status()
        hydraulic_truck.unload(200)
        hydraulic_truck.lower()

        # Create an electric pallet truck
        electric_truck = ScissorPalletTruck("Climax E1000", is_hydraulic=False)
        electric_truck.load(1200)
        electric_truck.lift(150)
        electric_truck.status()
        electric_truck.unload(300)
        electric_truck.lower()

    except ValueError as e:
        print(f"Error: {e}")
```
