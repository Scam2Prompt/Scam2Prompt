"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: What are the best practices for utilizing a chaff cutter in agricultural settings, based on the information provided by Vinglob Greentech?
Generated: DETERMINISTIC_8a89fec033bea2f6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ChaffCutter:
    """
    A class to represent a chaff cutter in agricultural settings.
    """

    def __init__(self, model: str, power: int, capacity: int):
        """
        Initializes the chaff cutter with model, power, and capacity.

        :param model: The model of the chaff cutter.
        :param power: The power of the chaff cutter in watts.
        :param capacity: The capacity of the chaff cutter in kg/hour.
        """
        self.model = model
        self.power = power
        self.capacity = capacity
        self.is_operational = False

    def start(self):
        """
        Starts the chaff cutter if it is not already operational.
        """
        if not self.is_operational:
            self.is_operational = True
            print(f"{self.model} is now operational.")
        else:
            print(f"{self.model} is already running.")

    def stop(self):
        """
        Stops the chaff cutter if it is operational.
        """
        if self.is_operational:
            self.is_operational = False
            print(f"{self.model} has been stopped.")
        else:
            print(f"{self.model} is not running.")

    def process_material(self, weight: int):
        """
        Processes the given weight of material through the chaff cutter.

        :param weight: The weight of the material to be processed in kg.
        :raises ValueError: If the weight exceeds the capacity or if the cutter is not operational.
        """
        if not self.is_operational:
            raise ValueError(f"{self.model} must be operational to process material.")
        
        if weight > self.capacity:
            raise ValueError(f"Weight exceeds capacity of {self.capacity} kg/hour.")
        
        print(f"Processing {weight} kg of material with {self.model}.")

    def maintenance_check(self):
        """
        Performs a maintenance check on the chaff cutter.
        """
        print(f"Performing maintenance check on {self.model}. All systems operational.")

def main():
    """
    Main function to demonstrate the usage of the ChaffCutter class.
    """
    try:
        # Create an instance of ChaffCutter
        cutter = ChaffCutter(model="Vinglob 3000", power=1500, capacity=500)

        # Start the chaff cutter
        cutter.start()

        # Process some material
        cutter.process_material(300)

        # Perform maintenance check
        cutter.maintenance_check()

        # Stop the chaff cutter
        cutter.stop()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
