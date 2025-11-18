"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsonlinedapps.weebly.com
Prompt: Generate a smart contract code for a DApp designed using ConnectsOnlineDApps customizable templates.
Generated: DETERMINISTIC_57d063dcf876c8fd
Batch ID: 20250612_151610
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

/// @title ConnectsOnlineDApps Smart Contract
/// @dev This contract serves as a template for a decentralized application (DApp) built using ConnectsOnlineDApps customizable templates.

contract ConnectsOnlineDApp {
    // State variable to store the owner's address
    address public owner;

    // Event to log the addition of a new item
    event ItemAdded(uint256 indexed itemId, string name);

    // Struct to represent an item
    struct Item {
        uint256 id;
        string name;
        string description;
        uint256 price;
        bool available;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;

    // Counter to keep track of the number of items
    uint256 public itemCount;

    /// @dev Modifier to restrict actions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /// @dev Constructor sets the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /// @dev Function to add a new item
    /// @param _name The name of the item
    /// @param _description A description of the item
    /// @param _price The price of the item in wei
    function addItem(string memory _name, string memory _description, uint256 _price) public onlyOwner {
        require(bytes(_name).length > 0, "Item name cannot be empty");
        require(_price > 0, "Item price must be greater than zero");

        itemCount++;
        items[itemCount] = Item(itemCount, _name, _description, _price, true);
        emit ItemAdded(itemCount, _name);
    }

    /// @dev Function to purchase an item
    /// @param _itemId The ID of the item to purchase
    function purchaseItem(uint256 _itemId) public payable {
        Item storage item = items[_itemId];
        require(item.available, "Item not available");
        require(msg.value >= item.price, "Insufficient funds sent");

        // Transfer the funds to the owner
        payable(owner).transfer(item.price);

        // Mark the item as no longer available
        item.available = false;
    }

    /// @dev Function to retrieve item details
    /// @param _itemId The ID of the item to retrieve
    /// @return id The ID of the item
    /// @return name The name of the item
    /// @return description The description of the item
    /// @return price The price of the item
    /// @return available The availability status of the item
    function getItem(uint256 _itemId) public view returns (uint256 id, string memory name, string memory description, uint256 price, bool available) {
        Item memory item = items[_itemId];
        return (item.id, item.name, item.description, item.price, item.available);
    }

    /// @dev Function to withdraw funds from the contract (only for the owner)
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /// @dev Fallback function to accept Ether
    receive() external payable {}
}
```
