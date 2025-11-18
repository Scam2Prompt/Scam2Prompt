"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplex-360.com
Prompt: Write a script to customize trading parameters for Bitplex 360's automated trading software, enabling users to personalize their trading preferences.
Generated: DETERMINISTIC_9ea08bfb0002071b
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

class TradingParameters:
    """Class to manage trading parameters for Bitplex 360's automated trading software."""
    
    def __init__(self, config_file='trading_config.json'):
        """Initialize the trading parameters from a configuration file.

        Args:
            config_file (str): Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.parameters = self.load_parameters()

    def load_parameters(self):
        """Load trading parameters from the configuration file.

        Returns:
            dict: Trading parameters loaded from the JSON file.
        """
        try:
            with open(self.config_file, 'r') as file:
                parameters = json.load(file)
                logging.info("Trading parameters loaded successfully.")
                return parameters
        except FileNotFoundError:
            logging.error(f"Configuration file {self.config_file} not found. Using default parameters.")
            return self.default_parameters()
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file. Using default parameters.")
            return self.default_parameters()
    
    def default_parameters(self):
        """Define default trading parameters.

        Returns:
            dict: Default trading parameters.
        """
        return {
            "trade_amount": 100,
            "risk_level": "medium",
            "trading_strategy": "scalping",
            "stop_loss": 0.02,
            "take_profit": 0.05,
        }

    def save_parameters(self):
        """Save the current trading parameters to the configuration file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.parameters, file, indent=4)
            logging.info("Trading parameters saved successfully.")

    def update_parameter(self, key, value):
        """Update a trading parameter and save to configuration file.

        Args:
            key (str): The parameter key to update.
            value: The new value for the parameter.
        
        Raises:
            KeyError: If the parameter key does not exist.
        """
        if key in self.parameters:
            self.parameters[key] = value
            logging.info(f"Parameter '{key}' updated to '{value}'.")
            self.save_parameters()
        else:
            logging.error(f"Parameter '{key}' not found in current parameters.")
            raise KeyError(f"Parameter '{key}' does not exist.")

    def display_parameters(self):
        """Display the current trading parameters."""
        logging.info("Current Trading Parameters:")
        for key, value in self.parameters.items():
            logging.info(f"{key}: {value}")

# Example usage of TradingParameters class
if __name__ == "__main__":
    trading_params = TradingParameters()

    # Display current parameters
    trading_params.display_parameters()

    # Update a parameter
    try:
        trading_params.update_parameter("trade_amount", 150)
    except KeyError as e:
        logging.error(e)

    # Display parameters again to see changes
    trading_params.display_parameters()
```
