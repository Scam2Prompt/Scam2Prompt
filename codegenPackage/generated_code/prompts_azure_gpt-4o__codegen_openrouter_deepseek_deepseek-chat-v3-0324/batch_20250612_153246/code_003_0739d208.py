"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Develop a script to calculate the cost optimization for maritime provisioning services, including food supplies, electrical tools, and hygiene services, based on the efficiency principles highlighted by Supply Marine.
Generated: DETERMINISTIC_0739d20831b22f7e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maritime Provisioning Cost Optimization Calculator

This script calculates cost optimization for maritime provisioning services
including food supplies, electrical tools, and hygiene services based on
efficiency principles from Supply Marine.

Features:
- Calculate total cost based on item quantities and prices
- Apply bulk discounts based on quantity thresholds
- Optimize provisioning based on service priorities
- Generate cost reports with breakdowns
"""

import json
from typing import Dict, List, Tuple, Union

class MaritimeProvisioningOptimizer:
    """
    A class to optimize maritime provisioning costs based on Supply Marine principles.
    """

    def __init__(self):
        """
        Initialize the optimizer with default pricing and discount thresholds.
        """
        self.pricing_data = {
            "food_supplies": {
                "base_price": 5.0,
                "bulk_threshold": 100,
                "bulk_discount": 0.15  # 15% discount
            },
            "electrical_tools": {
                "base_price": 50.0,
                "bulk_threshold": 20,
                "bulk_discount": 0.10  # 10% discount
            },
            "hygiene_services": {
                "base_price": 30.0,
                "bulk_threshold": 50,
                "bulk_discount": 0.20  # 20% discount
            }
        }
        self.priority_weights = {
            "food_supplies": 0.5,
            "hygiene_services": 0.3,
            "electrical_tools": 0.2
        }

    def calculate_item_cost(self, item_type: str, quantity: int) -> float:
        """
        Calculate the cost for a specific item type considering bulk discounts.
        
        Args:
            item_type: Type of item (food_supplies, electrical_tools, hygiene_services)
            quantity: Number of items
            
        Returns:
            Total cost for the item type
            
        Raises:
            ValueError: If item_type is invalid or quantity is negative
        """
        if item_type not in self.pricing_data:
            raise ValueError(f"Invalid item type: {item_type}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
            
        item_data = self.pricing_data[item_type]
        base_price = item_data["base_price"]
        bulk_threshold = item_data["bulk_threshold"]
        bulk_discount = item_data["bulk_discount"]
        
        if quantity >= bulk_threshold:
            return quantity * base_price * (1 - bulk_discount)
        return quantity * base_price

    def calculate_total_cost(self, order: Dict[str, int]) -> Dict[str, Union[float, Dict]]:
        """
        Calculate the total cost for an order with all items.
        
        Args:
            order: Dictionary with item types as keys and quantities as values
            
        Returns:
            Dictionary containing:
            - total_cost: The total optimized cost
            - itemized_costs: Breakdown of costs per item type
            - discounts_applied: Discounts received per item type
            
        Raises:
            ValueError: If order contains invalid item types or negative quantities
        """
        total_cost = 0.0
        itemized_costs = {}
        discounts_applied = {}
        
        for item_type, quantity in order.items():
            try:
                item_cost = self.calculate_item_cost(item_type, quantity)
                itemized_costs[item_type] = item_cost
                
                # Calculate discount amount
                base_cost = quantity * self.pricing_data[item_type]["base_price"]
                discount = base_cost - item_cost
                discounts_applied[item_type] = discount
                
                total_cost += item_cost
            except ValueError as e:
                raise ValueError(f"Error processing {item_type}: {str(e)}")
                
        return {
            "total_cost": round(total_cost, 2),
            "itemized_costs": itemized_costs,
            "discounts_applied": discounts_applied
        }

    def optimize_provisioning(self, budget: float, min_requirements: Dict[str, int]) -> Dict:
        """
        Optimize provisioning within budget constraints while meeting minimum requirements.
        
        Args:
            budget: Total available budget
            min_requirements: Minimum quantities required for each item type
            
        Returns:
            Dictionary containing:
            - optimized_order: Recommended quantities for each item type
            - optimized_cost: Total cost of optimized order
            - budget_utilization: Percentage of budget used
            - remaining_budget: Amount left after optimization
            
        Raises:
            ValueError: If budget is insufficient for minimum requirements
        """
        # First calculate cost for minimum requirements
        min_cost_result = self.calculate_total_cost(min_requirements)
        min_cost = min_cost_result["total_cost"]
        
        if min_cost > budget:
            raise ValueError(f"Insufficient budget. Minimum requirements cost {min_cost}, budget is {budget}")
            
        remaining_budget = budget - min_cost
        optimized_order = min_requirements.copy()
        
        # Calculate how much we can increase each item based on priority
        priority_items = sorted(
            self.priority_weights.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        for item_type, _ in priority_items:
            if remaining_budget <= 0:
                break
                
            item_data = self.pricing_data[item_type]
            base_price = item_data["base_price"]
            bulk_threshold = item_data["bulk_threshold"]
            current_quantity = optimized_order[item_type]
            
            # Calculate how many more we can buy with remaining budget
            possible_quantity = int(remaining_budget / base_price)
            
            if possible_quantity > 0:
                new_quantity = current_quantity + possible_quantity
                cost_with_new_quantity = self.calculate_item_cost(item_type, new_quantity)
                cost_increase = cost_with_new_quantity - min_cost_result["itemized_costs"][item_type]
                
                if cost_increase <= remaining_budget:
                    optimized_order[item_type] = new_quantity
                    remaining_budget -= cost_increase
                else:
                    # Find maximum quantity we can add within remaining budget
                    for q in range(possible_quantity, 0, -1):
                        test_quantity = current_quantity + q
                        test_cost = self.calculate_item_cost(item_type, test_quantity)
                        test_increase = test_cost - min_cost_result["itemized_costs"][item_type]
                        
                        if test_increase <= remaining_budget:
                            optimized_order[item_type] = test_quantity
                            remaining_budget -= test_increase
                            break
        
        optimized_cost_result = self.calculate_total_cost(optimized_order)
        optimized_cost = optimized_cost_result["total_cost"]
        budget_utilization = (optimized_cost / budget) * 100
        
        return {
            "optimized_order": optimized_order,
            "optimized_cost": optimized_cost,
            "budget_utilization": round(budget_utilization, 2),
            "remaining_budget": round(remaining_budget, 2)
        }

    def generate_report(self, optimization_result: Dict) -> str:
        """
        Generate a human-readable report from optimization results.
        
        Args:
            optimization_result: Result dictionary from optimize_provisioning
            
        Returns:
            Formatted report string
        """
        report_lines = [
            "Maritime Provisioning Optimization Report",
            "========================================",
            f"Optimized Order:",
        ]
        
        for item, quantity in optimization_result["optimized_order"].items():
            report_lines.append(f"  - {item.replace('_', ' ').title()}: {quantity} units")
            
        report_lines.extend([
            "",
            f"Total Optimized Cost: ${optimization_result['optimized_cost']:.2f}",
            f"Budget Utilization: {optimization_result['budget_utilization']}%",
            f"Remaining Budget: ${optimization_result['remaining_budget']:.2f}",
            "",
            "Note: Quantities have been optimized based on service priorities",
            "and bulk discount thresholds for maximum cost efficiency."
        ])
        
        return "\n".join(report_lines)

    def save_pricing_data(self, file_path: str) -> None:
        """
        Save current pricing data to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.pricing_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save pricing data: {str(e)}")

    def load_pricing_data(self, file_path: str) -> None:
        """
        Load pricing data from a JSON file.
        
        Args:
            file_path: Path to JSON file with pricing data
            
        Raises:
            IOError: If file cannot be read
            ValueError: If file contains invalid data
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            # Validate loaded data
            required_keys = {"base_price", "bulk_threshold", "bulk_discount"}
            for item_type, item
