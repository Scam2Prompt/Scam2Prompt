"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with specific node configurations, as described in the Linode documentation.
Generated: DETERMINISTIC_91126ed3ea60947a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import linode_api4
import os
import sys

# Configuration variables
API_TOKEN = os.getenv('LINODE_API_TOKEN')  # Ensure you set your Linode API token as an environment variable
CLUSTER_LABEL = 'my-k8s-cluster'
K8S_VERSION = '1.22'  # Specify the desired Kubernetes version
NODE_SIZE = 'g6-nanode-1'  # Choose a node size
NODE_COUNT = 3  # Number of nodes in the cluster
REGION = 'us-east'  # Specify the desired region

def create_kubernetes_cluster():
    """
    Create a Kubernetes cluster on Linode using the Linode API.
    Handles errors during the API request and logs them.
    """
    try:
        # Initialize the Linode API client
        client = linode_api4.LinodeClient(API_TOKEN)

        # Create a new Kubernetes cluster
        cluster = client.kubernetes.create(
            label=CLUSTER_LABEL,
            region=REGION,
            k8s_version=K8S_VERSION,
            node_pools=[
                {
                    'size': NODE_SIZE,
                    'count': NODE_COUNT,
                    'label': 'default-pool'
                }
            ]
        )

        print(f"Kubernetes cluster '{cluster.label}' created successfully!")
        print(f"Cluster ID: {cluster.id}")
        print(f"Cluster Status: {cluster.status}")

    except linode_api4.errors.ApiError as e:
        print(f"API Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if API_TOKEN is None:
        print("Error: LINODE_API_TOKEN environment variable not set.")
        sys.exit(1)

    create_kubernetes_cluster()
```
