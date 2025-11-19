"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates secure transactions on a decentralized marketplace like Pushd, utilizing Ethereum's blockchain technology.
Generated: DETERMINISTIC_a4dd89a21bc237f8
Batch ID: 20250612_164305
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

/// @title Decentralized Marketplace Smart Contract
/// @author Your Name
/// @notice This contract facilitates secure transactions for digital goods in a decentralized marketplace.
/// @dev This contract uses OpenZeppelin's SafeERC20 for secure token transfers.

import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract DecentralizedMarketplace is Ownable {
    using SafeERC20 for IERC20;
    using Counters for Counters.Counter;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed itemId, address indexed seller, uint256 price, bool isActive);
    
    // Event emitted when an item is sold
    event ItemSold(uint256 indexed itemId, address indexed buyer, uint256 price);
    
    // Struct representing an item in the marketplace
    struct Item {
        uint256 id;
        address payable seller;
        uint256 price; // Price in wei
        bool isActive;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    Counters.Counter private itemIdCounter;

    /// @notice Lists a new item for sale
    /// @param _price The price of the item in wei
    function listItem(uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        itemIdCounter.increment();
        uint256 newItemId = itemIdCounter.current();

        items[newItemId] = Item({
            id: newItemId,
            seller: payable(msg.sender),
            price: _price,
            isActive: true
        });

        emit ItemListed(newItemId, msg.sender, _price, true);
    }

    /// @notice Purchases an item from the marketplace
    /// @param _itemId The ID of the item to purchase
    function buyItem(uint256 _itemId) external payable {
        Item storage item = items[_itemId];

        require(item.isActive, "Item is not active");
        require(msg.value >= item.price, "Insufficient payment");

        // Transfer payment to the seller
        item.seller.transfer(item.price);

        // Mark the item as inactive after sale
        item.isActive = false;

        emit ItemSold(_itemId, msg.sender, item.price);
    }

    /// @notice Allows the seller to withdraw unsold items
    /// @param _itemId The ID of the item to withdraw
    function withdrawItem(uint256 _itemId) external {
        Item storage item = items[_itemId];

        require(msg.sender == item.seller, "Only the seller can withdraw");
        require(item.isActive, "Item is not active");

        // Mark the item as inactive
        item.isActive = false;
    }

    /// @notice Returns the details of an item
    /// @param _itemId The ID of the item
    /// @return id The item ID
    /// @return seller The address of the seller
    /// @return price The price of the item
    /// @return isActive Whether the item is currently active for sale
    function getItemDetails(uint256 _itemId) external view returns (uint256 id, address seller, uint256 price, bool isActive) {
        Item storage item = items[_itemId];
        return (item.id, item.seller, item.price, item.isActive);
    }
}
```
