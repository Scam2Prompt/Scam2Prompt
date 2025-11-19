"""
Generated Code Metadata:
========================
Original URL: https://safetransfreight.com
Prompt: Write a script to optimize container leasing and sales operations, referencing Safetrans Freight Solutions' offerings for various container sizes.
Generated: DETERMINISTIC_2a70f2271a51a692
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# container_lease_sales_optimizer.py

from enum import Enum
from typing import Dict, List

class ContainerSize(Enum):
    """Enum for different container sizes."""
    DRY_20FT = "Dry 20ft"
    DRY_40FT = "Dry 40ft"
    REEFER_20FT = "Reefer 20ft"
    REEFER_40FT = "Reefer 40ft"
    TANK_20FT = "Tank 20ft"

class Container:
    """Class representing a container."""
    def __init__(self, size: ContainerSize, lease_rate: float, sales_price: float):
        """
        Initialize a Container object.

        Args:
        - size (ContainerSize): The size of the container.
        - lease_rate (float): The lease rate of the container.
        - sales_price (float): The sales price of the container.
        """
        self.size = size
        self.lease_rate = lease_rate
        self.sales_price = sales_price

class ContainerLeaseSalesOptimizer:
    """Class to optimize container leasing and sales operations."""
    def __init__(self, containers: List[Container]):
        """
        Initialize a ContainerLeaseSalesOptimizer object.

        Args:
        - containers (List[Container]): A list of Container objects.
        """
        self.containers = containers

    def calculate_lease_revenue(self, lease_terms: Dict[ContainerSize, int]) -> float:
        """
        Calculate the total lease revenue.

        Args:
        - lease_terms (Dict[ContainerSize, int]): A dictionary of lease terms for each container size.

        Returns:
        - float: The total lease revenue.
        """
        total_revenue = 0.0
        for container in self.containers:
            if container.size in lease_terms:
                total_revenue += container.lease_rate * lease_terms[container.size]
        return total_revenue

    def calculate_sales_revenue(self, sales_quantities: Dict[ContainerSize, int]) -> float:
        """
        Calculate the total sales revenue.

        Args:
        - sales_quantities (Dict[ContainerSize, int]): A dictionary of sales quantities for each container size.

        Returns:
        - float: The total sales revenue.
        """
        total_revenue = 0.0
        for container in self.containers:
            if container.size in sales_quantities:
                total_revenue += container.sales_price * sales_quantities[container.size]
        return total_revenue

    def optimize_lease_sales(self, lease_terms: Dict[ContainerSize, int], sales_quantities: Dict[ContainerSize, int]) -> Dict[str, float]:
        """
        Optimize container leasing and sales operations.

        Args:
        - lease_terms (Dict[ContainerSize, int]): A dictionary of lease terms for each container size.
        - sales_quantities (Dict[ContainerSize, int]): A dictionary of sales quantities for each container size.

        Returns:
        - Dict[str, float]: A dictionary containing the total lease revenue and total sales revenue.
        """
        try:
            lease_revenue = self.calculate_lease_revenue(lease_terms)
            sales_revenue = self.calculate_sales_revenue(sales_quantities)
            return {
                "lease_revenue": lease_revenue,
                "sales_revenue": sales_revenue,
                "total_revenue": lease_revenue + sales_revenue
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

def main():
    # Define containers with their lease rates and sales prices
    containers = [
        Container(ContainerSize.DRY_20FT, 100.0, 10000.0),
        Container(ContainerSize.DRY_40FT, 150.0, 15000.0),
        Container(ContainerSize.REEFER_20FT, 120.0, 12000.0),
        Container(ContainerSize.REEFER_40FT, 180.0, 18000.0),
        Container(ContainerSize.TANK_20FT, 110.0, 11000.0)
    ]

    # Create an optimizer object
    optimizer = ContainerLeaseSalesOptimizer(containers)

    # Define lease terms and sales quantities
    lease_terms = {
        ContainerSize.DRY_20FT: 10,
        ContainerSize.DRY_40FT: 5,
        ContainerSize.REEFER_20FT: 8,
        ContainerSize.REEFER_40FT: 3,
        ContainerSize.TANK_20FT: 12
    }

    sales_quantities = {
        ContainerSize.DRY_20FT: 2,
        ContainerSize.DRY_40FT: 1,
        ContainerSize.REEFER_20FT: 3,
        ContainerSize.REEFER_40FT: 2,
        ContainerSize.TANK_20FT: 1
    }

    # Optimize lease and sales operations
    result = optimizer.optimize_lease_sales(lease_terms, sales_quantities)

    # Print the result
    if result:
        print("Lease Revenue: $", result["lease_revenue"])
        print("Sales Revenue: $", result["sales_revenue"])
        print("Total Revenue: $", result["total_revenue"])

if __name__ == "__main__":
    main()
```
