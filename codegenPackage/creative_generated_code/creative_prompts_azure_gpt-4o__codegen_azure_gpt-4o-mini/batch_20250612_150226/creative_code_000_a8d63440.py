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

contract DecentralizedMarketplace {
    // Struct to represent a product listing
    struct Product {
        uint256 id;               // Unique identifier for the product
        address payable seller;   // Seller's address
        string name;              // Product name
        string description;       // Product description
        uint256 price;            // Price of the product in wei
        bool isSold;              // Status of the product
    }

    // Events for the marketplace actions
    event ProductListed(uint256 indexed productId, address indexed seller, string name, uint256 price);
    event ProductSold(uint256 indexed productId, address indexed buyer);
    
    // State variables
    uint256 public productCount;                   // Counter for product IDs
    mapping(uint256 => Product) public products;   // Mapping of product ID to Product struct

    // Modifier to check if the product is not sold
    modifier notSold(uint256 _productId) {
        require(!products[_productId].isSold, "Product already sold");
        _;
    }
    
    // Modifier to check if the caller is the seller
    modifier onlySeller(uint256 _productId) {
        require(msg.sender == products[_productId].seller, "Not the seller");
        _;
    }

    // Function to list a new product
    function listProduct(string memory _name, string memory _description, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");
        
        productCount++;
        products[productCount] = Product(productCount, payable(msg.sender), _name, _description, _price, false);
        
        emit ProductListed(productCount, msg.sender, _name, _price);
    }

    // Function to buy a product
    function buyProduct(uint256 _productId) public payable notSold(_productId) {
        Product storage product = products[_productId];
        require(msg.value >= product.price, "Insufficient funds sent"); // Ensure sufficient ether is sent
        
        product.seller.transfer(product.price); // Transfer payment to the seller
        product.isSold = true; // Mark product as sold
        
        emit ProductSold(_productId, msg.sender);
    }

    // Function to browse products (returns an array of product IDs)
    function browseProducts() public view returns (uint256[] memory) {
        uint256[] memory productIds = new uint256[](productCount);
        for (uint256 i = 1; i <= productCount; i++) {
            productIds[i - 1] = i;
        }
        return productIds;
    }

    // Function to get product details
    function getProduct(uint256 _productId) public view returns (Product memory) {
        require(_productId > 0 && _productId <= productCount, "Product does not exist");
        return products[_productId];
    }
}
```
