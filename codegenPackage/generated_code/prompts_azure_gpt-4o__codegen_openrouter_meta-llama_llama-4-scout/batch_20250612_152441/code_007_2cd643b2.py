"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Develop a smart contract to facilitate direct marketing and promotion for coffee farmers, ensuring full control over product pricing and listing as outlined in the Crypto N' Kafe ecosystem.
Generated: DETERMINISTIC_2cd643b2eea2a308
Batch ID: 20250612_152441
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Crypto N' Kafe Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates direct marketing and promotion for coffee farmers,
 *         ensuring full control over product pricing and listing.
 */
contract CryptoNKafe {
    // Mapping of coffee farmers to their product listings
    mapping (address => Product[]) public farmerProducts;

    // Mapping of product IDs to their respective farmers
    mapping (uint256 => address) public productOwners;

    // Mapping of product IDs to their respective details
    mapping (uint256 => Product) public products;

    // Product ID counter
    uint256 public productIdCounter;

    // Event emitted when a new product is listed
    event NewProductListed(uint256 productId, address farmer, string name, uint256 price);

    // Event emitted when a product is updated
    event ProductUpdated(uint256 productId, address farmer, string name, uint256 price);

    // Event emitted when a product is removed
    event ProductRemoved(uint256 productId, address farmer);

    // Struct representing a product
    struct Product {
        uint256 id;
        string name;
        uint256 price;
    }

    /**
     * @dev Lists a new product for a coffee farmer
     * @param _name Name of the product
     * @param _price Price of the product
     */
    function listProduct(string memory _name, uint256 _price) public {
        // Create a new product
        Product memory product = Product({
            id: productIdCounter,
            name: _name,
            price: _price
        });

        // Add product to farmer's product list
        farmerProducts[msg.sender].push(product);

        // Update product owners and products mappings
        productOwners[productIdCounter] = msg.sender;
        products[productIdCounter] = product;

        // Increment product ID counter
        productIdCounter++;

        // Emit NewProductListed event
        emit NewProductListed(product.id, msg.sender, product.name, product.price);
    }

    /**
     * @dev Updates a product listing for a coffee farmer
     * @param _productId ID of the product to update
     * @param _name New name of the product
     * @param _price New price of the product
     */
    function updateProduct(uint256 _productId, string memory _name, uint256 _price) public {
        // Check if product exists and is owned by the caller
        require(productOwners[_productId] == msg.sender, "Only the product owner can update the product");

        // Update product details
        products[_productId].name = _name;
        products[_productId].price = _price;

        // Emit ProductUpdated event
        emit ProductUpdated(_productId, msg.sender, _name, _price);
    }

    /**
     * @dev Removes a product listing for a coffee farmer
     * @param _productId ID of the product to remove
     */
    function removeProduct(uint256 _productId) public {
        // Check if product exists and is owned by the caller
        require(productOwners[_productId] == msg.sender, "Only the product owner can remove the product");

        // Remove product from farmer's product list
        for (uint256 i = 0; i < farmerProducts[msg.sender].length; i++) {
            if (farmerProducts[msg.sender][i].id == _productId) {
                farmerProducts[msg.sender].splice(i, 1);
                break;
            }
        }

        // Emit ProductRemoved event
        emit ProductRemoved(_productId, msg.sender);
    }

    /**
     * @dev Gets a list of products for a coffee farmer
     * @param _farmer Address of the coffee farmer
     * @return A list of products
     */
    function getProducts(address _farmer) public view returns (Product[] memory) {
        return farmerProducts[_farmer];
    }

    /**
     * @dev Gets a product by ID
     * @param _productId ID of the product
     * @return The product details
     */
    function getProduct(uint256 _productId) public view returns (Product memory) {
        return products[_productId];
    }
}
```
