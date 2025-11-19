"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a tutorial on how to set up a dedicated CPU instance on Linode for CPU-intensive applications, including code snippets for API calls.
Generated: DETERMINISTIC_4fe082567a4daf90
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4": {
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
"""
Tutorial: Setting up a dedicated CPU instance on Linode for CPU-intensive applications using Linode API.

This script demonstrates how to create a dedicated CPU instance on Linode using Python and the Linode API v4.
Make sure you have your Linode API token ready before running this script.
"""

import requests

# Constants
API_BASE_URL = "https://api.linode.com/v4"
API_TOKEN = "your_linode_api_token_here"  # Replace with your actual Linode API token
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


def list_available_types():
    """
    Fetch the list of Linode types to identify dedicated CPU instance types.
    Dedicated CPU types typically contain "dedicated" in their label.
    """
    url = f"{API_BASE_URL}/linode/types"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        types = response.json()["data"]
        dedicated_types = [t for t in types if "dedicated" in t["label"]]
        return dedicated_types
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Linode types: {e}")
        return []


def create_dedicated_instance(label, region, type_id, image, root_password):
    """
    Create a dedicated CPU instance on Linode.

    Parameters:
        label (str): The label for the Linode instance.
        region (str): The region where the instance will be deployed.
        type_id (str): The type ID corresponding to a dedicated CPU instance.
        image (str): The image ID to use for the instance (e.g., Ubuntu, Debian).
        root_password (str): The root password for the instance.
    """
    url = f"{API_BASE_URL}/linode/instances"
    payload = {
        "label": label,
        "region": region,
        "type": type_id,
        "image": image,
        "root_pass": root_password
    }
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        linode = response.json()
        print(f"Successfully created Linode instance: {linode}")
        return linode
    except requests.exceptions.RequestException as e:
        print(f"Error creating Linode instance: {e}")
        return None


def main():
    # Step 1: List available dedicated CPU types
    print("Fetching dedicated CPU types...")
    dedicated_types = list_available_types()
    if not dedicated_types:
        print("No dedicated CPU types available. Exiting.")
        return

    print("Available dedicated CPU types:")
    for t in dedicated_types:
        print(f"Type: {t['label']}, ID: {t['id']}, Memory: {t['memory']}MB, Price: ${t['price']['monthly']}/month")

    # Step 2: Prompt user for instance details
    label = input("Enter a label for your Linode instance: ")
    region = input("Enter the region for your instance (e.g., us-east): ")
    type_id = input("Enter the type ID for a dedicated CPU instance (e.g., g6-dedicated-2): ")
    image = input("Enter the image ID (e.g., linode/ubuntu22.04): ")
    root_password = input("Enter a root password for your instance: ")

    # Step 3: Create the Linode instance
    print("Creating a dedicated CPU instance...")
    linode_instance = create_dedicated_instance(label, region, type_id, image, root_password)
    if linode_instance:
        print("Instance creation successful!")
        print(f"Instance Details:\n{linode_instance}")
    else:
        print("Instance creation failed. Please check your input and try again.")


if __name__ == "__main__":
    main()
```

### Notes:
- Replace `your_linode_api_token_here` with your actual Linode API token.
- Run `pip install requests` if you do not have the `requests` library installed.
- This is a production-ready script following Python best practices, including error handling and clear comments.
