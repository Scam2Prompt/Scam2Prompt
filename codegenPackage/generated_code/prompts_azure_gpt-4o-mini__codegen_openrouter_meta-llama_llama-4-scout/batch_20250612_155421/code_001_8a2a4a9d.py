"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Write a function to evaluate the performance of air filters from R2C, focusing on their advantages for Dirt Modified racing as highlighted by Metal Fab Pro.
Generated: DETERMINISTIC_8a2a4a9dbb945bbb
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# air_filter_evaluator.py

class AirFilter:
    """Represents an air filter with its characteristics."""

    def __init__(self, brand, model, flow_rate, filtration_efficiency, price):
        """
        Initializes an AirFilter object.

        Args:
            brand (str): The brand of the air filter.
            model (str): The model of the air filter.
            flow_rate (float): The flow rate of the air filter in CFM.
            filtration_efficiency (float): The filtration efficiency of the air filter in %.
            price (float): The price of the air filter.
        """
        self.brand = brand
        self.model = model
        self.flow_rate = flow_rate
        self.filtration_efficiency = filtration_efficiency
        self.price = price


class R2CAirFilterEvaluator:
    """Evaluates the performance of R2C air filters for Dirt Modified racing."""

    def __init__(self):
        """Initializes an R2CAirFilterEvaluator object."""
        self.r2c_air_filters = []

    def add_r2c_air_filter(self, air_filter):
        """
        Adds an R2C air filter to the evaluator.

        Args:
            air_filter (AirFilter): The R2C air filter to add.
        """
        if air_filter.brand == "R2C":
            self.r2c_air_filters.append(air_filter)
        else:
            raise ValueError("Only R2C air filters are supported.")

    def evaluate_performance(self):
        """
        Evaluates the performance of the added R2C air filters.

        Returns:
            list: A list of dictionaries containing the performance metrics for each air filter.
        """
        performance_metrics = []
        for air_filter in self.r2c_air_filters:
            # Calculate the performance score based on flow rate and filtration efficiency
            performance_score = air_filter.flow_rate * air_filter.filtration_efficiency / 100
            performance_metrics.append({
                "brand": air_filter.brand,
                "model": air_filter.model,
                "flow_rate": air_filter.flow_rate,
                "filtration_efficiency": air_filter.filtration_efficiency,
                "price": air_filter.price,
                "performance_score": performance_score
            })
        return performance_metrics

    def compare_performance(self):
        """
        Compares the performance of the added R2C air filters.

        Returns:
            dict: A dictionary containing the best air filter and its performance metrics.
        """
        if not self.r2c_air_filters:
            raise ValueError("No air filters added.")

        performance_metrics = self.evaluate_performance()
        best_air_filter = max(performance_metrics, key=lambda x: x["performance_score"])
        return {
            "best_air_filter": best_air_filter["brand"] + " " + best_air_filter["model"],
            "performance_metrics": best_air_filter
        }


def main():
    try:
        evaluator = R2CAirFilterEvaluator()

        # Create R2C air filters
        r2c_air_filter1 = AirFilter("R2C", "A1", 100, 95, 50)
        r2c_air_filter2 = AirFilter("R2C", "A2", 120, 96, 60)

        # Add air filters to the evaluator
        evaluator.add_r2c_air_filter(r2c_air_filter1)
        evaluator.add_r2c_air_filter(r2c_air_filter2)

        # Evaluate performance
        performance_metrics = evaluator.evaluate_performance()
        print("Performance Metrics:")
        for metrics in performance_metrics:
            print(metrics)

        # Compare performance
        best_air_filter = evaluator.compare_performance()
        print("\nBest Air Filter:")
        print(best_air_filter)

    except Exception as e:
        print("An error occurred: ", str(e))


if __name__ == "__main__":
    main()
```
