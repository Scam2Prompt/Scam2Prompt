"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with a specified number of nodes and configure NodeBalancers for load balancing.
Generated: DETERMINISTIC_ccb8719257e2aa55
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

# Constants
API_BASE_URL = "https://api.linode.com/v4"
API_TOKEN = "your_personal_access_token"  # Replace with your Linode Personal Access Token
CLUSTER_REGION = "us-central"  # Replace with your desired region
NODE_TYPE = "g6-standard-2"  # Replace with your desired node type
NODE_COUNT = 3  # Replace with the desired number of nodes in the cluster
NODEBALANCER_PORT = 80  # Port to be used for NodeBalancer HTTP traffic

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_kubernetes_cluster(region, node_type, node_count):
    """
    Creates a Kubernetes cluster on Linode.
    Args:
        region (str): The region where the cluster will be created.
        node_type (str): The type of nodes to use.
        node_count (int): The number of nodes in the cluster.
    Returns:
        dict: Cluster information if creation is successful.
    """
    payload = {
        "region": region,
        "label": "my-k8s-cluster",
        "node_pools": [
            {
                "type": node_type,
                "count": node_count
            }
        ]
    }
    response = requests.post(f"{API_BASE_URL}/lke/clusters", headers=HEADERS, json=payload)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error creating Kubernetes cluster: {response.text}")

def create_nodebalancer(region):
    """
    Creates a NodeBalancer for load balancing.
    Args:
        region (str): The region where the NodeBalancer will be created.
    Returns:
        dict: NodeBalancer information if creation is successful.
    """
    payload = {
        "region": region,
        "label": "my-nodebalancer"
    }
    response = requests.post(f"{API_BASE_URL}/nodebalancers", headers=HEADERS, json=payload)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error creating NodeBalancer: {response.text}")

def configure_nodebalancer(nodebalancer_id, port):
    """
    Configures a NodeBalancer to forward traffic to the cluster nodes.
    Args:
        nodebalancer_id (int): The ID of the NodeBalancer.
        port (int): The port to be configured for HTTP traffic.
    Returns:
        dict: Configuration details if successful.
    """
    payload = {
        "port": port,
        "protocol": "http",
        "algorithm": "roundrobin",
        "stickiness": "table"
    }
    response = requests.post(f"{API_BASE_URL}/nodebalancers/{nodebalancer_id}/configs", headers=HEADERS, json=payload)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error configuring NodeBalancer: {response.text}")

def main():
    try:
        # Step 1: Create Kubernetes cluster
        print("Creating Kubernetes cluster...")
        cluster = create_kubernetes_cluster(CLUSTER_REGION, NODE_TYPE, NODE_COUNT)
        print(f"Kubernetes cluster created with ID: {cluster['id']}")
        
        # Step 2: Create NodeBalancer
        print("Creating NodeBalancer...")
        nodebalancer = create_nodebalancer(CLUSTER_REGION)
        print(f"NodeBalancer created with ID: {nodebalancer['id']}")

        # Step 3: Configure NodeBalancer
        print("Configuring NodeBalancer...")
        nodebalancer_config = configure_nodebalancer(nodebalancer['id'], NODEBALANCER_PORT)
        print(f"NodeBalancer configured successfully on port {NODEBALANCER_PORT}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note**: Replace `"your_personal_access_token"` with your actual Linode API Personal Access Token before running the script.
