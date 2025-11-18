"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Provide a Python script to design a fire protection system using motobombas like RTL-D, as described on the TROMBA website.
Generated: DETERMINISTIC_9dab4614a0a09809
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Fire Protection System Design Using Motobombas (e.g., RTL-D)
This script is a basic implementation to design and simulate a fire protection system
using motobombas, such as those described on the TROMBA website.

Author: [Your Name]
Date: [Insert Date]
"""

import sys

class Motobomba:
    """
    Represents a motobomba used in the fire protection system.
    
    Attributes:
        model (str): The model of the motobomba.
        flow_rate (float): The flow rate of the motobomba in liters per minute.
        pressure (float): The operating pressure of the motobomba in bar.
    """
    def __init__(self, model: str, flow_rate: float, pressure: float):
        self.model = model
        self.flow_rate = flow_rate
        self.pressure = pressure
    
    def __str__(self):
        return f"Motobomba Model: {self.model}, Flow Rate: {self.flow_rate} L/min, Pressure: {self.pressure} bar"


class FireProtectionSystem:
    """
    Represents the fire protection system.

    Attributes:
        motobombas (list): A list of Motobomba objects used in the system.
        target_flow_rate (float): The required flow rate for the system in liters per minute.
        target_pressure (float): The required operating pressure for the system in bar.
    """
    def __init__(self, target_flow_rate: float, target_pressure: float):
        self.motobombas = []
        self.target_flow_rate = target_flow_rate
        self.target_pressure = target_pressure

    def add_motobomba(self, motobomba: Motobomba):
        """
        Adds a motobomba to the system.
        
        Args:
            motobomba (Motobomba): The motobomba to be added.
        """
        self.motobombas.append(motobomba)

    def calculate_total_flow_rate(self) -> float:
        """
        Calculates the total flow rate provided by all motobombas.
        
        Returns:
            float: The total flow rate in liters per minute.
        """
        return sum(motobomba.flow_rate for motobomba in self.motobombas)

    def validate_system(self) -> bool:
        """
        Validates if the system meets the target flow rate and pressure.
        
        Returns:
            bool: True if the system is valid, False otherwise.
        """
        total_flow_rate = self.calculate_total_flow_rate()
        if total_flow_rate >= self.target_flow_rate and all(motobomba.pressure >= self.target_pressure for motobomba in self.motobombas):
            return True
        return False

    def display_system_info(self):
        """
        Displays information about the fire protection system's configuration.
        """
        print("Fire Protection System Configuration:")
        for motobomba in self.motobombas:
            print(motobomba)
        print(f"Target Flow Rate: {self.target_flow_rate} L/min")
        print(f"Target Pressure: {self.target_pressure} bar")
        print(f"Total Flow Rate: {self.calculate_total_flow_rate()} L/min")
        print(f"System Valid: {'Yes' if self.validate_system() else 'No'}")


def main():
    """
    Main function to set up and simulate the fire protection system.
    """
    try:
        # Define target system requirements
        target_flow_rate = 5000  # in liters per minute
        target_pressure = 8.0   # in bar

        # Initialize fire protection system
        system = FireProtectionSystem(target_flow_rate, target_pressure)

        # Add motobombas to the system
        system.add_motobomba(Motobomba("RTL-D1", 2500, 8.5))
        system.add_motobomba(Motobomba("RTL-D2", 3000, 9.0))

        # Display system configuration and validation results
        system.display_system_info()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
