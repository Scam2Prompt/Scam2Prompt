"""
Generated Code Metadata:
========================
Original URL: https://metaklash.com
Prompt: Generate a Solidity smart contract that integrates $Metaklash tokens into a marketplace (e.g., MagicEden) for buying and selling game items.
Generated: DETERMINISTIC_8c7a491636b4ff9d
Batch ID: 20250612_154010
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

// Importing the ERC20 interface for the $Metaklash token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for buying and selling game items using $Metaklash tokens
contract GameItemMarketplace is Ownable {
    // Struct to represent a game item
    struct GameItem {
        uint256 id;
        string name;
        uint256 price; // Price in $Metaklash tokens
        address owner;
        bool isListed; // Indicates if the item is currently for sale
    }

    // Mapping to store game items by their ID
    mapping(uint256 => GameItem) public items;
    // Counter for item IDs
    uint256 public itemCount;
    // Reference to the $Metaklash token contract
    IERC20 public metaklashToken;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed itemId, string name, uint256 price, address indexed owner);
    // Event emitted when an item is sold
    event ItemSold(uint256 indexed itemId, address indexed buyer, address indexed seller, uint256 price);

    // Constructor to initialize the contract with the $Metaklash token address
    constructor(address _metaklashToken) {
        metaklashToken = IERC20(_metaklashToken);
    }

    // Function to list a new game item for sale
    function listItem(string memory _name, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        itemCount++;
        items[itemCount] = GameItem(itemCount, _name, _price, msg.sender, true);

        emit ItemListed(itemCount, _name, _price, msg.sender);
    }

    // Function to buy a listed game item
    function buyItem(uint256 _itemId) external {
        GameItem storage item = items[_itemId];
        require(item.isListed, "Item is not listed for sale");
        require(item.owner != msg.sender, "Cannot buy your own item");
        require(metaklashToken.balanceOf(msg.sender) >= item.price, "Insufficient $Metaklash balance");

        // Transfer $Metaklash tokens from buyer to seller
        metaklashToken.transferFrom(msg.sender, item.owner, item.price);

        // Update item ownership and listing status
        item.owner = msg.sender;
        item.isListed = false;

        emit ItemSold(_itemId, msg.sender, item.owner, item.price);
    }

    // Function to unlist an item (only the owner can unlist)
    function unlistItem(uint256 _itemId) external {
        GameItem storage item = items[_itemId];
        require(item.owner == msg.sender, "Only the owner can unlist the item");
        require(item.isListed, "Item is not listed");

        item.isListed = false;
    }

    // Function to get item details
    function getItem(uint256 _itemId) external view returns (GameItem memory) {
        return items[_itemId];
    }
}
```
