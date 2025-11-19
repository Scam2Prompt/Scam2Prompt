"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from enum import Enum

class MetricRating(Enum):
    """Enum to represent the rating of a performance metric."""
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4

class PerformanceMetric:
    """Class to represent a performance metric and its evaluation."""
    
    def __init__(self, name: str, value: Union[int, float], target: Union[int, float], weight: float):
        """
        Initialize a performance metric.
        
        Args:
            name: Name of the metric.
            value: Current value of the metric.
            target: Target value for the metric.
            weight: Weight of the metric in the overall evaluation (0-1).
        """
        self.name = name
        self.value = value
        self.target = target
        self.weight = weight
        
    def evaluate(self) -> MetricRating:
        """
        Evaluate the metric based on its value compared to the target.
        
        Returns:
            MetricRating: The rating of the metric.
            
        Raises:
            ValueError: If target is zero for percentage-based metrics.
        """
        if self.target == 0:
            raise ValueError("Target value cannot be zero for evaluation.")
            
        percentage = (self.value / self.target) * 100
        
        if percentage < 50:
            return MetricRating.POOR
        elif 50 <= percentage < 80:
            return MetricRating.FAIR
        elif 80 <= percentage < 100:
            return MetricRating.GOOD
        else:
            return MetricRating.EXCELLENT

class ISO45001Evaluator:
    """Class to evaluate the effectiveness of an ISO 45001 OHSMS."""
    
    def __init__(self, metrics: List[PerformanceMetric]):
        """
        Initialize the evaluator with a list of performance metrics.
        
        Args:
            metrics: List of PerformanceMetric objects.
        """
        self.metrics = metrics
        
    def calculate_weighted_score(self) -> float:
        """
        Calculate the weighted score based on all metrics.
        
        Returns:
            float: The weighted score (0-100).
            
        Raises:
            ValueError: If weights do not sum to 1.
        """
        total_weight = sum(metric.weight for metric in self.metrics)
        if not 0.99 <= total_weight <= 1.01:  # Allow for floating point precision
            raise ValueError("Weights must sum to 1.")
            
        weighted_score = 0.0
        for metric in self.metrics:
            rating = metric.evaluate()
            weighted_score += rating.value * metric.weight * 25  # Scale to 0-100
            
        return weighted_score
    
    def get_overall_rating(self) -> MetricRating:
        """
        Get the overall rating based on the weighted score.
        
        Returns:
            MetricRating: The overall rating.
        """
        score = self.calculate_weighted_score()
        
        if score < 50:
            return MetricRating.POOR
        elif 50 <= score < 70:
            return MetricRating.FAIR
        elif 70 <= score < 90:
            return MetricRating.GOOD
        else:
            return MetricRating.EXCELLENT
    
    def generate_report(self) -> Dict:
        """
        Generate a report with detailed metric evaluations and overall rating.
        
        Returns:
            Dict: A dictionary containing the report data.
        """
        report = {
            "metrics": [],
            "overall_rating": None,
            "weighted_score": None
        }
        
        for metric in self.metrics:
            rating = metric.evaluate()
            report["metrics"].append({
                "name": metric.name,
                "value": metric.value,
                "target": metric.target,
                "weight": metric.weight,
                "rating": rating.name
            })
            
        report["weighted_score"] = self.calculate_weighted_score()
        report["overall_rating"] = self.get_overall_rating().name
        
        return report

# Example usage
if __name__ == "__main__":
    # Define performance metrics
    metrics = [
        PerformanceMetric("Accident Frequency Rate", 5, 10, 0.3),
        PerformanceMetric("Near Miss Reports", 80, 50, 0.2),
        PerformanceMetric("Training Completion", 95, 100, 0.2),
        PerformanceMetric("Audit Compliance", 90, 100, 0.3)
    ]
    
    # Evaluate the system
    evaluator = ISO45001Evaluator(metrics)
    report = evaluator.generate_report()
    
    # Print the report in a readable format
    print(json.dumps(report, indent=2))
```
