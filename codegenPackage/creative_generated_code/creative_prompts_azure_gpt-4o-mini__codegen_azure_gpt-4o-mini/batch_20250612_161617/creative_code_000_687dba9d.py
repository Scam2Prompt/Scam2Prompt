"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-store-en.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates secure transactions on a decentralized marketplace like Pushd, utilizing Ethereum blockchain technology.
Generated: DETERMINISTIC_687dba9d89ca95e5
Batch ID: 20250612_161617
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
 * @title Decentralized Marketplace Smart Contract
 * @dev This contract facilitates secure transactions in a decentralized marketplace
 */
contract Marketplace {
    // Struct to represent an item for sale
    struct Item {
        uint256 id;             // Unique identifier for the item
        address payable seller; // Address of the seller
        string name;           // Name of the item
        uint256 price;         // Price of the item in wei
        bool isSold;           // Status of the item (sold or not)
    }

    // Mapping to store items by their unique ID
    mapping(uint256 => Item) public items;
    uint256 public itemCount; // Counter for items

    // Event to emit when a new item is added
    event ItemAdded(uint256 id, string name, uint256 price, address seller);
    
    // Event to emit when an item is sold
    event ItemSold(uint256 id, address buyer);

    /**
     * @dev Add a new item to the marketplace
     * @param _name Name of the item
     * @param _price Price of the item (in wei)
     */
    function addItem(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero"); // Ensure valid price
        itemCount++; // Increment item count
        items[itemCount] = Item(itemCount, payable(msg.sender), _name, _price, false); // Add item to mapping
        emit ItemAdded(itemCount, _name, _price, msg.sender); // Emit event
    }

    /**
     * @dev Purchase an item from the marketplace
     * @param _id ID of the item to purchase
     */
    function purchaseItem(uint256 _id) public payable {
        Item storage item = items[_id]; // Reference to the item

        // Ensure item exists and is not sold
        require(_id > 0 && _id <= itemCount, "Item does not exist");
        require(!item.isSold, "Item is already sold");
        require(msg.value == item.price, "Incorrect price sent"); // Ensure correct amount sent

        item.seller.transfer(msg.value); // Transfer payment to the seller
        item.isSold = true; // Mark item as sold
        emit ItemSold(_id, msg.sender); // Emit event
    }

    /**
     * @dev Get details of an item
     * @param _id ID of the item
     * @return Item details
     */
    function getItem(uint256 _id) public view returns (Item memory) {
        require(_id > 0 && _id <= itemCount, "Item does not exist"); // Ensure valid ID
        return items[_id]; // Return item details
    }
}
```
