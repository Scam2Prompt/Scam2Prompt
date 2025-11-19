"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write Python code to simulate the functionality of a hydraulic breaker attachment for excavators, referencing the specifications and use cases described on the PT. Fuji Metal Teknik website.
Generated: DETERMINISTIC_30359127310aba20
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicBreaker:
    """
    A class to simulate the functionality of a hydraulic breaker attachment for excavators.
    
    Attributes:
        pressure (float): The hydraulic pressure in bars.
        impact_energy (float): The energy of the impact in joules.
        operational (bool): Indicates if the breaker is operational.
    """

    def __init__(self, pressure: float, impact_energy: float):
        """
        Initializes the HydraulicBreaker with specified pressure and impact energy.
        
        Args:
            pressure (float): The hydraulic pressure in bars.
            impact_energy (float): The energy of the impact in joules.
        """
        self.pressure = pressure
        self.impact_energy = impact_energy
        self.operational = True

    def activate(self):
        """Activates the hydraulic breaker if it is not already operational."""
        if not self.operational:
            self.operational = True
            print("Hydraulic breaker activated.")
        else:
            print("Hydraulic breaker is already operational.")

    def deactivate(self):
        """Deactivates the hydraulic breaker if it is operational."""
        if self.operational:
            self.operational = False
            print("Hydraulic breaker deactivated.")
        else:
            print("Hydraulic breaker is already deactivated.")

    def apply_impact(self):
        """
        Simulates applying an impact with the hydraulic breaker.
        
        Raises:
            RuntimeError: If the breaker is not operational.
        """
        if not self.operational:
            raise RuntimeError("Cannot apply impact: Hydraulic breaker is not operational.")
        
        # Simulate impact application
        print(f"Applying impact with energy: {self.impact_energy} joules at pressure: {self.pressure} bars.")
        # Here you could add more complex logic related to the impact simulation

    def adjust_pressure(self, new_pressure: float):
        """
        Adjusts the hydraulic pressure of the breaker.
        
        Args:
            new_pressure (float): The new hydraulic pressure in bars.
        
        Raises:
            ValueError: If the new pressure is not within acceptable limits.
        """
        if new_pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        
        self.pressure = new_pressure
        print(f"Hydraulic pressure adjusted to: {self.pressure} bars.")

    def set_impact_energy(self, new_energy: float):
        """
        Sets the impact energy of the breaker.
        
        Args:
            new_energy (float): The new impact energy in joules.
        
        Raises:
            ValueError: If the new energy is not positive.
        """
        if new_energy <= 0:
            raise ValueError("Impact energy must be positive.")
        
        self.impact_energy = new_energy
        print(f"Impact energy set to: {self.impact_energy} joules.")

# Example usage
if __name__ == "__main__":
    try:
        breaker = HydraulicBreaker(150, 1000)
        breaker.activate()
        breaker.apply_impact()
        breaker.adjust_pressure(200)
        breaker.set_impact_energy(1200)
        breaker.deactivate()
    except Exception as e:
        print(f"An error occurred: {e}")
```
