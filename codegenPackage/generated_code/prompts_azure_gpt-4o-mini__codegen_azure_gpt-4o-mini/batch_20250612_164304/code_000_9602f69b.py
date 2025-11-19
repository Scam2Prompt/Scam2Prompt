"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: Generate a code snippet for a decentralized marketplace using blockchain technology that incorporates secure transactions and lower fees, similar to the Pushd platform.
Generated: DETERMINISTIC_9602f69bdbaa8487
Batch ID: 20250612_164304
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Marketplace contract for decentralized transactions
contract DecentralizedMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _itemIdCounter;

    // Struct to represent an item for sale
    struct Item {
        uint256 id;
        address seller;
        address buyer;
        uint256 price;
        bool sold;
    }

    // Mapping from item ID to Item details
    mapping(uint256 => Item) public items;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed itemId, address indexed seller, uint256 price);
    
    // Event emitted when an item is sold
    event ItemSold(uint256 indexed itemId, address indexed buyer);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("DecentralizedMarketplaceToken", "DMT") {}

    // Function to list an item for sale
    function listItem(uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        _itemIdCounter.increment();
        uint256 newItemId = _itemIdCounter.current();

        items[newItemId] = Item({
            id: newItemId,
            seller: msg.sender,
            buyer: address(0),
            price: price,
            sold: false
        });

        emit ItemListed(newItemId, msg.sender, price);
    }

    // Function to purchase an item
    function purchaseItem(uint256 itemId) external payable {
        Item storage item = items[itemId];

        require(item.id == itemId, "Item does not exist");
        require(!item.sold, "Item already sold");
        require(msg.value >= item.price, "Insufficient funds sent");

        // Transfer the funds to the seller
        payable(item.seller).transfer(item.price);
        
        // Mark the item as sold
        item.buyer = msg.sender;
        item.sold = true;

        // Emit the sold event
        emit ItemSold(itemId, msg.sender);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get item details
    function getItem(uint256 itemId) external view returns (Item memory) {
        return items[itemId];
    }
}
```
