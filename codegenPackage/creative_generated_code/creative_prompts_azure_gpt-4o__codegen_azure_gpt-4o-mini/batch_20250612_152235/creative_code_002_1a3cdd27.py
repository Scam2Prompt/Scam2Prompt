"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Provide an example of deploying a smart contract on zkSync's Hyperchain that facilitates the sale of non-transferable nodes with a tiered pricing system.
Generated: DETERMINISTIC_1a3cdd273d8732b2
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/nodes/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts for security and governance
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// Contract for the Non-Transferable Node Sale
contract NonTransferableNodeSale is ERC721, Ownable {
    // Enum to define the tiers of pricing
    enum NodeTier { Basic, Standard, Premium }
    
    // Struct to hold information about the nodes
    struct Node {
        NodeTier tier;
        uint256 price;
    }

    // Mapping to manage nodes with their respective IDs
    mapping(uint256 => Node) public nodes;
    
    // Counter for node IDs
    uint256 private nodeIdCounter;

    // Event emitted when a new node is created
    event NodeCreated(uint256 indexed nodeId, NodeTier tier, uint256 price);
    
    // Event emitted when a node is sold
    event NodeSold(uint256 indexed nodeId, address buyer);
    
    // Constructor to initialize the ERC721 token
    constructor() ERC721("NonTransferableNode", "NTN") {}

    // Function to create a new node with a specific tier and price
    function createNode(NodeTier _tier, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");
        
        // Increment the node ID counter and create a new node
        nodeIdCounter++;
        uint256 newNodeId = nodeIdCounter;

        nodes[newNodeId] = Node(_tier, _price);
        
        // Mint a non-transferable NFT (node) to the contract owner
        _mint(msg.sender, newNodeId);

        // Emit an event for the new node creation
        emit NodeCreated(newNodeId, _tier, _price);
    }

    // Function to purchase a node
    function purchaseNode(uint256 _nodeId) external payable {
        Node memory node = nodes[_nodeId];
        
        // Validate that the node exists
        require(_exists(_nodeId), "Node does not exist");
        
        // Check if the payment matches the price of the node
        require(msg.value == node.price, "Incorrect payment amount");

        // Transfer the node to the buyer
        _transfer(owner(), msg.sender, _nodeId);
        
        // Emit an event for the node sale
        emit NodeSold(_nodeId, msg.sender);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        // Transfer the contract balance to the owner
        payable(msg.sender).transfer(address(this).balance);
    }

    // Override the _baseURI function to return the base URI for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.example.com/nodes/";
    }
}
```

Make sure to deploy this smart contract on zkSync's Hyperchain with appropriate tools and configurations, such as Hardhat or Truffle, and ensure to test it thoroughly in a development environment before going to production.
