"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions and immutable records using Ethereum blockchain technology. Include functionality for listing products, browsing listings, and completing transactions.
Generated: DETERMINISTIC_7fb7cc13e917197d
Batch ID: 20250612_152249
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
 * @dev A smart contract for a decentralized marketplace similar to Pushd.
 * Users can list products, browse listings, and complete transactions securely.
 */
contract DecentralizedMarketplace {

    // Struct to represent a product listing
    struct Product {
        uint256 id;             // Unique identifier for the product
        address payable seller; // Address of the seller
        string name;            // Product name
        string description;     // Product description
        uint256 price;          // Product price (in wei)
        bool sold;              // Indicates if the product has been sold
    }

    // Event emitted when a product is listed
    event ProductListed(uint256 id, address indexed seller, string name, uint256 price);

    // Event emitted when a transaction is completed
    event ProductPurchased(uint256 id, address indexed buyer, address indexed seller, uint256 price);

    // Mapping to store product listings
    mapping(uint256 => Product) public products;

    // Counter to generate unique product IDs
    uint256 private productCounter;

    /**
     * @dev Lists a new product in the marketplace.
     * @param name Name of the product.
     * @param description Description of the product.
     * @param price Price of the product (in wei).
     */
    function listProduct(string memory name, string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        productCounter++;

        // Create and store the product
        products[productCounter] = Product({
            id: productCounter,
            seller: payable(msg.sender),
            name: name,
            description: description,
            price: price,
            sold: false
        });

        emit ProductListed(productCounter, msg.sender, name, price);
    }

    /**
     * @dev Allows a user to purchase a product.
     * @param productId ID of the product to purchase.
     */
    function purchaseProduct(uint256 productId) external payable {
        Product memory product = products[productId];

        require(product.id != 0, "Product does not exist"); // Check that the product exists
        require(!product.sold, "Product already sold");     // Check that the product is not sold
        require(msg.value == product.price, "Incorrect payment amount"); // Ensure correct payment

        // Update product state
        product.sold = true;
        products[productId] = product;

        // Transfer funds to the seller
        product.seller.transfer(msg.value);

        emit ProductPurchased(productId, msg.sender, product.seller, product.price);
    }

    /**
     * @dev Retrieves product information.
     * @param productId ID of the product to fetch.
     * @return Product details.
     */
    function getProduct(uint256 productId) external view returns (Product memory) {
        Product memory product = products[productId];
        require(product.id != 0, "Product does not exist"); // Check that the product exists
        return product;
    }

    /**
     * @dev Retrieves the total number of products listed.
     * @return Total product count.
     */
    function getProductCount() external view returns (uint256) {
        return productCounter;
    }
}
```
