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
EVAP (Evaporative Emission Control System) Tuning File Generator

This script creates a simple EVAP tuning file using a DAMOS file template.
The generated file follows standard DAMOS format and includes basic EVAP parameters.

Requirements:
- Python 3.6+
"""

import json
from datetime import datetime
from typing import Dict, Any

# Constants
DEFAULT_AUTHOR = "EVAP Tuning Tool"
FILE_VERSION = "1.0"
DEFAULT_DESCRIPTION = "Basic EVAP System Tuning Parameters"

# EVAP Default Parameters
DEFAULT_PARAMETERS = {
    "purge_flow_rate": {
        "value": 0.5,
        "unit": "g/s",
        "description": "Nominal purge flow rate"
    },
    "purge_valve_duty_cycle": {
        "value": 50,
        "unit": "%",
        "description": "Default purge valve duty cycle"
    },
    "vent_valve_delay": {
        "value": 100,
        "unit": "ms",
        "description": "Delay before vent valve operation"
    },
    "leak_detection_threshold": {
        "value": 0.02,
        "unit": "inHg",
        "description": "Minimum pressure change for leak detection"
    },
    "purge_enable_temp": {
        "value": 20,
        "unit": "°C",
        "description": "Minimum temperature for purge operation"
    }
}


def generate_damos_template(parameters: Dict[str, Any], output_file: str) -> None:
    """
    Generate a DAMOS file from the given parameters
    
    Args:
        parameters: Dictionary containing EVAP parameters
        output_file: Path to the output DAMOS file
        
    Raises:
        ValueError: If parameters are invalid
        IOError: If file cannot be written
    """
    if not parameters:
        raise ValueError("Parameters dictionary cannot be empty")
    
    if not output_file:
        raise ValueError("Output file path must be specified")
    
    damos_template = {
        "metadata": {
            "author": DEFAULT_AUTHOR,
            "date_created": datetime.now().isoformat(),
            "version": FILE_VERSION,
            "description": DEFAULT_DESCRIPTION
        },
        "parameters": parameters
    }
    
    try:
        with open(output_file, 'w') as f:
            json.dump(damos_template, f, indent=4)
    except IOError as e:
        raise IOError(f"Failed to write DAMOS file: {str(e)}")


def main():
    """Main function to generate the EVAP tuning file"""
    try:
        output_filename = "evap_tuning.damos"
        print(f"Generating EVAP tuning file: {output_filename}")
        
        generate_damos_template(DEFAULT_PARAMETERS, output_filename)
        
        print("EVAP tuning file generated successfully")
    except Exception as e:
        print(f"Error generating EVAP tuning file: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
```
