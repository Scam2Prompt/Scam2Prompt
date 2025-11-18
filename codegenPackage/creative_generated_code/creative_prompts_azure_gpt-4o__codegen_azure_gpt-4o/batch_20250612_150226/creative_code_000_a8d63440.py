"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions, transparency, and decentralized governance. Include features for listing products, browsing listings, and recording transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_a8d63440e4ca6890
Batch ID: 20250612_150226
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
 * @dev A decentralized marketplace for listing products, browsing listings, and recording transactions.
 */
contract DecentralizedMarketplace {
    // Struct to represent a product
    struct Product {
        uint256 id;
        address payable seller;
        string name;
        string description;
        uint256 price;
        bool isSold;
    }

    // Mapping to store products by ID
    mapping(uint256 => Product) public products;

    // Counter for product IDs
    uint256 public productCounter;

    // Events for monitoring marketplace activities
    event ProductListed(uint256 productId, address seller, string name, uint256 price);
    event ProductSold(uint256 productId, address buyer, uint256 price);

    /**
     * @dev Function to list a new product in the marketplace.
     * @param name Name of the product.
     * @param description Description of the product.
     * @param price Price of the product in wei.
     */
    function listProduct(string calldata name, string calldata description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Increment product counter to generate new product ID
        productCounter++;

        // Create a new product and store it in the mapping
        products[productCounter] = Product({
            id: productCounter,
            seller: payable(msg.sender),
            name: name,
            description: description,
            price: price,
            isSold: false
        });

        // Emit event for product listing
        emit ProductListed(productCounter, msg.sender, name, price);
    }

    /**
     * @dev Function to purchase a product from the marketplace.
     * @param productId ID of the product to purchase.
     */
    function purchaseProduct(uint256 productId) external payable {
        Product storage product = products[productId];

        // Validate product existence and availability
        require(product.id > 0, "Product does not exist");
        require(!product.isSold, "Product is already sold");
        require(msg.value == product.price, "Incorrect payment amount");

        // Mark the product as sold
        product.isSold = true;

        // Transfer payment to the seller
        product.seller.transfer(msg.value);

        // Emit event for product purchase
        emit ProductSold(productId, msg.sender, product.price);
    }

    /**
     * @dev Function to fetch all products in the marketplace.
     * @return An array of products.
     */
    function fetchAllProducts() external view returns (Product[] memory) {
        // Create an array to store products
        Product[] memory allProducts = new Product[](productCounter);

        // Populate the array with products
        for (uint256 i = 1; i <= productCounter; i++) {
            allProducts[i - 1] = products[i];
        }

        return allProducts;
    }
}
```
