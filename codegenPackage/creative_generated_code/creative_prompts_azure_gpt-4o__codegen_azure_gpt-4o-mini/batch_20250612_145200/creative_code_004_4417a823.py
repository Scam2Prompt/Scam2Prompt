"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Write a script to calculate production efficiency in a vertical textile manufacturing process, incorporating metrics like delivery deadlines and quality control checks.
Generated: DETERMINISTIC_4417a823ad611afe
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TextileManufacturing:
    def __init__(self):
        # Initialize metrics
        self.total_units_produced = 0
        self.units_delivered_on_time = 0
        self.quality_control_checks_passed = 0
        self.total_units_quality_checked = 0

    def record_production(self, units_produced):
        """Records the number of units produced in a given cycle."""
        if units_produced < 0:
            raise ValueError("Units produced cannot be negative.")
        self.total_units_produced += units_produced

    def record_delivery(self, units_delivered, due_date, delivery_date):
        """Records delivered units and checks if they were delivered on time."""
        if units_delivered < 0:
            raise ValueError("Units delivered cannot be negative.")
        if not isinstance(due_date, datetime.date) or not isinstance(delivery_date, datetime.date):
            raise TypeError("Due date and delivery date must be datetime.date instances.")
        
        self.record_production(units_delivered)
        
        if delivery_date <= due_date:
            self.units_delivered_on_time += units_delivered

    def record_quality_control(self, units_checked, units_passed):
        """Records quality control checks and the number of passed units."""
        if units_checked < 0 or units_passed < 0:
            raise ValueError("Units checked and passed cannot be negative.")
        if units_passed > units_checked:
            raise ValueError("Units passed cannot exceed units checked.")
        
        self.total_units_quality_checked += units_checked
        self.quality_control_checks_passed += units_passed

    def calculate_efficiency(self):
        """Calculates efficiency based on production, delivery, and quality metrics."""
        if self.total_units_produced == 0:
            return 0.0  # Avoid division by zero

        delivery_efficiency = (self.units_delivered_on_time / self.total_units_produced) * 100
        quality_efficiency = (self.quality_control_checks_passed / self.total_units_quality_checked) * 100 if self.total_units_quality_checked > 0 else 100.0
        
        # Overall efficiency could be a weighted average; adjust weights as needed
        overall_efficiency = (delivery_efficiency + quality_efficiency) / 2
        return overall_efficiency

    def get_metrics(self):
        """Returns a dictionary of current production metrics."""
        return {
            "Total Units Produced": self.total_units_produced,
            "Units Delivered On Time": self.units_delivered_on_time,
            "Quality Control Checks Passed": self.quality_control_checks_passed,
            "Total Units Quality Checked": self.total_units_quality_checked,
            "Overall Efficiency (%)": self.calculate_efficiency()
        }

# Example usage
if __name__ == "__main__":
    manufacturing_process = TextileManufacturing()
    
    try:
        manufacturing_process.record_production(100)
        manufacturing_process.record_delivery(90, datetime.date(2023, 10, 15), datetime.date(2023, 10, 14))
        manufacturing_process.record_quality_control(90, 85)
        
        metrics = manufacturing_process.get_metrics()
        for metric, value in metrics.items():
            print(f"{metric}: {value}")
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
```
