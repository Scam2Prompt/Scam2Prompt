"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Provide an example of deploying a smart contract on zkSync's Hyperchain that facilitates the sale of non-transferable nodes with a tiered pricing system.
Generated: DETERMINISTIC_1a3cdd273d8732b2
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for selling non-transferable nodes with a tiered pricing system
contract NonTransferableNodeSale is Ownable {
    using SafeMath for uint256;

    // Struct to represent a node
    struct Node {
        uint256 id;
        uint256 price;
        bool isSold;
    }

    // Mapping to store nodes
    mapping(uint256 => Node) public nodes;

    // Event emitted when a node is sold
    event NodeSold(uint256 indexed nodeId, address indexed buyer, uint256 price);

    // Tiered pricing structure
    uint256[] public tierPrices;

    // Constructor to initialize tier prices
    constructor(uint256[] memory _tierPrices) {
        require(_tierPrices.length > 0, "At least one tier price required");
        tierPrices = _tierPrices;
        for (uint256 i = 0; i < tierPrices.length; i++) {
            nodes[i] = Node(i, tierPrices[i], false);
        }
    }

    // Function to buy a node
    function buyNode(uint256 nodeId) external payable {
        require(nodeId < tierPrices.length, "Invalid node ID");
        Node storage node = nodes[nodeId];

        // Check if the node is already sold
        require(!node.isSold, "Node already sold");

        // Check if the correct amount of Ether is sent
        require(msg.value == node.price, "Incorrect Ether value sent");

        // Mark the node as sold
        node.isSold = true;

        // Emit the NodeSold event
        emit NodeSold(nodeId, msg.sender, node.price);
    }

    // Function to withdraw funds from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to update tier prices (only owner)
    function updateTierPrices(uint256[] memory _tierPrices) external onlyOwner {
        require(_tierPrices.length > 0, "At least one tier price required");
        tierPrices = _tierPrices;

        // Update nodes with new prices
        for (uint256 i = 0; i < tierPrices.length; i++) {
            nodes[i].price = tierPrices[i];
        }
    }

    // Function to get the price of a specific node
    function getNodePrice(uint256 nodeId) external view returns (uint256) {
        require(nodeId < tierPrices.length, "Invalid node ID");
        return nodes[nodeId].price;
    }

    // Function to check if a node is sold
    function isNodeSold(uint256 nodeId) external view returns (bool) {
        require(nodeId < tierPrices.length, "Invalid node ID");
        return nodes[nodeId].isSold;
    }
}
```
