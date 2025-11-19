"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Design a gaming dapp on Linea that enables onchain in-game commerce with low fees and fast transaction processing.
Generated: DETERMINISTIC_6ec19f747c297740
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title GamingDApp
 * @dev A decentralized application (DApp) for on-chain in-game commerce on Linea.
 *      Enables players to buy, sell, and trade in-game items with low fees and fast transaction processing.
 */
contract GamingDApp {
    // Struct to represent an in-game item
    struct Item {
        uint256 id; // Unique identifier for the item
        string name; // Name of the item
        uint256 price; // Price of the item in wei
        address owner; // Current owner of the item
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;

    // Counter for generating unique item IDs
    uint256 private itemCounter;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed itemId, string name, uint256 price, address indexed owner);

    // Event emitted when an item is purchased
    event ItemPurchased(uint256 indexed itemId, address indexed buyer, address indexed seller, uint256 price);

    // Modifier to ensure the caller is the owner of the item
    modifier onlyItemOwner(uint256 itemId) {
        require(items[itemId].owner == msg.sender, "Caller is not the owner of the item");
        _;
    }

    /**
     * @dev List a new in-game item for sale.
     * @param name Name of the item.
     * @param price Price of the item in wei.
     */
    function listItem(string memory name, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Increment the item counter to generate a unique ID
        itemCounter++;

        // Create a new item and store it in the mapping
        items[itemCounter] = Item({
            id: itemCounter,
            name: name,
            price: price,
            owner: msg.sender
        });

        // Emit the ItemListed event
        emit ItemListed(itemCounter, name, price, msg.sender);
    }

    /**
     * @dev Purchase an in-game item.
     * @param itemId ID of the item to purchase.
     */
    function purchaseItem(uint256 itemId) external payable {
        Item storage item = items[itemId];

        // Ensure the item exists and is not owned by the buyer
        require(item.owner != address(0), "Item does not exist");
        require(item.owner != msg.sender, "Cannot purchase your own item");

        // Ensure the buyer has sent enough Ether to cover the item's price
        require(msg.value == item.price, "Incorrect payment amount");

        // Transfer the payment to the item's owner
        address seller = item.owner;
        item.owner = msg.sender; // Update the item's owner
        payable(seller).transfer(msg.value);

        // Emit the ItemPurchased event
        emit ItemPurchased(itemId, msg.sender, seller, item.price);
    }

    /**
     * @dev Get details of an item.
     * @param itemId ID of the item to retrieve.
     * @return id, name, price, owner Details of the item.
     */
    function getItem(uint256 itemId)
        external
        view
        returns (
            uint256 id,
            string memory name,
            uint256 price,
            address owner
        )
    {
        Item storage item = items[itemId];
        require(item.owner != address(0), "Item does not exist");

        return (item.id, item.name, item.price, item.owner);
    }
}
```
