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
class VSI6XSandMaker:
    """
    A class to simulate the operation of "الة الرمل بالسلسلة VSI6X" for producing construction-grade sand.
    This class models the sand production process with parameters for raw material, processing, and output.
    """

    def __init__(self, raw_material: float):
        """
        Initialize the VSI6X Sand Maker with the specified amount of raw material.

        :param raw_material: The initial quantity of raw material in tons.
        """
        if raw_material < 0:
            raise ValueError("Raw material quantity cannot be negative.")
        
        self.raw_material = raw_material  # Initial amount of raw material
        self.processed_material = 0.0      # Amount of material processed
        self.sand_output = 0.0              # Amount of sand produced

    def process_material(self, efficiency: float):
        """
        Process the raw material to produce construction-grade sand.

        :param efficiency: The efficiency of the VSI6X sand maker (0 to 1).
        :raises ValueError: If efficiency is not between 0 and 1.
        """
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")

        # Calculate the amount of sand produced based on efficiency
        sand_produced = self.raw_material * efficiency
        self.processed_material = self.raw_material  # All raw material is considered processed
        self.sand_output = sand_produced
        
        # Set raw material to zero after processing
        self.raw_material = 0
        return sand_produced

    def get_sand_output(self) -> float:
        """
        Get the total amount of construction-grade sand produced.

        :return: Amount of sand produced in tons.
        """
        return self.sand_output

    def reset(self):
        """
        Reset the sand maker to its initial state.
        """
        self.raw_material = 0.0
        self.processed_material = 0.0
        self.sand_output = 0.0

def main():
    """
    Main function to simulate the operation of the VSI6X sand maker.
    """
    try:
        # Example: Create a VSI6X sand maker with 100 tons of raw material
        sand_maker = VSI6XSandMaker(raw_material=100.0)

        # Process the material with an efficiency of 0.85 (85%)
        sand_made = sand_maker.process_material(efficiency=0.85)
        print(f"Sand produced: {sand_made} tons")

        # Get the total sand output
        total_sand_output = sand_maker.get_sand_output()
        print(f"Total sand output: {total_sand_output} tons")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
