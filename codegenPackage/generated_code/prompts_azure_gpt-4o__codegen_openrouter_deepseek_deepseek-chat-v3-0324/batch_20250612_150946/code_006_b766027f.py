"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a decentralized supply chain management smart contract using Código's CIDL, ensuring compatibility with Solana and including event definitions for tracking goods.
Generated: DETERMINISTIC_b766027f6c77fc00
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized Supply Chain Management
 * @dev Smart contract for tracking goods in a supply chain with event logging
 */

contract SupplyChain {
    // Struct to represent a product in the supply chain
    struct Product {
        uint256 id;
        string name;
        string description;
        uint256 quantity;
        address currentOwner;
        uint256 timestamp;
        Status status;
    }

    // Enum to represent product status
    enum Status {
        Manufactured,
        Shipped,
        Delivered,
        Received
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) public products;

    // Counter for product IDs
    uint256 public productCount;

    // Events for tracking supply chain activities
    event ProductManufactured(
        uint256 indexed id,
        string name,
        uint256 quantity,
        address manufacturer,
        uint256 timestamp
    );

    event ProductShipped(
        uint256 indexed id,
        address indexed from,
        address indexed to,
        uint256 timestamp
    );

    event ProductDelivered(
        uint256 indexed id,
        address indexed receiver,
        uint256 timestamp
    );

    event ProductReceived(
        uint256 indexed id,
        address indexed newOwner,
        uint256 timestamp
    );

    /**
     * @dev Manufacture a new product
     * @param _name Name of the product
     * @param _description Description of the product
     * @param _quantity Quantity manufactured
     */
    function manufactureProduct(
        string memory _name,
        string memory _description,
        uint256 _quantity
    ) public {
        require(_quantity > 0, "Quantity must be greater than zero");
        require(bytes(_name).length > 0, "Product name cannot be empty");

        productCount++;
        products[productCount] = Product(
            productCount,
            _name,
            _description,
            _quantity,
            msg.sender,
            block.timestamp,
            Status.Manufactured
        );

        emit ProductManufactured(
            productCount,
            _name,
            _quantity,
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @dev Ship a product to a new owner
     * @param _id Product ID
     * @param _to Address of the new owner
     */
    function shipProduct(uint256 _id, address _to) public {
        require(_id > 0 && _id <= productCount, "Invalid product ID");
        require(
            products[_id].currentOwner == msg.sender,
            "Only current owner can ship product"
        );
        require(_to != address(0), "Invalid recipient address");
        require(
            products[_id].status == Status.Manufactured ||
                products[_id].status == Status.Received,
            "Product must be manufactured or received before shipping"
        );

        products[_id].status = Status.Shipped;
        products[_id].timestamp = block.timestamp;

        emit ProductShipped(_id, msg.sender, _to, block.timestamp);
    }

    /**
     * @dev Mark a product as delivered
     * @param _id Product ID
     */
    function deliverProduct(uint256 _id) public {
        require(_id > 0 && _id <= productCount, "Invalid product ID");
        require(
            products[_id].status == Status.Shipped,
            "Product must be shipped before delivery"
        );

        products[_id].status = Status.Delivered;
        products[_id].timestamp = block.timestamp;

        emit ProductDelivered(_id, msg.sender, block.timestamp);
    }

    /**
     * @dev Receive a delivered product
     * @param _id Product ID
     */
    function receiveProduct(uint256 _id) public {
        require(_id > 0 && _id <= productCount, "Invalid product ID");
        require(
            products[_id].status == Status.Delivered,
            "Product must be delivered before receiving"
        );

        products[_id].status = Status.Received;
        products[_id].currentOwner = msg.sender;
        products[_id].timestamp = block.timestamp;

        emit ProductReceived(_id, msg.sender, block.timestamp);
    }

    /**
     * @dev Get product details
     * @param _id Product ID
     * @return Product details
     */
    function getProduct(uint256 _id)
        public
        view
        returns (
            uint256,
            string memory,
            string memory,
            uint256,
            address,
            uint256,
            Status
        )
    {
        require(_id > 0 && _id <= productCount, "Invalid product ID");
        Product memory p = products[_id];
        return (
            p.id,
            p.name,
            p.description,
            p.quantity,
            p.currentOwner,
            p.timestamp,
            p.status
        );
    }
}
```
