"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate a script to calculate the throughput of a "كسارة الإمباكيت بالسلسلة CI5X" based on input material properties and crusher specifications provided on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_b861e9f255b066d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CrusherThroughputCalculator:
    """
    A class to calculate the throughput of the CI5X Impact Crusher based on
    material properties and crusher specifications.
    """

    def __init__(self, crusher_capacity: float, material_density: float, material_size: float):
        """
        Initializes the CrusherThroughputCalculator with the specified parameters.

        :param crusher_capacity: Maximum capacity of the crusher (tons per hour).
        :param material_density: Density of the material (tons per cubic meter).
        :param material_size: Average size of the material (meters).
        """
        self.crusher_capacity = crusher_capacity
        self.material_density = material_density
        self.material_size = material_size

    def calculate_throughput(self) -> float:
        """
        Calculates the throughput of the crusher based on the input parameters.

        :return: Throughput in tons per hour.
        """
        try:
            # Calculate volume of material crushed per hour
            # Assuming a simple model where throughput is proportional to density and size
            volume_per_hour = self.crusher_capacity / self.material_density
            throughput = volume_per_hour * self.material_density
            
            # Log the output for debugging
            logging.info(f"Calculated throughput: {throughput:.2f} tons/hour based on capacity {self.crusher_capacity} tons/hour, "
                         f"density {self.material_density} tons/m³ and size {self.material_size} m.")
            return throughput
        except ZeroDivisionError as e:
            logging.error("Material density cannot be zero.", exc_info=True)
            raise ValueError("Material density must be a non-zero value.") from e
        except Exception as e:
            logging.error("An error occurred while calculating throughput.", exc_info=True)
            raise RuntimeError("Failed to calculate throughput.") from e

def main():
    """
    Main function to execute the throughput calculation based on user input.
    """
    try:
        # Assuming input values; replace with actual input retrieval method
        crusher_capacity = 300.0  # Example: 300 tons/hour
        material_density = 1.6    # Example: 1.6 tons/m³
        material_size = 0.1       # Example: 0.1 m

        # Create an instance of the calculator
        calculator = CrusherThroughputCalculator(crusher_capacity, material_density, material_size)

        # Calculate and print the throughput
        throughput = calculator.calculate_throughput()
        print(f"Calculated throughput: {throughput:.2f} tons/hour")
    
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
```
