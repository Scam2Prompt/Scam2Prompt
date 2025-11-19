"""
Generated Code Metadata:
========================
Original URL: https://sophpon.pages.dev
Prompt: Generate a smart contract code snippet for managing node sales on a blockchain network like Sophon, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_3215cb6658ca5a66
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

// Import OpenZeppelin libraries for security and functionality
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NodeSales is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a Node
    struct Node {
        uint256 id;
        address owner;
        uint256 price;
        bool isSold;
    }

    // Counter for unique Node IDs
    Counters.Counter private _nodeIdCounter;

    // Mapping to store nodes by ID
    mapping(uint256 => Node) private nodes;

    // Event emitted when a new node is listed for sale
    event NodeListed(uint256 indexed nodeId, address indexed owner, uint256 price);

    // Event emitted when a node is sold
    event NodeSold(uint256 indexed nodeId, address indexed buyer, uint256 price);

    // Function to list a new node for sale
    function listNode(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the node ID counter
        _nodeIdCounter.increment();
        uint256 newNodeId = _nodeIdCounter.current();

        // Create and store the new node
        nodes[newNodeId] = Node({
            id: newNodeId,
            owner: msg.sender,
            price: price,
            isSold: false
        });

        emit NodeListed(newNodeId, msg.sender, price);
    }

    // Function to purchase a node
    function purchaseNode(uint256 nodeId) external payable {
        Node storage node = nodes[nodeId];

        // Ensure the node exists and is not already sold
        require(node.id != 0, "Node does not exist");
        require(!node.isSold, "Node is already sold");

        // Ensure the buyer has sent enough Ether
        require(msg.value >= node.price, "Insufficient payment");

        // Mark the node as sold and transfer ownership
        node.isSold = true;
        node.owner = msg.sender;

        // Transfer payment to the original owner
        payable(owner()).transfer(node.price);

        emit NodeSold(nodeId, msg.sender, node.price);
    }

    // Function to retrieve node details
    function getNode(uint256 nodeId) external view returns (Node memory) {
        Node memory node = nodes[nodeId];
        require(node.id != 0, "Node does not exist");
        return node;
    }

    // Function to retrieve the total number of nodes listed
    function totalNodes() external view returns (uint256) {
        return _nodeIdCounter.current();
    }
}
```
