"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions, transparency, and immutable records using blockchain technology.
Generated: DETERMINISTIC_63edb71a501a92a2
Batch ID: 20250612_145923
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
 * @dev A smart contract for a decentralized marketplace that enables secure transactions,
 *      transparency, and immutable records on the Ethereum blockchain.
 */
contract Marketplace {
    // State variables
    uint256 public productCount = 0; // Tracks the number of products listed on the marketplace
    address public owner; // Contract owner address

    // Data structure for a Product
    struct Product {
        uint256 id; // Unique product ID
        string name; // Name of the product
        string description; // Description of the product
        uint256 price; // Price in wei
        address payable seller; // Address of the seller
        address buyer; // Address of the buyer
        bool purchased; // Whether the product has been purchased
    }

    // Mapping to store products by their ID
    mapping(uint256 => Product) public products;

    // Events
    event ProductListed(
        uint256 id,
        string name,
        string description,
        uint256 price,
        address seller
    );

    event ProductPurchased(
        uint256 id,
        string name,
        uint256 price,
        address seller,
        address buyer
    );

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier validProduct(uint256 _id) {
        require(_id > 0 && _id <= productCount, "Invalid product ID");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer of the contract as the owner
    }

    /**
     * @dev List a product on the marketplace.
     * @param _name Name of the product.
     * @param _description Description of the product.
     * @param _price Price of the product in wei.
     */
    function listProduct(string memory _name, string memory _description, uint256 _price) external {
        require(bytes(_name).length > 0, "Product name cannot be empty");
        require(bytes(_description).length > 0, "Product description cannot be empty");
        require(_price > 0, "Product price must be greater than zero");

        // Increment product count
        productCount++;

        // Create a new product and add it to the mapping
        products[productCount] = Product(
            productCount,
            _name,
            _description,
            _price,
            payable(msg.sender),
            address(0),
            false
        );

        // Emit event
        emit ProductListed(productCount, _name, _description, _price, msg.sender);
    }

    /**
     * @dev Purchase a product from the marketplace.
     * @param _id ID of the product to purchase.
     */
    function purchaseProduct(uint256 _id) external payable validProduct(_id) {
        Product storage product = products[_id];

        require(msg.sender != product.seller, "Seller cannot purchase their own product");
        require(!product.purchased, "Product has already been purchased");
        require(msg.value == product.price, "Incorrect payment amount");

        // Transfer payment to the seller
        product.seller.transfer(msg.value);

        // Update product details
        product.buyer = msg.sender;
        product.purchased = true;

        // Emit event
        emit ProductPurchased(_id, product.name, product.price, product.seller, msg.sender);
    }

    /**
     * @dev Get details of a specific product.
     * @param _id ID of the product.
     * @return Product details.
     */
    function getProduct(uint256 _id) external view validProduct(_id) returns (
        uint256 id,
        string memory name,
        string memory description,
        uint256 price,
        address seller,
        address buyer,
        bool purchased
    ) {
        Product memory product = products[_id];
        return (
            product.id,
            product.name,
            product.description,
            product.price,
            product.seller,
            product.buyer,
            product.purchased
        );
    }
}
```
