"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orange-pepe.pages.dev
Prompt: Create a smart contract that allows users to purchase exclusive merchandise using $ORPE tokens on the upcoming e-commerce platform.
Generated: DETERMINISTIC_fee39267a460a6ed
Batch ID: 20250612_160127
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Smart contract for merchandise sales using $ORPE tokens
contract MerchandiseStore is Ownable {
    using Address for address;

    // Token interface for $ORPE
    IERC20 public orpeToken;

    // Struct to represent a merchandise item
    struct Item {
        uint256 id;            // Unique identifier for the item
        string name;          // Name of the item
        uint256 price;        // Price of the item in ORPE tokens
        bool isAvailable;     // Availability status of the item
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    uint256 public itemCount; // Counter for the number of items

    // Event emitted when an item is purchased
    event ItemPurchased(address indexed buyer, uint256 indexed itemId);

    // Constructor to initialize the contract with the $ORPE token address
    constructor(address _orpeTokenAddress) {
        require(_orpeTokenAddress.isContract(), "Invalid token contract address");
        orpeToken = IERC20(_orpeTokenAddress);
    }

    // Function to add a new merchandise item
    function addItem(string memory _name, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        itemCount++;
        items[itemCount] = Item(itemCount, _name, _price, true);
    }

    // Function to purchase an item using $ORPE tokens
    function purchaseItem(uint256 _itemId) external {
        Item storage item = items[_itemId];
        require(item.isAvailable, "Item is not available");
        require(orpeToken.balanceOf(msg.sender) >= item.price, "Insufficient $ORPE balance");

        // Transfer tokens from the buyer to the contract owner
        require(orpeToken.transferFrom(msg.sender, owner(), item.price), "Token transfer failed");

        // Mark the item as sold
        item.isAvailable = false;

        // Emit the purchase event
        emit ItemPurchased(msg.sender, _itemId);
    }

    // Function to update the availability of an item
    function updateItemAvailability(uint256 _itemId, bool _isAvailable) external onlyOwner {
        Item storage item = items[_itemId];
        item.isAvailable = _isAvailable;
    }

    // Function to withdraw the contract's balance of $ORPE tokens
    function withdrawTokens() external onlyOwner {
        uint256 balance = orpeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(orpeToken.transfer(owner(), balance), "Token transfer failed");
    }
}
```
