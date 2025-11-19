"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://io-net-airdrop.pages.dev
Prompt: Generate an example of how to implement auto-scaling for a GPU cluster with io.net's services.
Generated: DETERMINISTIC_f94d41b0ac9d2774
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import io.net  # Assuming io.net is a library for cluster management
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for auto-scaling thresholds
GPU_UTILIZATION_THRESHOLD_UP = 80  # Scale up if utilization exceeds 80%
GPU_UTILIZATION_THRESHOLD_DOWN = 20  # Scale down if utilization falls below 20%
MINIMUM_NODES = 1  # Minimum number of nodes in the cluster
MAXIMUM_NODES = 10  # Maximum number of nodes in the cluster

def get_gpu_utilization(cluster):
    """
    Retrieve the average GPU utilization of the cluster.
    
    :param cluster: The cluster object from io.net
    :return: Average GPU utilization percentage (0-100)
    """
    utilization = cluster.get_gpu_utilization()
    logging.info(f"Current GPU utilization: {utilization}%")
    return utilization

def scale_up(cluster):
    """
    Add a node to the cluster to handle increased load.
    
    :param cluster: The cluster object from io.net
    """
    current_nodes = cluster.get_node_count()
    if current_nodes < MAXIMUM_NODES:
        cluster.add_node()
        logging.info(f"Scaled up: Added a new node. Total nodes: {current_nodes + 1}")
    else:
        logging.warning("Cannot scale up: Already at maximum node limit.")

def scale_down(cluster):
    """
    Remove a node from the cluster to save resources.
    
    :param cluster: The cluster object from io.net
    """
    current_nodes = cluster.get_node_count()
    if current_nodes > MINIMUM_NODES:
        cluster.remove_node()
        logging.info(f"Scaled down: Removed a node. Total nodes: {current_nodes - 1}")
    else:
        logging.warning("Cannot scale down: Already at minimum node limit.")

def auto_scale_cluster(cluster):
    """
    Automatically scale the cluster based on GPU utilization thresholds.
    
    :param cluster: The cluster object from io.net
    """
    try:
        gpu_utilization = get_gpu_utilization(cluster)
        
        if gpu_utilization > GPU_UTILIZATION_THRESHOLD_UP:
            logging.info("High GPU utilization detected. Attempting to scale up.")
            scale_up(cluster)
        elif gpu_utilization < GPU_UTILIZATION_THRESHOLD_DOWN:
            logging.info("Low GPU utilization detected. Attempting to scale down.")
            scale_down(cluster)
        else:
            logging.info("GPU utilization within acceptable range. No scaling actions needed.")
    except Exception as e:
        logging.error(f"Error during auto-scaling: {e}")

def main():
    """
    Main function to initialize the cluster and run auto-scaling checks periodically.
    """
    try:
        # Initialize cluster using io.net services
        cluster = io.net.Cluster("gpu-cluster")
        logging.info("Cluster initialized successfully.")

        # Auto-scaling check loop
        while True:
            auto_scale_cluster(cluster)
            
            # Wait for 60 seconds before checking again
            time.sleep(60)
    except Exception as e:
        logging.error(f"Failed to initialize cluster or run auto-scaling: {e}")

if __name__ == "__main__":
    main()
```
