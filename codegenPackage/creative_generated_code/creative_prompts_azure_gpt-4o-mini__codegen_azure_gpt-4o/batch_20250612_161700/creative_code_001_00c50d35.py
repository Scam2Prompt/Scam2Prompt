"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoastalroofing.com
Prompt: Write a Python script that integrates with an API to manage roofing project requests for Coastal Roofing & Waterproofing's services.
Generated: DETERMINISTIC_00c50d35a89d9624
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coastalroofing.com": {
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
from datetime import datetime

# Constants for API integration
API_BASE_URL = "https://api.coastalroofing.com"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key
TIMEOUT = 10  # Timeout for API requests in seconds

# Function to handle API requests with proper error handling
def api_request(endpoint, method="GET", data=None):
    """
    Handles API requests to the Coastal Roofing & Waterproofing service.
    
    Args:
        endpoint (str): The API endpoint to call.
        method (str): HTTP method (GET, POST, etc.). Defaults to "GET".
        data (dict): Payload for POST/PUT requests. Defaults to None.
    
    Returns:
        dict: Parsed JSON response from the API.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the API request
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data, timeout=TIMEOUT)
        else:
            raise ValueError("Unsupported HTTP method.")
        
        # Check if the response status code indicates success
        response.raise_for_status()
        
        # Parse and return the JSON response
        return response.json()
    except requests.RequestException as e:
        # Handle communication errors
        print(f"Error communicating with API: {e}")
        return {"error": str(e)}
    except ValueError as ve:
        # Handle JSON parsing or other value-related errors
        print(f"Value error: {ve}")
        return {"error": str(ve)}

# Function to create a new roofing project request
def create_project_request(customer_name, address, project_type, description):
    """
    Creates a new roofing project request.
    
    Args:
        customer_name (str): The name of the customer.
        address (str): Address of the project location.
        project_type (str): Type of roofing project (e.g., "residential", "commercial").
        description (str): Detailed description of the project.
    
    Returns:
        dict: Response from the API.
    """
    payload = {
        "customer_name": customer_name,
        "address": address,
        "project_type": project_type,
        "description": description,
        "request_date": datetime.now().isoformat()
    }
    return api_request(endpoint="project-requests", method="POST", data=payload)

# Function to retrieve all project requests
def get_all_project_requests():
    """
    Retrieves all roofing project requests.
    
    Returns:
        dict: Response from the API containing the list of project requests.
    """
    return api_request(endpoint="project-requests", method="GET")

# Main script functionality
if __name__ == "__main__":
    # Example usage of the script
    
    # Create a new project request
    new_request_response = create_project_request(
        customer_name="John Doe",
        address="123 Coastal Lane, Miami, FL",
        project_type="residential",
        description="Urgent roof repair needed after storm damage."
    )
    print("New Project Request Response:")
    print(json.dumps(new_request_response, indent=4))
    
    # Get all project requests
    all_requests_response = get_all_project_requests()
    print("\nAll Project Requests:")
    print(json.dumps(all_requests_response, indent=4))
```

Make sure to replace `API_BASE_URL` and `API_KEY` with the actual values provided by Coastal Roofing & Waterproofing's API documentation.
