"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code to calculate the reduction in property loss when fire sprinklers are installed, using the statistics provided by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_8de8e2fbb4f0918f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_sprinkler_calculator.py

class FireSprinklerCalculator:
    """
    Calculates the reduction in property loss when fire sprinklers are installed.
    """

    def __init__(self, 
                 average_property_loss_without_sprinklers: float, 
                 average_property_loss_with_sprinklers: float, 
                 total_number_of_fires: int):
        """
        Initializes the calculator with the provided statistics.

        Args:
        - average_property_loss_without_sprinklers (float): 
            The average property loss without fire sprinklers.
        - average_property_loss_with_sprinklers (float): 
            The average property loss with fire sprinklers.
        - total_number_of_fires (int): The total number of fires.
        """
        self.average_property_loss_without_sprinklers = average_property_loss_without_sprinklers
        self.average_property_loss_with_sprinklers = average_property_loss_with_sprinklers
        self.total_number_of_fires = total_number_of_fires

    def calculate_reduction_in_property_loss(self) -> float:
        """
        Calculates the reduction in property loss when fire sprinklers are installed.

        Returns:
        - float: The reduction in property loss as a percentage.
        """
        if self.total_number_of_fires <= 0:
            raise ValueError("Total number of fires must be greater than zero.")

        if self.average_property_loss_without_sprinklers < 0 or self.average_property_loss_with_sprinklers < 0:
            raise ValueError("Average property losses cannot be negative.")

        loss_reduction = (self.average_property_loss_without_sprinklers - self.average_property_loss_with_sprinklers) / \
                         self.average_property_loss_without_sprinklers

        return max(0, min(loss_reduction, 1)) * 100

    def calculate_total_property_loss_without_sprinklers(self) -> float:
        """
        Calculates the total property loss without fire sprinklers.

        Returns:
        - float: The total property loss without fire sprinklers.
        """
        return self.average_property_loss_without_sprinklers * self.total_number_of_fires

    def calculate_total_property_loss_with_sprinklers(self) -> float:
        """
        Calculates the total property loss with fire sprinklers.

        Returns:
        - float: The total property loss with fire sprinklers.
        """
        return self.average_property_loss_with_sprinklers * self.total_number_of_fires


def main():
    try:
        # Statistics provided by Independence Fire Sprinkler Company
        avg_loss_without_sprinklers = 75000  # Average property loss without sprinklers
        avg_loss_with_sprinklers = 15000    # Average property loss with sprinklers
        total_fires = 100                    # Total number of fires

        calculator = FireSprinklerCalculator(avg_loss_without_sprinklers, 
                                              avg_loss_with_sprinklers, 
                                              total_fires)

        reduction_in_loss = calculator.calculate_reduction_in_property_loss()
        total_loss_without_sprinklers = calculator.calculate_total_property_loss_without_sprinklers()
        total_loss_with_sprinklers = calculator.calculate_total_property_loss_with_sprinklers()

        print(f"Reduction in property loss: {reduction_in_loss:.2f}%")
        print(f"Total property loss without sprinklers: ${total_loss_without_sprinklers:,.2f}")
        print(f"Total property loss with sprinklers: ${total_loss_with_sprinklers:,.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
