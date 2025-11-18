"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Create an API integration example for tracking debt enforcement (exekuce) cases and automating legal documentation preparation, inspired by Arbitum Consulting's services.
Generated: DETERMINISTIC_868b05450190ccb2
Batch ID: 20250612_150347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debtenforcement.example.com/v1": {
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

# Constants
API_BASE_URL = "https://api.debtenforcement.example.com/v1"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Exception class for error handling
class DebtEnforcementAPIError(Exception):
    pass


def fetch_enforcement_cases():
    """
    Fetch a list of ongoing debt enforcement cases from the API.

    Returns:
        list: A list of enforcement cases.

    Raises:
        DebtEnforcementAPIError: If the API request fails or returns an error response.
    """
    endpoint = f"{API_BASE_URL}/cases"
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        cases = response.json()  # Parse JSON response
        return cases
    except requests.exceptions.RequestException as e:
        raise DebtEnforcementAPIError(f"Failed to fetch enforcement cases: {str(e)}")


def prepare_legal_document(case_id, template_id):
    """
    Prepare a legal document for a specific debt enforcement case.

    Args:
        case_id (str): The ID of the enforcement case.
        template_id (str): The ID of the legal document template.

    Returns:
        dict: The prepared legal document details.

    Raises:
        DebtEnforcementAPIError: If the API request fails or returns an error response.
    """
    endpoint = f"{API_BASE_URL}/cases/{case_id}/documents"
    payload = {
        "template_id": template_id,
    }

    try:
        response = requests.post(endpoint, headers=HEADERS, json=payload)
        response.raise_for_status()

        document = response.json()
        return document
    except requests.exceptions.RequestException as e:
        raise DebtEnforcementAPIError(f"Failed to prepare legal document: {str(e)}")


def main():
    """
    Main function for automating the process of tracking enforcement cases and preparing legal documents.
    """
    try:
        # Fetch enforcement cases
        cases = fetch_enforcement_cases()
        print("Fetched Enforcement Cases:")
        for case in cases:
            print(json.dumps(case, indent=4))  # Pretty-print case details

        # Example: Prepare legal document for the first case
        if cases:
            first_case_id = cases[0]["id"]  # Assume the first case has an "id" field
            template_id = "template_legal_doc_001"  # Replace with an actual template ID

            # Prepare legal document
            document = prepare_legal_document(first_case_id, template_id)
            print("Prepared Legal Document:")
            print(json.dumps(document, indent=4))
        else:
            print("No enforcement cases found.")
    except DebtEnforcementAPIError as api_error:
        print(f"Error: {api_error}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")


if __name__ == "__main__":
    main()
```
