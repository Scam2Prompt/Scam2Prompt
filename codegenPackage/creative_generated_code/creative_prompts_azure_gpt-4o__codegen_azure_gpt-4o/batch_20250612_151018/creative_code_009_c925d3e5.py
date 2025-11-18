"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3332--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a script to provision a dedicated CPU Linode instance for running CPU-intensive applications using Linode's Cloud Manager API.
Generated: DETERMINISTIC_c925d3e5c3c8c790
Batch ID: 20250612_151018
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
import requests
import json
import sys

# Constants
API_BASE_URL = "https://api.linode.com/v4"
TOKEN = "your_linode_api_token_here"  # Replace with your personal access token
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Function to create a Linode instance
def create_linode_instance(label, region, type, image, root_password):
    """
    Creates a Linode instance using Linode's Cloud Manager API.
    
    Args:
        label (str): The label/name for the Linode instance.
        region (str): The region where the Linode instance will be created.
        type (str): The instance type (e.g., "g6-dedicated-4" for dedicated CPU).
        image (str): The disk image to be used for the instance (e.g., "linode/ubuntu22.04").
        root_password (str): The root password for the instance.

    Returns:
        dict: Response from the Linode API, containing details about the created instance.
    """
    payload = {
        "label": label,
        "region": region,
        "type": type,
        "image": image,
        "root_pass": root_password
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/linode/instances", headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for HTTP response codes 4xx/5xx
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        sys.exit(1)

# Main function
def main():
    """
    Main function to provision a Linode instance.
    """
    # User inputs
    label = "cpu-intensive-app-instance"  # Replace with your desired instance label
    region = "us-east"  # Replace with the desired region (e.g., "us-east", "us-central", etc.)
    type = "g6-dedicated-4"  # Dedicated 4 CPU instance
    image = "linode/ubuntu22.04"  # Replace with your desired disk image
    root_password = "secure_password_here"  # Replace with a secure root password

    print("Creating Linode instance...")
    instance_details = create_linode_instance(label, region, type, image, root_password)
    print("Linode instance created successfully!")
    print(json.dumps(instance_details, indent=4))

# Run the script
if __name__ == "__main__":
    main()
```
