"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instantconnect.info
Prompt: Describe how to measure the results of AI implementation in a business context, referencing Instant Connect AI's approach.
Generated: DETERMINISTIC_9d02c5249e8013e3
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AIImplementationMetrics:
    """
    A class to measure the results of AI implementation in a business context.
    
    Attributes:
        business_metrics (dict): A dictionary to store business metrics.
        ai_metrics (dict): A dictionary to store AI-specific metrics.
    """

    def __init__(self):
        """
        Initializes the AIImplementationMetrics with empty metrics dictionaries.
        """
        self.business_metrics = {}
        self.ai_metrics = {}

    def add_business_metric(self, metric_name, value):
        """
        Adds a business metric to the metrics collection.

        Args:
            metric_name (str): The name of the business metric.
            value (float): The value of the business metric.
        
        Raises:
            ValueError: If the value is not a float.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number.")
        self.business_metrics[metric_name] = value

    def add_ai_metric(self, metric_name, value):
        """
        Adds an AI-specific metric to the metrics collection.

        Args:
            metric_name (str): The name of the AI metric.
            value (float): The value of the AI metric.
        
        Raises:
            ValueError: If the value is not a float.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number.")
        self.ai_metrics[metric_name] = value

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) for the AI implementation.
        
        Returns:
            float: The calculated ROI as a percentage.
        
        Raises:
            ZeroDivisionError: If the total costs are zero.
        """
        try:
            total_benefits = sum(self.business_metrics.values())
            total_costs = sum(self.ai_metrics.values())
            roi = (total_benefits - total_costs) / total_costs * 100
            return roi
        except ZeroDivisionError:
            return float('inf')  # Infinite ROI if no costs are incurred

    def report_metrics(self):
        """
        Prints a summary report of business and AI metrics.
        """
        print("Business Metrics:")
        for name, value in self.business_metrics.items():
            print(f" - {name}: {value}")

        print("\nAI Metrics:")
        for name, value in self.ai_metrics.items():
            print(f" - {name}: {value}")

        try:
            roi = self.calculate_roi()
            print(f"\nReturn on Investment (ROI): {roi:.2f}%")
        except ZeroDivisionError:
            print("\nReturn on Investment (ROI): Undefined (zero costs)")

# Example usage
if __name__ == "__main__":
    metrics = AIImplementationMetrics()

    # Adding business and AI metrics
    metrics.add_business_metric("Increased Revenue", 150000.00)
    metrics.add_business_metric("Cost Savings", 30000.00)
    metrics.add_ai_metric("AI Development Costs", 50000.00)
    metrics.add_ai_metric("AI Maintenance Costs", 20000.00)

    # Reporting metrics
    metrics.report_metrics()
```
