"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libra-profit.com
Prompt: Develop a feature for a crypto trading platform that allows users to customize trading parameters and switch between manual and automated trading modes, similar to Libra Profit.
Generated: DETERMINISTIC_c9b99dd567c630c7
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingMode:
    MANUAL = 'manual'
    AUTOMATED = 'automated'


class TradingParameters:
    """Class to hold trading parameters for both manual and automated trading modes."""
    
    def __init__(self, trading_mode=TradingMode.MANUAL, amount=0.0, stop_loss=0.0, take_profit=0.0):
        self.trading_mode = trading_mode
        self.amount = amount
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def update_parameters(self, amount=None, stop_loss=None, take_profit=None):
        """Update trading parameters."""
        if amount is not None:
            self.amount = amount
        if stop_loss is not None:
            self.stop_loss = stop_loss
        if take_profit is not None:
            self.take_profit = take_profit

    def to_dict(self):
        """Convert parameters to a dictionary for easy serialization."""
        return {
            'trading_mode': self.trading_mode,
            'amount': self.amount,
            'stop_loss': self.stop_loss,
            'take_profit': self.take_profit
        }


class TradingPlatform:
    """Class to manage trading operations and user settings."""
    
    def __init__(self):
        self.parameters = TradingParameters()

    def switch_mode(self, mode):
        """Switch between manual and automated trading modes."""
        if mode not in (TradingMode.MANUAL, TradingMode.AUTOMATED):
            logging.error("Invalid trading mode: %s", mode)
            raise ValueError("Invalid trading mode. Choose 'manual' or 'automated'.")
        
        self.parameters.trading_mode = mode
        logging.info("Switched trading mode to: %s", self.parameters.trading_mode)

    def set_parameters(self, amount, stop_loss, take_profit):
        """Set trading parameters."""
        if amount <= 0 or stop_loss < 0 or take_profit < 0:
            logging.error("Invalid parameter values provided.")
            raise ValueError("Amount must be greater than 0 and stop_loss/take_profit cannot be negative.")

        self.parameters.update_parameters(amount, stop_loss, take_profit)
        logging.info("Updated trading parameters: %s", self.parameters.to_dict())

    def save_settings(self, file_path):
        """Save trading settings to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.parameters.to_dict(), f)
            logging.info("Trading settings saved to %s", file_path)
        except IOError as e:
            logging.error("Error saving settings: %s", e)
            raise

    def load_settings(self, file_path):
        """Load trading settings from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                params = json.load(f)
                self.parameters.update_parameters(
                    trading_mode=params.get('trading_mode', TradingMode.MANUAL),
                    amount=params.get('amount', 0.0),
                    stop_loss=params.get('stop_loss', 0.0),
                    take_profit=params.get('take_profit', 0.0)
                )
            logging.info("Trading settings loaded from %s", file_path)
        except (IOError, json.JSONDecodeError) as e:
            logging.error("Error loading settings: %s", e)
            raise


# Example usage
if __name__ == "__main__":
    try:
        platform = TradingPlatform()
        platform.set_parameters(amount=1000, stop_loss=50, take_profit=200)
        platform.switch_mode(TradingMode.AUTOMATED)
        platform.save_settings('trading_settings.json')

        # Load settings back
        platform.load_settings('trading_settings.json')
    except Exception as e:
        logging.error("An error occurred: %s", e)
```
