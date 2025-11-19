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
import linode_api4
from linode_api4 import LinodeClient, Cluster, NodeBalancer, Instance

# Load environment variables for Linode API token
LINODE_API_TOKEN = os.getenv('LINODE_API_TOKEN')

# Initialize the Linode API client
client = LinodeClient(LINODE_API_TOKEN)

def create_kubernetes_cluster(cluster_name, region, node_count, node_type):
    """
    Create a Kubernetes cluster on Linode with specified parameters.

    :param cluster_name: Name of the Kubernetes cluster
    :param region: Region to deploy the cluster
    :param node_count: Number of nodes in the cluster
    :param node_type: Type of Linode instance to use for nodes
    :return: The created Kubernetes cluster object
    """
    try:
        # Create the Kubernetes cluster
        cluster = client.kubernetes.create(
            label=cluster_name,
            region=region,
            node_count=node_count,
            node_type=node_type,
            private_networking=True,
            tags=['high-availability']
        )
        print(f"Kubernetes cluster '{cluster_name}' created successfully.")
        return cluster
    except Exception as e:
        print(f"Error creating Kubernetes cluster: {e}")
        return None

def main():
    # Define parameters for the Kubernetes cluster
    cluster_name = "my-high-availability-cluster"
    region = "us-east"  # Choose a region that supports Kubernetes
    node_count = 3      # Number of nodes for high availability
    node_type = "g6-standard-2"  # Choose a suitable Linode instance type

    # Create the Kubernetes cluster
    cluster = create_kubernetes_cluster(cluster_name, region, node_count, node_type)

    if cluster:
        print(f"Cluster ID: {cluster.id}")
        print(f"Cluster Status: {cluster.status}")

if __name__ == "__main__":
    main()
```

Make sure to set the `LINODE_API_TOKEN` environment variable with your Linode API token before running the code.
