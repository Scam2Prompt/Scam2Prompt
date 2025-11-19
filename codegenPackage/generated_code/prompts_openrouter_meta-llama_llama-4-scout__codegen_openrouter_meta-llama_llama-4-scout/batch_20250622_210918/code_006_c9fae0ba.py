"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.pages.dev
Prompt: "Develop a basic smart contract in Solidity for a decentralized marketplace, ensuring secure transactions and transparent records, as featured in the Pushd platform."
Generated: DETERMINISTIC_c9fae0ba77514a0f
Batch ID: 20250622_210918
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Pushd Marketplace Smart Contract
 * @author [Your Name]
 * @notice A basic smart contract for a decentralized marketplace.
 */
contract PushdMarketplace {
    // Mapping of product IDs to their respective owners
    mapping(address => mapping(uint256 => Product)) public products;

    // Mapping of product IDs to their respective prices
    mapping(uint256 => uint256) public prices;

    // Mapping of product IDs to their respective statuses (0 - available, 1 - sold, 2 - removed)
    mapping(uint256 => uint8) public productStatuses;

    // Event emitted when a new product is added
    event NewProduct(address indexed owner, uint256 productId);

    // Event emitted when a product is sold
    event ProductSold(address indexed buyer, uint256 productId);

    // Event emitted when a product is removed
    event ProductRemoved(address indexed owner, uint256 productId);

    // Struct representing a product
    struct Product {
        uint256 id;
        string name;
        string description;
        address owner;
    }

    // Counter for product IDs
    Counters.Counter private _productIds;

    /**
     * @notice Adds a new product to the marketplace
     * @param _name Product name
     * @param _description Product description
     * @param _price Product price
     */
    function addProduct(string memory _name, string memory _description, uint256 _price) public {
        // Increment product ID counter
        _productIds.increment();

        // Create a new product
        uint256 productId = _productIds.current();
        Product memory product = Product(productId, _name, _description, msg.sender);

        // Store product data
        products[msg.sender][productId] = product;

        // Set product price
        prices[productId] = _price;

        // Set product status to available
        productStatuses[productId] = 0;

        // Emit event
        emit NewProduct(msg.sender, productId);
    }

    /**
     * @notice Buys a product from the marketplace
     * @param _productId Product ID
     */
    function buyProduct(uint256 _productId) public payable {
        // Check if product exists and is available
        require(productStatuses[_productId] == 0, "Product is not available");

        // Get product owner and price
        address productOwner = products[msg.sender][_productId].owner;
        uint256 productPrice = prices[_productId];

        // Check if buyer has paid the correct price
        require(msg.value == productPrice, "Incorrect price");

        // Transfer ownership to buyer
        products[productOwner][_productId].owner = msg.sender;

        // Update product status
        productStatuses[_productId] = 1;

        // Emit event
        emit ProductSold(msg.sender, _productId);
    }

    /**
     * @notice Removes a product from the marketplace
     * @param _productId Product ID
     */
    function removeProduct(uint256 _productId) public {
        // Check if product exists and is owned by caller
        require(products[msg.sender][_productId].owner == msg.sender, "Product does not exist or is not owned by caller");

        // Update product status
        productStatuses[_productId] = 2;

        // Emit event
        emit ProductRemoved(msg.sender, _productId);
    }

    /**
     * @notice Gets product details
     * @param _productId Product ID
     * @return Product details
     */
    function getProduct(uint256 _productId) public view returns (uint256, string memory, string memory, address) {
        Product memory product = products[msg.sender][_productId];
        return (product.id, product.name, product.description, product.owner);
    }
}
```
