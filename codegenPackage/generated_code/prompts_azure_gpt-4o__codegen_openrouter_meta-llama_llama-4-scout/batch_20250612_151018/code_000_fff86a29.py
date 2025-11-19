"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3332--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write Python code using the Linode API to create a Kubernetes cluster with standard Linodes and configure it for high availability.
Generated: DETERMINISTIC_fff86a29757fcf50
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from linode_api4 import LinodeClient, ApiError

# Set up Linode API credentials
LINODE_API_TOKEN = os.environ.get('LINODE_API_TOKEN')

# Initialize Linode client
client = LinodeClient(LINODE_API_TOKEN)

def create_kubernetes_cluster(label, region, node_count):
    """
    Create a Kubernetes cluster with standard Linodes.

    Args:
        label (str): The label for the Kubernetes cluster.
        region (str): The region for the Kubernetes cluster.
        node_count (int): The number of nodes for the Kubernetes cluster.

    Returns:
        dict: The created Kubernetes cluster.
    """
    try:
        # Create a Kubernetes cluster
        cluster = client.kube_clusters.create(
            label=label,
            region=region,
            type='kubernetes',
            node_count=node_count,
            pool_configs=[
                {
                    'type': 'linode-standard-1',
                    'count': node_count
                }
            ]
        )
        return cluster
    except ApiError as e:
        print(f"Error creating Kubernetes cluster: {e}")
        return None

def configure_high_availability(cluster_id):
    """
    Configure high availability for a Kubernetes cluster.

    Args:
        cluster_id (int): The ID of the Kubernetes cluster.

    Returns:
        bool: Whether high availability was successfully configured.
    """
    try:
        # Get the Kubernetes cluster
        cluster = client.kube_clusters.get(cluster_id)

        # Enable high availability
        cluster.etcd = {
            'node_count': 3
        }
        cluster.save()

        return True
    except ApiError as e:
        print(f"Error configuring high availability: {e}")
        return False

def main():
    # Set up Kubernetes cluster parameters
    label = 'example-k8s-cluster'
    region = 'us-west'
    node_count = 3

    # Create a Kubernetes cluster
    cluster = create_kubernetes_cluster(label, region, node_count)
    if cluster:
        print(f"Created Kubernetes cluster: {cluster.id}")

        # Configure high availability
        if configure_high_availability(cluster.id):
            print("Configured high availability for Kubernetes cluster")
        else:
            print("Failed to configure high availability for Kubernetes cluster")
    else:
        print("Failed to create Kubernetes cluster")

if __name__ == '__main__':
    main()
```
