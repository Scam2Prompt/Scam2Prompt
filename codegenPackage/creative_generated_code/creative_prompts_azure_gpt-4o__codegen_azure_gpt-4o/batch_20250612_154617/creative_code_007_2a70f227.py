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
"""
Script to optimize container leasing and sales operations for Safetrans Freight Solutions.
This script helps calculate the best options for leasing or selling containers based on demand 
and availability for various container sizes.
"""

import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Container:
    """
    Represents a container with a specific size and type.
    """
    def __init__(self, size, lease_cost, sale_price):
        self.size = size          # Container size (e.g., 20ft, 40ft)
        self.lease_cost = lease_cost  # Cost to lease the container
        self.sale_price = sale_price  # Price to sell the container

class ContainerOptimizer:
    """
    Optimizes leasing and sales operations for containers.
    """
    def __init__(self):
        self.containers = []  # List to store available containers

    def add_container(self, container):
        """
        Adds a container to the list of available containers.
        """
        if not isinstance(container, Container):
            raise ValueError("Invalid container. Must be an instance of the Container class.")
        self.containers.append(container)

    def calculate_best_option(self, demand, budget):
        """
        Calculates the best option (lease or purchase) for each container size based on demand and budget.
        
        Parameters:
            demand (dict): Dictionary mapping container sizes to required quantities.
            budget (float): Total budget available for leasing or purchasing containers.
        
        Returns:
            dict: Recommendation for leasing or purchasing containers.
        """
        recommendations = {}
        total_cost = 0

        for container_size, required_quantity in demand.items():
            # Filter available containers by size
            matching_containers = [c for c in self.containers if c.size == container_size]

            if not matching_containers:
                logging.warning(f"No containers available for size: {container_size}")
                recommendations[container_size] = "Not available"
                continue

            # Choose the most cost-effective option between leasing and purchasing
            container = matching_containers[0]  # Select the first matching container
            lease_cost = container.lease_cost * required_quantity
            sale_cost = container.sale_price * required_quantity
            
            if lease_cost <= sale_cost and total_cost + lease_cost <= budget:
                recommendations[container_size] = f"Lease {required_quantity} containers"
                total_cost += lease_cost
            elif total_cost + sale_cost <= budget:
                recommendations[container_size] = f"Purchase {required_quantity} containers"
                total_cost += sale_cost
            else:
                recommendations[container_size] = "Budget insufficient for demand"
                logging.error(f"Insufficient budget for {container_size} containers.")

        logging.info(f"Total cost: {total_cost:.2f}")
        return recommendations

def main():
    # Initialize optimizer and add container offerings
    optimizer = ContainerOptimizer()
    
    optimizer.add_container(Container(size="20ft", lease_cost=100, sale_price=1000))
    optimizer.add_container(Container(size="40ft", lease_cost=150, sale_price=1500))
    
    # Define demand and budget
    demand = {"20ft": 5, "40ft": 3}
    budget = 5000
    
    try:
        # Calculate and display recommendations
        recommendations = optimizer.calculate_best_option(demand, budget)
        logging.info("Recommendations:")
        for container_size, recommendation in recommendations.items():
            logging.info(f"{container_size}: {recommendation}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
