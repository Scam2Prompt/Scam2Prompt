"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with specific node configurations, as described in the Linode documentation.
Generated: DETERMINISTIC_91126ed3ea60947a
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
API_URL = "https://api.linode.com/v4"
API_TOKEN = "YOUR_LINODE_API_TOKEN"  # Replace with your Linode API token

# Node configuration
NODE_POOL = [
    {
        "type": "g6-standard-2",  # Linode instance type (e.g., 2GB RAM, 1 CPU)
        "count": 3,               # Number of nodes of this type
    },
    {
        "type": "g6-standard-4",  # Linode instance type (e.g., 4GB RAM, 2 CPU)
        "count": 2,               # Number of nodes of this type
    },
]

CLUSTER_REGION = "us-east"         # Replace with your preferred Linode region
CLUSTER_LABEL = "my-k8s-cluster"  # Replace with your desired cluster name

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

def create_kubernetes_cluster():
    """
    Creates a Linode Kubernetes cluster using the Linode API.
    """
    try:
        # Prepare the request payload
        payload = {
            "label": CLUSTER_LABEL,
            "region": CLUSTER_REGION,
            "node_pools": NODE_POOL,
        }

        # Make the API request
        response = requests.post(
            f"{API_URL}/lke/clusters",
            headers=HEADERS,
            data=json.dumps(payload),
        )

        # Check response status
        if response.status_code == 201:
            cluster = response.json()
            print(f"Cluster created successfully! Cluster ID: {cluster['id']}")
            print(f"Cluster details: {json.dumps(cluster, indent=2)}")
        else:
            print(f"Failed to create cluster: {response.status_code}")
            print(response.text)
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Validate API token
    if not API_TOKEN or API_TOKEN == "YOUR_LINODE_API_TOKEN":
        print("Error: Please set a valid Linode API token.")
        sys.exit(1)

    # Create the Kubernetes cluster
    create_kubernetes_cluster()
```

### Notes:
1. Replace `YOUR_LINODE_API_TOKEN` with your actual Linode API token.
2. Modify `NODE_POOL`, `CLUSTER_REGION`, and `CLUSTER_LABEL` as per your requirements.
3. This script assumes you have a Linode account and the Kubernetes service enabled in your account.
4. Run the script in a secure environment to avoid exposing your API token.
