"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: Explain how to set up a Copy Stop Loss (CSL) feature in a trading platform to protect investments, as outlined by Premier Trade Options.
Generated: DETERMINISTIC_e0de392054ffab1a
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CopyStopLoss:
    """
    Class to manage Copy Stop Loss (CSL) functionality for a trading platform.
    
    Attributes:
        investments (dict): A dictionary to store investment details.
        stop_loss_percentage (float): The percentage decrease to trigger the stop loss.
    """

    def __init__(self, stop_loss_percentage: float):
        """
        Initializes the CopyStopLoss with the specified stop loss percentage.
        
        Args:
            stop_loss_percentage (float): The percentage decrease to trigger stop loss.
        
        Raises:
            ValueError: If stop_loss_percentage is not between 0 and 100.
        """
        if not (0 <= stop_loss_percentage <= 100):
            raise ValueError("Stop loss percentage must be between 0 and 100.")
        
        self.investments = {}
        self.stop_loss_percentage = stop_loss_percentage / 100

    def add_investment(self, investment_id: str, current_value: float):
        """
        Adds a new investment to the CSL manager.
        
        Args:
            investment_id (str): Unique identifier for the investment.
            current_value (float): Current market value of the investment.
        
        Raises:
            ValueError: If current_value is negative.
        """
        if current_value < 0:
            raise ValueError("Current value cannot be negative.")
        
        self.investments[investment_id] = current_value

    def check_stop_loss(self, investment_id: str, new_value: float) -> bool:
        """
        Checks whether the stop loss condition is met for the given investment.
        
        Args:
            investment_id (str): Unique identifier for the investment.
            new_value (float): The new market value of the investment.
        
        Returns:
            bool: True if the stop loss condition is met, False otherwise.
        
        Raises:
            KeyError: If the investment_id does not exist.
        """
        if investment_id not in self.investments:
            raise KeyError(f"Investment ID {investment_id} not found.")
        
        initial_value = self.investments[investment_id]
        loss_threshold = initial_value * (1 - self.stop_loss_percentage)

        return new_value < loss_threshold

    def trigger_stop_loss(self, investment_id: str):
        """
        Handles the stop loss trigger for the specified investment.
        
        Args:
            investment_id (str): Unique identifier for the investment.
        
        Raises:
            KeyError: If the investment_id does not exist.
        """
        if investment_id not in self.investments:
            raise KeyError(f"Investment ID {investment_id} not found.")
        
        # Remove investment from active investments
        del self.investments[investment_id]
        print(f"Stop loss triggered for investment {investment_id}. Investment has been sold.")

# Example usage:
if __name__ == "__main__":
    try:
        csl_manager = CopyStopLoss(stop_loss_percentage=10.0)
        csl_manager.add_investment('INV001', current_value=100.0)

        # Simulating a market change
        new_market_value = 85.0  # New market value after a decline
        if csl_manager.check_stop_loss('INV001', new_market_value):
            csl_manager.trigger_stop_loss('INV001')

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
