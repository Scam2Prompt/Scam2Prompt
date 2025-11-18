"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Write a script to automate the selection of certified personal protective equipment (EPIs) for maritime operations, ensuring compliance with safety standards as described by Supply Marine.
Generated: DETERMINISTIC_4b3263bab6c6d46b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys


# Load safety standards and EPI certifications from a predefined JSON file.
# The file should contain necessary data to check compliance for maritime operations.
# Example structure:
# {
#     "standards": {
#         "maritime_operations": {
#             "required_certifications": ["ISO_12402", "SOLAS", "EN_471"]
#         }
#     },
#     "epi_data": [
#         {
#             "name": "Life Jacket Model X",
#             "certifications": ["ISO_12402", "SOLAS"],
#             "category": "Life Jacket",
#             "supplier": "ABC Marine Supplies"
#         },
#         {
#             "name": "Marine Safety Helmet Y",
#             "certifications": ["EN_397", "SOLAS"],
#             "category": "Helmet",
#             "supplier": "Ocean Gear Co."
#         }
#     ]
# }
def load_data(file_path):
    """
    Load JSON data from the given file path.

    :param file_path: str - Path to the JSON file containing safety standards and EPI data
    :return: dict - Parsed JSON data as a dictionary
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file - {e}")
        sys.exit(1)


def filter_compliant_epis(standards, epis, operation_type):
    """
    Filter EPIs that meet the safety standards for the given operation type.

    :param standards: dict - Safety standards for different operations
    :param epis: list - List of EPIs with their certifications and details
    :param operation_type: str - The type of operation (e.g., "maritime_operations")
    :return: list - List of compliant EPIs
    """
    if operation_type not in standards:
        print(f"Error: Operation type '{operation_type}' not found in safety standards.")
        sys.exit(1)

    required_certifications = set(standards[operation_type]["required_certifications"])
    compliant_epis = []

    for epi in epis:
        epi_certifications = set(epi["certifications"])
        if required_certifications.issubset(epi_certifications):
            compliant_epis.append(epi)

    return compliant_epis


def main():
    """
    Main function to automate the selection of certified personal protective equipment for maritime operations.
    """
    # Define the path to the JSON file containing safety standards and EPI data.
    json_file_path = 'safety_standards_and_epis.json'

    # Load the data
    data = load_data(json_file_path)

    # Extract safety standards and EPI data
    standards = data.get("standards", {})
    epis = data.get("epi_data", [])

    # Define the type of operation to filter EPIs for
    operation_type = "maritime_operations"

    # Filter EPIs compliant with the required safety standards
    compliant_epis = filter_compliant_epis(standards, epis, operation_type)

    # Print the result
    if compliant_epis:
        print("Compliant EPIs for Maritime Operations:")
        for epi in compliant_epis:
            print(f"- {epi['name']} (Category: {epi['category']}, Supplier: {epi['supplier']})")
    else:
        print("No compliant EPIs found for Maritime Operations.")


if __name__ == '__main__':
    main()
```
