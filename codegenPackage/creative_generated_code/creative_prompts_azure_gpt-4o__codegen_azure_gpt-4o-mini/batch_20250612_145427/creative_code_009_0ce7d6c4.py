"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: Generate a configuration for AppKit using Ethers as the driving library, excluding both email and social authentication options.
Generated: DETERMINISTIC_0ce7d6c4fe2bf2bb
Batch ID: 20250612_145427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json

class AppKitConfig:
    """
    Class to generate a configuration for AppKit using Ethers library.
    This configuration excludes both email and social authentication options.
    """

    def __init__(self, app_name, ethers_provider_url):
        """
        Initializes the configuration with the application name and
        Ethers provider URL.

        Parameters:
        - app_name (str): The name of the application.
        - ethers_provider_url (str): The URL of the Ethers provider (e.g., Infura, Alchemy).
        """
        self.app_name = app_name
        self.ethers_provider_url = ethers_provider_url
        self.config = {
            "app_name": self.app_name,
            "authentication": {
                "email": False,
                "social": False
            },
            "ethers": {
                "provider": self.ethers_provider_url
            }
        }

    def save_config(self, file_path):
        """
        Saves the configuration to a JSON file.

        Parameters:
        - file_path (str): The path to the file where the configuration will be saved.

        Raises:
        - IOError: If an I/O error occurs during file operation.
        """
        try:
            with open(file_path, 'w') as config_file:
                json.dump(self.config, config_file, indent=4)
            print(f"Configuration saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def get_config(self):
        """
        Returns the current configuration as a dictionary.

        Returns:
        - dict: The current configuration.
        """
        return self.config


# Example usage
if __name__ == "__main__":
    # Define your application name and Ethers provider URL
    app_name = "MyDApp"
    ethers_provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

    # Create AppKit configuration instance
    app_config = AppKitConfig(app_name, ethers_provider_url)

    # Get the configuration dictionary
    config = app_config.get_config()
    print("Current Configuration:", config)

    # Save the configuration to a file
    app_config.save_config("app_config.json")
```
