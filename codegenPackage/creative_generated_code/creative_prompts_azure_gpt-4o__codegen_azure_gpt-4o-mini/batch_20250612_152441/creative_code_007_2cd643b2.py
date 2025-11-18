"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Develop a smart contract to facilitate direct marketing and promotion for coffee farmers, ensuring full control over product pricing and listing as outlined in the Crypto N' Kafe ecosystem.
Generated: DETERMINISTIC_2cd643b2eea2a308
Batch ID: 20250612_152441
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

// Importing OpenZeppelin's ReentrancyGuard for security
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Define the CoffeeFarmersMarketing contract
contract CoffeeFarmersMarketing is ReentrancyGuard {
    // Struct to represent a coffee product
    struct CoffeeProduct {
        uint256 id;
        address owner;
        string name;
        string description;
        uint256 price; // in wei
        bool isListed;
    }

    // Mapping to store coffee products by ID
    mapping(uint256 => CoffeeProduct) public products;
    // Counter for the product IDs
    uint256 public productCounter;

    // Event for product creation
    event ProductCreated(uint256 indexed productId, address indexed owner, string name, uint256 price);
    // Event for product updated
    event ProductUpdated(uint256 indexed productId, uint256 newPrice);
    // Event for product listing status change
    event ProductListingStatusChanged(uint256 indexed productId, bool isListed);

    // Function to create a new coffee product
    function createProduct(string memory _name, string memory _description, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        productCounter++;
        products[productCounter] = CoffeeProduct({
            id: productCounter,
            owner: msg.sender,
            name: _name,
            description: _description,
            price: _price,
            isListed: true
        });

        emit ProductCreated(productCounter, msg.sender, _name, _price);
    }

    // Function to update the price of a coffee product
    function updateProductPrice(uint256 _productId, uint256 _newPrice) external {
        require(products[_productId].owner == msg.sender, "Only the owner can update the price");
        require(_newPrice > 0, "New price must be greater than zero");

        products[_productId].price = _newPrice;

        emit ProductUpdated(_productId, _newPrice);
    }

    // Function to change the listing status of a coffee product
    function changeListingStatus(uint256 _productId, bool _isListed) external {
        require(products[_productId].owner == msg.sender, "Only the owner can change the listing status");

        products[_productId].isListed = _isListed;

        emit ProductListingStatusChanged(_productId, _isListed);
    }

    // Function to get product details
    function getProduct(uint256 _productId) external view returns (CoffeeProduct memory) {
        return products[_productId];
    }

    // Function to purchase a coffee product
    function purchaseProduct(uint256 _productId) external payable nonReentrant {
        CoffeeProduct storage product = products[_productId];

        require(product.isListed, "Product is not listed for sale");
        require(msg.value >= product.price, "Insufficient payment");

        // Transfer ownership and funds
        product.owner = msg.sender;
        product.isListed = false;

        // Transfer the funds to the seller (initial owner)
        payable(product.owner).transfer(msg.value);

        emit ProductListingStatusChanged(_productId, false);
    }
}
```
