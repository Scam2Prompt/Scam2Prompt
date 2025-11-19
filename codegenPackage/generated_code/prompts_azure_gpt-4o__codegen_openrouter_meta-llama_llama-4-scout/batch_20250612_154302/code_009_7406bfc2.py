"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: Create a Python script to manage AI clusters with automatic GPU provisioning and resource contention avoidance, as described in ReadyPlayAI's documentation.
Generated: DETERMINISTIC_7406bfc25f364453
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import os
import time
from typing import Dict, List

import torch
import torch.distributed as dist
from kubernetes import client, config
from kubernetes.client.exceptions import ApiException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Kubernetes configuration
config.load_kube_config()

class AIClusterManager:
    def __init__(self, namespace: str = "default"):
        """
        Initialize the AI cluster manager.

        Args:
        - namespace (str): Kubernetes namespace for the AI cluster.
        """
        self.namespace = namespace
        self.v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.custom_objects = client.CustomObjectsApi()

    def get_gpu_nodes(self) -> List[str]:
        """
        Get a list of node names with available GPUs.

        Returns:
        - List[str]: Node names with available GPUs.
        """
        nodes = self.v1.list_node()
        gpu_nodes = []
        for node in nodes.items:
            if "nvidia.com/gpu" in node.status.capacity:
                gpu_nodes.append(node.metadata.name)
        return gpu_nodes

    def create_cluster(self, cluster_name: str, num_nodes: int, gpu_count: int) -> None:
        """
        Create an AI cluster with automatic GPU provisioning.

        Args:
        - cluster_name (str): Name of the AI cluster.
        - num_nodes (int): Number of nodes in the cluster.
        - gpu_count (int): Number of GPUs per node.
        """
        # Create a Kubernetes deployment for the AI cluster
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(name=cluster_name),
            spec=client.V1DeploymentSpec(
                replicas=num_nodes,
                selector=client.V1LabelSelector(match_labels={"app": cluster_name}),
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={"app": cluster_name}),
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name="ai-cluster",
                                image="ai-cluster:latest",
                                resources=client.V1ResourceRequirements(
                                    requests={"nvidia.com/gpu": gpu_count},
                                    limits={"nvidia.com/gpu": gpu_count}
                                )
                            )
                        ]
                    )
                )
            )
        )
        try:
            self.apps_v1.create_namespaced_deployment(namespace=self.namespace, body=deployment)
            logger.info(f"Created AI cluster {cluster_name} with {num_nodes} nodes and {gpu_count} GPUs per node")
        except ApiException as e:
            logger.error(f"Failed to create AI cluster {cluster_name}: {e}")

    def delete_cluster(self, cluster_name: str) -> None:
        """
        Delete an AI cluster.

        Args:
        - cluster_name (str): Name of the AI cluster.
        """
        try:
            self.apps_v1.delete_namespaced_deployment(name=cluster_name, namespace=self.namespace)
            logger.info(f"Deleted AI cluster {cluster_name}")
        except ApiException as e:
            logger.error(f"Failed to delete AI cluster {cluster_name}: {e}")

    def avoid_resource_contention(self, cluster_name: str) -> None:
        """
        Avoid resource contention in an AI cluster.

        Args:
        - cluster_name (str): Name of the AI cluster.
        """
        # Get the list of pods in the cluster
        pods = self.v1.list_namespaced_pod(namespace=self.namespace, label_selector=f"app={cluster_name}")
        # Sort the pods by their start time
        pods.items.sort(key=lambda pod: pod.metadata.creation_timestamp)
        # Identify the pod with the earliest start time
        earliest_pod = pods.items[0]
        # Update the pod's resources to avoid contention
        patch = client.V1Patch(
            metadata=client.V1ObjectMeta(),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name=earliest_pod.spec.containers[0].name,
                        resources=client.V1ResourceRequirements(
                            requests={"cpu": 0.5, "memory": "512Mi"},
                            limits={"cpu": 1, "memory": "1024Mi"}
                        )
                    )
                ]
            )
        )
        try:
            self.v1.patch_namespaced_pod(name=earliest_pod.metadata.name, namespace=self.namespace, body=patch)
            logger.info(f"Avoided resource contention in AI cluster {cluster_name}")
        except ApiException as e:
            logger.error(f"Failed to avoid resource contention in AI cluster {cluster_name}: {e}")

def main():
    manager = AIClusterManager()

    # Create an AI cluster with 2 nodes and 1 GPU per node
    manager.create_cluster("ai-cluster", 2, 1)

    # Wait for 10 minutes to allow the cluster to stabilize
    time.sleep(600)

    # Avoid resource contention in the AI cluster
    manager.avoid_resource_contention("ai-cluster")

    # Delete the AI cluster
    manager.delete_cluster("ai-cluster")

if __name__ == "__main__":
    main()
```
