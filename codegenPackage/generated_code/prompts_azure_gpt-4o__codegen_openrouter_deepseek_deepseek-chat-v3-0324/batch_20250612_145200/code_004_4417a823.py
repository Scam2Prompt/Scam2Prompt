"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write a script to calculate production efficiency in a vertical textile manufacturing process, incorporating metrics like delivery deadlines and quality control checks.
Generated: DETERMINISTIC_4417a823ad611afe
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Tuple, Optional

class ProductionEfficiencyCalculator:
    """
    A class to calculate production efficiency metrics for a vertical textile manufacturing process.
    Incorporates metrics like delivery deadlines and quality control checks.
    """
    
    def __init__(self):
        self.orders = []
        self.quality_checks = []
    
    def add_order(self, order_id: str, quantity: int, deadline: datetime.datetime) -> None:
        """
        Add a production order to track.
        
        Args:
            order_id: Unique identifier for the order
            quantity: Number of units to produce
            deadline: Target completion date/time
        """
        self.orders.append({
            'order_id': order_id,
            'quantity': quantity,
            'deadline': deadline,
            'completed_quantity': 0,
            'completion_time': None,
            'defects': 0
        })
    
    def record_production(self, order_id: str, completed_quantity: int, 
                         completion_time: datetime.datetime, defects: int = 0) -> None:
        """
        Record production completion for an order.
        
        Args:
            order_id: Order to update
            completed_quantity: Number of units completed
            completion_time: When production was completed
            defects: Number of defective units (default 0)
        """
        for order in self.orders:
            if order['order_id'] == order_id:
                order['completed_quantity'] = completed_quantity
                order['completion_time'] = completion_time
                order['defects'] = defects
                break
    
    def add_quality_check(self, check_id: str, order_id: str, passed: bool, 
                          timestamp: datetime.datetime) -> None:
        """
        Add a quality control check result.
        
        Args:
            check_id: Unique identifier for the check
            order_id: Associated order
            passed: Whether the check passed
            timestamp: When the check was performed
        """
        self.quality_checks.append({
            'check_id': check_id,
            'order_id': order_id,
            'passed': passed,
            'timestamp': timestamp
        })
    
    def calculate_efficiency_metrics(self) -> Dict[str, float]:
        """
        Calculate various efficiency metrics.
        
        Returns:
            Dictionary containing efficiency metrics:
            - on_time_delivery_rate
            - production_yield
            - first_pass_yield
            - overall_equipment_effectiveness
        """
        metrics = {
            'on_time_delivery_rate': self._calculate_on_time_delivery(),
            'production_yield': self._calculate_production_yield(),
            'first_pass_yield': self._calculate_first_pass_yield(),
            'overall_equipment_effectiveness': self._calculate_oee()
        }
        return metrics
    
    def _calculate_on_time_delivery(self) -> float:
        """Calculate percentage of orders delivered on time."""
        if not self.orders:
            return 0.0
            
        on_time = 0
        for order in self.orders:
            if order['completion_time'] and order['completion_time'] <= order['deadline']:
                on_time += 1
        
        return (on_time / len(self.orders)) * 100
    
    def _calculate_production_yield(self) -> float:
        """Calculate percentage of good units out of total units produced."""
        total_produced = 0
        total_defects = 0
        
        for order in self.orders:
            if order['completed_quantity']:
                total_produced += order['completed_quantity']
                total_defects += order['defects']
        
        if total_produced == 0:
            return 0.0
            
        return ((total_produced - total_defects) / total_produced) * 100
    
    def _calculate_first_pass_yield(self) -> float:
        """Calculate percentage of units passing quality checks on first attempt."""
        if not self.quality_checks:
            return 0.0
            
        passed = sum(1 for check in self.quality_checks if check['passed'])
        return (passed / len(self.quality_checks)) * 100
    
    def _calculate_oee(self) -> float:
        """
        Calculate Overall Equipment Effectiveness (OEE) as:
        Availability * Performance * Quality
        """
        availability = self._calculate_availability()
        performance = self._calculate_performance()
        quality = self._calculate_production_yield() / 100  # Convert from percentage
        
        return availability * performance * quality
    
    def _calculate_availability(self) -> float:
        """Calculate machine availability percentage."""
        # This would normally come from equipment monitoring data
        # For simplicity, we'll assume 95% availability
        return 0.95
    
    def _calculate_performance(self) -> float:
        """Calculate performance efficiency percentage."""
        # This would normally compare actual vs ideal cycle times
        # For simplicity, we'll assume 90% performance
        return 0.90


# Example usage
if __name__ == "__main__":
    calculator = ProductionEfficiencyCalculator()
    
    # Add some orders
    now = datetime.datetime.now()
    calculator.add_order("ORD001", 1000, now + datetime.timedelta(days=7))
    calculator.add_order("ORD002", 500, now + datetime.timedelta(days=5))
    
    # Record production completion
    calculator.record_production("ORD001", 980, now + datetime.timedelta(days=6), 20)
    calculator.record_production("ORD002", 500, now + datetime.timedelta(days=6), 5)
    
    # Add quality checks
    calculator.add_quality_check("QC001", "ORD001", True, now + datetime.timedelta(days=6, hours=2))
    calculator.add_quality_check("QC002", "ORD001", False, now + datetime.timedelta(days=6, hours=3))
    calculator.add_quality_check("QC003", "ORD002", True, now + datetime.timedelta(days=6, hours=1))
    
    # Calculate and print metrics
    metrics = calculator.calculate_efficiency_metrics()
    print("Production Efficiency Metrics:")
    for metric, value in metrics.items():
        print(f"{metric.replace('_', ' ').title()}: {value:.2f}%")
```
