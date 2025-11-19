"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: "Create a blockchain solution using Solidity for a business use case, incorporating efficient and secure practices."
Generated: DETERMINISTIC_996e3cfce1adaef1
Batch ID: 20250622_205156
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
 * @title SupplyChain
 * @dev A blockchain-based solution for tracking goods in a supply chain.
 * This contract allows businesses to register products, update their status, and track ownership securely.
 */
contract SupplyChain {
    // Struct to represent a product in the supply chain
    struct Product {
        uint256 id; // Unique product ID
        string name; // Name of the product
        string description; // Description of the product
        address currentOwner; // Current owner of the product
        string status; // Current status of the product (e.g., "Manufactured", "In Transit", "Delivered")
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) private products;

    // Event emitted when a new product is registered
    event ProductRegistered(uint256 indexed productId, string name, address indexed owner);

    // Event emitted when a product's status is updated
    event ProductStatusUpdated(uint256 indexed productId, string newStatus);

    // Event emitted when ownership of a product is transferred
    event ProductOwnershipTransferred(uint256 indexed productId, address indexed newOwner);

    // Counter for generating unique product IDs
    uint256 private productCounter;

    /**
     * @dev Registers a new product in the supply chain.
     * @param name Name of the product.
     * @param description Description of the product.
     */
    function registerProduct(string memory name, string memory description) external {
        require(bytes(name).length > 0, "Product name cannot be empty");
        require(bytes(description).length > 0, "Product description cannot be empty");

        productCounter++;
        uint256 newProductId = productCounter;

        products[newProductId] = Product({
            id: newProductId,
            name: name,
            description: description,
            currentOwner: msg.sender,
            status: "Manufactured"
        });

        emit ProductRegistered(newProductId, name, msg.sender);
    }

    /**
     * @dev Updates the status of a product.
     * @param productId ID of the product to update.
     * @param newStatus New status of the product.
     */
    function updateProductStatus(uint256 productId, string memory newStatus) external {
        require(bytes(newStatus).length > 0, "Status cannot be empty");
        Product storage product = products[productId];
        require(product.id != 0, "Product does not exist");
        require(product.currentOwner == msg.sender, "Only the current owner can update the status");

        product.status = newStatus;

        emit ProductStatusUpdated(productId, newStatus);
    }

    /**
     * @dev Transfers ownership of a product to a new owner.
     * @param productId ID of the product to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(uint256 productId, address newOwner) external {
        require(newOwner != address(0), "New owner address cannot be zero");
        Product storage product = products[productId];
        require(product.id != 0, "Product does not exist");
        require(product.currentOwner == msg.sender, "Only the current owner can transfer ownership");

        product.currentOwner = newOwner;

        emit ProductOwnershipTransferred(productId, newOwner);
    }

    /**
     * @dev Retrieves details of a product.
     * @param productId ID of the product to retrieve.
     * @return id Product ID.
     * @return name Product name.
     * @return description Product description.
     * @return currentOwner Current owner of the product.
     * @return status Current status of the product.
     */
    function getProduct(uint256 productId)
        external
        view
        returns (
            uint256 id,
            string memory name,
            string memory description,
            address currentOwner,
            string memory status
        )
    {
        Product storage product = products[productId];
        require(product.id != 0, "Product does not exist");

        return (product.id, product.name, product.description, product.currentOwner, product.status);
    }
}
```
