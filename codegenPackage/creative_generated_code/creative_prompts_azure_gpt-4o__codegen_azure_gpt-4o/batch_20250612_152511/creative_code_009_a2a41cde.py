"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesprotector.pages.dev
Prompt: Generate a Solidity smart contract template for managing in-game purchases using CAKE tokens in a multiplayer tower defense game like Pancake Protector.
Generated: DETERMINISTIC_a2a41cde58595b56
Batch ID: 20250612_152511
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

// Import the ERC20 interface for interacting with the CAKE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title TowerDefenseGameMarketplace
/// @dev A smart contract for managing in-game purchases in Pancake Protector using CAKE tokens.
contract TowerDefenseGameMarketplace {
    // Address of the CAKE token contract
    IERC20 public immutable cakeToken;

    // Address of the game owner/admin
    address public owner;

    // Events
    event ItemPurchased(address indexed buyer, uint256 itemId, uint256 amount);
    event ItemAdded(uint256 indexed itemId, string itemName, uint256 price);
    event ItemUpdated(uint256 indexed itemId, string itemName, uint256 price);
    event ItemRemoved(uint256 indexed itemId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Struct to store item details
    struct Item {
        string name;       // Name of the in-game item
        uint256 price;     // Price of the item in CAKE tokens
        bool isAvailable;  // Availability status of the item
    }

    // Mapping of item IDs to item details
    mapping(uint256 => Item) public items;

    // Variable to track the next item ID
    uint256 public nextItemId;

    /// @dev Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /// @dev Constructor to initialize the smart contract
    /// @param _cakeToken Address of the CAKE token contract
    constructor(address _cakeToken) {
        require(_cakeToken != address(0), "Invalid CAKE token address");
        cakeToken = IERC20(_cakeToken);
        owner = msg.sender;
    }

    /// @dev Function to add a new in-game item
    /// @param _name Name of the item
    /// @param _price Price of the item in CAKE tokens
    function addItem(string memory _name, uint256 _price) external onlyOwner {
        require(bytes(_name).length > 0, "Item name cannot be empty");
        require(_price > 0, "Item price must be greater than zero");

        items[nextItemId] = Item({
            name: _name,
            price: _price,
            isAvailable: true
        });

        emit ItemAdded(nextItemId, _name, _price);

        nextItemId++;
    }

    /// @dev Function to update an existing item's details
    /// @param _itemId ID of the item to update
    /// @param _name New name of the item
    /// @param _price New price of the item in CAKE tokens
    function updateItem(uint256 _itemId, string memory _name, uint256 _price) external onlyOwner {
        require(_itemId < nextItemId, "Item does not exist");
        require(bytes(_name).length > 0, "Item name cannot be empty");
        require(_price > 0, "Item price must be greater than zero");

        Item storage item = items[_itemId];
        item.name = _name;
        item.price = _price;

        emit ItemUpdated(_itemId, _name, _price);
    }

    /// @dev Function to remove an item from the marketplace
    /// @param _itemId ID of the item to remove
    function removeItem(uint256 _itemId) external onlyOwner {
        require(_itemId < nextItemId, "Item does not exist");

        Item storage item = items[_itemId];
        item.isAvailable = false;

        emit ItemRemoved(_itemId);
    }

    /// @dev Function for a player to purchase an item
    /// @param _itemId ID of the item to purchase
    function purchaseItem(uint256 _itemId) external {
        require(_itemId < nextItemId, "Item does not exist");
        Item storage item = items[_itemId];
        require(item.isAvailable, "Item is not available");

        uint256 price = item.price;

        // Transfer CAKE tokens from the buyer to the contract
        require(cakeToken.transferFrom(msg.sender, address(this), price), "Token transfer failed");

        emit ItemPurchased(msg.sender, _itemId, price);
    }

    /// @dev Function to withdraw CAKE tokens from the contract
    /// @param _amount Amount of CAKE tokens to withdraw
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(cakeToken.balanceOf(address(this)) >= _amount, "Insufficient balance");
        require(cakeToken.transfer(owner, _amount), "Token transfer failed");
    }

    /// @dev Function to transfer ownership of the contract
    /// @param _newOwner Address of the new owner
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}
```
