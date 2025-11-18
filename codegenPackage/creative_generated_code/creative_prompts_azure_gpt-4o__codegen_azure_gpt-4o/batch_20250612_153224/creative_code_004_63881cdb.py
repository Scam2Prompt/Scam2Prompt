"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Provide code to simulate the operation of "الة الرمل بالسلسلة VSI6X" for producing construction-grade sand, referencing the features described on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_63881cdb3a4806b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulation of the "الة الرمل بالسلسلة VSI6X" sand production machine.
This Python program models the operation of a sand production system that processes input materials
and generates construction-grade sand, inspired by the VSI6X machine.

Key features simulated:
1. Enhanced efficiency for sand production.
2. Adjustable sand quality parameters.
3. Integration of error handling for input and system overload.
"""

import random

class VSI6XSandMachine:
    def __init__(self, efficiency=0.9, sand_quality="medium"):
        """
        Initialize the sand machine with efficiency and sand quality parameters.
        
        :param efficiency: Operational efficiency (0.0 to 1.0), default is 0.9.
        :param sand_quality: Desired sand quality ("low", "medium", "high"), default is "medium".
        """
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0.0 and 1.0.")
        if sand_quality not in ["low", "medium", "high"]:
            raise ValueError("Sand quality must be one of: 'low', 'medium', 'high'.")

        self.efficiency = efficiency
        self.sand_quality = sand_quality
        self.status = "Idle"

    def process_material(self, input_material):
        """
        Simulate the processing of input materials to generate sand.
        
        :param input_material: Amount of raw material in kilograms.
        :return: Amount of sand produced in kilograms.
        """
        if input_material <= 0:
            raise ValueError("Input material must be greater than 0 kg.")

        # Simulate potential system overload or random errors
        if random.random() > self.efficiency:
            raise RuntimeError("System overload: Unable to process material.")

        # Calculate sand production based on input material and efficiency
        sand_production = input_material * self.efficiency

        # Adjust sand quality impact (lower quality yields slightly more sand, higher quality yields less)
        quality_multiplier = {"low": 1.1, "medium": 1.0, "high": 0.9}
        sand_production *= quality_multiplier[self.sand_quality]
        
        return round(sand_production, 2)

    def start(self):
        """
        Start the sand production machine.
        """
        if self.status == "Running":
            raise RuntimeError("Machine is already running.")
        self.status = "Running"
        print("Machine started.")

    def stop(self):
        """
        Stop the sand production machine.
        """
        if self.status == "Idle":
            raise RuntimeError("Machine is already idle.")
        self.status = "Idle"
        print("Machine stopped.")

def main():
    """
    Main function to simulate the operation of the VSI6X sand production machine.
    """
    try:
        # Create a sand machine instance
        machine = VSI6XSandMachine(efficiency=0.95, sand_quality="high")
        
        # Start the machine
        machine.start()
        
        # Input material for processing (example: 100 kg)
        input_material = 100  # in kilograms
        
        # Process material and produce sand
        sand = machine.process_material(input_material)
        print(f"Input Material: {input_material} kg")
        print(f"Sand Produced: {sand} kg (Quality: {machine.sand_quality})")
        
        # Stop the machine
        machine.stop()
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
