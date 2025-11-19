"""
Generated Code Metadata:
========================
Original URL: https://www.sardiniameetsazores.eu
Prompt: Provide code to simulate the operation of "الة الرمل بالسلسلة VSI6X" for producing construction-grade sand, referencing the features described on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_63881cdb3a4806b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VSI6XSandMaker:
    """
    A class to simulate the operation of the VSI6X sand making machine for producing construction-grade sand.
    """

    def __init__(self, input_material: float):
        """
        Initializes the VSI6X sand maker with the given amount of input material.

        :param input_material: The amount of raw material (in tons) to be processed.
        """
        if input_material <= 0:
            raise ValueError("Input material must be a positive number.")
        self.input_material = input_material
        self.output_sand = 0.0

    def crush_material(self):
        """
        Simulates the crushing process of the input material to produce sand.
        The crushing efficiency is assumed to be 80%.
        """
        try:
            crushing_efficiency = 0.8
            self.output_sand = self.input_material * crushing_efficiency
            print(f"Crushed {self.input_material} tons of material to produce {self.output_sand} tons of sand.")
        except Exception as e:
            print(f"An error occurred during the crushing process: {e}")

    def screen_sand(self):
        """
        Simulates the screening process to ensure the sand meets construction-grade specifications.
        The screening efficiency is assumed to be 90%.
        """
        try:
            screening_efficiency = 0.9
            screened_sand = self.output_sand * screening_efficiency
            print(f"Screened sand: {screened_sand} tons meet construction-grade specifications.")
            return screened_sand
        except Exception as e:
            print(f"An error occurred during the screening process: {e}")
            return 0.0

    def produce_sand(self):
        """
        Simulates the complete process of producing construction-grade sand.
        """
        try:
            self.crush_material()
            final_sand = self.screen_sand()
            print(f"Total construction-grade sand produced: {final_sand} tons.")
            return final_sand
        except Exception as e:
            print(f"An error occurred during the sand production process: {e}")
            return 0.0


if __name__ == "__main__":
    try:
        # Example usage of the VSI6X sand maker
        input_material = 100.0  # tons of raw material
        sand_maker = VSI6XSandMaker(input_material)
        sand_maker.produce_sand()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
