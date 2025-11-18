"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script using the Linode API to create a Kubernetes cluster with a specified number of nodes and configure NodeBalancers for load balancing.
Generated: DETERMINISTIC_ccb8719257e2aa55
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

# Configuration variables
LINODE_TOKEN = os.getenv('LINODE_TOKEN')  # Ensure this environment variable is set
K8S_CLUSTER_NAME = "my-kubernetes-cluster"
NODE_COUNT = 3
NODE_BALANCER_NAME = "my-node-balancer"

def create_kubernetes_cluster(client, cluster_name, node_count):
    """
    Create a Kubernetes cluster with the specified number of nodes.

    :param client: Linode API client
    :param cluster_name: Name of the Kubernetes cluster
    :param node_count: Number of nodes in the cluster
    :return: Kubernetes cluster object
    """
    try:
        print(f"Creating Kubernetes cluster: {cluster_name} with {node_count} nodes.")
        k8s_cluster = client.kubernetes.create(
            label=cluster_name,
            region='us-east',  # Specify your preferred region
            version='1.21',    # Specify the desired Kubernetes version
            node_pools=[
                {
                    'count': node_count,
                    'type': 'g6-standard-1',  # Specify your desired Linode type
                }
            ]
        )
        return k8s_cluster
    except Exception as e:
        print(f"Error creating Kubernetes cluster: {e}")
        raise

def create_node_balancer(client, balancer_name):
    """
    Create a NodeBalancer for the Kubernetes cluster.

    :param client: Linode API client
    :param balancer_name: Name of the NodeBalancer
    :return: NodeBalancer object
    """
    try:
        print(f"Creating NodeBalancer: {balancer_name}.")
        node_balancer = client.nodebalancers.create(
            label=balancer_name,
            region='us-east',  # Ensure this matches your Kubernetes cluster region
            policies=[
                {
                    'type': 'http',  # Type of policy
                    'algorithm': 'roundrobin',
                    'ports': [
                        {
                            'port': 80,
                            'protocol': 'http',
                        }
                    ]
                }
            ]
        )
        return node_balancer
    except Exception as e:
        print(f"Error creating NodeBalancer: {e}")
        raise

def main():
    """
    Main function to create a Kubernetes cluster and a NodeBalancer.
    """
    # Initialize Linode API client
    try:
        client = linode_api4.LinodeClient(LINODE_TOKEN)
        print("Linode API client initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize Linode API client: {e}")
        return

    # Create Kubernetes cluster
    k8s_cluster = create_kubernetes_cluster(client, K8S_CLUSTER_NAME, NODE_COUNT)
    
    # Create NodeBalancer
    node_balancer = create_node_balancer(client, NODE_BALANCER_NAME)

    print(f"Kubernetes Cluster created: {k8s_cluster.label}")
    print(f"NodeBalancer created: {node_balancer.label}")

if __name__ == "__main__":
    main()
```

Make sure to set the `LINODE_TOKEN` environment variable to your Linode API token before running the script. This token is required to authenticate with the Linode API.
