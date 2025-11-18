"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.com.tr
Prompt: Write Solidity code for a decentralized marketplace that allows users to trade Ether (ETH) securely, inspired by the Ethereum purchasing section on ethereum.com.tr.
Generated: DETERMINISTIC_dab8fd762eedfd11
Batch ID: 20250612_151308
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

// Import OpenZeppelin's SafeMath library to handle arithmetic safely
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for trading Ether securely
contract DecentralizedMarketplace is Ownable {
    using SafeMath for uint256;

    // Struct to represent an item listing
    struct Item {
        uint256 id;
        address payable seller;
        string name;
        uint256 price; // Price in wei
        bool isSold;
    }

    // Mapping of item ID to Item
    mapping(uint256 => Item) public items;
    // Counter for item IDs
    uint256 public itemCount;

    // Event emitted when a new item is listed
    event ItemListed(uint256 id, address seller, string name, uint256 price);
    // Event emitted when an item is purchased
    event ItemPurchased(uint256 id, address buyer, uint256 price);

    // Function to list a new item for sale
    function listItem(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");
        
        itemCount++;
        items[itemCount] = Item(itemCount, payable(msg.sender), _name, _price, false);
        
        emit ItemListed(itemCount, msg.sender, _name, _price);
    }

    // Function to purchase an item
    function purchaseItem(uint256 _id) public payable {
        Item storage item = items[_id];
        
        require(_id > 0 && _id <= itemCount, "Item ID is invalid");
        require(msg.value >= item.price, "Insufficient payment");
        require(!item.isSold, "Item has already been sold");
        
        item.seller.transfer(item.price); // Transfer payment to the seller
        item.isSold = true; // Mark item as sold
        
        emit ItemPurchased(_id, msg.sender, item.price);
    }

    // Function to fetch item details by ID
    function getItem(uint256 _id) public view returns (uint256, address, string memory, uint256, bool) {
        Item memory item = items[_id];
        return (item.id, item.seller, item.name, item.price, item.isSold);
    }
    
    // Fallback function to prevent sending Ether to the contract directly
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    // Function to withdraw any accidental Ether sent to the contract (only owner can call)
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
