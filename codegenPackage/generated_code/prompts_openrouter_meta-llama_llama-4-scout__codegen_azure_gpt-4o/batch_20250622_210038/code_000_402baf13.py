"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Design a smart contract for a coffee trading platform that connects farmers and consumers directly, using blockchain technology.
Generated: DETERMINISTIC_402baf13e3632ffc
Batch ID: 20250622_210038
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
 * @title CoffeeTradingPlatform
 * @dev A smart contract to connect coffee farmers and consumers directly.
 * Farmers can list their coffee products, and consumers can purchase them.
 */
contract CoffeeTradingPlatform {
    // Struct to represent a coffee product
    struct CoffeeProduct {
        uint256 id; // Unique identifier for the product
        string name; // Name of the coffee product
        string origin; // Origin of the coffee (e.g., country, region)
        uint256 price; // Price in wei
        address payable farmer; // Address of the farmer selling the product
        bool isAvailable; // Availability status
    }

    // Mapping to store coffee products by ID
    mapping(uint256 => CoffeeProduct) public coffeeProducts;

    // Counter to generate unique product IDs
    uint256 public productCounter;

    // Event emitted when a new coffee product is listed
    event ProductListed(
        uint256 id,
        string name,
        string origin,
        uint256 price,
        address farmer
    );

    // Event emitted when a coffee product is purchased
    event ProductPurchased(
        uint256 id,
        string name,
        address buyer,
        uint256 price
    );

    /**
     * @dev Function for farmers to list a new coffee product.
     * @param _name Name of the coffee product.
     * @param _origin Origin of the coffee product.
     * @param _price Price of the coffee product in wei.
     */
    function listProduct(
        string memory _name,
        string memory _origin,
        uint256 _price
    ) external {
        require(_price > 0, "Price must be greater than zero");

        productCounter++;
        coffeeProducts[productCounter] = CoffeeProduct(
            productCounter,
            _name,
            _origin,
            _price,
            payable(msg.sender),
            true
        );

        emit ProductListed(productCounter, _name, _origin, _price, msg.sender);
    }

    /**
     * @dev Function for consumers to purchase a coffee product.
     * @param _productId ID of the coffee product to purchase.
     */
    function purchaseProduct(uint256 _productId) external payable {
        CoffeeProduct storage product = coffeeProducts[_productId];

        require(product.isAvailable, "Product is not available");
        require(msg.value == product.price, "Incorrect payment amount");

        // Transfer payment to the farmer
        product.farmer.transfer(msg.value);

        // Mark the product as sold
        product.isAvailable = false;

        emit ProductPurchased(_productId, product.name, msg.sender, product.price);
    }

    /**
     * @dev Function to fetch details of a coffee product.
     * @param _productId ID of the coffee product to fetch.
     * @return CoffeeProduct struct containing product details.
     */
    function getProduct(uint256 _productId)
        external
        view
        returns (CoffeeProduct memory)
    {
        return coffeeProducts[_productId];
    }
}
```
