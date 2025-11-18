"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itab.com
Prompt: Create a script to calculate reduced operational costs for a retail store by optimizing customer journey efficiency, as described in ITAB's value proposition.
Generated: DETERMINISTIC_ef6812a9db4b63c5
Batch ID: 20250612_154621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class OperationalCostOptimizer:
    """
    A class to calculate reduced operational costs by optimizing customer journey efficiency in a retail store.
    """

    def __init__(self, current_costs, average_customer_journey_time, customer_footfall):
        """
        Initialize the OperationalCostOptimizer.

        :param current_costs: (float) Current operational costs in dollars
        :param average_customer_journey_time: (float) Average journey time per customer in minutes
        :param customer_footfall: (int) Number of customers visiting the store daily
        """
        self.current_costs = current_costs
        self.average_customer_journey_time = average_customer_journey_time
        self.customer_footfall = customer_footfall

    def calculate_cost_reduction(self, efficiency_percentage):
        """
        Calculate the reduced operational costs based on improved customer journey efficiency.

        :param efficiency_percentage: (float) Percentage improvement in customer journey efficiency
        :return: (dict) Dictionary with reduced costs and summary of optimization
        """
        try:
            if not (0 <= efficiency_percentage <= 100):
                raise ValueError("Efficiency percentage must be between 0 and 100.")

            # Calculate reduction factor based on efficiency percentage
            reduction_factor = efficiency_percentage / 100

            # Calculate reduced journey time
            reduced_journey_time = self.average_customer_journey_time * (1 - reduction_factor)

            # Calculate new operational costs assuming time efficiency reduces costs proportionally
            reduced_costs = self.current_costs * (1 - reduction_factor)

            # Generate a summary of optimization
            optimization_summary = {
                "current_costs": self.current_costs,
                "reduced_costs": round(reduced_costs, 2),
                "average_customer_journey_time": self.average_customer_journey_time,
                "reduced_customer_journey_time": round(reduced_journey_time, 2),
                "customer_footfall": self.customer_footfall,
                "efficiency_percentage": efficiency_percentage,
                "timestamp": datetime.datetime.now().isoformat()
            }

            return optimization_summary
        except Exception as e:
            # Handle unexpected errors
            return {"error": str(e), "timestamp": datetime.datetime.now().isoformat()}

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters for the retail store
        current_operational_costs = 50000  # in dollars
        avg_customer_journey_time = 15  # in minutes
        daily_customer_footfall = 300  # number of customers
        efficiency_improvement = 20  # in percentage

        # Initialize the optimizer instance
        optimizer = OperationalCostOptimizer(
            current_costs=current_operational_costs,
            average_customer_journey_time=avg_customer_journey_time,
            customer_footfall=daily_customer_footfall
        )

        # Calculate and display optimization results
        optimization_results = optimizer.calculate_cost_reduction(efficiency_improvement)
        print("Optimization Results:")
        for key, value in optimization_results.items():
            print(f"{key}: {value}")

    except Exception as main_error:
        print(f"An error occurred: {main_error}")
```
