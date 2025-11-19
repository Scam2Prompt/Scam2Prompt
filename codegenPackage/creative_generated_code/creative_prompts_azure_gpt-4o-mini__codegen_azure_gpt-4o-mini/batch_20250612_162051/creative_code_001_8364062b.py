"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Generate a code snippet that demonstrates how to use VinaRoy's air blower models in a system for transporting bulk materials.
Generated: DETERMINISTIC_8364062bdd98fa27
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import random

class AirBlower:
    """
    Class to represent an air blower model for transporting bulk materials.
    """

    def __init__(self, model_name: str, airflow_capacity: float):
        """
        Initializes the air blower with its model name and airflow capacity.

        :param model_name: Name of the air blower model
        :param airflow_capacity: Maximum airflow capacity in cubic meters per hour
        """
        self.model_name = model_name
        self.airflow_capacity = airflow_capacity  # m³/h
        self.is_running = False

    def start(self):
        """Starts the air blower."""
        if not self.is_running:
            self.is_running = True
            print(f"{self.model_name} started.")
        else:
            print(f"{self.model_name} is already running.")

    def stop(self):
        """Stops the air blower."""
        if self.is_running:
            self.is_running = False
            print(f"{self.model_name} stopped.")
        else:
            print(f"{self.model_name} is already stopped.")

    def blow_material(self, material_weight: float):
        """
        Simulates blowing bulk materials using the air blower.

        :param material_weight: Weight of the material to be transported in kilograms
        :raises ValueError: If the material weight exceeds a reasonable limit
        """
        if material_weight <= 0:
            raise ValueError("Material weight must be greater than zero.")
        
        if material_weight > 10000:  # Example limit for bulk material weight
            raise ValueError("Material weight exceeds the allowable limit for this blower.")

        # Simulate the blowing process
        self.start()
        time_to_blow = material_weight / (self.airflow_capacity / 3600)  # Time in seconds
        print(f"Blowing {material_weight}kg of material...")
        time.sleep(min(time_to_blow, 10))  # Wait, limit max wait time to 10 seconds for simulation
        self.stop()

def main():
    """
    Main function to simulate the use of VinaRoy's air blower models.
    """
    try:
        # Create an instance of AirBlower
        blower = AirBlower(model_name="VinaRoy X200", airflow_capacity=500)

        # Simulate blowing different materials
        for weight in [500, 15000, -100]:  # Test with varying weights, including invalid cases
            try:
                print(f"Attempting to blow {weight} kg of material...")
                blower.blow_material(weight)
            except ValueError as e:
                print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
