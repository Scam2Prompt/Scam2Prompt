"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "Design a pipe roller cradle for pipeline construction using nylon material."
Generated: DETERMINISTIC_8ca01d89ef206b38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PipeRollerCradle:
    """
    A class to represent a pipe roller cradle for pipeline construction.
    
    Attributes:
        length (float): The length of the cradle in meters.
        width (float): The width of the cradle in meters.
        height (float): The height of the cradle in meters.
        material (str): The material used for the cradle.
        load_capacity (float): The maximum load capacity of the cradle in kilograms.
    """

    def __init__(self, length: float, width: float, height: float, load_capacity: float):
        """
        Initializes the PipeRollerCradle with specified dimensions and load capacity.
        
        Args:
            length (float): Length of the cradle.
            width (float): Width of the cradle.
            height (float): Height of the cradle.
            load_capacity (float): Load capacity of the cradle.
        
        Raises:
            ValueError: If any dimension or load capacity is non-positive.
        """
        if length <= 0 or width <= 0 or height <= 0 or load_capacity <= 0:
            raise ValueError("Dimensions and load capacity must be positive values.")
        
        self.length = length
        self.width = width
        self.height = height
        self.material = "Nylon"  # Material is fixed as per user request
        self.load_capacity = load_capacity

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the cradle.
        
        Returns:
            float: Volume of the cradle in cubic meters.
        """
        return self.length * self.width * self.height

    def is_load_within_capacity(self, load: float) -> bool:
        """
        Checks if the given load is within the cradle's load capacity.
        
        Args:
            load (float): The load to check.
        
        Returns:
            bool: True if the load is within capacity, False otherwise.
        """
        if load < 0:
            raise ValueError("Load must be a non-negative value.")
        return load <= self.load_capacity

    def __str__(self) -> str:
        """
        Returns a string representation of the PipeRollerCradle.
        
        Returns:
            str: Description of the cradle's dimensions and material.
        """
        return (f"Pipe Roller Cradle:\n"
                f"Material: {self.material}\n"
                f"Dimensions (L x W x H): {self.length}m x {self.width}m x {self.height}m\n"
                f"Load Capacity: {self.load_capacity}kg\n"
                f"Volume: {self.calculate_volume()}m³")

# Example usage
if __name__ == "__main__":
    try:
        cradle = PipeRollerCradle(length=3.0, width=1.5, height=0.5, load_capacity=1000.0)
        print(cradle)
        
        load = 800.0  # Example load
        if cradle.is_load_within_capacity(load):
            print(f"The load of {load}kg is within the capacity.")
        else:
            print(f"The load of {load}kg exceeds the capacity.")
    except ValueError as e:
        print(f"Error: {e}")
```
