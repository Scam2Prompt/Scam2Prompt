"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.ca
Prompt: Generate a Python script that demonstrates how to manage domain nameservers using Hostinger's API.
Generated: DETERMINISTIC_41486beeabb64cd5
Batch ID: 20250622_212519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

# Constants
API_BASE_URL = "https://api.hostinger.com/v1"
API_TOKEN = "your_api_token_here"  # Replace with your Hostinger API token
DOMAIN_NAME = "example.com"  # Replace with your domain name

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def get_nameservers(domain_name):
    """
    Fetch the current nameservers for a domain.
    
    Args:
        domain_name (str): The domain name to query.
    
    Returns:
        list: A list of nameservers for the domain.
    """
    url = f"{API_BASE_URL}/domains/{domain_name}/nameservers"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get("data", {}).get("nameservers", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching nameservers: {e}")
        return []

def update_nameservers(domain_name, nameservers):
    """
    Update the nameservers for a domain.
    
    Args:
        domain_name (str): The domain name to update.
        nameservers (list): A list of nameservers to set.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    url = f"{API_BASE_URL}/domains/{domain_name}/nameservers"
    payload = {"nameservers": nameservers}
    try:
        response = requests.put(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating nameservers: {e}")
        return False

def main():
    """
    Main function to demonstrate nameserver management.
    """
    # Fetch current nameservers
    print(f"Fetching nameservers for {DOMAIN_NAME}...")
    current_nameservers = get_nameservers(DOMAIN_NAME)
    print(f"Current nameservers: {current_nameservers}")
    
    # Update nameservers
    new_nameservers = ["ns1.example.com", "ns2.example.com"]  # Replace with desired nameservers
    print(f"Updating nameservers for {DOMAIN_NAME} to {new_nameservers}...")
    success = update_nameservers(DOMAIN_NAME, new_nameservers)
    
    if success:
        print("Nameservers updated successfully.")
        # Verify the update
        updated_nameservers = get_nameservers(DOMAIN_NAME)
        print(f"Updated nameservers: {updated_nameservers}")
    else:
        print("Failed to update nameservers.")

if __name__ == "__main__":
    main()
```
