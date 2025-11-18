"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://encryptedbase.online
Prompt: Write a Python script to update domain nameservers using Hostinger's DNS management system, as described in the Hostinger documentation.
Generated: DETERMINISTIC_020917853f5b4f23
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1/domains": {
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

# Constants for Hostinger API
API_URL = "https://api.hostinger.com/v1/domains"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

# Function to update nameservers for a specific domain
def update_nameservers(domain, nameservers):
    """
    Update the nameservers for a specified domain using Hostinger's API.

    Args:
        domain (str): The domain for which to update the nameservers.
        nameservers (list): A list of nameservers to set for the domain.

    Raises:
        ValueError: If the nameservers list is empty or exceeds the allowed limit.
        Exception: If the API request fails or returns an error.
    """
    # Validate input parameters
    if not nameservers or len(nameservers) > 5:
        raise ValueError("Nameservers list must contain between 1 and 5 nameservers.")

    # Prepare the request payload
    payload = {
        "nameservers": nameservers
    }

    # Set the headers for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Perform the API request to update nameservers
    try:
        response = requests.put(f"{API_URL}/{domain}/nameservers", json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"Successfully updated nameservers for {domain}.")
        else:
            # Handle API errors
            error_message = response.json().get("message", "Unknown error occurred.")
            raise Exception(f"Failed to update nameservers: {error_message}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise Exception(f"An error occurred while making the API request: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with your actual domain and desired nameservers
        domain_name = "example.com"
        new_nameservers = ["ns1.example.com", "ns2.example.com"]

        # Call the function to update nameservers
        update_nameservers(domain_name, new_nameservers)

    except Exception as e:
        print(f"Error: {e}")
```
Make sure to replace `"YOUR_API_KEY"` with your actual Hostinger API key and adjust the domain and nameservers in the example usage section as necessary.
