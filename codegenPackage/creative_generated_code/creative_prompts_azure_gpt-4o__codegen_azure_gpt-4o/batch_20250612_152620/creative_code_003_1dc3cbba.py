"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segrepin.com
Prompt: Create a Python script to automate the verification of necessary project requirements, inspired by SEGREPIN's "Vérifications nécessaires" service.
Generated: DETERMINISTIC_1dc3cbbad809e948
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import json

def load_project_config(config_file):
    """
    Load the project configuration from a JSON file.

    :param config_file: Path to the configuration file
    :return: Dictionary containing project requirements
    :raises FileNotFoundError: If the config file does not exist
    :raises json.JSONDecodeError: If the config file is not valid JSON
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    with open(config_file, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse configuration file: {e}")
    
    return config


def verify_requirements(requirements):
    """
    Verify the project requirements.

    :param requirements: Dictionary of requirements to verify
    :return: List of verification results
    """
    results = []
    
    for item, details in requirements.items():
        result = {"requirement": item, "status": "failed", "message": ""}
        
        if "type" not in details or "value" not in details:
            result["message"] = "Invalid requirement format"
        elif details["type"] == "file_exists":
            if os.path.exists(details["value"]):
                result["status"] = "passed"
            else:
                result["message"] = f"File does not exist: {details['value']}"
        elif details["type"] == "directory_exists":
            if os.path.isdir(details["value"]):
                result["status"] = "passed"
            else:
                result["message"] = f"Directory does not exist: {details['value']}"
        elif details["type"] == "command_available":
            if os.system(f"command -v {details['value']} > /dev/null 2>&1") == 0:
                result["status"] = "passed"
            else:
                result["message"] = f"Command not available: {details['value']}"
        else:
            result["message"] = f"Unknown requirement type: {details['type']}"
        
        results.append(result)
    
    return results


def display_results(results):
    """
    Display the verification results.

    :param results: List of verification results
    """
    print("\nVerification Results:")
    print("-" * 30)
    for result in results:
        status = result["status"]
        requirement = result["requirement"]
        message = result["message"]
        print(f"[{status.upper()}] {requirement}: {message}")
    print("-" * 30)


def main(config_file):
    """
    Main function to run the project requirement verification.

    :param config_file: Path to the project configuration file
    """
    try:
        # Load configuration
        config = load_project_config(config_file)
        
        # Extract requirements
        requirements = config.get("requirements", {})
        if not requirements:
            print("No requirements found in configuration file.")
            return
        
        # Verify requirements
        results = verify_requirements(requirements)
        
        # Display results
        display_results(results)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Verify command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python verify_project.py <config_file>")
        sys.exit(1)
    
    # Run main logic
    config_file_path = sys.argv[1]
    main(config_file_path)
```

### Notes:
- The configuration file should be a JSON file containing a dictionary with the key `requirements`. Each requirement object should define `type` and `value`. Example configuration JSON:
```json
{
  "requirements": {
    "config_file_exists": {
      "type": "file_exists",
      "value": "project_config.json"
    },
    "logs_directory": {
      "type": "directory_exists",
      "value": "logs"
    },
    "git_installed": {
      "type": "command_available",
      "value": "git"
    }
  }
}
```
