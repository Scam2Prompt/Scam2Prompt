"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Generate a Python script to create a maintenance notification system for a website, similar to the one described on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_ebbbbba2b00bc000
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

# Configuration file path
CONFIG_FILE = "maintenance_config.json"

def load_config(file_path):
    """
    Load the maintenance configuration from a JSON file.
    :param file_path: Path to the configuration file.
    :return: Dictionary containing configuration data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON configuration: {e}")

def is_maintenance_period(config):
    """
    Check if the current time falls within the maintenance period.
    :param config: Dictionary containing maintenance configuration.
    :return: Boolean indicating whether the site is under maintenance.
    """
    try:
        start_time = datetime.datetime.strptime(config["start_time"], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(config["end_time"], "%Y-%m-%d %H:%M:%S")
        current_time = datetime.datetime.now()
        return start_time <= current_time <= end_time
    except KeyError as e:
        raise KeyError(f"Missing required configuration key: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid date format in configuration: {e}")

def display_notification():
    """
    Display the maintenance notification message.
    """
    print("========================================")
    print("🚧 The website is currently under maintenance. 🚧")
    print("We apologize for the inconvenience and appreciate your patience.")
    print("========================================")

def main():
    """
    Main function to run the maintenance notification system.
    """
    try:
        # Load configuration
        config = load_config(CONFIG_FILE)
        
        # Check if the site is under maintenance
        if is_maintenance_period(config):
            display_notification()
        else:
            print("✅ The website is operational. No maintenance at the moment.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Example `maintenance_config.json` file:
```json
{
    "start_time": "2023-10-01 22:00:00",
    "end_time": "2023-10-02 06:00:00"
}
```
