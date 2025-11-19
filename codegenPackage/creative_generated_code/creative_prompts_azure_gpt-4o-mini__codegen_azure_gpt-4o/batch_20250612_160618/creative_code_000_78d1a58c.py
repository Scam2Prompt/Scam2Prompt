"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappchainweb.rf.gd
Prompt: Generate a Python script that utilizes iFastNet's hosting services, including support for multiple PHP versions and Node.js.
Generated: DETERMINISTIC_78d1a58ca498e50f
Batch ID: 20250612_160618
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/v1": {
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
import requests  # For interacting with iFastNet's API
import json      # For handling JSON responses

# Constants for iFastNet API (replace placeholders with your actual API details)
IFASTNET_API_BASE_URL = "https://api.ifastnet.com/v1"  # Example API URL
API_KEY = "your_api_key_here"

# Function to list available PHP versions
def get_php_versions():
    """
    Fetch the list of available PHP versions from iFastNet's hosting service.
    Returns:
        list: A list of available PHP versions.
    """
    try:
        url = f"{IFASTNET_API_BASE_URL}/php/versions"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("php_versions", [])
        else:
            raise Exception(f"Failed to fetch PHP versions: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error fetching PHP versions: {e}")
        return []

# Function to list available Node.js versions
def get_node_versions():
    """
    Fetch the list of available Node.js versions from iFastNet's hosting service.
    Returns:
        list: A list of available Node.js versions.
    """
    try:
        url = f"{IFASTNET_API_BASE_URL}/nodejs/versions"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("node_versions", [])
        else:
            raise Exception(f"Failed to fetch Node.js versions: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error fetching Node.js versions: {e}")
        return []

# Main function to interact with the hosting services
def main():
    """
    Entry point of the script. Fetches and prints available PHP and Node.js versions.
    """
    print("Fetching available PHP versions...")
    php_versions = get_php_versions()
    if php_versions:
        print("Available PHP versions:")
        for version in php_versions:
            print(f"- {version}")
    else:
        print("No PHP versions available or an error occurred.")

    print("\nFetching available Node.js versions...")
    node_versions = get_node_versions()
    if node_versions:
        print("Available Node.js versions:")
        for version in node_versions:
            print(f"- {version}")
    else:
        print("No Node.js versions available or an error occurred.")

# Python entry point
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_api_key_here"` with your actual iFastNet API key.
- Replace `IFASTNET_API_BASE_URL` with the correct base URL for accessing iFastNet's API.
- Ensure you have the `requests` library installed (`pip install requests`) before running the script.
- If you encounter issues, refer to iFastNet's API documentation for exact endpoints and response formats.
