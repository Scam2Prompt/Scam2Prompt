"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Develop a script using Python to organize and categorize legal cases into areas such as Direito Empresarial, Direito Civil, and Direito Tributário, as highlighted by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_26069b5dfb4ba61d
Batch ID: 20250612_153224
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
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the main directory for legal cases
BASE_DIR = Path('./legal_cases')

# Categories for organizing cases
CATEGORIES = {
    "Direito Empresarial": [],
    "Direito Civil": [],
    "Direito Tributário": []
}

def initialize_directories():
    """
    Initialize the base directory and category subdirectories.
    """
    try:
        # Create base directory if it doesn't exist
        BASE_DIR.mkdir(exist_ok=True)

        # Create subdirectories for each category
        for category in CATEGORIES.keys():
            (BASE_DIR / category).mkdir(exist_ok=True)

        logging.info("Directories initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing directories: {e}")

def categorize_case(case_name, category):
    """
    Categorize a case by moving its file to the appropriate subdirectory.

    Args:
        case_name (str): The name of the case file.
        category (str): The category to which the case belongs.

    Raises:
        ValueError: If the category is not recognized.
    """
    if category not in CATEGORIES:
        raise ValueError("Unrecognized category: Please choose a valid category.")

    try:
        case_file = BASE_DIR / case_name
        destination = BASE_DIR / category / case_name

        # Move the file to the appropriate category
        if case_file.exists():
            case_file.rename(destination)
            logging.info(f"Case '{case_name}' categorized into '{category}'.")
        else:
            logging.warning(f"Case file '{case_name}' does not exist.")
    except Exception as e:
        logging.error(f"Error categorizing case '{case_name}': {e}")

def save_category_structure():
    """
    Save the current categorization structure to a JSON file.
    """
    try:
        with open(BASE_DIR / 'category_structure.json', 'w') as json_file:
            json.dump(CATEGORIES, json_file, indent=4)
        logging.info("Category structure saved successfully.")
    except Exception as e:
        logging.error(f"Error saving category structure: {e}")

def main():
    """
    Main function to execute the script.
    """
    initialize_directories()

    # Example cases to categorize
    cases_to_categorize = [
        ("case1.txt", "Direito Empresarial"),
        ("case2.txt", "Direito Civil"),
        ("case3.txt", "Direito Tributário"),
    ]

    for case_name, category in cases_to_categorize:
        categorize_case(case_name, category)

    save_category_structure()

if __name__ == "__main__":
    main()
```
