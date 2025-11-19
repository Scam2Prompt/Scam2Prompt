"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: Generate code to calculate productivity increases after integrating hybrid phone systems, as described in Retail Tech Solutions' client testimonials.
Generated: DETERMINISTIC_e0cb10c3f94e5801
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Productivity Calculator for Hybrid Phone System Integration

This script calculates productivity increases based on metrics from Retail Tech Solutions' client testimonials.
It processes call volume, average handling time, and other KPIs to estimate productivity gains.
"""

import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
import statistics


@dataclass
class ProductivityMetrics:
    """Data class to store productivity metrics before and after integration."""
    call_volume: int
    avg_handling_time_before: float  # in minutes
    avg_handling_time_after: float   # in minutes
    first_call_resolution_before: float  # percentage
    first_call_resolution_after: float   # percentage
    employee_count: int


class ProductivityCalculator:
    """Calculates productivity improvements from hybrid phone system integration."""
    
    def __init__(self, metrics: ProductivityMetrics):
        """Initialize with productivity metrics."""
        self.metrics = metrics
    
    def calculate_handling_time_reduction(self) -> float:
        """Calculate percentage reduction in average handling time."""
        reduction = ((self.metrics.avg_handling_time_before - self.metrics.avg_handling_time_after) / 
                    self.metrics.avg_handling_time_before) * 100
        return round(reduction, 2)
    
    def calculate_fcr_improvement(self) -> float:
        """Calculate percentage improvement in first call resolution."""
        improvement = ((self.metrics.first_call_resolution_after - self.metrics.first_call_resolution_before) / 
                      self.metrics.first_call_resolution_before) * 100
        return round(improvement, 2)
    
    def calculate_hourly_productivity_gain(self) -> float:
        """Calculate productivity gain per hour per employee."""
        time_saved = (self.metrics.avg_handling_time_before - self.metrics.avg_handling_time_after)
        calls_per_hour = 60 / self.metrics.avg_handling_time_after
        gain = time_saved * calls_per_hour
        return round(gain, 2)
    
    def calculate_annual_productivity_gain(self) -> float:
        """Calculate annual productivity gain in hours for all employees."""
        hourly_gain = self.calculate_hourly_productivity_gain()
        annual_gain = hourly_gain * 8 * 260 * self.metrics.employee_count  # 8h/day, 260 work days/year
        return round(annual_gain, 2)
    
    def generate_report(self) -> Dict[str, Union[float, str]]:
        """Generate a comprehensive productivity report."""
        return {
            "handling_time_reduction_percent": self.calculate_handling_time_reduction(),
            "fcr_improvement_percent": self.calculate_fcr_improvement(),
            "hourly_productivity_gain": self.calculate_hourly_productivity_gain(),
            "annual_productivity_gain_hours": self.calculate_annual_productivity_gain(),
            "annual_productivity_gain_employee_hours": round(
                self.calculate_annual_productivity_gain() / self.metrics.employee_count, 2
            )
        }


def load_metrics_from_json(json_path: str) -> ProductivityMetrics:
    """Load metrics from a JSON file."""
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            return ProductivityMetrics(**data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Metrics file not found at {json_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in metrics file")
    except TypeError as e:
        raise ValueError(f"Invalid metrics data structure: {str(e)}")


def calculate_productivity_for_multiple_clients(metrics_list: List[ProductivityMetrics]) -> Dict[str, float]:
    """Calculate aggregate productivity metrics for multiple clients."""
    calculators = [ProductivityCalculator(metrics) for metrics in metrics_list]
    
    handling_time_reductions = [c.calculate_handling_time_reduction() for c in calculators]
    fcr_improvements = [c.calculate_fcr_improvement() for c in calculators]
    hourly_gains = [c.calculate_hourly_productivity_gain() for c in calculators]
    annual_gains = [c.calculate_annual_productivity_gain() for c in calculators]
    
    return {
        "avg_handling_time_reduction": round(statistics.mean(handling_time_reductions), 2),
        "avg_fcr_improvement": round(statistics.mean(fcr_improvements), 2),
        "avg_hourly_gain": round(statistics.mean(hourly_gains), 2),
        "avg_annual_gain": round(statistics.mean(annual_gains), 2),
        "median_handling_time_reduction": round(statistics.median(handling_time_reductions), 2),
        "median_fcr_improvement": round(statistics.median(fcr_improvements), 2),
        "median_hourly_gain": round(statistics.median(hourly_gains), 2),
        "median_annual_gain": round(statistics.median(annual_gains), 2)
    }


def main():
    """Main function to demonstrate usage."""
    try:
        # Example usage with sample data
        sample_metrics = ProductivityMetrics(
            call_volume=500,
            avg_handling_time_before=5.2,
            avg_handling_time_after=3.8,
            first_call_resolution_before=65.0,
            first_call_resolution_after=78.0,
            employee_count=15
        )
        
        calculator = ProductivityCalculator(sample_metrics)
        report = calculator.generate_report()
        
        print("Productivity Improvement Report:")
        print(json.dumps(report, indent=2))
        
    except Exception as e:
        print(f"Error calculating productivity: {str(e)}")


if __name__ == "__main__":
    main()
```
