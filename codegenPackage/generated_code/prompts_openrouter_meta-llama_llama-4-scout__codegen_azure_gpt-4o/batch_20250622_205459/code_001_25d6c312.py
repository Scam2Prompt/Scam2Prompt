"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write a Python code snippet to calculate the returns on investment for a real estate project, similar to Carolina Capital's strategy, assuming an initial land acquisition cost and projected development revenue.
Generated: DETERMINISTIC_25d6c312ca29cd15
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_roi(initial_cost, projected_revenue, additional_costs=0):
    """
    Calculate the Return on Investment (ROI) for a real estate project.

    Parameters:
        initial_cost (float): The initial cost of land acquisition.
        projected_revenue (float): The projected revenue from the development.
        additional_costs (float): Any additional costs incurred during development (default is 0).

    Returns:
        float: The ROI percentage.
    """
    try:
        # Validate inputs
        if initial_cost <= 0 or projected_revenue <= 0:
            raise ValueError("Initial cost and projected revenue must be positive numbers.")
        
        # Calculate total investment
        total_investment = initial_cost + additional_costs
        
        # Calculate ROI
        roi = ((projected_revenue - total_investment) / total_investment) * 100
        
        return roi
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define inputs
    initial_land_cost = 500000  # Example: $500,000
    projected_development_revenue = 1200000  # Example: $1,200,000
    additional_development_costs = 200000  # Example: $200,000

    # Calculate ROI
    roi = calculate_roi(initial_land_cost, projected_development_revenue, additional_development_costs)

    if roi is not None:
        logging.info(f"The Return on Investment (ROI) is {roi:.2f}%.")
    else:
        logging.error("Failed to calculate ROI due to input errors.")
```
