"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write code to generate incorporation documents for a new business, including fields for business name, Federal ID number, and business license details, as outlined in the business startup services provided by Hispanic Services.
Generated: DETERMINISTIC_2acc341abf3552c9
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

def generate_incorporation_documents(business_name, federal_id, license_details, output_directory):
    """
    Generates incorporation documents for a new business.
    
    Args:
        business_name (str): Name of the business.
        federal_id (str): Federal ID number of the business.
        license_details (dict): Dictionary containing business license details.
                                Example: {"license_number": "123456", "issued_by": "City of Hispanic Services", "issue_date": "2023-10-01"}
        output_directory (str): Directory where the generated documents will be saved.
    
    Returns:
        str: Filepath of the generated incorporation document (JSON format).
    """
    try:
        # Validate input
        if not business_name or not federal_id or not license_details:
            raise ValueError("All fields (business_name, federal_id, license_details) are required.")
        
        if not isinstance(license_details, dict):
            raise TypeError("License details must be provided as a dictionary.")

        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Prepare incorporation document data
        incorporation_data = {
            "business_name": business_name,
            "federal_id": federal_id,
            "license_details": {
                "license_number": license_details.get("license_number"),
                "issued_by": license_details.get("issued_by"),
                "issue_date": license_details.get("issue_date")
            },
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Validate license details
        if not incorporation_data["license_details"]["license_number"]:
            raise ValueError("License number is required in license_details.")
        if not incorporation_data["license_details"]["issued_by"]:
            raise ValueError("Issued by is required in license_details.")
        if not incorporation_data["license_details"]["issue_date"]:
            raise ValueError("Issue date is required in license_details.")

        # Save incorporation document as JSON file
        output_filepath = os.path.join(output_directory, f"{business_name.replace(' ', '_')}_incorporation.json")
        with open(output_filepath, "w", encoding="utf-8") as json_file:
            json.dump(incorporation_data, json_file, indent=4)

        return output_filepath

    except Exception as e:
        # Log the error and re-raise it
        print(f"Error: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Business details
        business_name = "Hispanic Services LLC"
        federal_id = "123-45-6789"
        license_details = {
            "license_number": "HS123456",
            "issued_by": "City of Hispanic Services",
            "issue_date": "2023-10-01"
        }
        output_directory = "./documents"

        # Generate incorporation document
        filepath = generate_incorporation_documents(business_name, federal_id, license_details, output_directory)
        print(f"Incorporation document generated successfully: {filepath}")
    except Exception as e:
        print(f"Failed to generate incorporation document: {str(e)}")
```
