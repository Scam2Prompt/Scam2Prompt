"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Generate code to calculate the reduction in property loss when fire sprinklers are installed, using the statistics provided by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_8de8e2fbb4f0918f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireSprinklerReductionCalculator:
    """
    A class to calculate the reduction in property loss when fire sprinklers are installed.
    """

    def __init__(self, average_loss_no_sprinklers: float, average_loss_with_sprinklers: float):
        """
        Initializes the calculator with average losses.

        :param average_loss_no_sprinklers: The average property loss without fire sprinklers.
        :param average_loss_with_sprinklers: The average property loss with fire sprinklers.
        """
        if average_loss_no_sprinklers < 0 or average_loss_with_sprinklers < 0:
            raise ValueError("Average loss values must be non-negative.")

        self.average_loss_no_sprinklers = average_loss_no_sprinklers
        self.average_loss_with_sprinklers = average_loss_with_sprinklers

    def calculate_reduction(self) -> float:
        """
        Calculates the reduction in property loss due to fire sprinklers.

        :return: The percentage reduction in property loss.
        """
        if self.average_loss_no_sprinklers == 0:
            raise ValueError("Average loss without sprinklers cannot be zero to calculate reduction.")

        reduction = (
            (self.average_loss_no_sprinklers - self.average_loss_with_sprinklers) /
            self.average_loss_no_sprinklers
        ) * 100

        return reduction

    def get_reduction_summary(self) -> str:
        """
        Provides a summary of the reduction in property loss.

        :return: A formatted string summarizing the reduction.
        """
        try:
            reduction = self.calculate_reduction()
            return (f"With fire sprinklers installed, property loss is reduced by "
                    f"{reduction:.2f}% compared to properties without sprinklers.")
        except ValueError as e:
            return f"Error: {str(e)}"


# Example Usage
if __name__ == "__main__":
    try:
        # Example averages (these values should be replaced with actual statistics)
        average_loss_no_sprinklers = 50000  # Average loss without sprinklers
        average_loss_with_sprinklers = 10000  # Average loss with sprinklers

        calculator = FireSprinklerReductionCalculator(average_loss_no_sprinklers, average_loss_with_sprinklers)
        summary = calculator.get_reduction_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
