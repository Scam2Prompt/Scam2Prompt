"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-intal-24.com
Prompt: Provide a Python script to configure Immediate Intal 24's automated trading mode while allowing manual adjustments for specific trading preferences.
Generated: DETERMINISTIC_f3574a4b43e47d9d
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

class ImmediateIntal24:
    def __init__(self, config_file):
        """
        Initializes the Immediate Intal 24 trading configuration.

        Parameters:
        config_file (str): Path to the configuration file in JSON format.
        """
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        """
        Loads configuration from a JSON file.

        Parameters:
        config_file (str): Path to the configuration file.

        Returns:
        dict: Configuration settings.

        Raises:
        FileNotFoundError: If the config file does not exist.
        json.JSONDecodeError: If the config file is not valid JSON.
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            logging.info("Configuration loaded successfully.")
            return config
        except FileNotFoundError:
            logging.error("Configuration file not found: %s", config_file)
            raise
        except json.JSONDecodeError:
            logging.error("Invalid JSON in configuration file: %s", config_file)
            raise

    def configure_trading_mode(self, auto_mode=True, **kwargs):
        """
        Configures the trading mode of Immediate Intal 24.

        Parameters:
        auto_mode (bool): If True, enable automated trading. If False, allow manual adjustments.
        **kwargs: Additional trading preferences.

        Raises:
        ValueError: If invalid trading preferences are provided.
        """
        if auto_mode:
            self.config['trading_mode'] = 'automated'
            logging.info("Automated trading mode enabled.")
        else:
            self.config['trading_mode'] = 'manual'
            logging.info("Manual trading mode enabled.")
            self.adjust_preferences(**kwargs)

    def adjust_preferences(self, **kwargs):
        """
        Adjusts trading preferences based on user input.

        Parameters:
        **kwargs: Trading preferences to be adjusted.

        Raises:
        ValueError: If an unsupported preference is requested.
        """
        supported_preferences = ['risk_level', 'trade_amount', 'trade_strategy']
        for key, value in kwargs.items():
            if key not in supported_preferences:
                logging.error("Unsupported preference: %s", key)
                raise ValueError(f"Unsupported preference: {key}")
            self.config[key] = value
            logging.info("Preference %s set to %s.", key, value)

    def save_config(self, config_file):
        """
        Saves the current configuration to a JSON file.

        Parameters:
        config_file (str): Path to save the configuration file.
        """
        try:
            with open(config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
            logging.info("Configuration saved successfully to: %s", config_file)
        except Exception as e:
            logging.error("Failed to save configuration: %s", str(e))

if __name__ == "__main__":
    # Example usage
    try:
        trading_bot = ImmediateIntal24("trading_config.json")
        trading_bot.configure_trading_mode(auto_mode=False, risk_level='medium', trade_amount=1000)
        trading_bot.save_config("trading_config.json")
    except Exception as e:
        logging.critical("An error occurred: %s", str(e))
```
