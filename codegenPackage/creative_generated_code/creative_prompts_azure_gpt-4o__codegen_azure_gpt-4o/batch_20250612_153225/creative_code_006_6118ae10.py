"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Create a function to estimate the environmental impact reduction for businesses using renting solutions that promote energy efficiency and renewable energy, as described by Innova Renting.
Generated: DETERMINISTIC_6118ae109580e080
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: environmental_impact_estimator.py

import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def estimate_environmental_impact(current_emissions: float, reduction_percentage: float) -> float:
    """
    Estimate the reduction in environmental impact for businesses adopting energy-efficient renting solutions.

    Args:
        current_emissions (float): The current annual carbon emissions of the business in metric tons.
        reduction_percentage (float): The expected reduction percentage using Innova Renting solutions.

    Returns:
        float: The estimated annual emissions after adopting the renting solution.

    Raises:
        ValueError: If current_emissions or reduction_percentage are negative, or if reduction_percentage is > 100.
    """
    # Validate input values
    if current_emissions < 0:
        raise ValueError("Current emissions cannot be negative.")
    if reduction_percentage < 0 or reduction_percentage > 100:
        raise ValueError("Reduction percentage must be between 0 and 100.")

    # Calculate the estimated emissions after reduction
    try:
        reduced_emissions = current_emissions * (1 - reduction_percentage / 100)
        logging.info(f"Estimated emissions after reduction: {reduced_emissions} metric tons.")
        return reduced_emissions
    except Exception as e:
        logging.error(f"An error occurred during the calculation: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Example inputs
        current_emissions = 5000.0  # Example: 5000 metric tons per year
        reduction_percentage = 20.0  # Example: 20% reduction using energy-efficient solutions

        # Estimate environmental impact
        estimated_emissions = estimate_environmental_impact(current_emissions, reduction_percentage)
        print(f"Estimated annual emissions after reduction: {estimated_emissions:.2f} metric tons.")
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
