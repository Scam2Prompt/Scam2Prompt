"""
Generated Code Metadata:
========================
Original URL: https://www.sardiniameetsazores.eu
Prompt: Write a code snippet that demonstrates how to integrate the CI5X impact crusher into a mining operation workflow, referencing the features mentioned on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_9ebac746a727251d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CI5XImpactCrusher:
    """
    A class to represent the CI5X Impact Crusher in a mining operation workflow.
    """

    def __init__(self, capacity, power, weight):
        """
        Initializes the CI5X Impact Crusher with specified parameters.

        :param capacity: The processing capacity of the crusher (tons/hour)
        :param power: The power consumption of the crusher (kW)
        :param weight: The weight of the crusher (kg)
        """
        self.capacity = capacity
        self.power = power
        self.weight = weight
        self.is_operational = False

    def start(self):
        """
        Starts the CI5X Impact Crusher.
        """
        if not self.is_operational:
            self.is_operational = True
            print("CI5X Impact Crusher started.")
        else:
            print("CI5X Impact Crusher is already operational.")

    def stop(self):
        """
        Stops the CI5X Impact Crusher.
        """
        if self.is_operational:
            self.is_operational = False
            print("CI5X Impact Crusher stopped.")
        else:
            print("CI5X Impact Crusher is not operational.")

    def process_material(self, material_weight):
        """
        Processes the given weight of material through the crusher.

        :param material_weight: The weight of the material to be processed (kg)
        :raises ValueError: If the material weight exceeds the capacity of the crusher
        """
        if not self.is_operational:
            raise RuntimeError("CI5X Impact Crusher is not operational. Please start the crusher first.")

        if material_weight > self.capacity * 1000:  # Convert tons to kg
            raise ValueError("Material weight exceeds the crusher's capacity.")

        print(f"Processing {material_weight} kg of material...")

    def get_status(self):
        """
        Returns the operational status of the CI5X Impact Crusher.

        :return: Operational status (True/False)
        """
        return self.is_operational


def main():
    """
    Main function to demonstrate the integration of the CI5X Impact Crusher
    into a mining operation workflow.
    """
    try:
        # Initialize the CI5X Impact Crusher with example parameters
        crusher = CI5XImpactCrusher(capacity=200, power=400, weight=30000)

        # Start the crusher
        crusher.start()

        # Process a sample material weight
        sample_material_weight = 150000  # in kg
        crusher.process_material(sample_material_weight)

        # Stop the crusher
        crusher.stop()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
