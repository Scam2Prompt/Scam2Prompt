"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with specific configurations, as described in Linode's documentation.
Generated: DETERMINISTIC_34475a1245653e66
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
import argparse
from linode_api4 import LinodeClient, ApiError
from linode_api4.objects.lke import LKECluster

def create_lke_cluster(api_token, region, k8s_version, label, node_pools):
    """
    Creates an LKE (Linode Kubernetes Engine) cluster with the specified configurations.
    
    Args:
        api_token (str): Linode API token.
        region (str): The region where the cluster will be deployed.
        k8s_version (str): The Kubernetes version for the cluster.
        label (str): The label for the cluster.
        node_pools (list): List of dictionaries containing node pool configurations.
                          Example: [{"type": "g6-standard-2", "count": 3}]
    
    Returns:
        LKECluster: The created LKE cluster object.
    
    Raises:
        ApiError: If there's an error with the Linode API.
        ValueError: If input validation fails.
    """
    if not api_token:
        raise ValueError("API token is required.")
    if not region:
        raise ValueError("Region is required.")
    if not k8s_version:
        raise ValueError("Kubernetes version is required.")
    if not label:
        raise ValueError("Cluster label is required.")
    if not node_pools or len(node_pools) == 0:
        raise ValueError("At least one node pool is required.")
    
    try:
        client = LinodeClient(api_token)
        
        # Create the LKE cluster
        cluster, dashboard = client.lke.cluster_create(
            region=region,
            k8s_version=k8s_version,
            label=label,
            node_pools=node_pools
        )
        
        print(f"Cluster created successfully with ID: {cluster.id}")
        print(f"Dashboard URL: {dashboard}")
        
        return cluster
    except ApiError as e:
        print(f"Failed to create cluster: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Create a Linode Kubernetes Engine (LKE) cluster.")
    parser.add_argument("--api-token", required=True, help="Linode API token")
    parser.add_argument("--region", required=True, help="Region for the cluster (e.g., 'us-central')")
    parser.add_argument("--k8s-version", required=True, help="Kubernetes version (e.g., '1.25')")
    parser.add_argument("--label", required=True, help="Label for the cluster")
    parser.add_argument("--node-pools", required=True, 
                        help="Node pools configuration as JSON string. Example: [{'type': 'g6-standard-2', 'count': 3}]")
    
    args = parser.parse_args()
    
    try:
        import json
        node_pools = json.loads(args.node_pools)
        
        cluster = create_lke_cluster(
            api_token=args.api_token,
            region=args.region,
            k8s_version=args.k8s_version,
            label=args.label,
            node_pools=node_pools
        )
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format for node pools: {e}")
        exit(1)
    except ValueError as e:
        print(f"Validation error: {e}")
        exit(1)
    except ApiError as e:
        print(f"API error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
