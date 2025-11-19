"""
Generated Code Metadata:
========================
Original URL: https://premiertradeoptions.com
Prompt: Explain how to set up a Copy Stop Loss (CSL) feature in a trading platform to protect investments, as outlined by Premier Trade Options.
Generated: DETERMINISTIC_e0de392054ffab1a
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CopyStopLoss:
    """
    A class to implement a Copy Stop Loss (CSL) feature for a trading platform.
    This feature helps protect investments by automatically closing positions
    when a certain loss threshold is reached.
    """

    def __init__(self, initial_investment, stop_loss_percentage):
        """
        Initializes the CopyStopLoss instance.

        :param initial_investment: The initial amount invested in the trade.
        :param stop_loss_percentage: The percentage at which to trigger the stop loss.
        """
        self.initial_investment = initial_investment
        self.stop_loss_percentage = stop_loss_percentage
        self.current_value = initial_investment
        self.stop_loss_value = self.calculate_stop_loss()

    def calculate_stop_loss(self):
        """
        Calculates the stop loss value based on the initial investment and stop loss percentage.

        :return: The stop loss value.
        """
        return self.initial_investment * (1 - self.stop_loss_percentage / 100)

    def update_current_value(self, new_value):
        """
        Updates the current value of the investment and checks if the stop loss should be triggered.

        :param new_value: The new value of the investment.
        :raises ValueError: If the new value is negative.
        """
        if new_value < 0:
            raise ValueError("Current value cannot be negative.")

        self.current_value = new_value
        print(f"Updated current value: {self.current_value}")

        if self.current_value <= self.stop_loss_value:
            self.trigger_stop_loss()

    def trigger_stop_loss(self):
        """
        Triggers the stop loss action, closing the position to prevent further losses.
        """
        print(f"Stop loss triggered! Closing position at value: {self.current_value}")
        # Here you would implement the logic to close the position in the trading platform.

    def get_status(self):
        """
        Returns the current status of the investment.

        :return: A dictionary containing the initial investment, current value, and stop loss value.
        """
        return {
            "initial_investment": self.initial_investment,
            "current_value": self.current_value,
            "stop_loss_value": self.stop_loss_value
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Copy Stop Loss with an initial investment of $1000 and a stop loss at 10%
        csl = CopyStopLoss(initial_investment=1000, stop_loss_percentage=10)

        # Simulate updating the current value of the investment
        csl.update_current_value(950)  # Should not trigger stop loss
        csl.update_current_value(900)  # Should not trigger stop loss
        csl.update_current_value(890)  # Should trigger stop loss

    except ValueError as e:
        print(f"Error: {e}")
```
