"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with a specified number of nodes and configure NodeBalancers for load balancing.
Generated: DETERMINISTIC_ccb8719257e2aa55
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
from linode_api4 import LinodeClient, NodeBalancer, Instance, Region

# Load the Linode API token from environment variable
API_TOKEN = os.getenv('LINODE_API_TOKEN')
if not API_TOKEN:
    raise ValueError("Please set the LINODE_API_TOKEN environment variable.")

# Initialize the Linode API client
client = LinodeClient(API_TOKEN)

def create_kubernetes_cluster(cluster_name, region, node_count, node_type):
    """
    Create a Kubernetes cluster with the specified parameters.

    :param cluster_name: Name of the Kubernetes cluster
    :param region: Region to create the cluster in
    :param node_count: Number of nodes in the cluster
    :param node_type: Type of node (e.g., 'g6-standard-1')
    :return: The created Kubernetes cluster object
    """
    try:
        # Create the Kubernetes cluster
        cluster = client.kubernetes.create(
            label=cluster_name,
            region=region,
            node_count=node_count,
            node_type=node_type
        )
        print(f"Kubernetes cluster '{cluster_name}' created successfully.")
        return cluster
    except Exception as e:
        print(f"Error creating Kubernetes cluster: {e}")
        raise

def create_node_balancer(node_balancer_label, region):
    """
    Create a NodeBalancer for load balancing.

    :param node_balancer_label: Label for the NodeBalancer
    :param region: Region to create the NodeBalancer in
    :return: The created NodeBalancer object
    """
    try:
        # Create the NodeBalancer
        node_balancer = client.nodebalancers.create(
            label=node_balancer_label,
            region=region
        )
        print(f"NodeBalancer '{node_balancer_label}' created successfully.")
        return node_balancer
    except Exception as e:
        print(f"Error creating NodeBalancer: {e}")
        raise

def main():
    # Configuration parameters
    cluster_name = "my-k8s-cluster"
    node_balancer_label = "my-node-balancer"
    region = "us-east"  # Example region
    node_count = 3
    node_type = "g6-standard-1"  # Example node type

    # Create Kubernetes cluster
    cluster = create_kubernetes_cluster(cluster_name, region, node_count, node_type)

    # Create NodeBalancer
    node_balancer = create_node_balancer(node_balancer_label, region)

if __name__ == "__main__":
    main()
```

Make sure to set the `LINODE_API_TOKEN` environment variable with your Linode API token before running the script.
