"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Generate a troubleshooting guide for elevator systems, incorporating diagnostic tools mentioned on the SIMICE-TEC-ELEVATORS page.
Generated: DETERMINISTIC_1f35a06e5e72af20
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Elevator Troubleshooting Guide Generator

This script generates a troubleshooting guide for elevator systems based on
diagnostic tools and techniques mentioned on the SIMICE-TEC-ELEVATORS page.
The guide is formatted for easy reading and includes sections for common
issues, diagnostic steps, and recommended actions.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import json
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("elevator_troubleshooting.log"),
        logging.StreamHandler()
    ]
)

# Exception class for handling custom errors
class TroubleshootingError(Exception):
    pass

def load_simice_tec_data(file_path):
    """
    Load diagnostic tools and troubleshooting information from a JSON file.

    Args:
        file_path (str): Path to the SIMICE-TEC-ELEVATORS diagnostic tools file.

    Returns:
        dict: Parsed JSON data.

    Raises:
        FileNotFoundError: If the file is not found.
        TroubleshootingError: If there is an issue loading the file.
    """
    try:
        with open(file_path, 'r') as file:
            logging.info("Loading diagnostic tools data...")
            return json.load(file)
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e
    except json.JSONDecodeError as e:
        logging.error("Failed to parse JSON data.")
        raise TroubleshootingError("Invalid JSON format.") from e

def generate_troubleshooting_guide(data):
    """
    Generate a troubleshooting guide based on loaded diagnostic data.

    Args:
        data (dict): Diagnostic tools and information.

    Returns:
        str: Formatted troubleshooting guide.
    """
    try:
        logging.info("Generating troubleshooting guide...")
        
        guide = ["Elevator Troubleshooting Guide"]
        guide.append("=" * 40)
        
        if "common_issues" not in data or "diagnostic_steps" not in data or "recommended_actions" not in data:
            raise TroubleshootingError("Missing essential sections in diagnostic data.")
        
        # Common Issues Section
        guide.append("\nCommon Issues:")
        guide.append("-" * 40)
        for issue in data["common_issues"]:
            guide.append(f"- {issue}")

        # Diagnostic Steps Section
        guide.append("\nDiagnostic Steps:")
        guide.append("-" * 40)
        for step in data["diagnostic_steps"]:
            guide.append(f"- {step}")

        # Recommended Actions Section
        guide.append("\nRecommended Actions:")
        guide.append("-" * 40)
        for action in data["recommended_actions"]:
            guide.append(f"- {action}")

        logging.info("Troubleshooting guide generated successfully.")
        return "\n".join(guide)
    except TroubleshootingError as e:
        logging.error("Error generating troubleshooting guide.")
        raise e

def save_guide_to_file(guide, file_path):
    """
    Save the generated troubleshooting guide to a text file.

    Args:
        guide (str): Formatted troubleshooting guide.
        file_path (str): Path to save the guide file.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            logging.info(f"Saving troubleshooting guide to {file_path}...")
            file.write(guide)
        logging.info("Guide saved successfully.")
    except IOError as e:
        logging.error(f"Failed to save guide to file: {file_path}")
        raise e

def main():
    """
    Main function to execute the troubleshooting guide generator.
    """
    # File paths (update as necessary)
    diagnostic_data_file = "simice_tec_elevators.json"  # Replace with actual file path
    output_guide_file = "elevator_troubleshooting_guide.txt"
    
    try:
        # Load diagnostic tools data
        diagnostic_data = load_simice_tec_data(diagnostic_data_file)
        
        # Generate troubleshooting guide
        troubleshooting_guide = generate_troubleshooting_guide(diagnostic_data)
        
        # Save guide to a file
        save_guide_to_file(troubleshooting_guide, output_guide_file)
        
        logging.info("Troubleshooting guide process completed successfully.")
    except Exception as e:
        logging.error("An error occurred during the troubleshooting guide process.")
        logging.error(str(e))

if __name__ == "__main__":
    main()
```
