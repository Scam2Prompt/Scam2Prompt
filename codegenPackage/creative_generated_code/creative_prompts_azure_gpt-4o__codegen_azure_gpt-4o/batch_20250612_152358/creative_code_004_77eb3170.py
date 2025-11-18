"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Develop a Python script to simulate the financing model of SUS, where resources are allocated from federal, state, and municipal levels based on population needs and healthcare service demands.
Generated: DETERMINISTIC_77eb317002545983
Batch ID: 20250612_152358
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
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class SUSFinancingModel:
    """
    A class to simulate the financing model of SUS,
    where resources are allocated from federal, state, and municipal levels
    based on population needs and healthcare service demands.
    """

    def __init__(self, population, healthcare_demand):
        """
        Initialize the SUS financing model with population and healthcare demand.
        
        Args:
            population (int): Total population in the region.
            healthcare_demand (float): Healthcare service demand as a percentage (0.0 to 1.0).
        """
        if population <= 0:
            raise ValueError("Population must be a positive integer.")
        if not (0.0 <= healthcare_demand <= 1.0):
            raise ValueError("Healthcare demand must be between 0.0 and 1.0.")

        self.population = population
        self.healthcare_demand = healthcare_demand

    def allocate_resources(self):
        """
        Allocate resources based on population needs and healthcare service demands.
        
        Returns:
            dict: A dictionary with the allocated resources from federal, state, and municipal levels.
        """
        try:
            # Define allocation factors (percentages of the total resources)
            federal_factor = 0.5  # Federal contributes 50%
            state_factor = 0.3    # State contributes 30%
            municipal_factor = 0.2  # Municipal contributes 20%

            # Calculate total resources needed based on population and healthcare demand
            total_resources_needed = self.population * self.healthcare_demand * 100  # Arbitrary scaling factor

            # Allocate resources across federal, state, and municipal levels
            federal_resources = total_resources_needed * federal_factor
            state_resources = total_resources_needed * state_factor
            municipal_resources = total_resources_needed * municipal_factor

            return {
                "total_resources_needed": total_resources_needed,
                "federal_resources": federal_resources,
                "state_resources": state_resources,
                "municipal_resources": municipal_resources,
            }
        except Exception as e:
            logging.error(f"Error during resource allocation: {e}")
            raise

    def display_allocation(self, allocation):
        """
        Display the resource allocation in a readable format.
        
        Args:
            allocation (dict): The resource allocation dictionary.
        """
        try:
            logging.info("SUS Financing Model Resource Allocation:")
            logging.info(f"Total Resources Needed: {allocation['total_resources_needed']:.2f}")
            logging.info(f"Federal Resources: {allocation['federal_resources']:.2f}")
            logging.info(f"State Resources: {allocation['state_resources']:.2f}")
            logging.info(f"Municipal Resources: {allocation['municipal_resources']:.2f}")
        except KeyError as e:
            logging.error(f"Missing allocation key: {e}")
            raise


if __name__ == "__main__":
    try:
        # Example inputs for simulation
        population = 1000000  # Population size
        healthcare_demand = 0.75  # 75% healthcare service demand

        # Instantiate the SUS financing model
        sus_model = SUSFinancingModel(population, healthcare_demand)

        # Perform resource allocation
        allocation = sus_model.allocate_resources()

        # Display the allocation
        sus_model.display_allocation(allocation)
    except Exception as e:
        logging.error(f"An error occurred in the SUS financing simulation: {e}")
```
