"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Write a Python code snippet to compare the properties of Inconel Alloy 600 Pipes and Duplex Steel Pipes for a specific industrial application."
Generated: DETERMINISTIC_bb019f9e7777faac
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a base class for pipes
class Pipe:
    def __init__(self, name, material, diameter, thickness, temperature_range, pressure_rating):
        """
        Initialize a Pipe object.

        Args:
            name (str): Name of the pipe.
            material (str): Material of the pipe.
            diameter (float): Diameter of the pipe in inches.
            thickness (float): Thickness of the pipe in inches.
            temperature_range (tuple): Temperature range in degrees Celsius.
            pressure_rating (float): Pressure rating in PSI.
        """
        self.name = name
        self.material = material
        self.diameter = diameter
        self.thickness = thickness
        self.temperature_range = temperature_range
        self.pressure_rating = pressure_rating

    def __str__(self):
        return f"Name: {self.name}\nMaterial: {self.material}\nDiameter: {self.diameter} inches\nThickness: {self.thickness} inches\nTemperature Range: {self.temperature_range}°C\nPressure Rating: {self.pressure_rating} PSI"


# Define a class for Inconel Alloy600 Pipes
class InconelAlloy600Pipe(Pipe):
    def __init__(self, diameter, thickness):
        """
        Initialize an Inconel Alloy600 Pipe object.

        Args:
            diameter (float): Diameter of the pipe in inches.
            thickness (float): Thickness of the pipe in inches.
        """
        super().__init__("Inconel Alloy600 Pipe", "Inconel Alloy600", diameter, thickness, (-196, 1093), 1500)


# Define a class for Duplex Steel Pipes
class DuplexSteelPipe(Pipe):
    def __init__(self, diameter, thickness):
        """
        Initialize a Duplex Steel Pipe object.

        Args:
            diameter (float): Diameter of the pipe in inches.
            thickness (float): Thickness of the pipe in inches.
        """
        super().__init__("Duplex Steel Pipe", "Duplex Steel", diameter, thickness, (-20, 300), 1200)


# Function to compare pipe properties
def compare_pipes(pipe1, pipe2):
    """
    Compare properties of two pipes.

    Args:
        pipe1 (Pipe): First pipe object.
        pipe2 (Pipe): Second pipe object.

    Returns:
        dict: Dictionary containing comparison results.
    """
    try:
        comparison_results = {
            "Material": f"{pipe1.material} vs {pipe2.material}",
            "Temperature Range": f"{pipe1.temperature_range}°C vs {pipe2.temperature_range}°C",
            "Pressure Rating": f"{pipe1.pressure_rating} PSI vs {pipe2.pressure_rating} PSI",
            "Diameter": f"{pipe1.diameter} inches vs {pipe2.diameter} inches",
            "Thickness": f"{pipe1.thickness} inches vs {pipe2.thickness} inches",
        }
        return comparison_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        inconel_pipe = InconelAlloy600Pipe(10, 0.5)
        duplex_pipe = DuplexSteelPipe(10, 0.5)

        print("Inconel Alloy600 Pipe Properties:")
        print(inconel_pipe)
        print("\nDuplex Steel Pipe Properties:")
        print(duplex_pipe)

        comparison_results = compare_pipes(inconel_pipe, duplex_pipe)
        print("\nComparison Results:")
        for key, value in comparison_results.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
