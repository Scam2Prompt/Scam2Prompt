"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write code to simulate the application of sublimation on various materials like glass, ceramic, and polyester, as outlined by CreatexPro.
Generated: DETERMINISTIC_a63e22117e71a4c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Material:
    """Class representing a material that can undergo sublimation."""
    
    def __init__(self, name: str, sublimation_temp: float, sublimation_rate: float):
        """
        Initialize a Material instance.
        
        Args:
            name (str): The name of the material.
            sublimation_temp (float): The temperature at which sublimation occurs (in Celsius).
            sublimation_rate (float): The rate of sublimation (material loss per minute).
        """
        self.name = name
        self.sublimation_temp = sublimation_temp
        self.sublimation_rate = sublimation_rate
        self.is_sublimated = False

    def apply_sublimation(self, temperature: float, duration: int) -> None:
        """
        Simulate the sublimation process on the material.
        
        Args:
            temperature (float): The temperature applied to the material (in Celsius).
            duration (int): The duration of sublimation (in minutes).
        
        Raises:
            ValueError: If the temperature is below zero or duration is negative.
        """
        if temperature < 0:
            raise ValueError("Temperature must be above absolute zero.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        
        # Check if the temperature is sufficient for sublimation
        if temperature >= self.sublimation_temp:
            sublimation_amount = self.sublimation_rate * duration
            print(f"Applying sublimation on {self.name} for {duration} minutes.")
            print(f"Sublimation rate: {self.sublimation_rate} units/min, total loss: {sublimation_amount} units.")
            self.is_sublimated = True
        else:
            print(f"{self.name} did not sublimate. Insufficient temperature: {temperature}C.")

class SublimationSimulator:
    """Class to simulate sublimation on various materials."""
    
    def __init__(self, materials: List[Material]):
        """
        Initialize a SublimationSimulator instance.
        
        Args:
            materials (List[Material]): List of materials to simulate.
        """
        self.materials = materials

    def simulate(self, temperature: float, duration: int) -> None:
        """
        Simulate sublimation for all materials at given temperature and duration.
        
        Args:
            temperature (float): The temperature for sublimation (in Celsius).
            duration (int): The duration for sublimation (in minutes).
        """
        for material in self.materials:
            try:
                material.apply_sublimation(temperature, duration)
            except ValueError as e:
                print(f"Error for material {material.name}: {e}")

# Example materials based on CreatexPro guidelines
materials = [
    Material("Glass", sublimation_temp=500.0, sublimation_rate=0.1),
    Material("Ceramic", sublimation_temp=600.0, sublimation_rate=0.05),
    Material("Polyester", sublimation_temp=200.0, sublimation_rate=0.2),
]

# Initialize the simulator with the materials
simulator = SublimationSimulator(materials)

# Run the simulation with a specific temperature and duration
try:
    # Example temperature and duration
    simulator.simulate(250.0, 10)  # 250°C for 10 minutes
except Exception as e:
    print(f"Simulation failed: {e}")
```
