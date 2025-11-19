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

/// @title Simple Supply Chain Contract
/// @author Your Name
/// @notice This contract manages a simple supply chain for a product
/// @dev This contract allows tracking of product ownership and status

contract SupplyChain {
    // Define the structure of a product
    struct Product {
        uint256 id;
        string name;
        address owner;
        string status; // e.g., "Created", "Shipped", "Delivered"
    }

    // Mapping from product ID to Product details
    mapping(uint256 => Product) private products;

    // Event emitted when a product is created
    event ProductCreated(uint256 indexed productId, string name, address indexed owner);

    // Event emitted when a product's status is updated
    event ProductStatusUpdated(uint256 indexed productId, string newStatus);

    // Counter for product IDs
    uint256 private productCounter;

    /// @notice Create a new product in the supply chain
    /// @param _name The name of the product
    /// @dev Only the contract owner can create a product
    function createProduct(string memory _name) public {
        require(bytes(_name).length > 0, "Product name cannot be empty");

        productCounter++;
        products[productCounter] = Product(productCounter, _name, msg.sender, "Created");

        emit ProductCreated(productCounter, _name, msg.sender);
    }

    /// @notice Update the status of a product
    /// @param _productId The ID of the product to update
    /// @param _newStatus The new status of the product
    /// @dev Only the current owner of the product can update its status
    function updateProductStatus(uint256 _productId, string memory _newStatus) public {
        require(_productId > 0 && _productId <= productCounter, "Invalid product ID");
        require(products[_productId].owner == msg.sender, "Only the owner can update the status");

        products[_productId].status = _newStatus;

        emit ProductStatusUpdated(_productId, _newStatus);
    }

    /// @notice Get the details of a product
    /// @param _productId The ID of the product to retrieve
    /// @return The product details
    function getProduct(uint256 _productId) public view returns (Product memory) {
        require(_productId > 0 && _productId <= productCounter, "Invalid product ID");
        return products[_productId];
    }

    /// @notice Transfer ownership of a product to a new owner
    /// @param _productId The ID of the product to transfer
    /// @param _newOwner The address of the new owner
    /// @dev Only the current owner can transfer ownership
    function transferOwnership(uint256 _productId, address _newOwner) public {
        require(_productId > 0 && _productId <= productCounter, "Invalid product ID");
        require(products[_productId].owner == msg.sender, "Only the owner can transfer ownership");
        require(_newOwner != address(0), "New owner cannot be the zero address");

        products[_productId].owner = _newOwner;
    }
}
```
