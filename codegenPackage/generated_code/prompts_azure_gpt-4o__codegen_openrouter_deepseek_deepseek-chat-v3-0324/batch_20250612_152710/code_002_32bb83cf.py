"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Generate Python code to simulate cost savings in distribution based on PLM's geographic advantages and economies of scale.
Generated: DETERMINISTIC_32bb83cfd3c9b42a
Batch ID: 20250612_152710
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
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class DistributionCenter:
    """Represents a distribution center with geographic and cost attributes."""
    name: str
    latitude: float
    longitude: float
    fixed_cost: float  # Annual fixed cost in USD
    variable_cost_per_unit: float  # Cost per unit shipped in USD
    capacity: float  # Maximum units that can be handled annually

@dataclass
class CustomerLocation:
    """Represents a customer location with demand and geographic attributes."""
    name: str
    latitude: float
    longitude: float
    annual_demand: float  # Units required annually

class DistributionOptimizer:
    """Simulates cost savings from PLM's geographic advantages and economies of scale."""
    
    def __init__(self, distribution_centers: List[DistributionCenter], customers: List[CustomerLocation]):
        """Initialize with distribution centers and customer locations."""
        self.distribution_centers = distribution_centers
        self.customers = customers
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input data for consistency."""
        if not self.distribution_centers:
            raise ValueError("At least one distribution center must be provided")
        if not self.customers:
            raise ValueError("At least one customer location must be provided")
        for dc in self.distribution_centers:
            if dc.capacity <= 0:
                raise ValueError(f"Invalid capacity for distribution center {dc.name}")
    
    @staticmethod
    def _calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculate approximate distance between two points using Haversine formula."""
        R = 6371  # Earth radius in km
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return R * c
    
    def _assign_customers_to_nearest_dc(self) -> Dict[str, List[str]]:
        """Assign each customer to the nearest distribution center."""
        assignments = {dc.name: [] for dc in self.distribution_centers}
        
        for customer in self.customers:
            min_distance = float('inf')
            best_dc = None
            
            for dc in self.distribution_centers:
                distance = self._calculate_distance(
                    customer.latitude, customer.longitude,
                    dc.latitude, dc.longitude
                )
                if distance < min_distance:
                    min_distance = distance
                    best_dc = dc.name
            
            if best_dc:
                assignments[best_dc].append(customer.name)
        
        return assignments
    
    def _calculate_total_demand_per_dc(self, assignments: Dict[str, List[str]]) -> Dict[str, float]:
        """Calculate total demand for each distribution center."""
        customer_map = {c.name: c for c in self.customers}
        dc_demand = {dc.name: 0.0 for dc in self.distribution_centers}
        
        for dc_name, cust_names in assignments.items():
            for cust_name in cust_names:
                dc_demand[dc_name] += customer_map[cust_name].annual_demand
        
        return dc_demand
    
    def _calculate_costs(self, dc_demand: Dict[str, float]) -> Tuple[Dict[str, float], float]:
        """Calculate costs for each DC and total system cost."""
        dc_costs = {}
        total_cost = 0.0
        dc_map = {dc.name: dc for dc in self.distribution_centers}
        
        for dc_name, demand in dc_demand.items():
            dc = dc_map[dc_name]
            if demand > dc.capacity:
                logger.warning(f"Demand {demand} exceeds capacity {dc.capacity} for DC {dc_name}")
            
            variable_cost = demand * dc.variable_cost_per_unit
            total_dc_cost = dc.fixed_cost + variable_cost
            dc_costs[dc_name] = total_dc_cost
            total_cost += total_dc_cost
        
        return dc_costs, total_cost
    
    def simulate_current_state(self) -> Dict:
        """Simulate current distribution network costs."""
        assignments = self._assign_customers_to_nearest_dc()
        dc_demand = self._calculate_total_demand_per_dc(assignments)
        dc_costs, total_cost = self._calculate_costs(dc_demand)
        
        return {
            'assignments': assignments,
            'demand_per_dc': dc_demand,
            'costs_per_dc': dc_costs,
            'total_cost': total_cost
        }
    
    def simulate_plm_advantages(self, 
                              plm_dc: DistributionCenter,
                              economies_of_scale_factor: float = 0.9) -> Dict:
        """Simulate cost savings with PLM's geographic advantages and economies of scale."""
        if not isinstance(plm_dc, DistributionCenter):
            raise ValueError("plm_dc must be a DistributionCenter object")
        
        # Create new network with PLM DC added
        new_network = self.distribution_centers + [plm_dc]
        temp_optimizer = DistributionOptimizer(new_network, self.customers)
        
        # Get assignments with PLM DC in network
        assignments = temp_optimizer._assign_customers_to_nearest_dc()
        dc_demand = temp_optimizer._calculate_total_demand_per_dc(assignments)
        
        # Apply economies of scale to PLM DC's variable costs
        plm_dc_map = {dc.name: dc for dc in new_network}
        plm_dc_map[plm_dc.name].variable_cost_per_unit *= economies_of_scale_factor
        
        dc_costs, total_cost = temp_optimizer._calculate_costs(dc_demand)
        
        return {
            'assignments': assignments,
            'demand_per_dc': dc_demand,
            'costs_per_dc': dc_costs,
            'total_cost': total_cost,
            'savings_vs_current': self.simulate_current_state()['total_cost'] - total_cost
        }
    
    def visualize_network(self, assignments: Dict[str, List[str]], title: str = "Distribution Network") -> None:
        """Visualize the distribution network with assignments."""
        plt.figure(figsize=(12, 8))
        
        # Plot distribution centers
        for dc in self.distribution_centers:
            plt.scatter(dc.longitude, dc.latitude, c='red', s=100, marker='s', label='DC' if dc == self.distribution_centers[0] else "")
            plt.text(dc.longitude, dc.latitude, dc.name, fontsize=9)
        
        # Plot customers and their assignments
        customer_map = {c.name: c for c in self.customers}
        colors = plt.cm.tab20(np.linspace(0, 1, len(self.distribution_centers)))
        
        for i, (dc_name, cust_names) in enumerate(assignments.items()):
            dc = next(dc for dc in self.distribution_centers if dc.name == dc_name)
            for cust_name in cust_names:
                customer = customer_map[cust_name]
                plt.scatter(customer.longitude, customer.latitude, c=[colors[i]], s=50)
                plt.plot([dc.longitude, customer.longitude], [dc.latitude, customer.latitude], 
                         c=colors[i], alpha=0.3)
        
        plt.title(title)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(True)
        plt.legend()
        plt.show()

def example_usage():
    """Example usage of the DistributionOptimizer class."""
    try:
        # Sample distribution centers
        dc1 = DistributionCenter("DC1", 40.7128, -74.0060, 500000, 5.0, 100000)
        dc2 = DistributionCenter("DC2", 34.0522, -118.2437, 600000, 4.5, 120000)
        
        # Sample customers
        customers = [
            CustomerLocation("CustomerA", 41.8781, -87.6298, 20000),
            CustomerLocation("CustomerB", 39.9526, -75.1652, 15000),
            CustomerLocation("CustomerC", 32.7157, -117.1611, 25000),
            CustomerLocation("CustomerD", 37.7749, -122
