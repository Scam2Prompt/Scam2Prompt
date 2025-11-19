"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoin.rf.gd
Prompt: Create a configuration file for a web application hosted on iFastNet that takes advantage of unlimited disk space and SSL support.
Generated: DETERMINISTIC_a82f9970707c6e40
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

class Config:
    """Configuration class for the web application hosted on iFastNet."""
    
    def __init__(self, config_file='config.json'):
        """Initialize the configuration class.

        Args:
            config_file (str): The path to the configuration file.
        """
        self.config_file = config_file
        self.config_data = {}
        self.load_config()

    def load_config(self):
        """Load configuration from the JSON file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as file:
                    self.config_data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                raise
            except Exception as e:
                print(f"An error occurred while loading config: {e}")
                raise
        else:
            print(f"Config file not found: {self.config_file}")
            raise FileNotFoundError(f"Config file '{self.config_file}' does not exist.")

    def get(self, key, default=None):
        """Get a configuration value.

        Args:
            key (str): The key of the configuration value.
            default: The default value to return if the key does not exist.

        Returns:
            The configuration value or the default value.
        """
        return self.config_data.get(key, default)

    def set(self, key, value):
        """Set a configuration value.

        Args:
            key (str): The key of the configuration value.
            value: The value to set for the configuration key.
        """
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """Save the current configuration back to the JSON file."""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving config: {e}")
            raise


# Example usage of the Config class
if __name__ == "__main__":
    try:
        config = Config()

        # Setting configuration values
        config.set('app_name', 'MyWebApp')
        config.set('db_host', 'localhost')
        config.set('db_user', 'root')
        config.set('db_password', 'password')
        config.set('use_ssl', True)

        # Accessing configuration values
        print(f"App Name: {config.get('app_name')}")
        print(f"Use SSL: {config.get('use_ssl')}")
        
    except Exception as e:
        print(f"Configuration error: {e}")
```

```json
{
    "app_name": "MyWebApp",
    "db_host": "localhost",
    "db_user": "root",
    "db_password": "password",
    "use_ssl": true
}
```

This code creates a `Config` class to manage the configuration of a web application, utilizing a JSON file for storage. The example usage demonstrates how to set and get configuration values.
