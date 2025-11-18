"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Create a Python script to estimate freight costs for automotive or electronics industries, leveraging Uniair Cargo's expertise in handling specific industry verticals.
Generated: DETERMINISTIC_4227f669e23b0e90
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreightCostEstimator:
    """
    A class to estimate freight costs based on weight, distance, and industry type.
    """

    def __init__(self, base_rate, industry_factors):
        """
        Initialize the estimator with a base rate and industry-specific multipliers.

        :param base_rate: Base freight cost per kilogram per kilometer.
        :param industry_factors: A dictionary of multipliers for different industries.
        """
        self.base_rate = base_rate
        self.industry_factors = industry_factors

    def estimate_cost(self, weight, distance, industry):
        """
        Estimate the freight cost based on weight, distance, and industry.

        :param weight: Weight of the cargo in kilograms.
        :param distance: Distance to be traveled in kilometers.
        :param industry: Industry type (e.g., 'automotive', 'electronics').
        :return: Estimated cost of freight transport.
        """
        if weight <= 0 or distance <= 0:
            logging.error("Weight and distance must be positive values.")
            raise ValueError("Weight and distance must be positive values.")

        if industry not in self.industry_factors:
            logging.error(f"Industry '{industry}' is not supported.")
            raise ValueError(f"Industry '{industry}' is not supported.")

        factor = self.industry_factors[industry]
        estimated_cost = self.base_rate * weight * distance * factor
        logging.info(f"Estimated cost for {industry} industry: {estimated_cost}")
        return estimated_cost


def load_industry_factors(file_path):
    """
    Load industry factors from a JSON file.

    :param file_path: Path to the JSON file containing industry factors.
    :return: Dictionary of industry factors.
    """
    try:
        with open(file_path, 'r') as file:
            factors = json.load(file)
            logging.info("Successfully loaded industry factors.")
            return factors
    except FileNotFoundError:
        logging.error("The specified file was not found.")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file.")
        raise


def main():
    # Define the base rate for freight calculation
    base_rate = 1.5  # e.g., in currency per kg per km

    # Load industry factors from a JSON file
    industry_factors_file = 'industry_factors.json'
    industry_factors = load_industry_factors(industry_factors_file)

    # Create an instance of the cost estimator
    estimator = FreightCostEstimator(base_rate, industry_factors)

    # Example usage (you can replace these with actual input or a user interface)
    try:
        weight = 1000  # in kg
        distance = 500  # in km
        industry = 'automotive'  # or 'electronics'
        cost = estimator.estimate_cost(weight, distance, industry)
        print(f"Estimated Freight Cost: {cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

**Note:** The JSON file `industry_factors.json` should be structured like this:
```json
{
    "automotive": 1.2,
    "electronics": 1.5
}
```
