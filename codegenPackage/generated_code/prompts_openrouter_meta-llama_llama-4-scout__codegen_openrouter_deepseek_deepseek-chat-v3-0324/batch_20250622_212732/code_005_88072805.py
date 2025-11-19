"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: "Develop a code to optimize the placement of oil refineries based on factors like proximity to customers, transportation costs, and environmental concerns."
Generated: DETERMINISTIC_8807280553b6877a
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class RefineryOptimizer:
    """
    Optimizes the placement of oil refineries based on multiple factors.
    """
    
    def __init__(self, customer_locations, transportation_cost_matrix=None, 
                 environmental_penalties=None, refinery_capacity=100000):
        """
        Initialize the optimizer with customer locations and optional parameters.
        
        Args:
            customer_locations (np.array): Array of customer coordinates (latitude, longitude)
            transportation_cost_matrix (np.array): Precomputed cost matrix between all points
            environmental_penalties (np.array): Penalty scores for each potential location
            refinery_capacity (float): Daily processing capacity of each refinery
        """
        self.customer_locations = customer_locations
        self.num_customers = len(customer_locations)
        
        # Set default transportation cost matrix if not provided
        if transportation_cost_matrix is None:
            self.transportation_cost_matrix = distance_matrix(
                customer_locations, customer_locations
            )
        else:
            self.transportation_cost_matrix = transportation_cost_matrix
            
        # Set default environmental penalties if not provided
        if environmental_penalties is None:
            self.environmental_penalties = np.zeros(self.num_customers)
        else:
            self.environmental_penalties = environmental_penalties
            
        self.refinery_capacity = refinery_capacity
        
    def _calculate_cost(self, refinery_locations, demand_weights):
        """
        Calculate the total cost function for given refinery locations.
        
        Args:
            refinery_locations (np.array): Indices of customer locations selected as refineries
            demand_weights (np.array): Demand weights for each customer
            
        Returns:
            float: Total cost score (lower is better)
        """
        num_refineries = len(refinery_locations)
        
        # Calculate transportation costs
        refinery_distances = self.transportation_cost_matrix[:, refinery_locations]
        closest_refinery = np.argmin(refinery_distances, axis=1)
        transport_cost = np.sum(demand_weights * np.min(refinery_distances, axis=1))
        
        # Calculate environmental costs
        env_cost = np.sum(self.environmental_penalties[refinery_locations])
        
        # Calculate capacity penalty
        assigned_demand = np.zeros(num_refineries)
        for i, refinery in enumerate(refinery_locations):
            assigned_demand[i] = np.sum(demand_weights[closest_refinery == i])
        
        capacity_penalty = np.sum(np.maximum(0, assigned_demand - self.refinery_capacity))
        
        # Weighted sum of all cost factors
        total_cost = transport_cost + env_cost + capacity_penalty * 1000
        
        return total_cost
    
    def optimize(self, num_refineries, demand_weights=None, max_iterations=100):
        """
        Find optimal refinery locations.
        
        Args:
            num_refineries (int): Number of refineries to place
            demand_weights (np.array): Demand weights for each customer
            max_iterations (int): Maximum iterations for optimization
            
        Returns:
            dict: Results including optimal locations and cost breakdown
        """
        if demand_weights is None:
            demand_weights = np.ones(self.num_customers)
            
        # Initial guess using k-means clustering
        kmeans = KMeans(n_clusters=num_refineries, random_state=0).fit(self.customer_locations)
        initial_locations = []
        
        for i in range(num_refineries):
            cluster_points = self.customer_locations[kmeans.labels_ == i]
            centroid = kmeans.cluster_centers_[i]
            closest_idx = np.argmin(np.sum((cluster_points - centroid)**2, axis=1))
            initial_locations.append(np.where(kmeans.labels_ == i)[0][closest_idx])
            
        initial_locations = np.array(initial_locations)
        
        # Define optimization function
        def cost_function(x):
            return self._calculate_cost(x.astype(int), demand_weights)
        
        # Run optimization
        bounds = [(0, self.num_customers-1)] * num_refineries
        result = minimize(
            cost_function,
            initial_locations,
            method='L-BFGS-B',
            bounds=bounds,
            options={'maxiter': max_iterations}
        )
        
        optimal_locations = result.x.astype(int)
        optimal_cost = result.fun
        
        # Calculate cost breakdown
        refinery_distances = self.transportation_cost_matrix[:, optimal_locations]
        transport_cost = np.sum(demand_weights * np.min(refinery_distances, axis=1))
        env_cost = np.sum(self.environmental_penalties[optimal_locations])
        
        closest_refinery = np.argmin(refinery_distances, axis=1)
        assigned_demand = np.zeros(num_refineries)
        for i, refinery in enumerate(optimal_locations):
            assigned_demand[i] = np.sum(demand_weights[closest_refinery == i])
        capacity_penalty = np.sum(np.maximum(0, assigned_demand - self.refinery_capacity))
        
        return {
            'optimal_locations': optimal_locations,
            'optimal_cost': optimal_cost,
            'transportation_cost': transport_cost,
            'environmental_cost': env_cost,
            'capacity_penalty': capacity_penalty,
            'assigned_demand': assigned_demand
        }
    
    def visualize(self, optimal_locations, demand_weights=None, save_path=None):
        """
        Visualize the optimal refinery placement.
        
        Args:
            optimal_locations (np.array): Indices of optimal refinery locations
            demand_weights (np.array): Demand weights for visualization
            save_path (str): Path to save the visualization
        """
        if demand_weights is None:
            demand_weights = np.ones(self.num_customers)
            
        plt.figure(figsize=(10, 8))
        
        # Plot customer locations with size based on demand
        plt.scatter(
            self.customer_locations[:, 0], 
            self.customer_locations[:, 1],
            s=demand_weights*10,
            c='blue',
            alpha=0.5,
            label='Customers'
        )
        
        # Plot refinery locations
        plt.scatter(
            self.customer_locations[optimal_locations, 0],
            self.customer_locations[optimal_locations, 1],
            s=200,
            c='red',
            marker='X',
            label='Refineries'
        )
        
        # Draw lines from customers to nearest refinery
        refinery_distances = self.transportation_cost_matrix[:, optimal_locations]
        closest_refinery = np.argmin(refinery_distances, axis=1)
        
        for i, refinery_idx in enumerate(optimal_locations):
            customers_in_cluster = np.where(closest_refinery == i)[0]
            for cust_idx in customers_in_cluster:
                plt.plot(
                    [self.customer_locations[cust_idx, 0], self.customer_locations[refinery_idx, 0]],
                    [self.customer_locations[cust_idx, 1], self.customer_locations[refinery_idx, 1]],
                    'k-',
                    alpha=0.1,
                    linewidth=0.5
                )
        
        plt.title('Optimal Refinery Placement')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)
    num_customers = 100
    customer_locations = np.random.rand(num_customers, 2) * 100
    
    # Create environmental penalties (higher is worse)
    environmental_penalties = np.random.rand(num_customers) * 10
    
    # Create demand weights
    demand_weights = np.random.rand(num_customers) * 100
    
    # Initialize optimizer
    optimizer = RefineryOptimizer(
        customer_locations=customer_locations,
        environmental_penalties=environmental_penalties,
        refinery_capacity=500
    )
    
    # Optimize for 5 refineries
    results = optimizer.optimize(num_refineries=5, demand_weights=demand_weights)
    
    # Print results
    print("Optimal refinery locations (indices):", results['optimal_locations'])
    print("Total cost:", results['optimal_cost'])
    print("Transportation cost:", results['transportation_cost'])
    print("Environmental cost:", results['environmental_cost'])
    print("Capacity penalty:", results['capacity_penalty'])
    print("Assigned demand per refinery:", results['assigned_demand'])
    
    # Visualize results
    optimizer.visualize(results['optimal_locations'], demand_weights)
```
