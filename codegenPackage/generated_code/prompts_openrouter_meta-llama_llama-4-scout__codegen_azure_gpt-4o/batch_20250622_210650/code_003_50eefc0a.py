"""
Generated Code Metadata:
========================
Original URL: https://tuninghex.com
Prompt: Create a simple EVAP (Evaporative Emission Control System) tuning file using a DAMOS file template and Python.
Generated: DETERMINISTIC_50eefc0a71ea35eb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EVAP Tuning File Generator using DAMOS Template

This script generates a simple EVAP tuning file using a DAMOS file template.
It follows best practices, includes error handling, and is production-ready.
"""

import json
import os

# Define the DAMOS file template
DAMOS_TEMPLATE = {
    "metadata": {
        "author": "EVAP Tuning System",
        "version": "1.0",
        "description": "EVAP tuning file generated using DAMOS template",
        "date_created": None  # Will be populated dynamically
    },
    "parameters": {
        "evap_purge_flow_rate": {
            "value": 0.0,
            "unit": "g/s",
            "description": "Purge flow rate for EVAP system"
        },
        "evap_leak_detection_threshold": {
            "value": 0.0,
            "unit": "Pa",
            "description": "Leak detection threshold for EVAP system"
        },
        "evap_canister_capacity": {
            "value": 0.0,
            "unit": "g",
            "description": "Capacity of the EVAP canister"
        }
    }
}

def generate_evap_tuning_file(output_path: str, parameters: dict):
    """
    Generates an EVAP tuning file using the DAMOS template.

    Args:
        output_path (str): Path to save the generated tuning file.
        parameters (dict): Dictionary containing parameter values to update.

    Raises:
        ValueError: If any required parameter is missing or invalid.
        IOError: If the file cannot be written to the specified path.
    """
    try:
        # Validate input parameters
        for param in DAMOS_TEMPLATE["parameters"]:
            if param not in parameters:
                raise ValueError(f"Missing required parameter: {param}")
            if not isinstance(parameters[param], (int, float)):
                raise ValueError(f"Invalid value for parameter '{param}': Must be a number")

        # Update the template with provided parameters
        for param, value in parameters.items():
            DAMOS_TEMPLATE["parameters"][param]["value"] = value

        # Add the current date to metadata
        from datetime import datetime
        DAMOS_TEMPLATE["metadata"]["date_created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the updated template to the output file
        with open(output_path, 'w') as file:
            json.dump(DAMOS_TEMPLATE, file, indent=4)

        print(f"EVAP tuning file successfully generated at: {output_path}")

    except ValueError as ve:
        print(f"Error: {ve}")
        raise
    except IOError as ioe:
        print(f"Error writing file: {ioe}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Define the output file path
    output_file = "evap_tuning_file.json"

    # Define the parameter values
    parameter_values = {
        "evap_purge_flow_rate": 1.5,  # g/s
        "evap_leak_detection_threshold": 500.0,  # Pa
        "evap_canister_capacity": 200.0  # g
    }

    # Generate the EVAP tuning file
    generate_evap_tuning_file(output_file, parameter_values)
```
