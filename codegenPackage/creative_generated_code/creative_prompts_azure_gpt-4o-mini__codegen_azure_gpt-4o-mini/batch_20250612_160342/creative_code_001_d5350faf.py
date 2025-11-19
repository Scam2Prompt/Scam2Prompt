"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: How can I use Vertiv's cooling solutions in a data center setup? Provide a sample configuration code.
Generated: DETERMINISTIC_d5350faf5883a86a
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DataCenterCoolingSystem:
    """
    A class to represent a cooling system for a data center using Vertiv's solutions.
    """

    def __init__(self, cooling_capacity, ambient_temp, desired_temp):
        """
        Initializes the cooling system with specified parameters.

        Args:
            cooling_capacity (float): Maximum cooling capacity in kW.
            ambient_temp (float): Current ambient temperature in degrees Celsius.
            desired_temp (float): Desired temperature for the data center in degrees Celsius.
        """
        self.cooling_capacity = cooling_capacity
        self.ambient_temp = ambient_temp
        self.desired_temp = desired_temp
        self.current_temp = ambient_temp

    def activate_cooling(self):
        """
        Activates the cooling system to maintain the desired temperature.
        
        Raises:
            ValueError: If the desired temperature is above ambient temperature.
        """
        if self.desired_temp > self.ambient_temp:
            raise ValueError("Desired temperature must be less than ambient temperature.")

        print(f"Activating cooling system with {self.cooling_capacity} kW capacity.")
        self.current_temp = self.desired_temp
        print(f"Current temperature adjusted to {self.current_temp}°C.")

    def monitor_temperature(self):
        """
        Monitors the current temperature of the data center.
        
        Returns:
            float: Current temperature in degrees Celsius.
        """
        print(f"Current temperature is {self.current_temp}°C.")
        return self.current_temp

    def adjust_cooling_capacity(self, new_capacity):
        """
        Adjusts the cooling capacity of the system.
        
        Args:
            new_capacity (float): New cooling capacity in kW.
        
        Raises:
            ValueError: If new capacity is not a positive number.
        """
        if new_capacity <= 0:
            raise ValueError("Cooling capacity must be a positive number.")
        self.cooling_capacity = new_capacity
        print(f"Cooling capacity adjusted to {self.cooling_capacity} kW.")

def main():
    """
    Main function to demonstrate the usage of the DataCenterCoolingSystem class.
    """
    try:
        # Sample configuration for the data center cooling system
        cooling_system = DataCenterCoolingSystem(cooling_capacity=50, ambient_temp=30, desired_temp=20)
        
        # Activating cooling
        cooling_system.activate_cooling()
        
        # Monitoring temperature
        cooling_system.monitor_temperature()
        
        # Adjusting cooling capacity
        cooling_system.adjust_cooling_capacity(75)
        
        # Activating cooling again
        cooling_system.activate_cooling()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
