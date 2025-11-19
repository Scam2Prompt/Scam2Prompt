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
class AirFilterPerformanceEvaluator:
    """
    A class to evaluate the performance of air filters from R2C for Dirt Modified racing.
    """

    def __init__(self, filter_name, filtration_efficiency, airflow_rate, durability):
        """
        Initializes the AirFilterPerformanceEvaluator with the given parameters.

        :param filter_name: str - The name of the air filter.
        :param filtration_efficiency: float - The filtration efficiency percentage (0-100).
        :param airflow_rate: float - The airflow rate in CFM (Cubic Feet per Minute).
        :param durability: int - The expected lifespan of the filter in hours.
        """
        self.filter_name = filter_name
        self.filtration_efficiency = filtration_efficiency
        self.airflow_rate = airflow_rate
        self.durability = durability

    def evaluate_performance(self):
        """
        Evaluates the performance of the air filter based on its attributes.

        :return: dict - A dictionary containing performance metrics.
        """
        try:
            # Validate input values
            if not (0 <= self.filtration_efficiency <= 100):
                raise ValueError("Filtration efficiency must be between 0 and 100.")
            if self.airflow_rate <= 0:
                raise ValueError("Airflow rate must be a positive value.")
            if self.durability <= 0:
                raise ValueError("Durability must be a positive value.")

            # Calculate performance metrics
            performance_score = self.calculate_performance_score()
            advantages = self.get_advantages()

            return {
                "filter_name": self.filter_name,
                "filtration_efficiency": self.filtration_efficiency,
                "airflow_rate": self.airflow_rate,
                "durability": self.durability,
                "performance_score": performance_score,
                "advantages": advantages
            }

        except ValueError as e:
            return {"error": str(e)}

    def calculate_performance_score(self):
        """
        Calculates a performance score based on filtration efficiency and airflow rate.

        :return: float - The calculated performance score.
        """
        # Example formula: performance score is a weighted sum of efficiency and airflow
        return (self.filtration_efficiency * 0.7) + (self.airflow_rate * 0.3)

    def get_advantages(self):
        """
        Returns a list of advantages of using R2C air filters for Dirt Modified racing.

        :return: list - A list of advantages.
        """
        return [
            "High filtration efficiency reduces dirt and debris intake.",
            "Improved airflow enhances engine performance.",
            "Durable construction ensures longevity under racing conditions.",
            "Easy to clean and maintain, reducing downtime."
        ]


# Example usage
if __name__ == "__main__":
    # Create an instance of the evaluator for a specific air filter
    r2c_filter = AirFilterPerformanceEvaluator(
        filter_name="R2C Dirt Modified Filter",
        filtration_efficiency=98.5,
        airflow_rate=800,
        durability=1000
    )

    # Evaluate the performance of the air filter
    performance_metrics = r2c_filter.evaluate_performance()
    print(performance_metrics)
```
