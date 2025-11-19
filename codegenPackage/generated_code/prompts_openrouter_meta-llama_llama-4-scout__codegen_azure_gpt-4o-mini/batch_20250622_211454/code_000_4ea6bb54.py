"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: "Design a 3-piece modular wheel using aerospace grade aluminum for a Lamborghini Huracan Sterrato, considering Vehicle Dynamics and OEM load ratings."
Generated: DETERMINISTIC_4ea6bb54b0de2099
Batch ID: 20250622_211454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wheel:
    """
    A class to represent a modular wheel for a Lamborghini Huracan Sterrato.
    
    Attributes:
        diameter (float): Diameter of the wheel in inches.
        width (float): Width of the wheel in inches.
        material (str): Material of the wheel.
        load_rating (float): Load rating of the wheel in pounds.
    """

    def __init__(self, diameter: float, width: float, material: str, load_rating: float):
        """
        Initializes a Wheel instance with the given parameters.
        
        Args:
            diameter (float): Diameter of the wheel in inches.
            width (float): Width of the wheel in inches.
            material (str): Material of the wheel.
            load_rating (float): Load rating of the wheel in pounds.
        
        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        if width <= 0:
            raise ValueError("Width must be a positive value.")
        if material not in ["Aerospace Grade Aluminum"]:
            raise ValueError("Material must be 'Aerospace Grade Aluminum'.")
        if load_rating <= 0:
            raise ValueError("Load rating must be a positive value.")

        self.diameter = diameter
        self.width = width
        self.material = material
        self.load_rating = load_rating

    def __str__(self):
        """Returns a string representation of the Wheel instance."""
        return (f"Wheel(diameter={self.diameter}, width={self.width}, "
                f"material={self.material}, load_rating={self.load_rating})")


class ModularWheel:
    """
    A class to represent a modular wheel assembly consisting of three pieces.
    
    Attributes:
        wheel_pieces (list): A list containing the three wheel pieces.
    """

    def __init__(self, wheel_piece1: Wheel, wheel_piece2: Wheel, wheel_piece3: Wheel):
        """
        Initializes a ModularWheel instance with three wheel pieces.
        
        Args:
            wheel_piece1 (Wheel): The first piece of the wheel.
            wheel_piece2 (Wheel): The second piece of the wheel.
            wheel_piece3 (Wheel): The third piece of the wheel.
        
        Raises:
            ValueError: If the wheel pieces do not match in specifications.
        """
        if not all(isinstance(piece, Wheel) for piece in [wheel_piece1, wheel_piece2, wheel_piece3]):
            raise ValueError("All pieces must be instances of the Wheel class.")
        
        if (wheel_piece1.diameter != wheel_piece2.diameter or
                wheel_piece1.diameter != wheel_piece3.diameter):
            raise ValueError("All wheel pieces must have the same diameter.")
        
        if (wheel_piece1.width != wheel_piece2.width or
                wheel_piece1.width != wheel_piece3.width):
            raise ValueError("All wheel pieces must have the same width.")
        
        if (wheel_piece1.material != wheel_piece2.material or
                wheel_piece1.material != wheel_piece3.material):
            raise ValueError("All wheel pieces must be made of the same material.")
        
        if (wheel_piece1.load_rating != wheel_piece2.load_rating or
                wheel_piece1.load_rating != wheel_piece3.load_rating):
            raise ValueError("All wheel pieces must have the same load rating.")

        self.wheel_pieces = [wheel_piece1, wheel_piece2, wheel_piece3]

    def __str__(self):
        """Returns a string representation of the ModularWheel instance."""
        return f"ModularWheel(pieces={[str(piece) for piece in self.wheel_pieces]})"


# Example usage
if __name__ == "__main__":
    try:
        # Create three identical wheel pieces
        wheel1 = Wheel(diameter=20.0, width=9.0, material="Aerospace Grade Aluminum", load_rating=1500.0)
        wheel2 = Wheel(diameter=20.0, width=9.0, material="Aerospace Grade Aluminum", load_rating=1500.0)
        wheel3 = Wheel(diameter=20.0, width=9.0, material="Aerospace Grade Aluminum", load_rating=1500.0)

        # Create a modular wheel assembly
        modular_wheel = ModularWheel(wheel1, wheel2, wheel3)
        print(modular_wheel)

    except ValueError as e:
        print(f"Error: {e}")
```
