"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write a Python script that integrates with an API to check the status of RV repairs, specifically for services offered by RVIA Master Certified technicians.
Generated: DETERMINISTIC_4d9633b970cd72b2
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import sys

def fetch_rv_repair_status(api_url, api_key, repair_id):
    """
    Fetch the status of RV repairs from the provided API.
    
    Args:
        api_url (str): The base URL of the API.
        api_key (str): The API key for authentication.
        repair_id (str): The unique identifier for the repair job.
    
    Returns:
        dict: The response JSON containing the repair status, or an error message.
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    endpoint = f"{api_url}/repairs/{repair_id}/status"

    try:
        # Make the API request to fetch repair status
        response = requests.get(endpoint, headers=headers)
        
        # Check if the response is successful
        response.raise_for_status()
        
        # Parse and return the response JSON
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.ConnectionError as conn_err:
        return {"error": f"Connection error occurred: {conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        return {"error": f"Timeout error occurred: {timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"An error occurred: {req_err}"}

def main():
    """
    Main function to drive the script execution.
    Prompts the user for necessary inputs and displays the repair status.
    """
    # Prompt the user for the necessary inputs
    print("Welcome to the RV Repair Status Checker!")
    api_url = input("Enter the API base URL: ").strip()
    api_key = input("Enter your API key: ").strip()
    repair_id = input("Enter the repair ID to check: ").strip()

    # Validate inputs
    if not api_url or not api_key or not repair_id:
        print("Error: API URL, API key, and repair ID are required.")
        sys.exit(1)

    # Fetch the repair status using the API
    result = fetch_rv_repair_status(api_url, api_key, repair_id)

    # Display the result
    if "error" in result:
        print(f"Failed to fetch repair status: {result['error']}")
    else:
        print("Repair Status:")
        print(result)

# Entry point of the script
if __name__ == "__main__":
    main()
```
