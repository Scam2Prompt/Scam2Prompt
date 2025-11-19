"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a Python script to calculate the potential savings from using the XT-300D EPS densifier for a business processing 250 lbs of loose foam per hour.
Generated: DETERMINISTIC_30cc2796c74a910e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture detailed information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class XT300D:
    def __init__(self, processing_rate_lbs_per_hour, density_conversion_factor):
        """
        Initializes the XT-300D densifier with processing rate and density conversion factor.

        :param processing_rate_lbs_per_hour: Processing rate in pounds per hour
        :param density_conversion_factor: Factor to convert loose foam to densified foam
        """
        self.processing_rate = processing_rate_lbs_per_hour
        self.density_conversion_factor = density_conversion_factor

    def calculate_densified_output(self):
        """
        Calculate the output of densified foam in pounds per hour.

        :return: Densified output in pounds per hour
        """
        densified_output = self.processing_rate * self.density_conversion_factor
        logging.info(f"Densified output calculated: {densified_output:.2f} lbs/hour")
        return densified_output

    def calculate_savings(self, cost_per_pound_loose_foam, cost_per_pound_densified_foam):
        """
        Calculate potential savings by comparing costs of loose foam vs. densified foam.

        :param cost_per_pound_loose_foam: Cost of loose foam per pound
        :param cost_per_pound_densified_foam: Cost of densified foam per pound
        :return: Potential savings per hour
        """
        try:
            loose_foam_cost = self.processing_rate * cost_per_pound_loose_foam
            densified_output = self.calculate_densified_output()
            densified_foam_cost = densified_output * cost_per_pound_densified_foam
            
            savings = loose_foam_cost - densified_foam_cost
            
            logging.info(f"Loose foam cost: ${loose_foam_cost:.2f}, Densified foam cost: ${densified_foam_cost:.2f}, Savings: ${savings:.2f} per hour")
            return savings
        except Exception as e:
            logging.error("Error calculating savings: %s", e)
            raise

def main():
    # Configuration for the XT-300D EPS densifier
    processing_rate = 250  # lbs of loose foam per hour
    density_conversion_factor = 0.1  # Example conversion factor
    cost_per_pound_loose_foam = 0.50  # Cost of loose foam
    cost_per_pound_densified_foam = 1.00  # Cost of densified foam

    # Create an instance of the XT-300D
    densifier = XT300D(processing_rate, density_conversion_factor)

    # Calculate potential savings
    try:
        savings = densifier.calculate_savings(cost_per_pound_loose_foam, cost_per_pound_densified_foam)
        logging.info(f"Potential savings from using XT-300D EPS densifier: ${savings:.2f} per hour")
    except Exception as e:
        logging.error(f"An error occurred while calculating savings: {e}")

if __name__ == "__main__":
    main()
```
