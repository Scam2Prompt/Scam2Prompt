"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skinport.in
Prompt: Create a function that calculates the cost of various skin treatments offered by Skinport, including PRP and medi facials.
Generated: DETERMINISTIC_36ff5585fc0755eb
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SkinTreatmentCalculator:
    """
    A class to calculate the cost of various skin treatments offered by Skinport.
    """

    # Predefined treatment costs
    TREATMENT_COSTS = {
        'PRP': 300.00,  # Cost for PRP treatment
        'Medi Facial': 150.00,  # Cost for Medi Facial treatment
    }

    def __init__(self):
        """
        Initializes the SkinTreatmentCalculator instance.
        """
        pass

    def calculate_cost(self, treatment_name: str, quantity: int) -> float:
        """
        Calculates the total cost for a given skin treatment.

        Args:
            treatment_name (str): The name of the treatment.
            quantity (int): The number of treatments.

        Returns:
            float: The total cost of the treatments.

        Raises:
            ValueError: If the treatment name is invalid or quantity is not positive.
        """
        # Validate the treatment name
        treatment_name = treatment_name.strip()
        if treatment_name not in self.TREATMENT_COSTS:
            raise ValueError(f"Invalid treatment name: '{treatment_name}'. Available treatments: {list(self.TREATMENT_COSTS.keys())}")

        # Validate the quantity
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(f"Quantity must be a positive integer. Given: {quantity}")

        # Calculate total cost
        total_cost = self.TREATMENT_COSTS[treatment_name] * quantity
        return total_cost

    def get_available_treatments(self) -> list:
        """
        Returns a list of available treatments.

        Returns:
            list: A list of strings representing available treatments.
        """
        return list(self.TREATMENT_COSTS.keys())


# Example usage
if __name__ == "__main__":
    calculator = SkinTreatmentCalculator()

    # Example of calculating the cost of 2 PRP treatments
    try:
        treatment = 'PRP'
        quantity = 2
        cost = calculator.calculate_cost(treatment, quantity)
        print(f"The total cost for {quantity} {treatment} treatments is: ${cost:.2f}")

        # Display available treatments
        available_treatments = calculator.get_available_treatments()
        print("Available treatments:", available_treatments)

    except ValueError as e:
        print(f"Error: {e}")
```
