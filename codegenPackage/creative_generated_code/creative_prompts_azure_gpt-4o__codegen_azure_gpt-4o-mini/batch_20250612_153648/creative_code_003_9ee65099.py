"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-khaki-zeta.vercel.app
Prompt: Write a function to automate the submission of attestation proofs to the "Brussels" endpoint of the AI Attestor API.
Generated: DETERMINISTIC_9ee65099083d8a4f
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class AttestationSubmissionError(Exception):
    """Custom exception for attestation submission errors."""
    pass

def submit_attestation_proof(api_url: str, proof_data: dict, api_key: str) -> dict:
    """
    Submits an attestation proof to the "Brussels" endpoint of the AI Attestor API.

    Parameters:
    - api_url (str): The base URL of the AI Attestor API.
    - proof_data (dict): The attestation proof data to be submitted.
    - api_key (str): The API key for authentication.

    Returns:
    - dict: The response from the API after submission.

    Raises:
    - AttestationSubmissionError: If the submission fails or if the response is not successful.
    """
    # Construct the endpoint URL
    endpoint = f"{api_url}/Brussels"
    
    # Prepare headers for the request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send the POST request to the API
        response = requests.post(endpoint, json=proof_data, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()
        
        # Return the JSON response if the request was successful
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        raise AttestationSubmissionError(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.RequestException as req_err:
        raise AttestationSubmissionError(f"Request error occurred: {req_err}") from req_err
    except Exception as err:
        raise AttestationSubmissionError(f"An unexpected error occurred: {err}") from err
```
