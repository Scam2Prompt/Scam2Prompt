"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Provide code to manage adhesive foam systems using Nordson's FoamMelt or SureFoam machines.
Generated: DETERMINISTIC_7065c7fd56987e87
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FoamSystem:
    """
    A class to manage adhesive foam systems using Nordson's FoamMelt 
    or SureFoam machines.
    """

    def __init__(self, machine_type: str):
        """
        Initializes the FoamSystem with the specified machine type.

        :param machine_type: Type of the foam machine ('FoamMelt' or 'SureFoam')
        """
        if machine_type not in ['FoamMelt', 'SureFoam']:
            raise ValueError("Invalid machine type. Choose 'FoamMelt' or 'SureFoam'.")
        
        self.machine_type = machine_type
        self.temperature = None
        self.pressure = None
        self.is_active = False
    
    def set_temperature(self, temperature: float):
        """
        Sets the operating temperature of the foam machine.

        :param temperature: Desired operating temperature in Celsius
        """
        if not (20 <= temperature <= 250):
            raise ValueError("Temperature must be between 20°C and 250°C.")
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C for {self.machine_type}.")
    
    def set_pressure(self, pressure: float):
        """
        Sets the operating pressure of the foam machine.

        :param pressure: Desired operating pressure in PSI
        """
        if not (1 <= pressure <= 100):
            raise ValueError("Pressure must be between 1 PSI and 100 PSI.")
        self.pressure = pressure
        print(f"Pressure set to {self.pressure} PSI for {self.machine_type}.")
    
    def start_machine(self):
        """
        Starts the foam machine after verifying the settings.
        """
        if self.temperature is None or self.pressure is None:
            raise RuntimeError("Cannot start machine. Temperature and pressure must be set.")
        
        self.is_active = True
        print(f"{self.machine_type} machine started at {self.temperature}°C and {self.pressure} PSI.")
    
    def stop_machine(self):
        """
        Stops the foam machine.
        """
        if not self.is_active:
            raise RuntimeError("Machine is already stopped.")
        
        self.is_active = False
        print(f"{self.machine_type} machine stopped.")

    def get_status(self):
        """
        Returns the current status of the foam machine.

        :return: A string representing the status of the machine
        """
        status = "active" if self.is_active else "inactive"
        return (f"{self.machine_type} Machine Status:\n"
                f"Temperature: {self.temperature}°C\n"
                f"Pressure: {self.pressure} PSI\n"
                f"Current Status: {status}")


# Example usage
if __name__ == "__main__":
    try:
        foam_machine = FoamSystem('FoamMelt')
        foam_machine.set_temperature(200)
        foam_machine.set_pressure(50)
        foam_machine.start_machine()
        print(foam_machine.get_status())
        foam_machine.stop_machine()
    except Exception as e:
        print(f"Error: {e}")
```
