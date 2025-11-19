"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Generate code to calculate the fuel consumption of an MG car model (e.g., NSE 1.5L engine with 5.3L/100km) over a given distance in kilometers.
Generated: DETERMINISTIC_b6c9e18abfd8dcaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FuelConsumptionCalculator:
    """
    A class to calculate fuel consumption for MG car models.
    
    Attributes:
        model (str): The car model name
        engine (str): The engine specification
        consumption_rate (float): Fuel consumption rate in liters per 100 km
    """
    
    def __init__(self, model: str, engine: str, consumption_rate: float):
        """
        Initialize the calculator with car specifications.
        
        Args:
            model: Name of the car model (e.g., "NSE")
            engine: Engine specification (e.g., "1.5L")
            consumption_rate: Fuel consumption rate in L/100km (e.g., 5.3)
        """
        self.model = model
        self.engine = engine
        self.consumption_rate = consumption_rate
        
    def calculate_fuel(self, distance: float) -> float:
        """
        Calculate fuel consumption for a given distance.
        
        Args:
            distance: Distance to travel in kilometers
            
        Returns:
            float: Fuel required in liters
            
        Raises:
            ValueError: If distance is negative
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        return (self.consumption_rate * distance) / 100
    
    def get_model_info(self) -> str:
        """
        Get formatted car model information.
        
        Returns:
            str: Formatted string with model and engine info
        """
        return f"MG {self.model} ({self.engine} engine)"


def main():
    try:
        # Example usage with MG NSE 1.5L engine
        calculator = FuelConsumptionCalculator(
            model="NSE",
            engine="1.5L",
            consumption_rate=5.3
        )
        
        print(f"Fuel consumption calculator for {calculator.get_model_info()}")
        
        while True:
            try:
                distance = float(input("Enter distance in kilometers (or 0 to exit): "))
                if distance == 0:
                    print("Exiting...")
                    break
                
                fuel_needed = calculator.calculate_fuel(distance)
                print(f"Fuel needed for {distance} km: {fuel_needed:.2f} liters")
                
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid positive number.")
                
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
