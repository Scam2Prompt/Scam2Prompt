"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to calculate carbon footprint reduction for logistics operations, referencing Alexa Shipping's commitment to sustainability.
Generated: DETERMINISTIC_e3b8e14a0a976114
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CarbonFootprintCalculator:
    """
    A class to calculate the carbon footprint reduction for logistics operations
    based on various sustainability factors related to shipping.
    """

    def __init__(self, base_footprint: float, reduction_factors: dict):
        """
        Initializes the CarbonFootprintCalculator with a base footprint and
        reduction factors.

        :param base_footprint: The initial carbon footprint in metric tons.
        :param reduction_factors: A dictionary of reduction factors with their
                                   respective percentages.
        """
        self.base_footprint = base_footprint
        self.reduction_factors = reduction_factors

    def calculate_reduction(self) -> float:
        """
        Calculates the total reduction in carbon footprint based on the
        reduction factors provided.

        :return: The total reduced carbon footprint in metric tons.
        """
        total_reduction = self.base_footprint  # Start with the base footprint
        try:
            for factor, percentage in self.reduction_factors.items():
                reduction = (percentage / 100) * total_reduction
                total_reduction -= reduction
                logging.info(f"Reducing by {reduction:.2f} tons due to {factor}.")

            return total_reduction
        except Exception as e:
            logging.error(f"Error calculating reduction: {e}")
            raise

def load_reduction_factors(file_path: str) -> dict:
    """
    Loads reduction factors from a JSON file.

    :param file_path: The path to the JSON file containing reduction factors.
    :return: A dictionary of reduction factors.
    """
    try:
        with open(file_path, 'r') as file:
            reduction_factors = json.load(file)
            logging.info("Reduction factors loaded successfully.")
            return reduction_factors
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file.")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

def main():
    """
    Main function to run the carbon footprint reduction calculation.
    """
    base_footprint = 1000.0  # Initial carbon footprint in metric tons
    reduction_factors_file = 'reduction_factors.json'

    try:
        reduction_factors = load_reduction_factors(reduction_factors_file)
        calculator = CarbonFootprintCalculator(base_footprint, reduction_factors)
        new_footprint = calculator.calculate_reduction()
        logging.info(f"New carbon footprint after reductions: {new_footprint:.2f} tons.")
    except Exception as e:
        logging.error(f"Failed to compute carbon footprint reduction: {e}")

if __name__ == "__main__":
    main()
```

This program calculates the carbon footprint reduction based on the provided reduction factors and logs all relevant details. Ensure you have a JSON file named `reduction_factors.json` in the same directory, containing your reduction factors structured as a dictionary.
