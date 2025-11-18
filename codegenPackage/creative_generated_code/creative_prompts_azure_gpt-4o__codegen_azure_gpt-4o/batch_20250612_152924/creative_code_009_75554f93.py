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
"""
Automate the creation and review of contracts for foreign workers in Spain.
The script ensures compliance with Spanish civil and labor laws.
The script uses Python's `docx` library to generate Word documents for contracts
and checks basic compliance parameters.
"""

import os
from docx import Document
from datetime import datetime

# Constants
CONTRACT_TEMPLATE = "contract_template.docx"  # Path to contract template
OUTPUT_DIR = "generated_contracts"  # Directory to save generated contracts
REQUIRED_FIELDS = [
    "worker_name", "worker_nationality", "worker_id", "start_date",
    "end_date", "job_description", "salary", "contract_type"
]

def validate_input(data):
    """
    Validate input data for required fields.
    
    :param data: Dictionary containing contract details.
    :return: Boolean indicating whether data is valid.
    :raises ValueError: If required fields are missing.
    """
    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    return True

def generate_contract(data):
    """
    Generate a contract document based on input data.
    
    :param data: Dictionary containing contract details.
    :return: Path to the generated contract file.
    """
    # Validate input data
    validate_input(data)

    # Load contract template
    if not os.path.exists(CONTRACT_TEMPLATE):
        raise FileNotFoundError(f"Contract template '{CONTRACT_TEMPLATE}' not found.")
    document = Document(CONTRACT_TEMPLATE)

    # Replace placeholders in the contract template
    placeholders = {
        "[WORKER_NAME]": data["worker_name"],
        "[WORKER_NATIONALITY]": data["worker_nationality"],
        "[WORKER_ID]": data["worker_id"],
        "[START_DATE]": data["start_date"],
        "[END_DATE]": data["end_date"],
        "[JOB_DESCRIPTION]": data["job_description"],
        "[SALARY]": data["salary"],
        "[CONTRACT_TYPE]": data["contract_type"],
    }

    for paragraph in document.paragraphs:
        for placeholder, value in placeholders.items():
            if placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(placeholder, value)

    # Save the contract to the output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    contract_filename = f"{data['worker_name'].replace(' ', '_')}_contract.docx"
    contract_path = os.path.join(OUTPUT_DIR, contract_filename)
    document.save(contract_path)

    return contract_path

def review_contract(data):
    """
    Review the contract for compliance with Spanish civil and labor laws.
    
    :param data: Dictionary containing contract details.
    :return: Boolean indicating whether the contract is compliant.
    """
    # Example compliance checks
    if data["salary"] < 1000:  # Assuming minimum salary is 1000 EUR
        raise ValueError("Salary does not meet minimum wage requirements.")
    if datetime.strptime(data["start_date"], "%Y-%m-%d") >= datetime.strptime(data["end_date"], "%Y-%m-%d"):
        raise ValueError("End date must be after start date.")
    # Add additional compliance checks as needed

    return True

def main():
    """
    Main function to generate and review contracts.
    """
    try:
        # Example input data
        contract_data = {
            "worker_name": "John Doe",
            "worker_nationality": "American",
            "worker_id": "A12345678",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "job_description": "Software Developer",
            "salary": 3000,
            "contract_type": "Full-Time"
        }

        # Generate the contract
        print("Generating contract...")
        contract_path = generate_contract(contract_data)
        print(f"Contract saved at: {contract_path}")

        # Review the contract for compliance
        print("Reviewing contract for compliance...")
        if review_contract(contract_data):
            print("Contract is compliant with Spanish civil and labor laws.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
