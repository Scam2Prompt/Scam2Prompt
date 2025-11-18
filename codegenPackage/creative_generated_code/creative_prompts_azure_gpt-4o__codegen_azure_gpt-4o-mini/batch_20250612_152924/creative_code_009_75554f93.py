"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Create a Python script to automate the creation and review of contracts for foreign workers in Spain, ensuring compliance with Spanish civil and labor laws.
Generated: DETERMINISTIC_75554f93b1eb4a4c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import pandas as pd
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration Constants
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'contracts'
CONTRACT_DATA_FILE = 'contract_data.json'

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def load_contract_data(file_path):
    """
    Load contract data from a JSON file.
    
    :param file_path: path to the JSON file containing contract data
    :return: dictionary with contract data
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logging.info("Contract data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error("Contract data file not found.")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        raise

def render_contract(template_name, context):
    """
    Render a contract template with the given context data.
    
    :param template_name: name of the template file
    :param context: data to render the template
    :return: rendered contract as a string
    """
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)
    return template.render(context)

def save_contract(file_name, content):
    """
    Save the rendered contract to a file.
    
    :param file_name: name of the output file
    :param content: content to write to the file
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        logging.info(f"Contract saved successfully: {file_name}")
    except IOError as e:
        logging.error(f"Error saving contract: {e}")
        raise

def create_contracts(contract_data):
    """
    Create contracts for each worker based on the provided data.
    
    :param contract_data: list of dictionaries containing contract details
    """
    for worker in contract_data['workers']:
        try:
            contract_content = render_contract('contract_template.txt', worker)
            file_name = os.path.join(OUTPUT_DIR, f"contract_{worker['id']}_{datetime.now().strftime('%Y%m%d')}.txt")
            save_contract(file_name, contract_content)
        except Exception as e:
            logging.error(f"Failed to create contract for worker ID {worker['id']}: {e}")

def main():
    """
    Main function to execute the contract creation process.
    """
    logging.info("Starting contract creation process.")
    contract_data = load_contract_data(CONTRACT_DATA_FILE)
    create_contracts(contract_data)
    logging.info("Contract creation process completed.")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that you have a folder named `templates` with a contract template file named `contract_template.txt` in the same directory as this script.
- The `contract_data.json` file should contain a JSON structure that includes a list of workers, each with necessary attributes such as 'id', 'name', 'position', etc.
- The code uses the Jinja2 template engine for rendering contracts, so ensure to install it using `pip install Jinja2`.
