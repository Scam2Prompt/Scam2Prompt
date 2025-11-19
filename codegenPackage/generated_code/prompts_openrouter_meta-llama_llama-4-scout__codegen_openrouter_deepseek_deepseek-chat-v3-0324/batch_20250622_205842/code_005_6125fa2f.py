"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "Write a Python code snippet to calculate the optimal tire pressure for a given industrial equipment, considering factors like load capacity and temperature."
Generated: DETERMINISTIC_6125fa2f8d2735ec
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class TirePressureCalculator:
    """
    A class to calculate optimal tire pressure for industrial equipment based on load and temperature.
    
    Attributes:
        base_pressure (float): Base tire pressure in PSI at standard conditions (20°C, no load).
        max_load_capacity (float): Maximum load capacity in kg the tire can handle at base pressure.
        temperature_coefficient (float): Coefficient for temperature adjustment (PSI/°C).
    """
    
    def __init__(self, base_pressure, max_load_capacity, temperature_coefficient=0.1):
        """
        Initialize the TirePressureCalculator with base parameters.
        
        Args:
            base_pressure (float): Base tire pressure in PSI at standard conditions.
            max_load_capacity (float): Maximum load capacity in kg at base pressure.
            temperature_coefficient (float, optional): PSI per °C adjustment. Defaults to 0.1.
        """
        self.base_pressure = base_pressure
        self.max_load_capacity = max_load_capacity
        self.temperature_coefficient = temperature_coefficient
    
    def calculate_optimal_pressure(self, current_load, current_temp):
        """
        Calculate optimal tire pressure considering load and temperature.
        
        Args:
            current_load (float): Current load on tire in kg.
            current_temp (float): Current temperature in °C.
            
        Returns:
            float: Optimal tire pressure in PSI.
            
        Raises:
            ValueError: If inputs are invalid (negative values, load exceeds capacity).
        """
        if current_load < 0:
            raise ValueError("Load cannot be negative")
        if current_temp < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        if current_load > self.max_load_capacity:
            raise ValueError(f"Load exceeds maximum capacity of {self.max_load_capacity} kg")
            
        # Calculate load adjustment
        load_factor = current_load / self.max_load_capacity
        load_adjusted_pressure = self.base_pressure * (1 + 0.2 * load_factor)  # 20% increase at max load
        
        # Calculate temperature adjustment
        temp_diff = current_temp - 20  # Difference from standard 20°C
        temp_adjusted_pressure = load_adjusted_pressure + (temp_diff * self.temperature_coefficient)
        
        # Ensure pressure doesn't drop below minimum safe value
        min_pressure = self.base_pressure * 0.8
        optimal_pressure = max(temp_adjusted_pressure, min_pressure)
        
        return round(optimal_pressure, 2)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator for a specific tire
        calculator = TirePressureCalculator(base_pressure=35.0, max_load_capacity=5000.0)
        
        # Calculate optimal pressure for given conditions
        load = 3000.0  # kg
        temp = 25.0    # °C
        optimal_p = calculator.calculate_optimal_pressure(load, temp)
        
        print(f"Optimal tire pressure: {optimal_p} PSI")
    except ValueError as e:
        print(f"Error: {e}")
```
