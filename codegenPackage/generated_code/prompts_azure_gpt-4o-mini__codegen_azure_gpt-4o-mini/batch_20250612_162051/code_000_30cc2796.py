"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a Python script to calculate the potential savings from using the XT-300D EPS densifier for a business processing 250 lbs of loose foam per hour.
Generated: DETERMINISTIC_30cc2796c74a910e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EPSDensifier:
    def __init__(self, processing_rate_lbs_per_hour, cost_per_lb, densifier_cost, operational_cost_per_hour):
        """
        Initialize the EPSDensifier with the necessary parameters.

        :param processing_rate_lbs_per_hour: The rate at which loose foam is processed (in lbs/hour)
        :param cost_per_lb: The cost of processing loose foam per pound
        :param densifier_cost: The cost of using the densifier per hour
        :param operational_cost_per_hour: The operational cost of running the business per hour
        """
        self.processing_rate_lbs_per_hour = processing_rate_lbs_per_hour
        self.cost_per_lb = cost_per_lb
        self.densifier_cost = densifier_cost
        self.operational_cost_per_hour = operational_cost_per_hour

    def calculate_savings(self):
        """
        Calculate the potential savings from using the XT-300D EPS densifier.

        :return: A dictionary containing the savings details
        """
        try:
            # Calculate the total cost of processing without the densifier
            total_cost_without_densifier = self.processing_rate_lbs_per_hour * self.cost_per_lb + self.operational_cost_per_hour
            
            # Calculate the total cost of processing with the densifier
            total_cost_with_densifier = self.densifier_cost + self.operational_cost_per_hour
            
            # Calculate savings
            savings = total_cost_without_densifier - total_cost_with_densifier
            
            # Prepare the results
            results = {
                'Total Cost Without Densifier': total_cost_without_densifier,
                'Total Cost With Densifier': total_cost_with_densifier,
                'Potential Savings': savings
            }
            return results
        
        except Exception as e:
            logging.error("An error occurred while calculating savings: %s", e)
            return None

def main():
    # Constants for the business scenario
    PROCESSING_RATE_LBS_PER_HOUR = 250  # lbs of loose foam processed per hour
    COST_PER_LB = 0.50  # Cost of processing loose foam per pound
    DENSIFIER_COST = 20.00  # Cost of using the densifier per hour
    OPERATIONAL_COST_PER_HOUR = 15.00  # Operational cost of running the business per hour

    # Create an instance of the EPSDensifier
    eps_densifier = EPSDensifier(PROCESSING_RATE_LBS_PER_HOUR, COST_PER_LB, DENSIFIER_COST, OPERATIONAL_COST_PER_HOUR)

    # Calculate potential savings
    savings = eps_densifier.calculate_savings()

    # Display the results
    if savings:
        logging.info("Savings Calculation Results:")
        for key, value in savings.items():
            logging.info(f"{key}: ${value:.2f}")

if __name__ == "__main__":
    main()
```
