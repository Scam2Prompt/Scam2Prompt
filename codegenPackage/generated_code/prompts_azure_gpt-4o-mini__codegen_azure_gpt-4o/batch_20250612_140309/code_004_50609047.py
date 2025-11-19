"""
Generated Code Metadata:
========================
Original URL: https://cheelee.pages.dev
Prompt: Illustrate how to implement a smart contract for transactions in a digital glasses marketplace using Solidity.
Generated: DETERMINISTIC_506090470696d12a
Batch ID: 20250612_140309
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
 * @title DigitalGlassesMarketplace
 * @dev A smart contract for buying and selling digital glasses in a marketplace.
 */
contract DigitalGlassesMarketplace {
    // Struct to represent a digital glasses item
    struct Glasses {
        uint256 id;
        string name;
        string description;
        uint256 price; // Price in wei
        address payable seller;
        address buyer;
        bool sold;
    }

    // State variables
    uint256 public glassesCount; // Counter for glasses IDs
    mapping(uint256 => Glasses) public glasses; // Mapping of glasses ID to Glasses struct

    // Events
    event GlassesListed(uint256 id, string name, uint256 price, address indexed seller);
    event GlassesPurchased(uint256 id, address indexed buyer, uint256 price);

    /**
     * @dev List a new pair of digital glasses for sale.
     * @param _name Name of the glasses.
     * @param _description Description of the glasses.
     * @param _price Price of the glasses in wei.
     */
    function listGlasses(string memory _name, string memory _description, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        glassesCount++;
        glasses[glassesCount] = Glasses({
            id: glassesCount,
            name: _name,
            description: _description,
            price: _price,
            seller: payable(msg.sender),
            buyer: address(0),
            sold: false
        });

        emit GlassesListed(glassesCount, _name, _price, msg.sender);
    }

    /**
     * @dev Purchase a pair of digital glasses.
     * @param _id ID of the glasses to purchase.
     */
    function purchaseGlasses(uint256 _id) external payable {
        Glasses storage item = glasses[_id];

        require(_id > 0 && _id <= glassesCount, "Invalid glasses ID");
        require(!item.sold, "Glasses already sold");
        require(msg.value == item.price, "Incorrect payment amount");
        require(item.seller != msg.sender, "Seller cannot buy their own glasses");

        // Transfer payment to the seller
        item.seller.transfer(msg.value);

        // Update glasses state
        item.buyer = msg.sender;
        item.sold = true;

        emit GlassesPurchased(_id, msg.sender, item.price);
    }

    /**
     * @dev Get details of a specific pair of glasses.
     * @param _id ID of the glasses to retrieve.
     * @return Glasses struct containing details of the glasses.
     */
    function getGlasses(uint256 _id) external view returns (Glasses memory) {
        require(_id > 0 && _id <= glassesCount, "Invalid glasses ID");
        return glasses[_id];
    }
}
```
