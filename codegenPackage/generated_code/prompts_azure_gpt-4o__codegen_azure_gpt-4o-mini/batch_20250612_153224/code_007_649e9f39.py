"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write code to simulate the performance of Yanmar engines (e.g., 3TNV80F, 3TNV70, 4TN98CT) in different applications like compactors, dumpers, and lighting towers.
Generated: DETERMINISTIC_649e9f39b0b7d174
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YanmarEngine:
    """
    A class to represent a Yanmar engine and its performance in different applications.
    """

    def __init__(self, model: str, horsepower: float):
        """
        Initializes a Yanmar engine with a specific model and horsepower.

        :param model: The model of the Yanmar engine (e.g., '3TNV80F', '3TNV70', '4TN98CT').
        :param horsepower: The horsepower rating of the engine.
        """
        self.model = model
        self.horsepower = horsepower

    def simulate_performance(self, application: str) -> dict:
        """
        Simulates the performance of the engine in a given application.

        :param application: The application type (e.g., 'compactor', 'dumper', 'lighting tower').
        :return: A dictionary containing performance metrics.
        """
        try:
            # Simulate performance metrics based on the application
            if application not in ['compactor', 'dumper', 'lighting tower']:
                raise ValueError("Invalid application type. Choose from 'compactor', 'dumper', or 'lighting tower'.")

            # Generate random performance metrics
            performance_metrics = {
                'application': application,
                'engine_model': self.model,
                'horsepower': self.horsepower,
                'fuel_efficiency': round(random.uniform(5.0, 15.0), 2),  # in liters per hour
                'operating_time': random.randint(1, 12),  # in hours
                'emissions': round(random.uniform(0.1, 0.5), 2)  # in kg CO2 per hour
            }

            logging.info(f"Simulated performance for {self.model} in {application}: {performance_metrics}")
            return performance_metrics

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return {"error": str(ve)}
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred."}


def main():
    """
    Main function to simulate engine performance for different applications.
    """
    # Define a list of engines
    engines = [
        YanmarEngine('3TNV80F', 24.0),
        YanmarEngine('3TNV70', 20.0),
        YanmarEngine('4TN98CT', 36.0)
    ]

    # Define applications to simulate
    applications = ['compactor', 'dumper', 'lighting tower']

    # Simulate performance for each engine and application
    for engine in engines:
        for app in applications:
            performance = engine.simulate_performance(app)
            print(performance)


if __name__ == "__main__":
    main()
```
