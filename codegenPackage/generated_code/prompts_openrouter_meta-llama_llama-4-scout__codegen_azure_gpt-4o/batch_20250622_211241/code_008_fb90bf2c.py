"""
Generated Code Metadata:
========================
Original URL: https://aethiredge.tw
Prompt: Develop a simple smart contract to manage Aethir Edge nodes and distribute rewards to node owners on a blockchain network.
Generated: DETERMINISTIC_fb90bf2c9481e817
Batch ID: 20250622_211241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AethirEdgeNodeManager
 * @dev A smart contract to manage Aethir Edge nodes and distribute rewards to node owners.
 */
contract AethirEdgeNodeManager {
    // Struct to represent an Edge Node
    struct EdgeNode {
        address owner; // Address of the node owner
        uint256 rewards; // Accumulated rewards for the node
        bool isActive; // Status of the node (active/inactive)
    }

    // Mapping to store Edge Nodes by their unique ID
    mapping(uint256 => EdgeNode) public edgeNodes;

    // Event emitted when a new node is registered
    event NodeRegistered(uint256 indexed nodeId, address indexed owner);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 indexed nodeId, uint256 amount);

    // Modifier to ensure only the owner of a node can perform certain actions
    modifier onlyNodeOwner(uint256 nodeId) {
        require(edgeNodes[nodeId].owner == msg.sender, "Caller is not the node owner");
        _;
    }

    /**
     * @dev Register a new Edge Node.
     * @param nodeId The unique ID of the node.
     */
    function registerNode(uint256 nodeId) external {
        require(edgeNodes[nodeId].owner == address(0), "Node ID already registered");

        // Register the node
        edgeNodes[nodeId] = EdgeNode({
            owner: msg.sender,
            rewards: 0,
            isActive: true
        });

        emit NodeRegistered(nodeId, msg.sender);
    }

    /**
     * @dev Distribute rewards to a specific node.
     * @param nodeId The unique ID of the node.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(uint256 nodeId, uint256 amount) external {
        require(edgeNodes[nodeId].isActive, "Node is not active");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the node's rewards
        edgeNodes[nodeId].rewards += amount;

        emit RewardsDistributed(nodeId, amount);
    }

    /**
     * @dev Claim accumulated rewards for a node.
     * @param nodeId The unique ID of the node.
     */
    function claimRewards(uint256 nodeId) external onlyNodeOwner(nodeId) {
        uint256 rewards = edgeNodes[nodeId].rewards;
        require(rewards > 0, "No rewards to claim");

        // Reset rewards to zero
        edgeNodes[nodeId].rewards = 0;

        // Transfer rewards to the node owner
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @dev Deactivate a node.
     * @param nodeId The unique ID of the node.
     */
    function deactivateNode(uint256 nodeId) external onlyNodeOwner(nodeId) {
        require(edgeNodes[nodeId].isActive, "Node is already inactive");

        // Deactivate the node
        edgeNodes[nodeId].isActive = false;
    }

    /**
     * @dev Reactivate a node.
     * @param nodeId The unique ID of the node.
     */
    function reactivateNode(uint256 nodeId) external onlyNodeOwner(nodeId) {
        require(!edgeNodes[nodeId].isActive, "Node is already active");

        // Reactivate the node
        edgeNodes[nodeId].isActive = true;
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdrawContractBalance() external {
        require(msg.sender == address(this), "Only contract owner can withdraw");
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
}
```
