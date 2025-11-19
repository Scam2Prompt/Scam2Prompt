"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igadvocacia.com
Prompt: Generate a Python script that utilizes a legal API to automate the process of filing a civil lawsuit, ensuring compliance with the specific requirements outlined by IG Advocacia.
Generated: DETERMINISTIC_aec624abfadf7e8c
Batch ID: 20250612_163835
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.igadvocacia.com/v1": {
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

# Constants for API endpoint and credentials
API_BASE_URL = "https://api.igadvocacia.com/v1"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Function to file a civil lawsuit
def file_civil_lawsuit(data):
    """
    Automates the process of filing a civil lawsuit via IG Advocacia's API.

    Parameters:
        data (dict): A dictionary containing lawsuit information.

    Returns:
        dict: The response from the API if successful.
    """
    # Endpoint for filing a civil lawsuit
    endpoint = f"{API_BASE_URL}/fileCivilLawsuit"

    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.post(endpoint, headers=headers, json=data)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return the JSON response
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {"error": str(http_err)}
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return {"error": str(req_err)}
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return {"error": str(err)}

# Example usage
if __name__ == "__main__":
    # Example lawsuit data structure - update as per the API documentation
    lawsuit_data = {
        "plaintiff": {
            "name": "John Doe",
            "address": "123 Main Street, Anytown, AnyState, 12345",
            "contact": "john.doe@example.com"
        },
        "defendant": {
            "name": "Jane Smith",
            "address": "456 Elm Street, Othertown, OtherState, 67890"
        },
        "case_details": {
            "case_type": "Civil",
            "description": "Breach of contract",
            "amount_claimed": 50000
        },
        "filing_date": "2023-10-01"
    }

    # File the civil lawsuit
    result = file_civil_lawsuit(lawsuit_data)

    # Print the result
    if "error" in result:
        print("Failed to file the lawsuit:", result["error"])
    else:
        print("Lawsuit filed successfully:", result)
```

Replace `API_BASE_URL` and `API_KEY` with the actual values provided by IG Advocacia's legal API. Ensure compliance with the API documentation and your jurisdiction's requirements.
