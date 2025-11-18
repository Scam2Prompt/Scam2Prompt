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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for a decentralized marketplace
contract DecentralizedMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a product
    struct Product {
        uint256 id;
        string name;
        string description;
        uint256 price;
        address seller;
        bool isAvailable;
    }

    // Events for logging
    event ProductListed(uint256 indexed productId, string name, uint256 price, address indexed seller);
    event ProductSold(uint256 indexed productId, address indexed buyer);
    event ProductUpdated(uint256 indexed productId, uint256 newPrice);
    event ProductRemoved(uint256 indexed productId);
    
    // Mapping to store products by ID
    mapping(uint256 => Product) public products;
    Counters.Counter private productIdCounter; // Counter for product IDs

    // Modifier to check if product exists
    modifier productExists(uint256 productId) {
        require(products[productId].seller != address(0), "Product does not exist.");
        _;
    }

    // Modifier to check if the product is available
    modifier isAvailable(uint256 productId) {
        require(products[productId].isAvailable, "Product is not available.");
        _;
    }

    // Function to list a new product
    function listProduct(string memory name, string memory description, uint256 price) public {
        require(price > 0, "Price must be greater than zero.");
        
        // Increment product ID counter and create a new product
        productIdCounter.increment();
        uint256 newProductId = productIdCounter.current();
        
        products[newProductId] = Product(newProductId, name, description, price, msg.sender, true);
        
        emit ProductListed(newProductId, name, price, msg.sender);
    }

    // Function to buy a product
    function buyProduct(uint256 productId) public payable productExists(productId) isAvailable(productId) {
        Product storage product = products[productId];
        
        // Ensure the buyer sends the correct amount of Ether
        require(msg.value >= product.price, "Insufficient payment.");

        // Transfer Ether to the seller
        payable(product.seller).transfer(product.price);

        // Mark product as sold
        product.isAvailable = false;

        emit ProductSold(productId, msg.sender);
    }

    // Function to update product price
    function updateProductPrice(uint256 productId, uint256 newPrice) public productExists(productId) isAvailable(productId) {
        require(msg.sender == products[productId].seller, "Only the seller can update the price.");
        require(newPrice > 0, "Price must be greater than zero.");
        
        products[productId].price = newPrice;
        
        emit ProductUpdated(productId, newPrice);
    }

    // Function to remove a product
    function removeProduct(uint256 productId) public productExists(productId) {
        require(msg.sender == products[productId].seller, "Only the seller can remove the product.");
        
        delete products[productId];
        
        emit ProductRemoved(productId);
    }

    // Function to view product details
    function getProduct(uint256 productId) public view productExists(productId) returns (Product memory) {
        return products[productId];
    }

    // Fallback function to prevent Ether from being sent to the contract directly
    receive() external payable {
        revert("Direct payments not allowed. Use the buyProduct function.");
    }
}
```
