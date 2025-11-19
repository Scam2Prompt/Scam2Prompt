"""
Generated Code Metadata:
========================
Original URL: https://chainback-en.web.app
Prompt: Design a system architecture for a decentralized cloud computing platform that allows individuals and data centers to contribute their unused GPU resources, similar to Chainback's GPU cloud computing model.
Generated: DETERMINISTIC_d51806407321d365
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# decentralized_cloud.py

import hashlib
import logging
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Node:
    """Represents a node in the decentralized cloud network."""
    
    def __init__(self, node_id: str, gpu_resources: int):
        """
        Initializes a Node object.

        Args:
        - node_id (str): Unique identifier for the node.
        - gpu_resources (int): Amount of available GPU resources.
        """
        self.node_id = node_id
        self.gpu_resources = gpu_resources
        self.tasks: List[Task] = []

    def add_task(self, task: 'Task'):
        """Adds a task to the node's task list."""
        self.tasks.append(task)

    def __str__(self):
        return f"Node {self.node_id} - GPU Resources: {self.gpu_resources}"


class Task:
    """Represents a task in the decentralized cloud network."""
    
    def __init__(self, task_id: str, gpu_requirements: int):
        """
        Initializes a Task object.

        Args:
        - task_id (str): Unique identifier for the task.
        - gpu_requirements (int): Amount of GPU resources required.
        """
        self.task_id = task_id
        self.gpu_requirements = gpu_requirements
        self.node: Node = None

    def assign_node(self, node: Node):
        """Assigns a node to the task."""
        self.node = node

    def __str__(self):
        return f"Task {self.task_id} - GPU Requirements: {self.gpu_requirements}"


class DecentralizedCloud:
    """Represents the decentralized cloud network."""
    
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.tasks: Dict[str, Task] = {}

    def add_node(self, node: Node):
        """Adds a node to the network."""
        self.nodes[node.node_id] = node

    def add_task(self, task: Task):
        """Adds a task to the network."""
        self.tasks[task.task_id] = task

    def assign_task(self, task_id: str, node_id: str):
        """
        Assigns a task to a node.

        Args:
        - task_id (str): ID of the task to assign.
        - node_id (str): ID of the node to assign to.

        Raises:
        - ValueError: If task or node does not exist.
        """
        task = self.tasks.get(task_id)
        node = self.nodes.get(node_id)

        if not task:
            raise ValueError(f"Task {task_id} does not exist")
        if not node:
            raise ValueError(f"Node {node_id} does not exist")

        if node.gpu_resources < task.gpu_requirements:
            raise ValueError(f"Node {node_id} does not have sufficient GPU resources")

        task.assign_node(node)
        node.add_task(task)

    def __str__(self):
        cloud_info = "Decentralized Cloud Network:\n"
        for node in self.nodes.values():
            cloud_info += f"- {node}\n"
            for task in node.tasks:
                cloud_info += f"  - {task}\n"
        return cloud_info


def hash_node(node: Node) -> str:
    """Generates a unique hash for a node."""
    node_data = f"{node.node_id}{node.gpu_resources}"
    return hashlib.sha256(node_data.encode()).hexdigest()


def hash_task(task: Task) -> str:
    """Generates a unique hash for a task."""
    task_data = f"{task.task_id}{task.gpu_requirements}"
    return hashlib.sha256(task_data.encode()).hexdigest()


def main():
    # Create decentralized cloud network
    cloud = DecentralizedCloud()

    # Create nodes
    node1 = Node("Node1", 100)
    node2 = Node("Node2", 50)

    # Add nodes to cloud network
    cloud.add_node(node1)
    cloud.add_node(node2)

    # Create tasks
    task1 = Task("Task1", 20)
    task2 = Task("Task2", 80)

    # Add tasks to cloud network
    cloud.add_task(task1)
    cloud.add_task(task2)

    # Assign tasks to nodes
    cloud.assign_task("Task1", "Node1")
    cloud.assign_task("Task2", "Node2")

    # Print cloud network information
    print(cloud)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```

```solidity
// DecentralizedCloud.sol

pragma solidity ^0.8.0;

contract DecentralizedCloud {
    // Mapping of node IDs to node information
    mapping (string => Node) public nodes;

    // Mapping of task IDs to task information
    mapping (string => Task) public tasks;

    // Struct to represent a node
    struct Node {
        string nodeId;
        uint256 gpuResources;
        uint256 availableResources;
        address nodeAddress;
    }

    // Struct to represent a task
    struct Task {
        string taskId;
        uint256 gpuRequirements;
        string assignedNodeId;
    }

    // Event emitted when a node is added
    event NodeAdded(string nodeId, uint256 gpuResources);

    // Event emitted when a task is added
    event TaskAdded(string taskId, uint256 gpuRequirements);

    // Event emitted when a task is assigned to a node
    event TaskAssigned(string taskId, string nodeId);

    // Function to add a node to the network
    function addNode(string memory _nodeId, uint256 _gpuResources) public {
        // Check if node already exists
        require(bytes(nodes[_nodeId].nodeId).length == 0, "Node already exists");

        // Create new node
        Node memory newNode;
        newNode.nodeId = _nodeId;
        newNode.gpuResources = _gpuResources;
        newNode.availableResources = _gpuResources;
        newNode.nodeAddress = msg.sender;

        // Add node to mapping
        nodes[_nodeId] = newNode;

        // Emit event
        emit NodeAdded(_nodeId, _gpuResources);
    }

    // Function to add a task to the network
    function addTask(string memory _taskId, uint256 _gpuRequirements) public {
        // Check if task already exists
        require(bytes(tasks[_taskId].taskId).length == 0, "Task already exists");

        // Create new task
        Task memory newTask;
        newTask.taskId = _taskId;
        newTask.gpuRequirements = _gpuRequirements;
        newTask.assignedNodeId = "";

        // Add task to mapping
        tasks[_taskId] = newTask;

        // Emit event
        emit TaskAdded(_taskId, _gpuRequirements);
    }

    // Function to assign a task to a node
    function assignTask(string memory _taskId, string memory _nodeId) public {
        // Check if task and node exist
        require(bytes(tasks[_taskId].taskId).length != 0, "Task does not exist");
        require(bytes(nodes[_nodeId].nodeId).length != 0, "Node does not exist");

        // Check if node has sufficient resources
        require(nodes[_nodeId].availableResources >= tasks[_taskId].gpuRequirements, "Node does not have sufficient resources");

        // Update task and node
        tasks[_taskId].assignedNodeId = _nodeId;
        nodes[_nodeId].availableResources -= tasks[_taskId].gpuRequirements;

        // Emit event
        emit TaskAssigned(_taskId, _nodeId);
    }
}
```
