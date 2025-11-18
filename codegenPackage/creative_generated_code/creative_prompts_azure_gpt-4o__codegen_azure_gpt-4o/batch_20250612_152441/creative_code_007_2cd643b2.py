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

Certainly! Below is a clean, production-ready smart contract written in Solidity for the Ethereum blockchain. This contract allows coffee farmers to list their products, set pricing, and manage sales.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CryptoNKafeMarketplace
 * @dev A smart contract for coffee farmers to list and sell their products directly.
 * Farmers have full control over pricing and listings in the Crypto N' Kafe ecosystem.
 */
contract CryptoNKafeMarketplace {
    // Struct to represent a coffee product
    struct CoffeeProduct {
        uint256 id; // Unique ID for the product
        string name; // Name of the coffee product
        string description; // Description of the product
        uint256 price; // Price in wei (1 ETH = 10^18 wei)
        address payable farmer; // Address of the farmer who listed the product
        bool isAvailable; // Availability of the product
    }

    // Mapping to store coffee products by ID
    mapping(uint256 => CoffeeProduct) public coffeeProducts;

    // Counter to generate unique product IDs
    uint256 private nextProductId;

    // Event emitted when a product is listed
    event ProductListed(
        uint256 indexed id,
        string name,
        uint256 price,
        address indexed farmer
    );

    // Event emitted when a product is purchased
    event ProductPurchased(
        uint256 indexed id,
        string name,
        uint256 price,
        address indexed buyer,
        address indexed farmer
    );

    /**
     * @dev Function for farmers to list a new coffee product.
     * @param name Name of the coffee product.
     * @param description Description of the product.
     * @param price Price of the product in wei.
     */
    function listProduct(
        string memory name,
        string memory description,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero");

        uint256 productId = nextProductId;

        coffeeProducts[productId] = CoffeeProduct({
            id: productId,
            name: name,
            description: description,
            price: price,
            farmer: payable(msg.sender),
            isAvailable: true
        });

        nextProductId++;

        emit ProductListed(productId, name, price, msg.sender);
    }

    /**
     * @dev Function for customers to purchase a coffee product.
     * The payment is sent directly to the farmer's address.
     * @param productId ID of the product to purchase.
     */
    function purchaseProduct(uint256 productId) external payable {
        CoffeeProduct storage product = coffeeProducts[productId];

        require(product.isAvailable, "Product is not available for purchase");
        require(msg.value == product.price, "Incorrect payment amount");

        // Transfer payment to the farmer
        product.farmer.transfer(msg.value);

        // Mark the product as unavailable after purchase
        product.isAvailable = false;

        emit ProductPurchased(
            product.id,
            product.name,
            product.price,
            msg.sender,
            product.farmer
        );
    }

    /**
     * @dev Function for farmers to update product availability.
     * @param productId ID of the product to update.
     * @param isAvailable New availability status of the product.
     */
    function updateAvailability(uint256 productId, bool isAvailable) external {
        CoffeeProduct storage product = coffeeProducts[productId];

        require(
            msg.sender == product.farmer,
            "Only the farmer can update product availability"
        );

        product.isAvailable = isAvailable;
    }

    /**
     * @dev Get details of a coffee product.
     * @param productId ID of the product to retrieve.
     * @return CoffeeProduct Struct containing product details.
     */
    function getProduct(uint256 productId)
        external
        view
        returns (CoffeeProduct memory)
    {
        return coffeeProducts[productId];
    }
}
```

This contract is ready for deployment on an Ethereum network and fulfills the requirements of enabling coffee farmers to control pricing and listings while allowing direct sales.
