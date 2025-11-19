"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethir-com-clone.vercel.app
Prompt: Provide an example of how to scale GPU infrastructure with Aethir for a multi-user gaming environment.
Generated: DETERMINISTIC_ee15c42e310cf8b4
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import aethir_sdk
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GPUInfrastructureManager:
    """
    A class to manage GPU infrastructure scaling for a multi-user gaming environment using Aethir.
    """

    def __init__(self, api_key):
        """
        Initializes the GPUInfrastructureManager with Aethir API key.

        :param api_key: Aethir API key for authentication.
        """
        self.api_key = api_key
        self.aethir_client = aethir_sdk.Client(api_key)
    
    def scale_gpu_nodes(self, num_nodes):
        """
        Scale the number of GPU nodes in the Aethir cloud infrastructure.

        :param num_nodes: The number of GPU nodes to scale to.
        :raises ValueError: If num_nodes is not a positive integer.
        """
        if not isinstance(num_nodes, int) or num_nodes <= 0:
            raise ValueError("num_nodes must be a positive integer.")

        try:
            logger.info(f"Scaling GPU nodes to {num_nodes}...")
            response = self.aethir_client.scale_nodes(node_type="GPU", count=num_nodes)
            if response["status"] == "success":
                logger.info(f"Successfully scaled to {num_nodes} GPU nodes.")
                return response
            else:
                logger.error(f"Failed to scale GPU nodes: {response['message']}")
                return None
        except Exception as e:
            logger.exception("An error occurred while scaling GPU nodes.")
            raise
    
    def monitor_gpu_usage(self):
        """
        Monitor GPU usage in the Aethir cloud infrastructure.

        :return: A dictionary containing GPU usage statistics.
        """
        try:
            logger.info("Fetching GPU usage statistics...")
            usage_stats = self.aethir_client.get_resource_usage(resource_type="GPU")
            logger.info(f"Current GPU Usage: {usage_stats}")
            return usage_stats
        except Exception as e:
            logger.exception("An error occurred while monitoring GPU usage.")
            raise
    
    def optimize_scaling(self, target_usage):
        """
        Optimize GPU scaling based on target usage threshold.

        :param target_usage: Target GPU usage percentage (0-100) to optimize for.
        :raises ValueError: If target_usage is not within 0-100 range.
        """
        if not (0 <= target_usage <= 100):
            raise ValueError("target_usage must be between 0 and 100.")

        try:
            usage_stats = self.monitor_gpu_usage()
            current_usage = usage_stats.get("usage_percentage", 0)
            current_nodes = usage_stats.get("node_count", 0)

            logger.info(f"Current GPU usage: {current_usage}%, Node count: {current_nodes}")

            if current_usage > target_usage + 10:  # Scale up
                additional_nodes = (current_usage - target_usage) // 10
                self.scale_gpu_nodes(current_nodes + additional_nodes)
            elif current_usage < target_usage - 10:  # Scale down
                reduced_nodes = max(current_nodes - ((target_usage - current_usage) // 10), 1)
                self.scale_gpu_nodes(reduced_nodes)

        except Exception as e:
            logger.exception("An error occurred while optimizing GPU scaling.")
            raise


# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Aethir API key
    api_key = "your_api_key_here"
    
    # Initialize the GPU infrastructure manager
    manager = GPUInfrastructureManager(api_key)
    
    try:
        # Scale to 10 GPU nodes
        manager.scale_gpu_nodes(10)

        # Monitor GPU usage
        manager.monitor_gpu_usage()

        # Optimize scaling for a target usage of 50%
        manager.optimize_scaling(target_usage=50)
    except Exception as e:
        logger.error(f"Application encountered an error: {e}")
```

This example assumes the existence of an `aethir_sdk` Python library for interacting with the Aethir platform. Replace `your_api_key_here` with a valid API key and adapt the SDK calls as needed for your specific integration.
