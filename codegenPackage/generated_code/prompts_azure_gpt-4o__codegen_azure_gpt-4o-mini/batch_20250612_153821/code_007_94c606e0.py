"""
Generated Code Metadata:
========================
Original URL: https://miden.cloud
Prompt: Provide an example of a decentralized application (dApp) that utilizes the Miden Pioneer Program's technical support to implement on-chain economic features.
Generated: DETERMINISTIC_94c606e056373afb
Batch ID: 20250612_153821
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

/// @title Decentralized Marketplace
/// @author Your Name
/// @notice This contract implements a simple decentralized marketplace
/// @dev The marketplace allows users to list items for sale and purchase them
contract DecentralizedMarketplace {
    // Struct to represent an item for sale
    struct Item {
        uint256 id;
        address payable seller;
        string name;
        uint256 price;
        bool sold;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    // Counter for item IDs
    uint256 public itemCount;

    // Event emitted when a new item is listed
    event ItemListed(uint256 id, address seller, string name, uint256 price);
    // Event emitted when an item is sold
    event ItemSold(uint256 id, address buyer, uint256 price);

    /// @notice Lists a new item for sale
    /// @param _name The name of the item
    /// @param _price The price of the item in wei
    function listItem(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");

        itemCount++;
        items[itemCount] = Item(itemCount, payable(msg.sender), _name, _price, false);

        emit ItemListed(itemCount, msg.sender, _name, _price);
    }

    /// @notice Purchases an item from the marketplace
    /// @param _id The ID of the item to purchase
    function purchaseItem(uint256 _id) public payable {
        Item storage item = items[_id];

        require(_id > 0 && _id <= itemCount, "Item does not exist");
        require(msg.value >= item.price, "Insufficient funds sent");
        require(!item.sold, "Item already sold");
        require(item.seller != msg.sender, "Seller cannot buy their own item");

        // Mark the item as sold
        item.sold = true;

        // Transfer funds to the seller
        item.seller.transfer(item.price);

        emit ItemSold(_id, msg.sender, item.price);
    }

    /// @notice Retrieves item details by ID
    /// @param _id The ID of the item
    /// @return The item details
    function getItem(uint256 _id) public view returns (Item memory) {
        require(_id > 0 && _id <= itemCount, "Item does not exist");
        return items[_id];
    }
}
```
