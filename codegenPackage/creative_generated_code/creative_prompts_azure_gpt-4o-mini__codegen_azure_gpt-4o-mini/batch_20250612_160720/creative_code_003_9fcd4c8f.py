"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: Explain how to safely change the fan profile and temperature thresholds in NiBiTor for NVIDIA GPUs.
Generated: DETERMINISTIC_9fcd4c8fb121b12e
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging
import sys
import json

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for the NiBiTor executable and configuration file
NIBITOR_PATH = "C:\\Program Files (x86)\\NiBiTor\\NiBiTor.exe"
CONFIG_FILE_PATH = "gpu_config.json"

def load_config(config_file_path):
    """Load fan profile and temperature thresholds from a JSON configuration file."""
    try:
        with open(config_file_path, 'r') as file:
            config = json.load(file)
            logging.info("Configuration loaded successfully.")
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from configuration file.")
        sys.exit(1)

def change_fan_profile_and_thresholds(fan_profile, temp_thresholds):
    """Change the fan profile and temperature thresholds using NiBiTor."""
    try:
        # Construct the command for NiBiTor with the desired settings
        command = [
            NIBITOR_PATH,
            '-fan', fan_profile,
            '-thresh', ','.join(map(str, temp_thresholds))
        ]
        logging.info(f"Executing command: {' '.join(command)}")

        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors during execution
        if result.returncode != 0:
            logging.error(f"Error changing fan profile or temperature thresholds: {result.stderr}")
            raise RuntimeError("NiBiTor command failed.")
        
        logging.info("Fan profile and temperature thresholds changed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

def main():
    """Main function to handle GPU configuration changes."""
    # Load configurations from the JSON file
    config = load_config(CONFIG_FILE_PATH)
    
    # Extract fan profile and temperature thresholds
    fan_profile = config.get('fan_profile')
    temp_thresholds = config.get('temp_thresholds')

    if not fan_profile or not isinstance(temp_thresholds, list):
        logging.error("Invalid configuration: 'fan_profile' or 'temp_thresholds' are missing or incorrect.")
        sys.exit(1)

    # Change the fan profile and temperature thresholds
    change_fan_profile_and_thresholds(fan_profile, temp_thresholds)

if __name__ == "__main__":
    main()
```

### Configuration File Example (gpu_config.json):
```json
{
    "fan_profile": "75",
    "temp_thresholds": [80, 85, 90]
}
``` 

### Notes:
- Ensure that the paths and JSON structure match your environment and requirements.
- This code assumes that NiBiTor can accept command line arguments for the fan profile and temperature thresholds. Adjust the `command` list as necessary based on actual command-line options supported by NiBiTor.
