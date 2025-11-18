"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astertex.com
Prompt: Create a script to toggle between Simple Mode and Pro Mode in Aster's trading interface, ensuring seamless user experience for both beginners and advanced traders.
Generated: DETERMINISTIC_8ffdfe7aa197713c
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# toggle_mode.py

# Import necessary modules
import json

# Path to the configuration file where the current mode is stored
CONFIG_FILE_PATH = "trading_interface_config.json"

def load_config(file_path):
    """
    Load the configuration from the specified file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Configuration data as a dictionary.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        json.JSONDecodeError: If the configuration file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {file_path}.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode configuration file: {e}")

def save_config(file_path, config_data):
    """
    Save the configuration to the specified file.

    Args:
        file_path (str): Path to the configuration file.
        config_data (dict): Configuration data to save.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(config_data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Failed to save configuration file: {e}")

def toggle_mode(file_path):
    """
    Toggle between 'Simple Mode' and 'Pro Mode' in the trading interface.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        str: The new mode after toggling.
    """
    try:
        config = load_config(file_path)
        current_mode = config.get("mode", "Simple")  # Default to 'Simple' if not present

        # Determine the new mode
        new_mode = "Pro" if current_mode == "Simple" else "Simple"

        # Update the configuration
        config["mode"] = new_mode
        save_config(file_path, config)

        return new_mode
    except Exception as e:
        print(f"An error occurred while toggling the mode: {e}")
        return None

def main():
    """
    Main function to toggle the mode and provide user feedback.
    """
    print("Toggling trading interface mode...")
    new_mode = toggle_mode(CONFIG_FILE_PATH)
    if new_mode:
        print(f"Successfully switched to {new_mode} Mode.")
    else:
        print("Failed to toggle mode. Please try again later.")

if __name__ == "__main__":
    main()
```
