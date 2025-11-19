"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Create a function that estimates the cost of composite letters based on the specifications provided by ThePrintNan.
Generated: DETERMINISTIC_959e91a7b33fd4b2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompositeLetterCostEstimator:
    """
    A class to estimate the cost of composite letters based on specified rates.
    """

    def __init__(self, base_cost: float, additional_cost_per_letter: float):
        """
        Initializes the estimator with base cost and additional cost per letter.

        :param base_cost: The base cost for creating a composite letter.
        :param additional_cost_per_letter: The cost added for each additional letter.
        """
        if base_cost < 0 or additional_cost_per_letter < 0:
            raise ValueError("Costs must be non-negative.")
        
        self.base_cost = base_cost
        self.additional_cost_per_letter = additional_cost_per_letter

    def estimate_cost(self, number_of_letters: int) -> float:
        """
        Estimates the total cost of a composite letter based on the number of letters.

        :param number_of_letters: The total number of letters in the composite.
        :return: The estimated total cost.
        :raises ValueError: If the number of letters is negative.
        """
        if number_of_letters < 0:
            raise ValueError("Number of letters must be non-negative.")

        # Calculate total cost
        total_cost = self.base_cost + (self.additional_cost_per_letter * number_of_letters)
        return total_cost


def main():
    """
    Main function to demonstrate the usage of the CompositeLetterCostEstimator.
    """
    try:
        # Example rates
        base_cost = 10.0  # Base cost for the composite letter
        additional_cost_per_letter = 2.0  # Cost for each additional letter

        # Create an instance of the estimator
        estimator = CompositeLetterCostEstimator(base_cost, additional_cost_per_letter)

        # Example number of letters
        number_of_letters = 5  # Change this value to test different scenarios

        # Estimate the cost
        estimated_cost = estimator.estimate_cost(number_of_letters)
        print(f"Estimated cost for {number_of_letters} letters: ${estimated_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
