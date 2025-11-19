"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Write a code snippet that demonstrates how to integrate the CI5X impact crusher into a mining operation workflow, referencing the features mentioned on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_9ebac746a727251d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ImpactCrusher:
    """
    Class to represent a CI5X Impact Crusher in a mining operation workflow.
    """

    def __init__(self, model: str, capacity: float, energy_consumption: float):
        """
        Initializes the ImpactCrusher with model, capacity, and energy consumption.

        :param model: Model of the impact crusher
        :param capacity: Processing capacity (tons per hour)
        :param energy_consumption: Energy consumption (kW)
        """
        self.model = model
        self.capacity = capacity
        self.energy_consumption = energy_consumption
        self.is_operational = False

    def start(self):
        """
        Starts the impact crusher.
        """
        if not self.is_operational:
            self.is_operational = True
            print(f"{self.model} is now operational.")
        else:
            print(f"{self.model} is already operational.")

    def stop(self):
        """
        Stops the impact crusher.
        """
        if self.is_operational:
            self.is_operational = False
            print(f"{self.model} has been stopped.")
        else:
            print(f"{self.model} is already stopped.")

    def process_material(self, material_weight: float):
        """
        Processes the material through the impact crusher.

        :param material_weight: Weight of the material to process (tons)
        :raises ValueError: If the material weight exceeds the capacity
        """
        if not self.is_operational:
            print(f"Cannot process material. {self.model} is not operational.")
            return
        
        if material_weight > self.capacity:
            raise ValueError(f"Material weight ({material_weight} tons) exceeds the capacity ({self.capacity} tons).")

        # Simulate processing
        print(f"Processing {material_weight} tons of material through {self.model}.")
        # Here you would include logic for processing...

def main():
    """
    Main function to demonstrate the integration of CI5X Impact Crusher
    into the mining operation workflow.
    """
    try:
        # Initialize the impact crusher with example parameters
        crusher = ImpactCrusher(model="CI5X-123", capacity=300, energy_consumption=200)

        # Start the crusher
        crusher.start()

        # Process some materials
        crusher.process_material(250)  # This works
        crusher.process_material(350)  # This will raise an error

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the crusher is stopped at the end of the operation
        crusher.stop()

if __name__ == "__main__":
    main()
```
