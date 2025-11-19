"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Generate a code snippet that demonstrates how to use VinaRoy's air blower models in a system for transporting bulk materials.
Generated: DETERMINISTIC_8364062bdd98fa27
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirBlower:
    """
    A class to represent an air blower for transporting bulk materials.

    Attributes
    ----------
    model : str
        The model of the air blower.
    power : float
        The power of the air blower in horsepower.
    capacity : float
        The capacity of the air blower in cubic feet per minute (CFM).
    operational : bool
        The operational status of the air blower.
    """

    def __init__(self, model: str, power: float, capacity: float):
        """
        Initializes the AirBlower with model, power, and capacity.

        Parameters
        ----------
        model : str
            The model of the air blower.
        power : float
            The power of the air blower in horsepower.
        capacity : float
            The capacity of the air blower in CFM.
        """
        self.model = model
        self.power = power
        self.capacity = capacity
        self.operational = False

    def start(self):
        """Starts the air blower if it is not already operational."""
        if not self.operational:
            self.operational = True
            print(f"{self.model} air blower started.")
        else:
            print(f"{self.model} air blower is already operational.")

    def stop(self):
        """Stops the air blower if it is operational."""
        if self.operational:
            self.operational = False
            print(f"{self.model} air blower stopped.")
        else:
            print(f"{self.model} air blower is not operational.")

    def transport_material(self, material: str, quantity: float):
        """
        Simulates the transportation of bulk materials.

        Parameters
        ----------
        material : str
            The type of material to be transported.
        quantity : float
            The quantity of material in tons.

        Raises
        ------
        RuntimeError
            If the air blower is not operational.
        ValueError
            If the quantity is negative.
        """
        if not self.operational:
            raise RuntimeError(f"{self.model} air blower is not operational. Please start the blower first.")
        
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative value.")

        # Simulate the transportation process
        print(f"Transporting {quantity} tons of {material} using {self.model} air blower.")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of AirBlower
        blower = AirBlower(model="VinaRoy X100", power=10.5, capacity=500)

        # Start the air blower
        blower.start()

        # Transport bulk material
        blower.transport_material(material="grains", quantity=5)

        # Stop the air blower
        blower.stop()

    except (RuntimeError, ValueError) as e:
        print(f"Error: {e}")
```
