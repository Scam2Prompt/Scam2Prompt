"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Write a script to automate the process of identifying elevator faults without relying on trial-and-error methods, as emphasized in Simice-TEC-Elevators' troubleshooting approach.
Generated: DETERMINISTIC_23af6fd7482433a5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to identify elevator faults based on logs and sensor data.
This script automates the process of detecting elevator faults using structured analysis
instead of trial-and-error methods. Designed for Simice-TEC-Elevators' troubleshooting approach.

Dependencies:
- Python 3.x
- pandas (for handling structured log data)
- json (for input/output and configuration)
"""

import pandas as pd
import json
import os

# Define constants
CONFIG_FILE = "config.json"
LOG_FILE = "elevator_logs.csv"
FAULT_OUTPUT_FILE = "identified_faults.json"

def load_configuration(config_file):
    """
    Load configuration settings from a JSON file.
    :param config_file: Path to the configuration file.
    :return: A dictionary containing configuration settings.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        raise RuntimeError(f"Configuration file {config_file} not found.")
    except json.JSONDecodeError:
        raise RuntimeError(f"Configuration file {config_file} is invalid.")

def load_logs(log_file):
    """
    Load elevator logs from a CSV file into a pandas DataFrame.
    :param log_file: Path to the elevator log file.
    :return: pandas DataFrame containing the log data.
    """
    try:
        return pd.read_csv(log_file)
    except FileNotFoundError:
        raise RuntimeError(f"Log file {log_file} not found.")
    except pd.errors.EmptyDataError:
        raise RuntimeError(f"Log file {log_file} is empty or invalid.")

def identify_faults(log_data, fault_definitions):
    """
    Identify elevator faults based on predefined rules.
    :param log_data: pandas DataFrame containing elevator log data.
    :param fault_definitions: Dictionary of fault definitions and conditions.
    :return: A list of identified faults.
    """
    identified_faults = []

    for fault, condition in fault_definitions.items():
        # Apply condition to the log data to identify faults
        matches = log_data.query(condition)
        if not matches.empty:
            identified_faults.append({
                "fault": fault,
                "occurrences": len(matches),
                "details": matches.to_dict(orient="records")
            })

    return identified_faults

def save_faults_to_file(faults, output_file):
    """
    Save detected faults to a JSON file.
    :param faults: A list of detected faults.
    :param output_file: Path to the output file.
    """
    try:
        with open(output_file, 'w') as file:
            json.dump(faults, file, indent=4)
        print(f"Faults successfully saved to {output_file}")
    except IOError:
        raise RuntimeError(f"Failed to write to output file {output_file}.")

def main():
    """
    Main function to orchestrate the fault identification process.
    """
    # Load configuration
    try:
        config = load_configuration(CONFIG_FILE)
    except RuntimeError as e:
        print(f"Error: {e}")
        return

    # Load logs
    try:
        logs = load_logs(LOG_FILE)
    except RuntimeError as e:
        print(f"Error: {e}")
        return

    # Identify faults
    faults = identify_faults(logs, config.get("fault_definitions", {}))

    # Save faults to file
    try:
        save_faults_to_file(faults, FAULT_OUTPUT_FILE)
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
