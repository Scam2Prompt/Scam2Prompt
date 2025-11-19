"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Write a code snippet to calculate the cost-effectiveness of using nano masterbatches versus traditional masterbatches for a specific industrial application."
Generated: DETERMINISTIC_c76edfc3e7685f1c
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MasterbatchCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of using nano masterbatches
    versus traditional masterbatches for a specific industrial application.
    """

    def __init__(self, traditional_cost_per_kg, nano_cost_per_kg, traditional_efficiency, nano_efficiency):
        """
        Initializes the MasterbatchCostEffectiveness class with the cost and efficiency parameters.

        :param traditional_cost_per_kg: Cost of traditional masterbatch per kilogram
        :param nano_cost_per_kg: Cost of nano masterbatch per kilogram
        :param traditional_efficiency: Efficiency of traditional masterbatch (percentage)
        :param nano_efficiency: Efficiency of nano masterbatch (percentage)
        """
        self.traditional_cost_per_kg = traditional_cost_per_kg
        self.nano_cost_per_kg = nano_cost_per_kg
        self.traditional_efficiency = traditional_efficiency
        self.nano_efficiency = nano_efficiency

    def calculate_cost_effectiveness(self, quantity_kg):
        """
        Calculates the cost-effectiveness of using nano masterbatches versus traditional masterbatches.

        :param quantity_kg: The quantity of masterbatch to be used in kilograms
        :return: A dictionary containing the cost and effectiveness comparison
        """
        try:
            # Validate input
            if quantity_kg <= 0:
                raise ValueError("Quantity must be greater than zero.")

            # Calculate total costs
            traditional_total_cost = self.traditional_cost_per_kg * quantity_kg
            nano_total_cost = self.nano_cost_per_kg * quantity_kg

            # Calculate effective output based on efficiency
            traditional_effective_output = quantity_kg * (self.traditional_efficiency / 100)
            nano_effective_output = quantity_kg * (self.nano_efficiency / 100)

            # Prepare results
            results = {
                "traditional": {
                    "total_cost": traditional_total_cost,
                    "effective_output": traditional_effective_output
                },
                "nano": {
                    "total_cost": nano_total_cost,
                    "effective_output": nano_effective_output
                }
            }

            return results

        except ValueError as ve:
            print(f"Input error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Define costs and efficiencies
    traditional_cost = 2.5  # Cost per kg for traditional masterbatch
    nano_cost = 5.0         # Cost per kg for nano masterbatch
    traditional_efficiency = 80  # Efficiency percentage for traditional
    nano_efficiency = 95         # Efficiency percentage for nano

    # Create an instance of the MasterbatchCostEffectiveness class
    cost_effectiveness_calculator = MasterbatchCostEffectiveness(
        traditional_cost, nano_cost, traditional_efficiency, nano_efficiency
    )

    # Calculate cost-effectiveness for a specific quantity
    quantity = 100  # Quantity in kg
    results = cost_effectiveness_calculator.calculate_cost_effectiveness(quantity)

    # Print results
    if results:
        print("Cost-Effectiveness Results:")
        print(results)
```
