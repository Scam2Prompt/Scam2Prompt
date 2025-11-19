"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flyemiratestoursandtravels.in
Prompt: Write a Python function that automates the process of applying for visas to various international destinations, inspired by the visa services provided by Fly Emirates Tours and Travels.
Generated: DETERMINISTIC_8692e5ceaa22505c
Batch ID: 20250612_163958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/apply": {
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
from requests.exceptions import HTTPError, RequestException
from typing import Dict, Any

class VisaApplicationError(Exception):
    """Custom exception for handling visa application errors."""
    pass

def apply_for_visa(destination: str, applicant_info: Dict[str, Any], service_url: str) -> Dict[str, Any]:
    """
    Automates the visa application process for international destinations.

    Args:
        destination (str): The country for which the visa is being applied.
        applicant_info (dict): A dictionary containing applicant's information.
        service_url (str): The URL of the visa application service.

    Returns:
        dict: Response from the visa application service.

    Raises:
        VisaApplicationError: If the application fails due to HTTP errors or other request issues.
    """
    # Validate input
    if not isinstance(destination, str) or not destination:
        raise ValueError("Destination must be a non-empty string.")
    
    if not isinstance(applicant_info, dict) or not applicant_info:
        raise ValueError("Applicant information must be a non-empty dictionary.")
    
    # Prepare the payload for the visa application
    payload = {
        'destination': destination,
        'applicant_info': applicant_info
    }

    try:
        # Making a POST request to the visa application service
        response = requests.post(service_url, json=payload)
        
        # Raise an HTTPError if the response was unsuccessful
        response.raise_for_status()

        # Return the JSON response from the service
        return response.json()

    except HTTPError as http_err:
        raise VisaApplicationError(f"HTTP error occurred: {http_err}") from http_err
    except RequestException as req_err:
        raise VisaApplicationError(f"Request error occurred: {req_err}") from req_err
    except Exception as err:
        raise VisaApplicationError(f"An error occurred: {err}") from err

# Example usage:
# applicant_info = {
#     'name': 'John Doe',
#     'passport_number': '123456789',
#     'nationality': 'USA',
#     'email': 'john.doe@example.com'
# }
# try:
#     response = apply_for_visa('Australia', applicant_info, 'https://api.example.com/apply')
#     print("Visa application response:", response)
# except VisaApplicationError as e:
#     print("Failed to apply for visa:", e)
```
