"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://g-4lz.pages.dev
Prompt: Explain how to implement auto-scaling for ML workloads using the flexible clusters from io.net, including a sample configuration.
Generated: DETERMINISTIC_1b9b33977b312983
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import io.net
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_flexible_cluster(cluster_name, node_count, instance_type):
    """
    Create a flexible cluster for ML workloads.

    Args:
        cluster_name (str): Name of the cluster to be created.
        node_count (int): Number of nodes in the cluster.
        instance_type (str): Type of instance to use for the nodes.

    Returns:
        Cluster: A reference to the created cluster.
    """
    try:
        # Initialize the io.net client
        client = io.net.Client()

        # Create the flexible cluster
        cluster = client.create_flexible_cluster(
            name=cluster_name,
            node_count=node_count,
            instance_type=instance_type,
        )

        logging.info(f"Cluster '{cluster_name}' created successfully with {node_count} nodes of type '{instance_type}'.")
        return cluster

    except Exception as e:
        logging.error(f"Error creating cluster '{cluster_name}': {e}")
        raise

def configure_auto_scaling(cluster, min_nodes, max_nodes, scaling_policy):
    """
    Configure auto-scaling for the given cluster.

    Args:
        cluster (Cluster): The cluster to configure for auto-scaling.
        min_nodes (int): Minimum number of nodes in the cluster.
        max_nodes (int): Maximum number of nodes in the cluster.
        scaling_policy (dict): The scaling policy defining the resource management.

    Returns:
        None
    """
    try:
        # Configure auto-scaling
        cluster.set_auto_scaling(min_nodes=min_nodes, max_nodes=max_nodes, policy=scaling_policy)
        logging.info(f"Auto-scaling configured: min_nodes={min_nodes}, max_nodes={max_nodes}.")

    except Exception as e:
        logging.error(f"Error configuring auto-scaling for cluster '{cluster.name}': {e}")
        raise

def main():
    """
    Main function to set up the flexible cluster and configure auto-scaling.
    """
    # Define parameters
    cluster_name = "ml-workload-cluster"
    node_count = 2
    instance_type = "ml.t2.medium"
    min_nodes = 1
    max_nodes = 5
    scaling_policy = {
        "cpu_threshold": 70,  # Scale up if CPU usage exceeds 70%
        "scale_up_increment": 1,  # Number of nodes to add
        "scale_down_increment": 1,  # Number of nodes to remove
        "cooldown_period": 300,  # Cooldown period in seconds before the next scale
    }

    # Create the flexible cluster
    cluster = create_flexible_cluster(cluster_name, node_count, instance_type)

    # Configure auto-scaling
    configure_auto_scaling(cluster, min_nodes, max_nodes, scaling_policy)

if __name__ == "__main__":
    main()
```
