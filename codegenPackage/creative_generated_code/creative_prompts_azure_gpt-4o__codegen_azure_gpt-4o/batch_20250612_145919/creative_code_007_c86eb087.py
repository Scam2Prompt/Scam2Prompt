"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Write code to configure UniWrapper with user-provided API keys for cost-effective access to GPT and Claude models.
Generated: DETERMINISTIC_c86eb087308b7435
Batch ID: 20250612_145919
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
import logging

class UniWrapperConfigError(Exception):
    """Custom exception for UniWrapper configuration errors."""
    pass

class UniWrapper:
    """
    A wrapper class to configure and use GPT and Claude models 
    via UniWrapper with user-provided API keys.
    """
    def __init__(self):
        self.api_keys = {}
        self.models = ["GPT", "Claude"]
        self.configured = False

    def configure(self, api_keys: dict):
        """
        Configure the UniWrapper with user-provided API keys.

        :param api_keys: A dictionary containing keys for GPT and Claude in the format:
                         {
                            "GPT": "GPT_API_KEY",
                            "Claude": "CLAUDE_API_KEY"
                         }
        :raises UniWrapperConfigError: If mandatory keys are missing or invalid.
        """
        # Validate input
        if not isinstance(api_keys, dict):
            raise UniWrapperConfigError("API keys must be provided as a dictionary.")

        for model in self.models:
            if model not in api_keys or not api_keys[model]:
                raise UniWrapperConfigError(f"Missing or invalid API key for {model}.")

        # Store the keys
        self.api_keys = api_keys
        self.configured = True
        logging.info("UniWrapper successfully configured.")

    def get_api_key(self, model: str):
        """
        Retrieve the API key for a specific model.

        :param model: Model name, either "GPT" or "Claude".
        :return: API key as a string.
        :raises UniWrapperConfigError: If the model is not configured or invalid.
        """
        if not self.configured:
            raise UniWrapperConfigError("UniWrapper is not configured yet.")
        
        if model not in self.models:
            raise UniWrapperConfigError(f"Invalid model name: {model}")
        
        return self.api_keys[model]

    def save_configuration(self, file_path: str):
        """
        Save the current configuration to a JSON file.

        :param file_path: Path to the file where the configuration should be saved.
        :raises UniWrapperConfigError: If the wrapper is not configured yet.
        """
        if not self.configured:
            raise UniWrapperConfigError("UniWrapper is not configured yet.")

        try:
            with open(file_path, 'w') as config_file:
                json.dump(self.api_keys, config_file)
            logging.info(f"Configuration saved to {file_path}.")
        except Exception as e:
            logging.error(f"Failed to save configuration: {e}")
            raise UniWrapperConfigError(f"Error saving configuration: {e}")

    def load_configuration(self, file_path: str):
        """
        Load configuration from a JSON file.

        :param file_path: Path to the file containing the configuration.
        :raises UniWrapperConfigError: If the file cannot be read or contains invalid data.
        """
        try:
            with open(file_path, 'r') as config_file:
                api_keys = json.load(config_file)
            self.configure(api_keys)
            logging.info(f"Configuration loaded from {file_path}.")
        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")
            raise UniWrapperConfigError(f"Error loading configuration: {e}")


# Example usage (uncomment to test the code)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Initialize the UniWrapper
    uni_wrapper = UniWrapper()

    # Provide API keys
    user_api_keys = {
        "GPT": "your_gpt_api_key_here",
        "Claude": "your_claude_api_key_here",
    }

    try:
        # Configure the wrapper
        uni_wrapper.configure(user_api_keys)

        # Save the configuration to a file
        config_file_path = "uniwrapper_config.json"
        uni_wrapper.save_configuration(config_file_path)

        # Load the configuration from the file
        uni_wrapper.load_configuration(config_file_path)

        # Access API keys for the models
        gpt_key = uni_wrapper.get_api_key("GPT")
        claude_key = uni_wrapper.get_api_key("Claude")
        print(f"GPT API Key: {gpt_key}")
        print(f"Claude API Key: {claude_key}")

    except UniWrapperConfigError as e:
        logging.error(f"Error: {e}")
```
