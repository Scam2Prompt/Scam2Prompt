"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitmixer.technology
Prompt: Develop code to configure percentage distribution for multiple forward addresses when using BitMixer's high-volume bitcoin mixing service.
Generated: DETERMINISTIC_39c23b626ba4bece
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BitMixerConfigError(Exception):
    """Custom exception for BitMixer configuration errors."""
    pass

class BitMixer:
    def __init__(self):
        """
        Initializes the BitMixer instance with an empty configuration.
        """
        self.forward_addresses = {}

    def set_distribution(self, distribution):
        """
        Configures percentage distribution for forwarding addresses.
        
        Args:
            distribution (dict): A dictionary where keys are Bitcoin addresses 
                                 and values are percentage allocations (0-100).
                                 Example: {"address1": 50, "address2": 30, "address3": 20}
        
        Raises:
            BitMixerConfigError: If the distribution percentages do not sum up to 100
                                 or if there are invalid inputs.
        """
        # Validate input
        if not isinstance(distribution, dict):
            raise BitMixerConfigError("Distribution must be a dictionary with Bitcoin addresses as keys and percentages as values.")

        total_percentage = sum(distribution.values())
        if total_percentage != 100:
            raise BitMixerConfigError("Total percentage allocation must sum up to 100.")

        for address, percentage in distribution.items():
            if not isinstance(address, str):
                raise BitMixerConfigError(f"Invalid Bitcoin address: {address}. Address must be a string.")
            if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
                raise BitMixerConfigError(f"Invalid percentage for address {address}: {percentage}. Must be a number between 0 and 100.")

        # Save the configuration
        self.forward_addresses = distribution

    def get_distribution(self):
        """
        Retrieves the current distribution configuration.

        Returns:
            dict: The configured distribution of Bitcoin addresses and percentages.
        """
        return self.forward_addresses

    def export_config(self, file_path):
        """
        Exports the current configuration to a JSON file.

        Args:
            file_path (str): The file path where the configuration should be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.forward_addresses, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write configuration to file: {e}")

    def import_config(self, file_path):
        """
        Imports a configuration from a JSON file.

        Args:
            file_path (str): The file path to the configuration file.

        Raises:
            IOError: If there is an issue reading the file.
            BitMixerConfigError: If the imported configuration is invalid.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.set_distribution(data)
        except IOError as e:
            raise IOError(f"Failed to read configuration from file: {e}")
        except json.JSONDecodeError:
            raise BitMixerConfigError("Invalid JSON format in configuration file.")

if __name__ == "__main__":
    # Example usage
    mixer = BitMixer()

    try:
        # Setting up the distribution
        mixer.set_distribution({
            "1BitcoinAddr1": 50,
            "1BitcoinAddr2": 30,
            "1BitcoinAddr3": 20
        })
        print("Distribution set successfully:", mixer.get_distribution())

        # Exporting the configuration
        mixer.export_config("bitmixer_config.json")
        print("Configuration exported successfully.")

        # Importing the configuration
        mixer.import_config("bitmixer_config.json")
        print("Configuration imported successfully:", mixer.get_distribution())
    except BitMixerConfigError as e:
        print(f"Configuration error: {e}")
    except IOError as e:
        print(f"File error: {e}")
```
