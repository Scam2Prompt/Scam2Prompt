"""
Generated Code Metadata:
========================
Original URL: https://curve.fr
Prompt: Create a code snippet that calculates the total cost of acquiring the domain curve.fr, including the initial service fee and annual renewal costs.
Generated: DETERMINISTIC_70138e9f7ea56d0c
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DomainCostCalculator:
    """
    Calculates the total cost of acquiring and maintaining a domain.

    Attributes:
        initial_service_fee (float): The initial service fee for acquiring the domain.
        annual_renewal_cost (float): The annual renewal cost for the domain.
        years (int): The number of years to calculate the cost for.
    """

    def __init__(self, initial_service_fee, annual_renewal_cost, years):
        """
        Initializes the DomainCostCalculator.

        Args:
            initial_service_fee (float): The initial service fee for acquiring the domain.
            annual_renewal_cost (float): The annual renewal cost for the domain.
            years (int): The number of years to calculate the cost for.

        Raises:
            ValueError: If years is not a positive integer.
            TypeError: If initial_service_fee or annual_renewal_cost is not a number.
        """
        if not isinstance(initial_service_fee, (int, float)) or not isinstance(annual_renewal_cost, (int, float)):
            raise TypeError("Initial service fee and annual renewal cost must be numbers.")
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Years must be a positive integer.")

        self.initial_service_fee = initial_service_fee
        self.annual_renewal_cost = annual_renewal_cost
        self.years = years

    def calculate_total_cost(self):
        """
        Calculates the total cost of acquiring and maintaining the domain.

        Returns:
            float: The total cost.
        """
        # Calculate the total cost by adding the initial service fee and the renewal costs for the given years
        total_cost = self.initial_service_fee + (self.annual_renewal_cost * self.years)
        return total_cost


def main():
    try:
        # Define the costs for the domain curve.fr
        initial_service_fee = 20.0  # Initial service fee in euros
        annual_renewal_cost = 15.0  # Annual renewal cost in euros
        years = 5  # Number of years to calculate the cost for

        # Create a DomainCostCalculator instance
        calculator = DomainCostCalculator(initial_service_fee, annual_renewal_cost, years)

        # Calculate the total cost
        total_cost = calculator.calculate_total_cost()

        # Print the result
        print(f"The total cost of acquiring and maintaining the domain curve.fr for {years} years is: {total_cost} euros")

    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
