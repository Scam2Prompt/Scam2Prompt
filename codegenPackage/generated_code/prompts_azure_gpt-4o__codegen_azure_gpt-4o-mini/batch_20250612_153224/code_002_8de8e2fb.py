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
class PropertyLossCalculator:
    """
    A class to calculate the reduction in property loss when fire sprinklers are installed.
    """

    def __init__(self, average_loss_without_sprinklers, average_loss_with_sprinklers):
        """
        Initializes the PropertyLossCalculator with average loss values.

        :param average_loss_without_sprinklers: Average property loss without sprinklers (float)
        :param average_loss_with_sprinklers: Average property loss with sprinklers (float)
        """
        if average_loss_without_sprinklers < 0 or average_loss_with_sprinklers < 0:
            raise ValueError("Average loss values must be non-negative.")

        self.average_loss_without_sprinklers = average_loss_without_sprinklers
        self.average_loss_with_sprinklers = average_loss_with_sprinklers

    def calculate_reduction(self):
        """
        Calculates the reduction in property loss due to the installation of fire sprinklers.

        :return: Reduction in property loss (float)
        """
        reduction = self.average_loss_without_sprinklers - self.average_loss_with_sprinklers
        if reduction < 0:
            raise ValueError("Loss with sprinklers cannot exceed loss without sprinklers.")
        return reduction

    def calculate_percentage_reduction(self):
        """
        Calculates the percentage reduction in property loss.

        :return: Percentage reduction (float)
        """
        if self.average_loss_without_sprinklers == 0:
            raise ValueError("Average loss without sprinklers cannot be zero for percentage calculation.")
        
        reduction = self.calculate_reduction()
        percentage_reduction = (reduction / self.average_loss_without_sprinklers) * 100
        return percentage_reduction


def main():
    """
    Main function to execute the property loss calculation.
    """
    try:
        # Example values for average loss without and with sprinklers
        average_loss_without_sprinklers = 100000.0  # Example: $100,000
        average_loss_with_sprinklers = 30000.0       # Example: $30,000

        # Create an instance of PropertyLossCalculator
        calculator = PropertyLossCalculator(average_loss_without_sprinklers, average_loss_with_sprinklers)

        # Calculate reduction and percentage reduction
        reduction = calculator.calculate_reduction()
        percentage_reduction = calculator.calculate_percentage_reduction()

        # Output results
        print(f"Reduction in property loss: ${reduction:.2f}")
        print(f"Percentage reduction in property loss: {percentage_reduction:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
