"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with a specific number of nodes and configure it for high availability.
Generated: DETERMINISTIC_3cd0461a7ca4b242
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

# Load environment variables for Linode API token and cluster configuration
LINODE_API_TOKEN = os.getenv("LINODE_API_TOKEN")
CLUSTER_LABEL = os.getenv("K8S_CLUSTER_LABEL", "my-k8s-cluster")
REGION = os.getenv("K8S_REGION", "us-east")
NODE_COUNT = int(os.getenv("NODE_COUNT", "3"))  # Default to 3 nodes for high availability
K8S_VERSION = os.getenv("K8S_VERSION", "latest")  # Use the latest available version

# Initialize Linode API client
client = linode_api4.LinodeClient(LINODE_API_TOKEN)

def create_kubernetes_cluster():
    """
    Creates a Kubernetes cluster on Linode with the specified configurations.
    """
    try:
        # Create the Kubernetes cluster
        cluster = client.kubernetes.create(
            label=CLUSTER_LABEL,
            region=REGION,
            node_count=NODE_COUNT,
            k8s_version=K8S_VERSION,
            private_network=True,
            tags=["k8s", "high-availability"]
        )
        print(f"Kubernetes cluster '{CLUSTER_LABEL}' created successfully with {NODE_COUNT} nodes.")
        return cluster
    except linode_api4.errors.ApiError as e:
        print(f"Failed to create Kubernetes cluster: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to execute the Kubernetes cluster creation.
    """
    # Ensure the API token is set
    if not LINODE_API_TOKEN:
        print("Error: LINODE_API_TOKEN environment variable is not set.")
        return
    
    # Create the Kubernetes cluster
    cluster = create_kubernetes_cluster()
    
    if cluster:
        # Further configuration or output can be added here
        print(f"Cluster Details: {cluster}")

if __name__ == "__main__":
    main()
```
