"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lookscoin.com
Prompt: Develop a Solidity smart contract that records the metadata and state of a creative product line on the blockchain, ensuring immutability and transparency.
Generated: DETERMINISTIC_06c06210563e1fcd
Batch ID: 20250612_153256
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

contract CreativeProductLine {
    // Struct to represent a creative product
    struct Product {
        uint256 id;                // Unique identifier for the product
        string name;               // Name of the product
        string metadata;           // Metadata associated with the product
        address creator;           // Address of the creator
        uint256 createdAt;         // Timestamp of creation
        bool isActive;             // Status of the product (active/inactive)
    }

    // Events for logging product creation and updates
    event ProductCreated(uint256 indexed id, string name, address indexed creator);
    event ProductUpdated(uint256 indexed id, string metadata, bool isActive);

    // Mapping to store products by their ID
    mapping(uint256 => Product) private products;
    // Variable to keep track of the next product ID
    uint256 private nextProductId;

    // Function to create a new creative product
    function createProduct(string memory _name, string memory _metadata) public {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(bytes(_metadata).length > 0, "Product metadata cannot be empty");

        // Create a new product
        products[nextProductId] = Product({
            id: nextProductId,
            name: _name,
            metadata: _metadata,
            creator: msg.sender,
            createdAt: block.timestamp,
            isActive: true
        });

        emit ProductCreated(nextProductId, _name, msg.sender);

        // Increment the product ID for the next product
        nextProductId++;
    }

    // Function to update the metadata and status of an existing product
    function updateProduct(uint256 _id, string memory _metadata, bool _isActive) public {
        // Ensure the product exists
        require(_id < nextProductId, "Product does not exist");
        // Ensure the caller is the creator of the product
        require(products[_id].creator == msg.sender, "Only the creator can update the product");

        // Update the product's metadata and status
        products[_id].metadata = _metadata;
        products[_id].isActive = _isActive;

        emit ProductUpdated(_id, _metadata, _isActive);
    }

    // Function to retrieve product details
    function getProduct(uint256 _id) public view returns (Product memory) {
        // Ensure the product exists
        require(_id < nextProductId, "Product does not exist");
        return products[_id];
    }

    // Function to get the total number of products
    function totalProducts() public view returns (uint256) {
        return nextProductId;
    }
}
```
