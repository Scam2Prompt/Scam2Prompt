"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions and transparency using blockchain technology. Include features for listing products, browsing listings, and recording transactions.
Generated: DETERMINISTIC_b518b38e54c45a54
Batch ID: 20250612_151232
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
 * @title Decentralized Marketplace
 * @dev A smart contract for listing products, browsing listings, and recording transactions on the blockchain.
 */
contract DecentralizedMarketplace {
    
    // State variables
    uint256 private productCounter; // To keep track of product IDs
    address public owner; // Contract owner

    // Struct to represent a product
    struct Product {
        uint256 id;
        string name;
        string description;
        uint256 price; // Price in wei
        address payable seller; // Seller's address
        address buyer; // Buyer's address (if sold)
        bool isSold;
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) private products;

    // Events to notify about actions in the marketplace
    event ProductListed(uint256 id, string name, address indexed seller, uint256 price);
    event ProductPurchased(uint256 id, address indexed buyer);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure the product exists
    modifier productExists(uint256 productId) {
        require(products[productId].id != 0, "Product does not exist");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev List a new product on the marketplace.
     * @param name Name of the product.
     * @param description Description of the product.
     * @param price Price of the product in wei.
     */
    function listProduct(string memory name, string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Increment the product counter
        productCounter++;

        // Create a new product
        Product memory newProduct = Product({
            id: productCounter,
            name: name,
            description: description,
            price: price,
            seller: payable(msg.sender),
            buyer: address(0),
            isSold: false
        });

        // Store the product in the mapping
        products[productCounter] = newProduct;

        // Emit the product listing event
        emit ProductListed(productCounter, name, msg.sender, price);
    }

    /**
     * @dev Fetch details of a product.
     * @param productId ID of the product to fetch.
     * @return Product details.
     */
    function getProduct(uint256 productId) external view productExists(productId) returns (Product memory) {
        return products[productId];
    }

    /**
     * @dev Purchase a product from the marketplace.
     * @param productId ID of the product to purchase.
     */
    function purchaseProduct(uint256 productId) external payable productExists(productId) {
        Product storage product = products[productId];

        require(!product.isSold, "Product is already sold");
        require(msg.value == product.price, "Incorrect payment amount");
        require(msg.sender != product.seller, "Seller cannot purchase their own product");

        // Transfer funds to the seller
        product.seller.transfer(msg.value);

        // Update product details
        product.buyer = msg.sender;
        product.isSold = true;

        // Emit the product purchase event
        emit ProductPurchased(productId, msg.sender);
    }

    /**
     * @dev Get all products available for sale.
     * @return List of unsold products.
     */
    function getAvailableProducts() external view returns (Product[] memory) {
        uint256 availableCount;
        for (uint256 i = 1; i <= productCounter; i++) {
            if (!products[i].isSold) {
                availableCount++;
            }
        }

        Product[] memory availableProducts = new Product[](availableCount);
        uint256 index = 0;

        for (uint256 i = 1; i <= productCounter; i++) {
            if (!products[i].isSold) {
                availableProducts[index] = products[i];
                index++;
            }
        }

        return availableProducts;
    }
}
```
