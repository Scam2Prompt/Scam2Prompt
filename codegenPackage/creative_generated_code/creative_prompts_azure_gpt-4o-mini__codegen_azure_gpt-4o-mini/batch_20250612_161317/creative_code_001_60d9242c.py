"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FreightForwardingCalculator:
    """
    A class to calculate the total cost of air freight forwarding.
    """

    # Constants for the cost calculation
    BASE_RATE_PER_KG = 5.0     # Base rate per kilogram
    DISTANCE_RATE_PER_KM = 0.1  # Rate per kilometer
    INSURANCE_RATE = 0.02       # Insurance rate as a percentage of total cost

    def __init__(self, weight: float, distance: float, insure: bool = False):
        """
        Initializes the calculator with weight, distance, and insurance option.

        :param weight: Weight of the cargo in kilograms.
        :param distance: Distance for shipment in kilometers.
        :param insure: Boolean indicating if insurance is required.
        """
        self.weight = weight
        self.distance = distance
        self.insure = insure

    def calculate_base_cost(self) -> float:
        """
        Calculate base cost based on weight and distance.

        :return: Base cost of the air freight.
        """
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Weight and distance must be non-negative.")

        cost = (self.weight * self.BASE_RATE_PER_KG) + (self.distance * self.DISTANCE_RATE_PER_KM)
        return cost

    def calculate_insurance_cost(self, base_cost: float) -> float:
        """
        Calculate the insurance cost based on base cost.

        :param base_cost: The calculated base cost of the air freight.
        :return: Insurance cost if applicable, 0 otherwise.
        """
        if self.insure:
            insurance_cost = base_cost * self.INSURANCE_RATE
            return insurance_cost
        return 0.0

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost including base cost and insurance if applicable.

        :return: Total cost of the air freight.
        """
        base_cost = self.calculate_base_cost()
        insurance_cost = self.calculate_insurance_cost(base_cost)
        total_cost = base_cost + insurance_cost
        return total_cost


def main():
    """
    Main function to demonstrate the usage of the FreightForwardingCalculator.
    """
    # Example inputs
    weight = 100.0  # Weight in kg
    distance = 1500.0  # Distance in km
    insure = True  # Flag for insurance

    # Create an instance of the calculator
    calculator = FreightForwardingCalculator(weight, distance, insure)

    try:
        # Calculate and print the total cost
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of air freight forwarding is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
