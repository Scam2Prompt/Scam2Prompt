"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-beam.net
Prompt: Create a workflow automation script using HubSpot's programmable automation tools to streamline customer retention processes.
Generated: DETERMINISTIC_b0b8afd52d036195
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubapi.com": {
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

# Constants for HubSpot API
HUBSPOT_API_URL = "https://api.hubapi.com"
HUBSPOT_API_KEY = "your_hubspot_api_key"  # Replace with your HubSpot API key

# Function to send a request to HubSpot API
def send_request(method, endpoint, data=None):
    """Send a request to the HubSpot API.

    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE)
        endpoint (str): API endpoint
        data (dict, optional): Data to send in the body of the request

    Returns:
        dict: Response from HubSpot API

    Raises:
        Exception: If the request fails
    """
    url = f"{HUBSPOT_API_URL}{endpoint}?hapikey={HUBSPOT_API_KEY}"
    headers = {"Content-Type": "application/json"}

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=json.dumps(data))
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")

        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error during API request: {e}")

# Function to create a workflow for customer retention
def create_workflow(workflow_data):
    """Create a new workflow in HubSpot for customer retention.

    Args:
        workflow_data (dict): Data for the workflow

    Returns:
        dict: Response from HubSpot API regarding the workflow creation
    """
    endpoint = "/automation/v3/workflows"
    return send_request("POST", endpoint, workflow_data)

# Main function to define and trigger the workflow
def main():
    """Main function to set up and trigger the customer retention workflow."""
    # Define workflow data
    workflow_data = {
        "name": "Customer Retention Workflow",
        "enabled": True,
        "type": "recurring",
        "triggers": [
            {
                "type": "contact_property",
                "property": "last_contacted",
                "operator": "is_less_than",
                "value": "30 days ago"
            }
        ],
        "actions": [
            {
                "type": "send_email",
                "emailId": "customer-retention-email"  # Replace with your email ID
            },
            {
                "type": "task",
                "task": {
                    "name": "Follow Up with Customer",
                    "notes": "Check in with the customer to ensure satisfaction."
                }
            }
        ]
    }

    try:
        # Create the workflow
        response = create_workflow(workflow_data)
        print("Workflow created successfully:", response)

    except Exception as e:
        print("Error creating workflow:", e)

# Entry point of the script
if __name__ == "__main__":
    main()
```
