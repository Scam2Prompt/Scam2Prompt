"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: How can I use the Linode API to manage my Kubernetes cluster effectively?
Generated: DETERMINISTIC_79222e71892ccb87
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates how to use the Linode API to effectively manage a Kubernetes cluster. The example assumes you are using the Linode Python SDK (`linode_api4`) for interacting with the Linode API. It includes creating a Kubernetes cluster, listing existing clusters, and deleting a cluster.

```python
import os
from linode_api4 import LinodeClient, ApiError

# Load Linode API token from environment variable for security
API_TOKEN = os.getenv("LINODE_API_TOKEN")

if not API_TOKEN:
    raise ValueError("LINODE_API_TOKEN environment variable is not set")

# Initialize Linode API client
client = LinodeClient(API_TOKEN)

def create_kubernetes_cluster(label, region, node_type, node_count):
    """
    Create a Kubernetes cluster on Linode.
    
    :param label: The label for the Kubernetes cluster.
    :param region: The region to deploy the cluster.
    :param node_type: The Linode type for the nodes (e.g., "g6-standard-2").
    :param node_count: Number of nodes in the cluster.
    :return: Cluster object if created successfully.
    """
    try:
        cluster = client.create_lke_cluster(
            label=label,
            region=region,
            node_pools=[{
                "type": node_type,
                "count": node_count
            }]
        )
        print(f"Kubernetes cluster '{label}' created successfully.")
        return cluster
    except ApiError as e:
        print(f"Failed to create Kubernetes cluster: {e}")
        return None

def list_kubernetes_clusters():
    """
    List all Kubernetes clusters on Linode account.
    
    :return: List of Kubernetes clusters.
    """
    try:
        clusters = client.lke_clusters()
        print("Kubernetes clusters:")
        for cluster in clusters:
            print(f"ID: {cluster.id}, Label: {cluster.label}, Region: {cluster.region}")
        return clusters
    except ApiError as e:
        print(f"Failed to list Kubernetes clusters: {e}")
        return []

def delete_kubernetes_cluster(cluster_id):
    """
    Delete a Kubernetes cluster by ID.
    
    :param cluster_id: The ID of the cluster to delete.
    :return: True if deleted successfully, False otherwise.
    """
    try:
        cluster = client.lke_clusters(cluster_id)
        cluster.delete()
        print(f"Kubernetes cluster with ID {cluster_id} deleted successfully.")
        return True
    except ApiError as e:
        print(f"Failed to delete Kubernetes cluster: {e}")
        return False

if __name__ == "__main__":
    # Example usage:
    
    # Create a new Kubernetes cluster
    new_cluster = create_kubernetes_cluster(
        label="example-cluster",
        region="us-central",
        node_type="g6-standard-2",
        node_count=3
    )
    
    # List all Kubernetes clusters
    list_kubernetes_clusters()
    
    # Delete a Kubernetes cluster (replace with valid cluster ID)
    if new_cluster:
        delete_kubernetes_cluster(new_cluster.id)
```

### Requirements:
1. Install the `linode_api4` Python package if not already installed:
   ```bash
   pip install linode-api4
   ```

2. Set the `LINODE_API_TOKEN` environment variable containing your Linode API token:
   ```bash
   export LINODE_API_TOKEN="your_api_token_here"
   ```

Ensure your Linode API token has the appropriate permissions to manage Kubernetes clusters (`read_write` access).
.get(f"{self.base_url}/lke/clusters/{cluster_id}", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving cluster details: {e}")
            return {}

# Usage example
if __name__ == "__main__":
    linode_token = "your_linode_api_token_here"  # Replace with your Linode API token
    manager = LinodeKubernetesManager(linode_token)

    # List clusters
    clusters = manager.list_clusters()
    print("Clusters:", clusters)

    # Create a cluster
    new_cluster = manager.create_cluster(
        label="my-cluster",
        region="us-east",
        node_pools=[{"type": "g6-standard-4", "count": 3}]
    )
    print("Created Cluster:", new_cluster)

    # Get cluster details
    if "id" in new_cluster:
        details = manager.get_cluster_details(new_cluster["id"])
        print("Cluster Details:", details)

    # Delete the cluster
    if "id" in new_cluster:
        success = manager.delete_cluster(new_cluster["id"])
        print("Cluster Deleted:", success)
```
