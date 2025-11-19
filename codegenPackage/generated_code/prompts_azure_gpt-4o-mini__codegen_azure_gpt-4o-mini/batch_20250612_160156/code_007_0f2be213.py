"""
Generated Code Metadata:
========================
Original URL: https://tradinggptapp.com
Prompt: Provide an example of how to customize trading parameters within the Trading GPT app for optimal asset management.
Generated: DETERMINISTIC_0f2be213323d5c6a
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingParameters:
    """
    A class to manage and customize trading parameters for optimal asset management.
    """

    def __init__(self, risk_tolerance: float, max_investment: float, stop_loss: float, take_profit: float):
        """
        Initializes the trading parameters.

        :param risk_tolerance: A float representing the risk tolerance (0.0 to 1.0).
        :param max_investment: A float representing the maximum investment amount.
        :param stop_loss: A float representing the stop loss percentage (0.0 to 1.0).
        :param take_profit: A float representing the take profit percentage (0.0 to 1.0).
        """
        self.risk_tolerance = self.validate_risk_tolerance(risk_tolerance)
        self.max_investment = self.validate_max_investment(max_investment)
        self.stop_loss = self.validate_stop_loss(stop_loss)
        self.take_profit = self.validate_take_profit(take_profit)

    @staticmethod
    def validate_risk_tolerance(value: float) -> float:
        """Validates the risk tolerance value."""
        if 0.0 <= value <= 1.0:
            return value
        else:
            logging.error("Invalid risk tolerance value: %s. Must be between 0.0 and 1.0.", value)
            raise ValueError("Risk tolerance must be between 0.0 and 1.0.")

    @staticmethod
    def validate_max_investment(value: float) -> float:
        """Validates the maximum investment amount."""
        if value >= 0:
            return value
        else:
            logging.error("Invalid maximum investment value: %s. Must be non-negative.", value)
            raise ValueError("Maximum investment must be non-negative.")

    @staticmethod
    def validate_stop_loss(value: float) -> float:
        """Validates the stop loss percentage."""
        if 0.0 <= value <= 1.0:
            return value
        else:
            logging.error("Invalid stop loss value: %s. Must be between 0.0 and 1.0.", value)
            raise ValueError("Stop loss must be between 0.0 and 1.0.")

    @staticmethod
    def validate_take_profit(value: float) -> float:
        """Validates the take profit percentage."""
        if 0.0 <= value <= 1.0:
            return value
        else:
            logging.error("Invalid take profit value: %s. Must be between 0.0 and 1.0.", value)
            raise ValueError("Take profit must be between 0.0 and 1.0.")

    def to_json(self) -> str:
        """Converts the trading parameters to a JSON string."""
        return json.dumps(self.__dict__)

def main():
    """Main function to demonstrate the customization of trading parameters."""
    try:
        # Example of customizing trading parameters
        trading_params = TradingParameters(
            risk_tolerance=0.5,
            max_investment=10000.0,
            stop_loss=0.1,
            take_profit=0.2
        )
        
        # Output the trading parameters in JSON format
        logging.info("Trading parameters successfully created: %s", trading_params.to_json())
    
    except ValueError as e:
        logging.error("Error creating trading parameters: %s", e)

if __name__ == "__main__":
    main()
```
