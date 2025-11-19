"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Write a Python script that integrates with an API to manage service requests for water leakage detection, inspired by the techniques used by شركة انجاز.
Generated: DETERMINISTIC_98985f11b9ce89e7
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.water-leakage-detection.com": {
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

# Constants for API interaction
API_BASE_URL = "https://api.water-leakage-detection.com"  # Replace with actual API base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Error messages
API_ERROR_MSG = "An error occurred while interacting with the API."
CONNECTION_ERROR_MSG = "Could not connect to the API."

# Function to handle service requests
def create_service_request(address, customer_name, contact_number, description):
    """
    Creates a new service request for water leakage detection.
    
    :param address: str - The address where the service is needed.
    :param customer_name: str - Name of the customer.
    :param contact_number: str - Contact number of the customer.
    :param description: str - Description of the problem.
    :return: dict - Result of the service request creation.
    """
    try:
        payload = {
            "address": address,
            "customer_name": customer_name,
            "contact_number": contact_number,
            "description": description
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.post(f"{API_BASE_URL}/service-requests", json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 201:  # HTTP 201 Created
            return response.json()
        else:
            # Log error details
            print(f"{API_ERROR_MSG}: {response.status_code}, {response.text}")
            response.raise_for_status()

    except requests.ConnectionError:
        print(CONNECTION_ERROR_MSG)
        return {"error": CONNECTION_ERROR_MSG}
    except requests.RequestException as e:
        print(f"{API_ERROR_MSG}: {str(e)}")
        return {"error": API_ERROR_MSG}

# Function to get the status of an existing service request
def get_service_request_status(request_id):
    """
    Retrieves the status of an existing service request.
    
    :param request_id: str - The ID of the service request.
    :return: dict - The status of the service request.
    """
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(f"{API_BASE_URL}/service-requests/{request_id}", headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:  # HTTP 200 OK
            return response.json()
        else:
            # Log error details
            print(f"{API_ERROR_MSG}: {response.status_code}, {response.text}")
            response.raise_for_status()

    except requests.ConnectionError:
        print(CONNECTION_ERROR_MSG)
        return {"error": CONNECTION_ERROR_MSG}
    except requests.RequestException as e:
        print(f"{API_ERROR_MSG}: {str(e)}")
        return {"error": API_ERROR_MSG}

# Function to cancel an existing service request
def cancel_service_request(request_id):
    """
    Cancels an existing service request for water leakage detection.
    
    :param request_id: str - The ID of the service request to cancel.
    :return: dict - The result of the cancellation.
    """
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.delete(f"{API_BASE_URL}/service-requests/{request_id}", headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:  # HTTP 200 OK
            return response.json()
        else:
            # Log error details
            print(f"{API_ERROR_MSG}: {response.status_code}, {response.text}")
            response.raise_for_status()

    except requests.ConnectionError:
        print(CONNECTION_ERROR_MSG)
        return {"error": CONNECTION_ERROR_MSG}
    except requests.RequestException as e:
        print(f"{API_ERROR_MSG}: {str(e)}")
        return {"error": API_ERROR_MSG}

# Example usage of the script (can be removed in production)
if __name__ == "__main__":
    print("Creating a new service request...")
    result = create_service_request(
        address="123 Main Street, Water City",
        customer_name="John Doe",
        contact_number="123456789",
        description="Severe water leakage detected in the basement."
    )
    print("Create Service Request Result:", result)

    if "id" in result:
        request_id = result["id"]
        print("\nFetching service request status...")
        status = get_service_request_status(request_id)
        print("Service Request Status:", status)

        print("\nCanceling service request...")
        cancel_result = cancel_service_request(request_id)
        print("Cancel Service Request Result:", cancel_result)
```
