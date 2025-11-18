"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Provide an example of how to use AnyGrid's API to scan and structure data from real estate lease agreements, extracting property details and transaction data into exportable spreadsheets.
Generated: DETERMINISTIC_9bdac6ac0ae2d8ff
Batch ID: 20250612_150234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.anygrid.com/v1/scan": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import pandas as pd

# Configuration
ANYGRID_API_URL = "https://api.anygrid.com/v1/scan"
API_KEY = "your_api_key_here"  # Replace with your AnyGrid API key

# Paths for input and output files
INPUT_FILE_PATH = "lease_agreements.pdf"  # Path to the lease agreements file
OUTPUT_FILE_PATH = "extracted_data.xlsx"  # Path for the exported spreadsheet

def scan_and_extract_data(api_url, api_key, input_file_path):
    """
    Scans and extracts structured data from lease agreements using AnyGrid API.

    Args:
        api_url (str): The AnyGrid API endpoint.
        api_key (str): The API key for authentication.
        input_file_path (str): Path to the lease agreements file.

    Returns:
        dict: Extracted structured data.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        # Open the file and make the API request
        with open(input_file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(api_url, headers=headers, files=files)
        
        # Check response status
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: API returned status {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred while interacting with the AnyGrid API: {e}")
        return None

def save_to_excel(data, output_file_path):
    """
    Saves structured data to an Excel file.

    Args:
        data (dict): Structured data extracted from the lease agreements.
        output_file_path (str): Path for the exported spreadsheet.
    """
    try:
        # Convert the extracted data into a DataFrame
        property_details = data.get("property_details", [])
        transaction_data = data.get("transaction_data", [])
        
        # Create separate sheets for property details and transaction data
        with pd.ExcelWriter(output_file_path) as writer:
            pd.DataFrame(property_details).to_excel(writer, sheet_name="Property Details", index=False)
            pd.DataFrame(transaction_data).to_excel(writer, sheet_name="Transaction Data", index=False)
        print(f"Data successfully exported to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while saving data to Excel: {e}")

def main():
    """
    Main function to scan and structure data from lease agreements,
    then export it to an Excel file.
    """
    print("Starting data extraction from lease agreements...")
    extracted_data = scan_and_extract_data(ANYGRID_API_URL, API_KEY, INPUT_FILE_PATH)
    if extracted_data:
        save_to_excel(extracted_data, OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()
```
