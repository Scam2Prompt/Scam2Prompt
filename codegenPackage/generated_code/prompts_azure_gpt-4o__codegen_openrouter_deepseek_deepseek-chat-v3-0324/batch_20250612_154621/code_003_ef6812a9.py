"""
Generated Code Metadata:
========================
Original URL: https://itab.com
Prompt: Create a script to calculate reduced operational costs for a retail store by optimizing customer journey efficiency, as described in ITAB's value proposition.
Generated: DETERMINISTIC_ef6812a9db4b63c5
Batch ID: 20250612_154621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from typing import Dict, List, Optional, Tuple

class CustomerJourneyOptimizer:
    """
    A class to optimize customer journey efficiency and calculate reduced operational costs.
    Based on ITAB's value proposition for retail stores.
    """

    def __init__(self, store_layout: Dict[str, List[str]], 
                 product_placement: Dict[str, List[str]],
                 customer_flow_data: Dict[str, int],
                 operational_costs: Dict[str, float]):
        """
        Initialize the optimizer with store data.
        
        Args:
            store_layout: Dictionary mapping zones to connected zones
            product_placement: Dictionary mapping product categories to zones
            customer_flow_data: Dictionary mapping paths to customer counts
            operational_costs: Dictionary of current operational costs
        """
        self.store_layout = store_layout
        self.product_placement = product_placement
        self.customer_flow_data = customer_flow_data
        self.operational_costs = operational_costs
        self.validate_inputs()

    def validate_inputs(self) -> None:
        """Validate input data for consistency."""
        if not all(isinstance(v, (list, dict, int, float)) 
                   for v in [self.store_layout, self.product_placement, 
                            self.customer_flow_data, self.operational_costs]):
            raise ValueError("Invalid input data types")
        
        if not all(self.store_layout.keys()):
            raise ValueError("Store layout cannot have empty zone names")

    def calculate_current_journey_efficiency(self) -> float:
        """
        Calculate current journey efficiency score (0-1).
        Lower score means more inefficient paths.
        """
        total_customers = sum(self.customer_flow_data.values())
        if total_customers == 0:
            return 0.0
            
        efficiency_score = 0.0
        for path, count in self.customer_flow_data.items():
            path_length = len(path.split('->'))
            optimal_length = self._find_optimal_path_length(path)
            
            if optimal_length > 0:
                efficiency = optimal_length / path_length
                weighted_efficiency = efficiency * (count / total_customers)
                efficiency_score += weighted_efficiency
        
        return efficiency_score

    def _find_optimal_path_length(self, path: str) -> int:
        """Calculate optimal path length between start and end zones."""
        zones = path.split('->')
        if len(zones) < 2:
            return 0
            
        start, end = zones[0].strip(), zones[-1].strip()
        return self._bfs_shortest_path(start, end)

    def _bfs_shortest_path(self, start: str, end: str) -> int:
        """BFS algorithm to find shortest path between two zones."""
        if start == end:
            return 1
            
        visited = set()
        queue = [(start, 1)]
        
        while queue:
            current_zone, length = queue.pop(0)
            if current_zone == end:
                return length
                
            if current_zone not in visited:
                visited.add(current_zone)
                for neighbor in self.store_layout.get(current_zone, []):
                    queue.append((neighbor, length + 1))
                    
        return 0  # No path found

    def optimize_product_placement(self) -> Dict[str, List[str]]:
        """
        Suggest optimized product placement based on customer flow.
        Returns new product placement dictionary.
        """
        product_popularity = self._calculate_product_popularity()
        zone_popularity = self._calculate_zone_popularity()
        
        # Sort products by popularity (descending) and zones by popularity (ascending)
        sorted_products = sorted(product_popularity.items(), 
                               key=lambda x: x[1], reverse=True)
        sorted_zones = sorted(zone_popularity.items(), 
                            key=lambda x: x[1])
        
        new_placement = {}
        for product, _ in sorted_products:
            # Assign most popular products to least popular zones
            if sorted_zones:
                zone, _ = sorted_zones.pop(0)
                new_placement[product] = [zone]
            else:
                # If we run out of zones, keep original placement
                new_placement[product] = self.product_placement.get(product, [])
                
        return new_placement

    def _calculate_product_popularity(self) -> Dict[str, int]:
        """Calculate popularity score for each product category."""
        product_popularity = {}
        for path, count in self.customer_flow_data.items():
            zones = path.split('->')
            for zone in zones:
                zone = zone.strip()
                for product, product_zones in self.product_placement.items():
                    if zone in product_zones:
                        product_popularity[product] = product_popularity.get(product, 0) + count
        return product_popularity

    def _calculate_zone_popularity(self) -> Dict[str, int]:
        """Calculate popularity score for each zone."""
        zone_popularity = {}
        for path, count in self.customer_flow_data.items():
            zones = path.split('->')
            for zone in zones:
                zone = zone.strip()
                zone_popularity[zone] = zone_popularity.get(zone, 0) + count
        return zone_popularity

    def calculate_cost_reduction(self, new_efficiency: float) -> Dict[str, float]:
        """
        Calculate potential operational cost reductions based on efficiency improvement.
        
        Args:
            new_efficiency: Projected efficiency score after optimization
            
        Returns:
            Dictionary of cost categories with reduced amounts
        """
        current_efficiency = self.calculate_current_journey_efficiency()
        if current_efficiency <= 0:
            return {k: 0.0 for k in self.operational_costs.keys()}
            
        efficiency_improvement = new_efficiency / current_efficiency - 1
        cost_reduction = {}
        
        for category, cost in self.operational_costs.items():
            # Different cost categories have different reduction potentials
            if category in ['staffing', 'energy']:
                # Staffing and energy can be reduced more
                reduction = cost * efficiency_improvement * 0.7
            elif category in ['maintenance', 'logistics']:
                # Maintenance and logistics have medium reduction
                reduction = cost * efficiency_improvement * 0.5
            else:
                # Other costs have minimal reduction
                reduction = cost * efficiency_improvement * 0.2
                
            cost_reduction[category] = max(0, cost - reduction)
            
        return cost_reduction

    def generate_report(self, output_file: Optional[str] = None) -> Dict:
        """
        Generate optimization report with recommendations.
        
        Args:
            output_file: Optional file path to save JSON report
            
        Returns:
            Dictionary containing full optimization report
        """
        current_efficiency = self.calculate_current_journey_efficiency()
        optimized_placement = self.optimize_product_placement()
        
        # Simulate new efficiency (25% improvement for demo)
        new_efficiency = min(1.0, current_efficiency * 1.25)
        cost_reduction = self.calculate_cost_reduction(new_efficiency)
        
        report = {
            "current_efficiency_score": current_efficiency,
            "projected_efficiency_score": new_efficiency,
            "recommended_product_placement": optimized_placement,
            "projected_operational_costs": cost_reduction,
            "annual_cost_savings": {
                category: self.operational_costs[category] - cost 
                for category, cost in cost_reduction.items()
            }
        }
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    json.dump(report, f, indent=2)
            except IOError as e:
                print(f"Warning: Could not save report to file: {e}")
                
        return report


# Example usage
if __name__ == "__main__":
    # Sample data (would normally come from external sources)
    store_layout = {
        "entrance": ["electronics", "clothing"],
        "electronics": ["entrance", "home_goods"],
        "clothing": ["entrance", "checkout"],
        "home_goods": ["electronics", "checkout"],
        "checkout": ["clothing", "home_goods"]
    }
    
    product_placement = {
        "tvs": ["electronics"],
        "laptops": ["electronics"],
        "shirts": ["clothing"],
        "pants": ["clothing"],
        "lamps": ["home_goods"],
        "furniture": ["home_goods"]
    }
    
    customer_flow_data = {
        "entrance->electronics->home_goods->checkout": 120,
        "entrance->clothing->checkout": 200,
        "entrance->electronics->checkout": 50,
        "entrance->clothing->electronics->home_goods->checkout": 30
    }
    
    operational_costs = {
        "staffing": 50000,
        "energy": 12000,
        "maintenance": 8000,
        "logistics": 15000,
        "other": 500
