"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Generate a smart contract code snippet for participating in the Sophon node sale on zkSync, considering the tiered pricing system and non-transferable nodes for one year.
Generated: DETERMINISTIC_5a86d7d2eb8acdf3
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SophonNodeSale
 * @dev Smart contract for participating in the Sophon node sale on zkSync
 * with a tiered pricing system and non-transferable nodes for one year.
 */
contract SophonNodeSale is Ownable {
    // Struct to represent a node
    struct Node {
        address owner;
        uint256 purchaseTime;
    }

    // Mapping to store nodes by their ID
    mapping(uint256 => Node) public nodes;

    // Price tiers in wei
    uint256[] public priceTiers = [1 ether, 2 ether, 3 ether]; // Example prices for tiers
    uint256 public constant MAX_NODES = 100; // Maximum number of nodes available
    uint256 public totalNodesSold;

    // Event emitted when a node is purchased
    event NodePurchased(address indexed buyer, uint256 indexed nodeId);

    /**
     * @dev Purchase a node in the sale.
     * @param nodeId The ID of the node to purchase.
     */
    function purchaseNode(uint256 nodeId) external payable {
        require(nodeId < MAX_NODES, "Node ID out of range");
        require(nodes[nodeId].owner == address(0), "Node already purchased");
        require(msg.value == getNodePrice(nodeId), "Incorrect payment amount");

        // Assign the node to the buyer
        nodes[nodeId] = Node({
            owner: msg.sender,
            purchaseTime: block.timestamp
        });

        totalNodesSold++;

        emit NodePurchased(msg.sender, nodeId);
    }

    /**
     * @dev Get the price of a node based on its ID.
     * @param nodeId The ID of the node.
     * @return The price of the node in wei.
     */
    function getNodePrice(uint256 nodeId) public view returns (uint256) {
        require(nodeId < priceTiers.length, "Node ID out of price tier range");
        return priceTiers[nodeId];
    }

    /**
     * @dev Withdraw funds from the contract.
     * Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Get the details of a node.
     * @param nodeId The ID of the node.
     * @return owner The owner of the node.
     * @return purchaseTime The purchase time of the node.
     */
    function getNodeDetails(uint256 nodeId) external view returns (address owner, uint256 purchaseTime) {
        Node memory node = nodes[nodeId];
        return (node.owner, node.purchaseTime);
    }
}
```
