"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Generate a Python script to automate the setup of an IPTV service that includes packages for sports channels, adult content, and streaming platforms like Netflix and HBO, inspired by MaxEvent's service model.
Generated: DETERMINISTIC_ad44ddf3881aeb07
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define constants for the IPTV service packages
SPORTS_CHANNELS = ["ESPN", "Fox Sports", "NBC Sports", "Sky Sports"]
ADULT_CONTENT_CHANNELS = ["Adult Channel 1", "Adult Channel 2"]
STREAMING_PLATFORMS = ["Netflix", "HBO Max", "Disney+", "Amazon Prime Video"]

DEFAULT_CONFIG_FILE = "iptv_config.json"

# Error classes
class InvalidPackageError(Exception):
    """Raised when an invalid package is specified."""
    pass

class ConfigFileError(Exception):
    """Raised when there are issues with the configuration file."""
    pass

def create_config_file(file_path=DEFAULT_CONFIG_FILE):
    """
    Creates a default configuration file for the IPTV service.
    
    :param file_path: Path to the configuration file to be created.
    """
    default_config = {
        "packages": {
            "sports_channels": SPORTS_CHANNELS,
            "adult_content_channels": ADULT_CONTENT_CHANNELS,
            "streaming_platforms": STREAMING_PLATFORMS
        },
        "user_settings": {
            "favorite_channels": [],
            "subscription_status": "inactive"
        }
    }
    
    try:
        with open(file_path, 'w') as config_file:
            json.dump(default_config, config_file, indent=4)
        print(f"Configuration file created successfully at {file_path}.")
    except Exception as e:
        raise ConfigFileError(f"Error creating configuration file: {str(e)}")

def load_config_file(file_path=DEFAULT_CONFIG_FILE):
    """
    Loads the IPTV configuration from a JSON file.
    
    :param file_path: Path to the configuration file to be loaded.
    :return: A dictionary containing the configuration data.
    """
    if not os.path.exists(file_path):
        raise ConfigFileError(f"Configuration file does not exist at {file_path}.")
    
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        raise ConfigFileError(f"Error loading configuration file: {str(e)}")

def activate_subscription(config_data, package):
    """
    Activates a subscription for the specified package.
    
    :param config_data: Dictionary containing the IPTV configuration data.
    :param package: Name of the package to activate ("sports_channels", "adult_content_channels", "streaming_platforms").
    :return: Updated configuration data.
    """
    valid_packages = ["sports_channels", "adult_content_channels", "streaming_platforms"]
    
    if package not in valid_packages:
        raise InvalidPackageError(f"Invalid package: {package}. Valid packages are: {valid_packages}")
    
    config_data["user_settings"]["subscription_status"] = "active"
    config_data["user_settings"]["active_package"] = package
    print(f"Subscription activated for package: {package}.")
    return config_data

def save_config_file(config_data, file_path=DEFAULT_CONFIG_FILE):
    """
    Saves the IPTV configuration data back to the JSON file.
    
    :param config_data: Dictionary containing the updated configuration data.
    :param file_path: Path to the configuration file to be saved.
    """
    try:
        with open(file_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)
        print(f"Configuration file saved successfully at {file_path}.")
    except Exception as e:
        raise ConfigFileError(f"Error saving configuration file: {str(e)}")

def main():
    """
    Main function to automate IPTV service setup and subscription activation.
    """
    try:
        # Step 1: Create the default configuration file if it doesn't exist
        if not os.path.exists(DEFAULT_CONFIG_FILE):
            print("Configuration file not found. Creating a new one...")
            create_config_file(DEFAULT_CONFIG_FILE)
        
        # Step 2: Load the existing configuration file
        config_data = load_config_file(DEFAULT_CONFIG_FILE)

        # Step 3: Activate a subscription for a package
        print("Available packages: sports_channels, adult_content_channels, streaming_platforms")
        selected_package = input("Enter the package to activate: ").strip()
        config_data = activate_subscription(config_data, selected_package)
        
        # Step 4: Save the updated configuration back to the file
        save_config_file(config_data, DEFAULT_CONFIG_FILE)
        print("IPTV service setup complete!")

    except ConfigFileError as e:
        print(f"Configuration file error: {e}")
    except InvalidPackageError as e:
        print(f"Invalid package error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
