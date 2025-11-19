"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapphashai.pages.dev
Prompt: Develop a smart contract for leasing nodes in the HashAI network using Solidity.
Generated: DETERMINISTIC_9bef1368c9c8dcef
Batch ID: 20250612_163915
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

/// @title HashAI Node Leasing Smart Contract
/// @author Your Name
/// @notice This contract allows users to lease nodes in the HashAI network
/// @dev This is a basic implementation; further optimizations and security checks may be required

contract HashAINodeLeasing {
    // Struct to represent a leased node
    struct Node {
        address lessee; // The address of the lessee
        uint256 leaseEnd; // Timestamp when the lease ends
        uint256 leasePrice; // Price of the lease
    }

    // Mapping from node ID to Node struct
    mapping(uint256 => Node) public nodes;

    // Event emitted when a node is leased
    event NodeLeased(uint256 indexed nodeId, address indexed lessee, uint256 leaseEnd);

    // Event emitted when a lease is terminated
    event LeaseTerminated(uint256 indexed nodeId);

    // Modifier to check if the caller is the lessee of a node
    modifier onlyLessee(uint256 nodeId) {
        require(nodes[nodeId].lessee == msg.sender, "Not the lessee of this node");
        _;
    }

    /// @notice Lease a node
    /// @param nodeId The ID of the node to lease
    /// @param leaseDuration The duration of the lease in seconds
    /// @param leasePrice The price to lease the node
    function leaseNode(uint256 nodeId, uint256 leaseDuration, uint256 leasePrice) external payable {
        require(leaseDuration > 0, "Lease duration must be greater than 0");
        require(msg.value == leasePrice, "Incorrect lease price");

        Node storage node = nodes[nodeId];
        require(node.lessee == address(0) || block.timestamp > node.leaseEnd, "Node is already leased");

        // Set the new lessee and lease details
        node.lessee = msg.sender;
        node.leaseEnd = block.timestamp + leaseDuration;
        node.leasePrice = leasePrice;

        emit NodeLeased(nodeId, msg.sender, node.leaseEnd);
    }

    /// @notice Terminate lease of a node
    /// @param nodeId The ID of the node to terminate lease
    function terminateLease(uint256 nodeId) external onlyLessee(nodeId) {
        delete nodes[nodeId]; // Clear the node data

        emit LeaseTerminated(nodeId);
    }

    /// @notice Check the status of a node
    /// @param nodeId The ID of the node to check
    /// @return lessee The address of the current lessee
    /// @return leaseEnd The timestamp when the lease ends
    /// @return leasePrice The price of the lease
    function getNodeStatus(uint256 nodeId) external view returns (address lessee, uint256 leaseEnd, uint256 leasePrice) {
        Node storage node = nodes[nodeId];
        return (node.lessee, node.leaseEnd, node.leasePrice);
    }

    /// @notice Withdraw funds from the contract (in case of overpayment or lease termination)
    /// @param amount The amount of Ether to withdraw
    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
