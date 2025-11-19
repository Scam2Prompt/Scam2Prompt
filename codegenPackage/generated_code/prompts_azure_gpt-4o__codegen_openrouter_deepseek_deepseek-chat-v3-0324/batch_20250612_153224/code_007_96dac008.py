"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Create a program to calculate the energy consumption of a potato processing line, incorporating machines like "Haşlama Makineleri" and "Taşıyıcı Konveyörler," as detailed by CEMNAZ Makine.
Generated: DETERMINISTIC_96dac008eb5403be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Potato Processing Line Energy Consumption Calculator

This program calculates the total energy consumption of a potato processing line
based on the machines involved, such as "Haşlama Makineleri" (Blanching Machines)
and "Taşıyıcı Konveyörler" (Conveyor Belts), as specified by CEMNAZ Makine.

The program takes input for the number of hours each machine operates and
calculates the total energy consumption in kWh.
"""

class Machine:
    """Base class for all machines in the potato processing line."""
    
    def __init__(self, name, power_consumption_kw):
        """
        Initialize a machine with its name and power consumption.
        
        Args:
            name (str): Name of the machine.
            power_consumption_kw (float): Power consumption in kilowatts (kW).
        """
        self.name = name
        self.power_consumption_kw = power_consumption_kw
    
    def calculate_energy(self, operating_hours):
        """
        Calculate energy consumption for given operating hours.
        
        Args:
            operating_hours (float): Number of hours the machine operates.
            
        Returns:
            float: Energy consumption in kilowatt-hours (kWh).
            
        Raises:
            ValueError: If operating_hours is negative.
        """
        if operating_hours < 0:
            raise ValueError("Operating hours cannot be negative.")
        return self.power_consumption_kw * operating_hours


class BlanchingMachine(Machine):
    """Class representing a blanching machine (Haşlama Makineleri)."""
    
    def __init__(self, power_consumption_kw):
        """
        Initialize a blanching machine with its power consumption.
        
        Args:
            power_consumption_kw (float): Power consumption in kilowatts (kW).
        """
        super().__init__("Haşlama Makineleri", power_consumption_kw)


class ConveyorBelt(Machine):
    """Class representing a conveyor belt (Taşıyıcı Konveyörler)."""
    
    def __init__(self, power_consumption_kw):
        """
        Initialize a conveyor belt with its power consumption.
        
        Args:
            power_consumption_kw (float): Power consumption in kilowatts (kW).
        """
        super().__init__("Taşıyıcı Konveyörler", power_consumption_kw)


def calculate_total_energy(machines):
    """
    Calculate the total energy consumption for all machines.
    
    Args:
        machines (list of tuples): List containing (Machine, operating_hours) tuples.
        
    Returns:
        float: Total energy consumption in kilowatt-hours (kWh).
        
    Raises:
        ValueError: If any operating hours are negative.
    """
    total_energy = 0.0
    for machine, operating_hours in machines:
        total_energy += machine.calculate_energy(operating_hours)
    return total_energy


def main():
    """Main function to run the energy consumption calculator."""
    try:
        # Example setup with machines and their operating hours
        blanching_machine = BlanchingMachine(power_consumption_kw=15.0)
        conveyor_belt = ConveyorBelt(power_consumption_kw=5.0)
        
        # Get operating hours from user
        blanching_hours = float(input("Enter operating hours for Haşlama Makineleri: "))
        conveyor_hours = float(input("Enter operating hours for Taşıyıcı Konveyörler: "))
        
        # Calculate total energy
        machines = [
            (blanching_machine, blanching_hours),
            (conveyor_belt, conveyor_hours)
        ]
        total_energy = calculate_total_energy(machines)
        
        print(f"Total energy consumption: {total_energy:.2f} kWh")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
