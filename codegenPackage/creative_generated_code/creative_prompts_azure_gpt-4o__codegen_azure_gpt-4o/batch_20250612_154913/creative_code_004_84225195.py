"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://permasolution.pages.dev
Prompt: Write a script to deploy a smart contract on the peaq blockchain for managing community nodes, inspired by Teneo Protocol's use case.
Generated: DETERMINISTIC_8422519501f00e33
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CommunityNodeManager
 * @dev Smart contract to manage community nodes on the peaq blockchain.
 * Inspired by Teneo Protocol's use case.
 */
contract CommunityNodeManager {
    // Struct representing a community node
    struct Node {
        address owner;      // Address of the node owner
        string metadata;    // Metadata associated with the node (e.g., description, location)
        bool active;        // Status of the node (active/inactive)
    }

    // Mapping to store nodes by unique ID
    mapping(uint256 => Node) private nodes;

    // Counter for generating unique node IDs
    uint256 private nodeCounter;

    // Event emitted when a new node is registered
    event NodeRegistered(uint256 indexed nodeId, address indexed owner, string metadata);

    // Event emitted when a node's status is updated
    event NodeStatusUpdated(uint256 indexed nodeId, bool active);

    // Modifier to ensure the caller is the owner of the node
    modifier onlyNodeOwner(uint256 nodeId) {
        require(nodes[nodeId].owner == msg.sender, "Caller is not the node owner");
        _;
    }

    /**
     * @dev Register a new community node.
     * @param metadata Metadata associated with the node.
     * @return nodeId The unique ID of the registered node.
     */
    function registerNode(string calldata metadata) external returns (uint256 nodeId) {
        // Generate a new unique node ID
        nodeId = ++nodeCounter;

        // Create a new node and store it in the mapping
        nodes[nodeId] = Node({
            owner: msg.sender,
            metadata: metadata,
            active: true
        });

        // Emit an event for the registered node
        emit NodeRegistered(nodeId, msg.sender, metadata);
    }

    /**
     * @dev Update the status of a node.
     * @param nodeId The ID of the node to update.
     * @param active The new status of the node (true for active, false for inactive).
     */
    function updateNodeStatus(uint256 nodeId, bool active) external onlyNodeOwner(nodeId) {
        // Update the node's status
        nodes[nodeId].active = active;

        // Emit an event for the status update
        emit NodeStatusUpdated(nodeId, active);
    }

    /**
     * @dev Retrieve information about a node.
     * @param nodeId The ID of the node to retrieve.
     * @return owner The owner of the node.
     * @return metadata The metadata of the node.
     * @return active The status of the node.
     */
    function getNode(uint256 nodeId) external view returns (address owner, string memory metadata, bool active) {
        require(nodeId > 0 && nodeId <= nodeCounter, "Node ID does not exist");

        Node memory node = nodes[nodeId];
        return (node.owner, node.metadata, node.active);
    }
}
```
