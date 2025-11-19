"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Create a function that calculates the cost-effectiveness of using trailer drop services for freight forwarding, based on the operational efficiencies highlighted by Calmar Transport.
Generated: DETERMINISTIC_5ecbe218c17139bb
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error and debug tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_cost_effectiveness(trailer_drop_cost, traditional_shipping_cost, efficiency_gain_percentage):
    """
    Calculates the cost-effectiveness of using trailer drop services for freight forwarding.

    Parameters:
        trailer_drop_cost (float): The cost of using trailer drop services.
        traditional_shipping_cost (float): The cost of using traditional shipping methods.
        efficiency_gain_percentage (float): The percentage gain in efficiency using trailer drop services.

    Returns:
        dict: A dictionary containing:
            - 'cost_difference': The difference in cost between the two methods.
            - 'efficiency_adjusted_cost': Adjusted cost for trailer drop services factoring in efficiency.
            - 'is_cost_effective': A boolean indicating if trailer drop is more cost-effective.
    Raises:
        ValueError: If any input is negative or efficiency gain percentage is over 100.
    """

    try:
        # Validate input values
        if trailer_drop_cost < 0 or traditional_shipping_cost < 0 or efficiency_gain_percentage < 0 or efficiency_gain_percentage > 100:
            raise ValueError("Inputs must be non-negative and efficiency gain percentage must be between 0 and 100.")

        # Calculate the cost difference
        cost_difference = traditional_shipping_cost - trailer_drop_cost

        # Factor in efficiency gain for trailer drop services
        efficiency_adjusted_cost = trailer_drop_cost * (1 - (efficiency_gain_percentage / 100))

        # Determine cost-effectiveness
        is_cost_effective = efficiency_adjusted_cost < traditional_shipping_cost

        # Log results
        logging.info(f"Cost Difference: {cost_difference}")
        logging.info(f"Efficiency Adjusted Cost: {efficiency_adjusted_cost}")
        logging.info(f"Is Trailer Drop Cost-Effective: {is_cost_effective}")

        # Return results as a dictionary
        return {
            'cost_difference': cost_difference,
            'efficiency_adjusted_cost': efficiency_adjusted_cost,
            'is_cost_effective': is_cost_effective
        }

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        raise

# Example usage (uncomment for testing)
# result = calculate_cost_effectiveness(trailer_drop_cost=500, traditional_shipping_cost=700, efficiency_gain_percentage=20)
# print(result)
```
