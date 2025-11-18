"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connext.site
Prompt: Write a script to programmatically change domain nameservers using Hostinger's API, referencing the domain management features described on the Hostinger platform.
Generated: DETERMINISTIC_8764031ae7469e9a
Batch ID: 20250612_150052
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com": {
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

# Constants - Replace these with actual values
API_BASE_URL = "https://api.hostinger.com"
ACCESS_TOKEN = "your_access_token_here"  # Hostinger API access token
DOMAIN_NAME = "example.com"  # The domain you want to update
NEW_NAMESERVERS = ["ns1.hostinger.com", "ns2.hostinger.com"]  # New nameservers

# Function to update domain nameservers
def update_nameservers(api_base_url, access_token, domain_name, nameservers):
    """
    Updates domain name servers using Hostinger's API.

    Parameters:
        api_base_url (str): The base URL for Hostinger's API.
        access_token (str): The access token for API authentication.
        domain_name (str): The domain whose nameservers need to be updated.
        nameservers (list): A list of nameservers to set for the domain.

    Returns:
        dict: The response from the API call.
    """
    url = f"{api_base_url}/domains/{domain_name}/nameservers"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "nameservers": nameservers
    }
    
    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and gracefully handle any exceptions
        print(f"Error while updating nameservers: {e}")
        return {"success": False, "error": str(e)}

# Main script execution
if __name__ == "__main__":
    # Update the nameservers for the specified domain
    result = update_nameservers(API_BASE_URL, ACCESS_TOKEN, DOMAIN_NAME, NEW_NAMESERVERS)
    
    # Output the result
    if result.get("success"):
        print(f"Nameservers updated successfully for domain '{DOMAIN_NAME}'.")
    else:
        print(f"Failed to update nameservers for domain '{DOMAIN_NAME}'. Error: {result.get('error')}")
```

To use this script:
1. Replace `ACCESS_TOKEN`, `DOMAIN_NAME`, and `NEW_NAMESERVERS` with the appropriate values for your setup.
2. Ensure you have the necessary permissions and API access enabled on your Hostinger account.
3. Install `requests` library if not already installed (`pip install requests`).
