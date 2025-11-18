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
from linode_api4.objects import KubernetesCluster, LKEClusterPool

# Configuration
API_TOKEN = "your_linode_api_token"  # Replace with your Linode API token
CLUSTER_NAME = "my-k8s-cluster"      # Name of the Kubernetes cluster
NODE_TYPE = "g6-standard-2"          # Node type (e.g., g6-standard-2 for 2GB RAM)
NODE_COUNT = 3                       # Number of nodes in the cluster
REGION = "us-east"                   # Region to deploy the cluster (e.g., us-east)

def create_kubernetes_cluster(api_token, cluster_name, region, node_type, node_count):
    """
    Creates a Kubernetes cluster on Linode with the specified configuration.

    :param api_token: Linode API token (string)
    :param cluster_name: Name for the Kubernetes cluster (string)
    :param region: Region to deploy the cluster (string)
    :param node_type: Type of nodes to use in the cluster (string)
    :param node_count: Number of nodes in the cluster (integer)
    """
    try:
        # Initialize the Linode API client
        client = linode_api4.LinodeClient(api_token)

        # Create the Kubernetes cluster
        cluster = client.linode.kubernetes_clusters.create(
            label=cluster_name,
            region=region,
            pools=[LKEClusterPool(type=node_type, count=node_count)],
        )

        print(f"Cluster '{cluster_name}' created successfully!")
        print(f"Cluster ID: {cluster.id}")
        print(f"API Endpoint: {cluster.api_endpoint}")
        return cluster

    except linode_api4.errors.ApiError as e:
        print(f"Linode API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main script execution
if __name__ == "__main__":
    cluster = create_kubernetes_cluster(API_TOKEN, CLUSTER_NAME, REGION, NODE_TYPE, NODE_COUNT)
    if cluster:
        print("Cluster configuration completed successfully.")
    else:
        print("Failed to create the Kubernetes cluster.")
```
