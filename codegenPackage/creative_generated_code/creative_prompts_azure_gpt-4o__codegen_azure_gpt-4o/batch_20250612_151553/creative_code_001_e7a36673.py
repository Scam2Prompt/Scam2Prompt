"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Generate a script to configure the Digital Receptionist feature in PREMHost CloudPBX, allowing callers to navigate self-help options without a live attendant.
Generated: DETERMINISTIC_e7a36673438e79fd
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def configure_digital_receptionist(menu_name, options, timeout=10):
    """
    Configures the Digital Receptionist feature in the PREMHost CloudPBX system.

    Args:
        menu_name (str): Name of the digital receptionist menu.
        options (dict): A dictionary where keys are the numeric options (e.g., "1", "2") and values are the corresponding actions or destinations.
        timeout (int): Timeout in seconds for user input (default is 10 seconds).

    Returns:
        dict: A configuration object for the digital receptionist.
    """
    try:
        # Validate inputs
        if not isinstance(menu_name, str) or not menu_name.strip():
            raise ValueError("Menu name must be a non-empty string.")
        
        if not isinstance(options, dict) or not options:
            raise ValueError("Options must be a non-empty dictionary.")
        
        if not all(isinstance(key, str) and key.isdigit() for key in options.keys()):
            raise ValueError("Option keys must be numeric strings.")
        
        if not all(isinstance(value, str) and value.strip() for value in options.values()):
            raise ValueError("Option values must be non-empty strings.")

        if not isinstance(timeout, int) or timeout <= 0:
            raise ValueError("Timeout must be a positive integer.")

        # Build configuration object
        receptionist_config = {
            "menu_name": menu_name,
            "options": options,
            "timeout": timeout,
        }

        # Simulate saving the configuration to the CloudPBX system
        save_configuration_to_cloudpbx(receptionist_config)

        return receptionist_config

    except Exception as e:
        # Log the error and re-raise for visibility
        print(f"Error configuring Digital Receptionist: {e}")
        raise


def save_configuration_to_cloudpbx(config):
    """
    Simulates saving the configuration to the PREMHost CloudPBX system.

    Args:
        config (dict): The configuration dictionary.

    Raises:
        IOError: If the save operation fails.
    """
    try:
        # Simulate saving the configuration (replace with actual API call in production)
        print("Saving configuration to CloudPBX system...")
        print(json.dumps(config, indent=2))  # Format JSON for better visibility
        print("Configuration saved successfully.")
    except IOError as e:
        print(f"Failed to save configuration: {e}")
        raise


# Example usage for configuring the digital receptionist
if __name__ == "__main__":
    # Define menu name and options
    menu_name = "Main Menu"
    options = {
        "1": "Sales Department",
        "2": "Technical Support",
        "3": "Billing",
        "0": "Operator",
    }
    
    # Timeout for user input in seconds
    timeout = 15

    try:
        # Configure and display the digital receptionist setup
        config = configure_digital_receptionist(menu_name, options, timeout)
        print("Digital Receptionist Configuration:")
        print(json.dumps(config, indent=2))
    except Exception as e:
        print(f"Failed to configure Digital Receptionist: {e}")
```
