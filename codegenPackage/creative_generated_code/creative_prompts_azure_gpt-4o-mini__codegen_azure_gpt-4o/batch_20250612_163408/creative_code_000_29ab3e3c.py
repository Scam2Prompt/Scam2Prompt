"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a Python script that uses the Linode API to create a new Kubernetes cluster with specific configurations.
Generated: DETERMINISTIC_29ab3e3cd25b85c9
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
import requests

# Constants for Linode API
API_BASE_URL = "https://api.linode.com/v4"
API_TOKEN = "your_personal_access_token_here"  # Replace with your Linode API token
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Configuration for the Kubernetes Cluster
CLUSTER_NAME = "my-k8s-cluster"
REGION = "us-east"  # Replace with your desired region
NODE_TYPE = "g6-standard-2"  # Replace with your desired Linode type
NODE_COUNT = 3  # Number of nodes in the cluster

def create_kubernetes_cluster():
    """
    Creates a new Kubernetes cluster using the Linode API.
    """
    # Define the payload with the cluster configuration
    payload = {
        "label": CLUSTER_NAME,
        "region": REGION,
        "node_pools": [
            {
                "type": NODE_TYPE,
                "count": NODE_COUNT
            }
        ]
    }

    try:
        # Send POST request to create the cluster
        response = requests.post(
            f"{API_BASE_URL}/lke/clusters",
            headers=HEADERS,
            json=payload
        )

        # Check if the request was successful
        if response.status_code == 200 or response.status_code == 201:
            cluster_data = response.json()
            print(f"Kubernetes cluster '{CLUSTER_NAME}' created successfully!")
            print(f"Cluster ID: {cluster_data['id']}")
            print(f"Cluster Status: {cluster_data['status']}")
        else:
            print(f"Failed to create cluster. Status Code: {response.status_code}")
            print(f"Error: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the Linode API: {e}")

if __name__ == "__main__":
    # Ensure the script runs only when executed directly
    create_kubernetes_cluster()
```
