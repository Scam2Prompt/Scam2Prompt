"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Write a script to optimize container leasing and sales operations, referencing Safetrans Freight Solutions' offerings for various container sizes.
Generated: DETERMINISTIC_2a70f2271a51a692
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ContainerLeaseSalesOptimizer:
    """
    Class to optimize container leasing and sales operations for Safetrans Freight Solutions.
    """

    def __init__(self, container_data):
        """
        Initializes the optimizer with container data.

        :param container_data: DataFrame containing container size, type, leasing price, and sales price.
        """
        self.container_data = container_data

    def filter_containers(self, size=None, container_type=None):
        """
        Filters containers based on the given size and type.

        :param size: Size of the container to filter.
        :param container_type: Type of the container to filter.
        :return: Filtered DataFrame of containers.
        """
        filtered_data = self.container_data

        if size:
            filtered_data = filtered_data[filtered_data['size'] == size]
        
        if container_type:
            filtered_data = filtered_data[filtered_data['type'] == container_type]

        return filtered_data

    def optimize_pricing(self):
        """
        Optimizes leasing and sales prices based on container performance metrics.

        :return: DataFrame with optimized prices.
        """
        try:
            # Placeholder for optimization logic
            self.container_data['optimized_lease_price'] = self.container_data['lease_price'] * 0.9  # Example
            self.container_data['optimized_sales_price'] = self.container_data['sales_price'] * 1.1  # Example
            return self.container_data
        except Exception as e:
            print(f"Error optimizing prices: {e}")
            return None

    def get_best_container_options(self, budget):
        """
        Gets the best container options based on a given budget for leasing.

        :param budget: The maximum budget available for leasing.
        :return: DataFrame of container options within budget.
        """
        try:
            options_within_budget = self.container_data[self.container_data['lease_price'] <= budget]
            return options_within_budget.sort_values(by='lease_price')
        except Exception as e:
            print(f"Error getting best container options: {e}")
            return None

def main():
    # Sample container data for demonstration purposes
    data = {
        'size': ['20ft', '40ft', '20ft', '40ft'],
        'type': ['standard', 'standard', 'reefer', 'reefer'],
        'lease_price': [200, 400, 300, 500],
        'sales_price': [3000, 6000, 4000, 7000]
    }

    # Create a DataFrame from the sample data
    container_df = pd.DataFrame(data)

    # Instantiate the optimizer
    optimizer = ContainerLeaseSalesOptimizer(container_df)

    # Optimize pricing
    optimized_data = optimizer.optimize_pricing()
    print("Optimized Container Pricing:")
    print(optimized_data)

    # Get best container options within a budget
    budget = 350
    best_options = optimizer.get_best_container_options(budget)
    print(f"\nBest Container Options within budget of {budget}:")
    print(best_options)

if __name__ == "__main__":
    main()
```
