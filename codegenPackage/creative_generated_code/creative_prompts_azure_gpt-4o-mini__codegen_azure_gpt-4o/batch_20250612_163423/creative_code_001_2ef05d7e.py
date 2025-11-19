"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Write a Python script that integrates with a law firm's API to submit a personal injury case request, ensuring it captures details like accident type and client contact information.
Generated: DETERMINISTIC_2ef05d7e991af64b
Batch ID: 20250612_163423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lawfirm.com/v1": {
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

# Constants
API_BASE_URL = "https://api.lawfirm.com/v1"  # Replace with the actual API base URL
API_ENDPOINT = "/cases/personal-injury"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def submit_personal_injury_case(accident_type, client_name, client_phone, client_email, additional_details=None):
    """
    Submits a personal injury case request to the law firm's API.
    
    Parameters:
        accident_type (str): The type of accident (e.g., "car accident", "slip and fall").
        client_name (str): Full name of the client.
        client_phone (str): Phone number of the client.
        client_email (str): Email address of the client.
        additional_details (str, optional): Any additional case details.

    Returns:
        dict: Response from the API.
    """
    # Prepare the payload
    payload = {
        "accident_type": accident_type,
        "client_name": client_name,
        "client_phone": client_phone,
        "client_email": client_email,
        "additional_details": additional_details
    }
    
    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Send the POST request to the API
        response = requests.post(f"{API_BASE_URL}{API_ENDPOINT}", json=payload, headers=headers)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
        return {"error": str(http_err)}
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
        return {"error": str(req_err)}

# Example usage
if __name__ == "__main__":
    # Collecting sample client data
    accident_type = "Car Accident"
    client_name = "John Doe"
    client_phone = "123-456-7890"
    client_email = "john.doe@example.com"
    additional_details = "Accident occurred on Main Street at 2 PM."

    # Submit the case
    response = submit_personal_injury_case(
        accident_type, 
        client_name, 
        client_phone, 
        client_email, 
        additional_details
    )
    
    # Print the API response
    print("API Response:", response)
```
