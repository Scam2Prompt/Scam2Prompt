"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Write Python code to simulate the functionality of a hydraulic breaker attachment for excavators, referencing the specifications and use cases described on the PT. Fuji Metal Teknik website.
Generated: DETERMINISTIC_30359127310aba20
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HydraulicBreaker:
    """
    A class representing a hydraulic breaker attachment for excavators.
    
    Attributes:
        weight (float): The weight of the hydraulic breaker in kilograms.
        impact_energy (float): The energy delivered by the breaker in joules.
        frequency (int): The number of impacts per minute.
        operational_status (bool): Indicates if the breaker is operational.
    """

    def __init__(self, weight: float, impact_energy: float, frequency: int):
        """
        Initializes the HydraulicBreaker with specified weight, impact energy, and frequency.
        
        Parameters:
            weight (float): The weight of the breaker.
            impact_energy (float): The impact energy delivered by the breaker.
            frequency (int): The frequency of impacts per minute.
        """
        self.weight = weight
        self.impact_energy = impact_energy
        self.frequency = frequency
        self.operational_status = False

    def start(self):
        """Starts the hydraulic breaker and sets its operational status to True."""
        if not self.operational_status:
            self.operational_status = True
            print("Hydraulic breaker started.")
        else:
            print("Hydraulic breaker is already operational.")

    def stop(self):
        """Stops the hydraulic breaker and sets its operational status to False."""
        if self.operational_status:
            self.operational_status = False
            print("Hydraulic breaker stopped.")
        else:
            print("Hydraulic breaker is not operational.")

    def calculate_output(self) -> float:
        """
        Calculates the output power of the hydraulic breaker.
        
        Returns:
            float: The output power in watts, or raises an error if not operational.
        """
        if not self.operational_status:
            raise RuntimeError("Cannot calculate output: Hydraulic breaker is not operational.")
        
        # Output power calculation (in watts): P = E * f
        power = self.impact_energy * (self.frequency / 60)  # frequency in Hz
        return power

    def __str__(self):
        """Returns a string representation of the hydraulic breaker."""
        return (f"Hydraulic Breaker - Weight: {self.weight} kg, "
                f"Impact Energy: {self.impact_energy} J, "
                f"Frequency: {self.frequency} impacts/min, "
                f"Operational: {self.operational_status}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a hydraulic breaker instance with specific parameters
        breaker = HydraulicBreaker(weight=500.0, impact_energy=1500.0, frequency=600)
        
        # Start the hydraulic breaker
        breaker.start()
        
        # Calculate and print output power
        output_power = breaker.calculate_output()
        print(f"Output Power: {output_power:.2f} W")
        
        # Print details about the breaker
        print(breaker)
        
        # Stop the hydraulic breaker
        breaker.stop()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
