"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Generate a Python script that automates the process of creating a company in Switzerland, including steps for domiciliation and appointing an administrator, as described by Hub Experts.
Generated: DETERMINISTIC_d738ecbd5072408a
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("company_creation.log"),
        logging.StreamHandler()
    ]
)

# Constants
COMPANY_DATA_FILE = "company_data.json"

# Helper functions
def load_company_data(file_path):
    """
    Load company data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing company data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        raise

def validate_company_data(data):
    """
    Validate the company data.
    :param data: Dictionary containing company data.
    :return: True if data is valid, False otherwise.
    """
    required_fields = ["company_name", "address", "administrator_name", "administrator_email"]
    for field in required_fields:
        if field not in data or not data[field]:
            logging.error(f"Missing or empty required field: {field}")
            return False
    return True

def create_company(data):
    """
    Simulate the process of creating a company in Switzerland.
    :param data: Dictionary containing company data.
    """
    try:
        logging.info(f"Creating company: {data['company_name']}")
        # Simulate domiciliation process
        logging.info(f"Domiciling company at address: {data['address']}")
        # Simulate appointing administrator
        logging.info(f"Appointing administrator: {data['administrator_name']} ({data['administrator_email']})")
        logging.info("Company creation process completed successfully.")
    except Exception as e:
        logging.error(f"Error during company creation: {e}")
        raise

def main():
    """
    Main function to automate the company creation process.
    """
    logging.info("Starting company creation automation process.")
    
    # Load company data
    try:
        company_data = load_company_data(COMPANY_DATA_FILE)
    except Exception as e:
        logging.error(f"Failed to load company data: {e}")
        return
    
    # Validate company data
    if not validate_company_data(company_data):
        logging.error("Company data validation failed.")
        return
    
    # Create company
    try:
        create_company(company_data)
    except Exception as e:
        logging.error(f"Failed to create company: {e}")
        return
    
    logging.info("Automation process completed successfully.")

if __name__ == "__main__":
    main()
```

### Notes:
1. To run this script, create a `company_data.json` file in the same directory with the following structure:
   ```json
   {
       "company_name": "Example AG",
       "address": "Bahnhofstrasse 1, Zurich, Switzerland",
       "administrator_name": "John Doe",
       "administrator_email": "john.doe@example.com"
   }
   ```
2. The script logs all actions to both the console and a `company_creation.log` file for traceability.
