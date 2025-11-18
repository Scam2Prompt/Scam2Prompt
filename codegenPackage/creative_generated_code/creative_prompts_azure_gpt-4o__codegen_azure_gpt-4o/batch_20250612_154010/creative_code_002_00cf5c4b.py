"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaklash.com
Prompt: Create a smart contract in Solidity to implement a node purchase system for the Metaklash platform, ensuring the purchased nodes power the platform infrastructure.
Generated: DETERMINISTIC_00cf5c4b8b055fd1
Batch ID: 20250612_154010
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
 * @title NodePurchaseSystem
 * @dev Implements a smart contract to allow users to purchase nodes to power the Metaklash platform infrastructure.
 */
contract NodePurchaseSystem {
    // Data structure representing a purchased node
    struct Node {
        uint256 id; // Unique identifier for the node
        address owner; // Owner of the node
        uint256 timestamp; // Time of purchase
    }

    // State variables
    uint256 public nodePrice; // Cost of each node (in wei)
    uint256 public nextNodeId; // Incremental node ID
    address public owner; // Owner of the contract (Metaklash admin)

    mapping(uint256 => Node) public nodes; // Mapping from node ID to Node details
    mapping(address => uint256[]) public ownedNodes; // Mapping from user address to list of node IDs

    event NodePurchased(address indexed buyer, uint256 nodeId, uint256 timestamp); // Event emitted when a node is purchased

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Modifier to ensure the user sends enough ETH to purchase a node
    modifier costs(uint256 amount) {
        require(msg.value >= amount, "Insufficient payment");
        _;
    }

    /**
     * @dev Constructor sets the initial node price and contract owner.
     * @param _nodePrice The price of each node in wei.
     */
    constructor(uint256 _nodePrice) {
        require(_nodePrice > 0, "Node price must be greater than zero");
        nodePrice = _nodePrice;
        owner = msg.sender;
    }

    /**
     * @dev Purchase a node by sending ETH equal to or greater than the node price.
     * The purchased node is automatically added to the user's account.
     */
    function purchaseNode() external payable costs(nodePrice) {
        // Generate a new node
        uint256 nodeId = nextNodeId++;
        nodes[nodeId] = Node(nodeId, msg.sender, block.timestamp);
        ownedNodes[msg.sender].push(nodeId);

        emit NodePurchased(msg.sender, nodeId, block.timestamp);

        // Refund excess ETH sent by the buyer
        if (msg.value > nodePrice) {
            uint256 excessAmount = msg.value - nodePrice;
            (bool success, ) = msg.sender.call{value: excessAmount}("");
            require(success, "Refund failed");
        }
    }

    /**
     * @dev Returns the total number of nodes owned by a specific address.
     * @param user The address of the user to query.
     */
    function getOwnedNodeCount(address user) external view returns (uint256) {
        return ownedNodes[user].length;
    }

    /**
     * @dev Returns the details of a specific node owned by a user.
     * @param nodeId The ID of the node to query.
     */
    function getNodeDetails(uint256 nodeId) external view returns (Node memory) {
        return nodes[nodeId];
    }

    /**
     * @dev Allows the contract owner to update the price of nodes.
     * @param _newNodePrice The new price of nodes (in wei).
     */
    function updateNodePrice(uint256 _newNodePrice) external onlyOwner {
        require(_newNodePrice > 0, "Node price must be greater than zero");
        nodePrice = _newNodePrice;
    }

    /**
     * @dev Allows the contract owner to withdraw the funds collected from node sales.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers without function calls.
     */
    fallback() external payable {
        revert("Direct transfer not allowed");
    }

    /**
     * @dev Receive function to handle direct ETH transfers.
     */
    receive() external payable {
        revert("Direct transfer not allowed");
    }
}
```
