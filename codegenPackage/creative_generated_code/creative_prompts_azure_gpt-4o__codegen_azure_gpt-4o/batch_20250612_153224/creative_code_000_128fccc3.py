"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Write Python code to simulate the operation of a "طاحونة عمودية-LM" using parameters for grinding efficiency and material classification as described on the Sardinia Meets Azores website.
Generated: DETERMINISTIC_128fccc375e2a522
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class VerticalMillLM:
    """
    Class to simulate the operation of a vertical mill (طاحونة عمودية-LM).
    This includes grinding efficiency and material classification.
    """

    def __init__(self, grinding_efficiency: float, material_hardness: float, classification_efficiency: float):
        """
        Initialize the vertical mill parameters.

        :param grinding_efficiency: Efficiency of the grinding process as a ratio (0.0 to 1.0).
        :param material_hardness: Hardness factor of the material being processed (1.0 to 10.0).
        :param classification_efficiency: Efficiency of material classification as a ratio (0.0 to 1.0).
        """
        if not (0.0 <= grinding_efficiency <= 1.0):
            raise ValueError("Grinding efficiency must be between 0.0 and 1.0.")
        if not (1.0 <= material_hardness <= 10.0):
            raise ValueError("Material hardness must be between 1.0 and 10.0.")
        if not (0.0 <= classification_efficiency <= 1.0):
            raise ValueError("Classification efficiency must be between 0.0 and 1.0.")

        self.grinding_efficiency = grinding_efficiency
        self.material_hardness = material_hardness
        self.classification_efficiency = classification_efficiency

    def calculate_output(self, input_material: float) -> float:
        """
        Calculate the output material based on input material, grinding efficiency, and classification efficiency.

        :param input_material: Amount of input material in tons.
        :return: Processed output material in tons.
        """
        try:
            # Simulating grinding process
            ground_material = input_material * self.grinding_efficiency

            # Adjusting based on material hardness
            adjusted_material = ground_material / math.log(self.material_hardness + 1)

            # Simulating classification efficiency
            classified_material = adjusted_material * self.classification_efficiency

            logging.info(f"Input Material: {input_material} tons")
            logging.info(f"Ground Material: {ground_material:.2f} tons")
            logging.info(f"Adjusted Material (Hardness Factor Applied): {adjusted_material:.2f} tons")
            logging.info(f"Classified Material: {classified_material:.2f} tons")

            return classified_material
        except Exception as e:
            logging.error(f"Error calculating output: {str(e)}")
            raise

    def simulate_operation(self, input_material: float) -> None:
        """
        Simulate the operation of the vertical mill and print the results.

        :param input_material: Amount of input material in tons.
        """
        try:
            output_material = self.calculate_output(input_material)
            print(f"Processed Output Material: {output_material:.2f} tons")
        except Exception as e:
            print(f"Simulation failed due to error: {str(e)}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the vertical mill with realistic parameters
        vertical_mill = VerticalMillLM(grinding_efficiency=0.85, material_hardness=7.0, classification_efficiency=0.9)

        # Simulate operation with an input material amount
        vertical_mill.simulate_operation(input_material=100.0)  # Input material in tons
    except Exception as e:
        logging.error(f"Failed to initialize or simulate vertical mill: {str(e)}")
```
