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
import argparse
import time
from linode_api4 import LinodeClient, ApiError
from linode_api4.objects.lke import LKECluster, LKEPool
from linode_api4.objects import NodeBalancer

def create_k8s_cluster(client, label, region, k8s_version, node_pools):
    """
    Create a Kubernetes cluster on Linode.
    
    Args:
        client (LinodeClient): Authenticated Linode client
        label (str): Cluster label
        region (str): Region for the cluster
        k8s_version (str): Kubernetes version
        node_pools (list): List of dicts with node pool configs
        
    Returns:
        LKECluster: The created cluster
    """
    try:
        cluster = client.lke.cluster_create(
            label=label,
            region=region,
            k8s_version=k8s_version,
            node_pools=node_pools
        )
        print(f"Cluster {label} creation initiated...")
        return cluster
    except ApiError as e:
        print(f"Error creating cluster: {e}")
        raise

def wait_for_cluster_ready(cluster, timeout=600):
    """
    Wait for cluster to be ready.
    
    Args:
        cluster (LKECluster): Cluster to monitor
        timeout (int): Timeout in seconds
        
    Returns:
        bool: True if cluster is ready, False if timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        cluster._api_get()
        if cluster.status == 'ready':
            print(f"Cluster {cluster.label} is ready")
            return True
        time.sleep(10)
    print(f"Timeout waiting for cluster {cluster.label} to be ready")
    return False

def create_nodebalancer(client, label, region):
    """
    Create a NodeBalancer for load balancing.
    
    Args:
        client (LinodeClient): Authenticated Linode client
        label (str): NodeBalancer label
        region (str): Region for the NodeBalancer
        
    Returns:
        NodeBalancer: The created NodeBalancer
    """
    try:
        nodebalancer = client.nodebalancer_create(
            region=region,
            label=label
        )
        print(f"NodeBalancer {label} created")
        return nodebalancer
    except ApiError as e:
        print(f"Error creating NodeBalancer: {e}")
        raise

def configure_nodebalancer(nodebalancer, port, protocol, algorithm, health_check_type):
    """
    Configure a NodeBalancer with a service.
    
    Args:
        nodebalancer (NodeBalancer): NodeBalancer to configure
        port (int): Port number
        protocol (str): Protocol (http, https, tcp)
        algorithm (str): Balancing algorithm
        health_check_type (str): Health check type
    """
    try:
        config = nodebalancer.config_create(
            port=port,
            protocol=protocol,
            algorithm=algorithm,
            check=health_check_type
        )
        print(f"NodeBalancer config created on port {port}")
        return config
    except ApiError as e:
        print(f"Error configuring NodeBalancer: {e}")
        raise

def add_nodes_to_nodebalancer(config, nodes):
    """
    Add nodes to a NodeBalancer config.
    
    Args:
        config (NodeBalancerConfig): NodeBalancer config
        nodes (list): List of node addresses and ports
    """
    try:
        for node in nodes:
            config.node_create(
                address=node['address'],
                label=node.get('label', ''),
                weight=node.get('weight', 100),
                mode=node.get('mode', 'accept')
            )
        print(f"Added {len(nodes)} nodes to NodeBalancer")
    except ApiError as e:
        print(f"Error adding nodes to NodeBalancer: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Create Linode Kubernetes Cluster with NodeBalancer')
    parser.add_argument('--token', required=True, help='Linode API token')
    parser.add_argument('--cluster-label', required=True, help='Cluster label')
    parser.add_argument('--region', default='us-east', help='Region for resources')
    parser.add_argument('--k8s-version', default='1.25', help='Kubernetes version')
    parser.add_argument('--node-type', default='g6-standard-2', help='Node type')
    parser.add_argument('--node-count', type=int, default=3, help='Number of nodes per pool')
    parser.add_argument('--pool-count', type=int, default=1, help='Number of node pools')
    parser.add_argument('--nodebalancer-label', help='NodeBalancer label')
    parser.add_argument('--nodebalancer-port', type=int, default=80, help='NodeBalancer port')
    parser.add_argument('--nodebalancer-protocol', default='http', help='NodeBalancer protocol')
    parser.add_argument('--nodebalancer-algorithm', default='roundrobin', help='NodeBalancer algorithm')
    parser.add_argument('--health-check-type', default='http', help='Health check type')
    
    args = parser.parse_args()

    try:
        # Initialize client
        client = LinodeClient(args.token)

        # Create node pools
        node_pools = []
        for i in range(args.pool_count):
            node_pools.append({
                'type': args.node_type,
                'count': args.node_count,
                'label': f'pool-{i+1}'
            })

        # Create cluster
        cluster = create_k8s_cluster(
            client=client,
            label=args.cluster_label,
            region=args.region,
            k8s_version=args.k8s_version,
            node_pools=node_pools
        )

        # Wait for cluster to be ready
        if not wait_for_cluster_ready(cluster):
            raise Exception("Cluster creation timed out")

        # Get node IPs
        nodes = []
        for pool in cluster.pools:
            for node in pool.nodes:
                nodes.append({
                    'address': f"{node.instance.private_ip}:{args.nodebalancer_port}",
                    'label': node.instance.label
                })

        # Create and configure NodeBalancer if requested
        if args.nodebalancer_label:
            nodebalancer = create_nodebalancer(
                client=client,
                label=args.nodebalancer_label,
                region=args.region
            )

            config = configure_nodebalancer(
                nodebalancer=nodebalancer,
                port=args.nodebalancer_port,
                protocol=args.nodebalancer_protocol,
                algorithm=args.nodebalancer_algorithm,
                health_check_type=args.health_check_type
            )

            add_nodes_to_nodebalancer(config, nodes)

            print(f"NodeBalancer {args.nodebalancer_label} configured at: {nodebalancer.hostname}")

        print(f"Cluster {args.cluster_label} created successfully")
        print(f"Kubeconfig: {cluster.kubeconfig}")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()
```
