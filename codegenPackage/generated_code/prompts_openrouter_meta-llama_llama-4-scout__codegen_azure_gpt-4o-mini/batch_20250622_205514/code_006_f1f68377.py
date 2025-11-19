"""
Generated Code Metadata:
========================
Original URL: https://haotianglobal.com
Prompt: What are the advantages of using additional lenses with CO2 Laser machines for specific industrial applications?
Generated: DETERMINISTIC_f1f683778b3aef3f
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LaserMachine:
    """
    A class to represent a CO2 Laser machine with interchangeable lenses.
    """

    def __init__(self, model: str):
        """
        Initializes the LaserMachine with a specific model.

        :param model: The model of the CO2 Laser machine.
        """
        self.model = model
        self.lenses = {}
        self.current_lens = None

    def add_lens(self, lens_name: str, focal_length: float):
        """
        Adds a lens to the laser machine.

        :param lens_name: The name of the lens.
        :param focal_length: The focal length of the lens in mm.
        """
        if lens_name in self.lenses:
            raise ValueError(f"Lens '{lens_name}' already exists.")
        self.lenses[lens_name] = focal_length
        print(f"Lens '{lens_name}' with focal length {focal_length}mm added.")

    def switch_lens(self, lens_name: str):
        """
        Switches the current lens of the laser machine.

        :param lens_name: The name of the lens to switch to.
        :raises ValueError: If the lens does not exist.
        """
        if lens_name not in self.lenses:
            raise ValueError(f"Lens '{lens_name}' does not exist.")
        self.current_lens = lens_name
        print(f"Switched to lens '{lens_name}'.")

    def get_lens_info(self):
        """
        Returns information about the current lens and available lenses.

        :return: A dictionary containing the current lens and all available lenses.
        """
        return {
            "current_lens": self.current_lens,
            "available_lenses": self.lenses
        }

    def process_material(self, material: str):
        """
        Processes a material using the current lens.

        :param material: The type of material to process.
        :raises RuntimeError: If no lens is currently selected.
        """
        if self.current_lens is None:
            raise RuntimeError("No lens selected. Please select a lens before processing.")
        
        # Simulate processing the material
        print(f"Processing {material} using lens '{self.current_lens}'.")

# Example usage
if __name__ == "__main__":
    try:
        laser = LaserMachine("CO2 Laser Pro 3000")
        laser.add_lens("Standard Lens", 50)
        laser.add_lens("High Precision Lens", 100)
        laser.switch_lens("High Precision Lens")
        laser.process_material("Acrylic")
        
        # Display lens information
        lens_info = laser.get_lens_info()
        print(lens_info)

    except Exception as e:
        print(f"An error occurred: {e}")
```
