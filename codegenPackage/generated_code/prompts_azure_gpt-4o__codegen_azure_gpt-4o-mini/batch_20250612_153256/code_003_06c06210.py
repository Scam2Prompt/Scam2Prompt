"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Develop a Solidity smart contract that records the metadata and state of a creative product line on the blockchain, ensuring immutability and transparency.
Generated: DETERMINISTIC_06c06210563e1fcd
Batch ID: 20250612_153256
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CreativeProductLine
 * @dev A smart contract to record the metadata and state of a creative product line
 */
contract CreativeProductLine is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold product metadata
    struct Product {
        uint256 id;
        string name;
        string description;
        string metadataURI; // URI for additional metadata (e.g., IPFS link)
        bool isActive; // State of the product (active/inactive)
    }

    // Mapping from product ID to Product struct
    mapping(uint256 => Product) private products;

    // Counter for product IDs
    Counters.Counter private productIdCounter;

    // Event emitted when a new product is added
    event ProductAdded(uint256 indexed productId, string name, string description, string metadataURI);

    // Event emitted when a product state is updated
    event ProductStateUpdated(uint256 indexed productId, bool isActive);

    /**
     * @dev Adds a new product to the product line
     * @param _name The name of the product
     * @param _description A brief description of the product
     * @param _metadataURI A URI pointing to additional metadata
     */
    function addProduct(string memory _name, string memory _description, string memory _metadataURI) external onlyOwner {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(bytes(_description).length > 0, "Product description cannot be empty");
        require(bytes(_metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment the product ID counter
        productIdCounter.increment();
        uint256 newProductId = productIdCounter.current();

        // Create a new product and store it in the mapping
        products[newProductId] = Product(newProductId, _name, _description, _metadataURI, true);

        // Emit the ProductAdded event
        emit ProductAdded(newProductId, _name, _description, _metadataURI);
    }

    /**
     * @dev Updates the state of an existing product
     * @param _productId The ID of the product to update
     * @param _isActive The new state of the product (active/inactive)
     */
    function updateProductState(uint256 _productId, bool _isActive) external onlyOwner {
        Product storage product = products[_productId];
        require(product.id != 0, "Product does not exist");

        // Update the product state
        product.isActive = _isActive;

        // Emit the ProductStateUpdated event
        emit ProductStateUpdated(_productId, _isActive);
    }

    /**
     * @dev Retrieves the details of a product
     * @param _productId The ID of the product to retrieve
     * @return The product details
     */
    function getProduct(uint256 _productId) external view returns (Product memory) {
        Product storage product = products[_productId];
        require(product.id != 0, "Product does not exist");
        return product;
    }

    /**
     * @dev Retrieves the total number of products
     * @return The total number of products added
     */
    function totalProducts() external view returns (uint256) {
        return productIdCounter.current();
    }
}
```
