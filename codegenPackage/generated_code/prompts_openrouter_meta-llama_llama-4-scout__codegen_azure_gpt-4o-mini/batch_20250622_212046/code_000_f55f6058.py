"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: "Design a water filtration system for a large industrial application using NF technology, considering the benefits of low pressure and high efficiency."
Generated: DETERMINISTIC_f55f6058dc92ae03
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WaterFiltrationSystem:
    """
    A class to represent a water filtration system using Nanofiltration (NF) technology.
    
    Attributes:
        flow_rate (float): The flow rate of water in liters per minute.
        pressure (float): The operating pressure in bar.
        efficiency (float): The filtration efficiency as a percentage.
    """

    def __init__(self, flow_rate: float, pressure: float, efficiency: float):
        """
        Initializes the water filtration system with specified parameters.
        
        Args:
            flow_rate (float): The flow rate of water in liters per minute.
            pressure (float): The operating pressure in bar.
            efficiency (float): The filtration efficiency as a percentage.
        
        Raises:
            ValueError: If any of the parameters are negative or zero.
        """
        if flow_rate <= 0 or pressure <= 0 or efficiency <= 0:
            raise ValueError("Flow rate, pressure, and efficiency must be positive values.")
        
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.efficiency = efficiency

    def filter_water(self, input_volume: float) -> float:
        """
        Filters a given volume of water using the NF technology.
        
        Args:
            input_volume (float): The volume of water to be filtered in liters.
        
        Returns:
            float: The volume of filtered water in liters.
        
        Raises:
            ValueError: If input_volume is negative or zero.
        """
        if input_volume <= 0:
            raise ValueError("Input volume must be a positive value.")
        
        # Calculate the volume of water that can be filtered based on efficiency
        filtered_volume = input_volume * (self.efficiency / 100)
        
        # Ensure that the filtered volume does not exceed the flow rate capacity
        if filtered_volume > self.flow_rate:
            filtered_volume = self.flow_rate
        
        return filtered_volume

    def display_system_info(self):
        """
        Displays the current configuration of the water filtration system.
        """
        print(f"Water Filtration System Configuration:")
        print(f"Flow Rate: {self.flow_rate} L/min")
        print(f"Operating Pressure: {self.pressure} bar")
        print(f"Filtration Efficiency: {self.efficiency}%")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the water filtration system
        filtration_system = WaterFiltrationSystem(flow_rate=100.0, pressure=5.0, efficiency=90.0)
        
        # Display system information
        filtration_system.display_system_info()
        
        # Filter a specific volume of water
        input_volume = 200.0  # Volume in liters
        filtered_volume = filtration_system.filter_water(input_volume)
        print(f"Filtered Volume: {filtered_volume} L")
        
    except ValueError as e:
        print(f"Error: {e}")
```
