"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a smart contract to facilitate direct marketing and promotion for coffee farmers, ensuring full control over product pricing and listing as outlined in the Crypto N' Kafe ecosystem.
Generated: DETERMINISTIC_2cd643b2eea2a308
Batch ID: 20250612_152441
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

// Smart contract for managing coffee farmers' product listings and pricing
contract CoffeeFarmersMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a coffee product
    struct CoffeeProduct {
        uint256 id;
        string name;
        string description;
        uint256 price; // Price in wei
        address payable farmer; // Farmer's address
        bool isListed; // Listing status
    }

    // Mapping to store coffee products by their ID
    mapping(uint256 => CoffeeProduct) private products;
    Counters.Counter private productIdCounter; // Counter for product IDs

    // Event emitted when a new product is listed
    event ProductListed(uint256 indexed productId, string name, uint256 price, address indexed farmer);
    
    // Event emitted when a product is purchased
    event ProductPurchased(uint256 indexed productId, address indexed buyer);

    // Modifier to check if the product is listed
    modifier onlyListed(uint256 productId) {
        require(products[productId].isListed, "Product is not listed");
        _;
    }

    // Function to list a new coffee product
    function listProduct(string memory name, string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        productIdCounter.increment();
        uint256 newProductId = productIdCounter.current();

        products[newProductId] = CoffeeProduct({
            id: newProductId,
            name: name,
            description: description,
            price: price,
            farmer: payable(msg.sender),
            isListed: true
        });

        emit ProductListed(newProductId, name, price, msg.sender);
    }

    // Function to purchase a coffee product
    function purchaseProduct(uint256 productId) external payable onlyListed(productId) {
        CoffeeProduct storage product = products[productId];
        require(msg.value >= product.price, "Insufficient payment");

        // Transfer payment to the farmer
        product.farmer.transfer(product.price);

        // Emit purchase event
        emit ProductPurchased(productId, msg.sender);
    }

    // Function to update the price of a listed product
    function updateProductPrice(uint256 productId, uint256 newPrice) external onlyListed(productId) {
        CoffeeProduct storage product = products[productId];
        require(msg.sender == product.farmer, "Only the farmer can update the price");
        require(newPrice > 0, "Price must be greater than zero");

        product.price = newPrice;
    }

    // Function to delist a product
    function delistProduct(uint256 productId) external onlyListed(productId) {
        CoffeeProduct storage product = products[productId];
        require(msg.sender == product.farmer, "Only the farmer can delist the product");

        product.isListed = false;
    }

    // Function to get product details
    function getProduct(uint256 productId) external view returns (CoffeeProduct memory) {
        return products[productId];
    }
}
```
