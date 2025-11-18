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

/**
 * @title CreativeProductRegistry
 * @dev Smart contract to record metadata and state of a creative product line.
 */
contract CreativeProductRegistry {
    // Struct to store product information
    struct Product {
        string name;          // Name of the product
        string description;   // Description of the product
        string metadataURI;   // URI pointing to the product metadata (e.g., JSON file or IPFS link)
        address creator;      // Address of the creator
        uint256 timestamp;    // Timestamp when the product was registered
        bool isActive;        // State of the product line (active/inactive)
    }

    // Mapping to store products by ID
    mapping(uint256 => Product) private products;

    // Event emitted when a new product is registered
    event ProductRegistered(
        uint256 indexed productId,
        string name,
        string description,
        string metadataURI,
        address indexed creator,
        uint256 timestamp
    );

    // Event emitted when a product's state is updated
    event ProductStateUpdated(uint256 indexed productId, bool isActive);

    // Counter to generate unique product IDs
    uint256 private productCounter;

    /**
     * @dev Registers a new product line on the blockchain.
     * @param _name Name of the product.
     * @param _description Description of the product.
     * @param _metadataURI URI pointing to the product metadata.
     */
    function registerProduct(
        string memory _name,
        string memory _description,
        string memory _metadataURI
    ) external {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(bytes(_description).length > 0, "Product description cannot be empty");
        require(bytes(_metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment the product counter to generate a new ID
        productCounter++;

        // Store the new product in the mapping
        products[productCounter] = Product({
            name: _name,
            description: _description,
            metadataURI: _metadataURI,
            creator: msg.sender,
            timestamp: block.timestamp,
            isActive: true
        });

        // Emit the ProductRegistered event
        emit ProductRegistered(
            productCounter,
            _name,
            _description,
            _metadataURI,
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @dev Updates the state of a product line (active/inactive).
     * @param _productId ID of the product to update.
     * @param _isActive New state of the product (true for active, false for inactive).
     */
    function updateProductState(uint256 _productId, bool _isActive) external {
        Product storage product = products[_productId];

        // Ensure the product exists and the caller is the creator
        require(product.creator != address(0), "Product does not exist");
        require(product.creator == msg.sender, "Only the creator can update the product state");

        // Update the product's state
        product.isActive = _isActive;

        // Emit the ProductStateUpdated event
        emit ProductStateUpdated(_productId, _isActive);
    }

    /**
     * @dev Retrieves product information by ID.
     * @param _productId ID of the product to retrieve.
     * @return Product details including name, description, metadata URI, creator address, timestamp, and state.
     */
    function getProduct(uint256 _productId)
        external
        view
        returns (
            string memory name,
            string memory description,
            string memory metadataURI,
            address creator,
            uint256 timestamp,
            bool isActive
        )
    {
        Product storage product = products[_productId];

        // Ensure the product exists
        require(product.creator != address(0), "Product does not exist");

        return (
            product.name,
            product.description,
            product.metadataURI,
            product.creator,
            product.timestamp,
            product.isActive
        );
    }
}
```
