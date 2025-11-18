"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to simulate the hybrid design of the Settled Collection fireplaces, combining furniture and fireplace elements in a single piece.
Generated: DETERMINISTIC_0c73fef2b40cd0a4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Furniture:
    """
    Base class for all furniture items.
    """
    def __init__(self, material: str, color: str):
        """
        Initialize the furniture with material and color.

        Args:
            material (str): The material of the furniture.
            color (str): The color of the furniture.
        """
        self.material = material
        self.color = color

    def __str__(self):
        return f"{self.color} {self.material} furniture"


class Fireplace:
    """
    Base class for fireplace elements.
    """
    def __init__(self, fuel_type: str):
        """
        Initialize the fireplace with fuel type.

        Args:
            fuel_type (str): The type of fuel used by the fireplace.
        """
        self.fuel_type = fuel_type

    def ignite(self):
        """
        Simulate igniting the fireplace.
        """
        return f"The {self.fuel_type} fireplace is now ignited."


class SettledCollectionFireplace(Furniture, Fireplace):
    """
    Combines furniture and fireplace elements into a single piece.
    """
    def __init__(self, material: str, color: str, fuel_type: str):
        """
        Initializes the Settled Collection Fireplace with specific attributes.

        Args:
            material (str): The material of the furniture.
            color (str): The color of the furniture.
            fuel_type (str): The type of fuel used by the fireplace.
        """
        Furniture.__init__(self, material, color)
        Fireplace.__init__(self, fuel_type)

    def __str__(self):
        """
        Returns a string representation of the Settled Collection Fireplace.
        """
        return f"{super().__str__()} with a {self.fuel_type} fireplace"

    def light_fire(self):
        """
        Simulate the action of lighting the fireplace.
        """
        try:
            fire_status = self.ignite()
            return f"{self} - {fire_status}"
        except Exception as e:
            return f"Failed to light the fire: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create an instance of SettledCollectionFireplace
    settled_fireplace = SettledCollectionFireplace("wood", "brown", "gas")
    
    # Print the representation of the fireplace
    print(settled_fireplace)
    
    # Attempt to light the fireplace
    fire_output = settled_fireplace.light_fire()
    print(fire_output)
```
