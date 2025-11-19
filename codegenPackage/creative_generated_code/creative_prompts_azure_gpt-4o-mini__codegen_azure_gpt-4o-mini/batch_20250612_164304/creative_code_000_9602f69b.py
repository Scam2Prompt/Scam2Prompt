"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Generate a code snippet for a decentralized marketplace using blockchain technology that incorporates secure transactions and lower fees, similar to the Pushd platform.
Generated: DETERMINISTIC_9602f69bdbaa8487
Batch ID: 20250612_164304
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

// Importing OpenZeppelin's ERC721 implementation for NFT support
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for decentralized asset trading
contract DecentralizedMarketplace is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Item {
        uint256 id;
        address owner;
        uint256 price;
        bool isForSale;
    }

    // Mapping from item ID to Item details
    mapping(uint256 => Item) public items;

    // Event emitted when an item is listed for sale
    event ItemListed(uint256 indexed id, uint256 price);

    // Event emitted when an item is sold
    event ItemSold(uint256 indexed id, address buyer, uint256 price);

    // Constructor to initialize the marketplace with a name and symbol
    constructor() ERC721("Decentralized Marketplace", "DMP") {}

    // Function to create a new item and mint an NFT
    function createItem() external {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        items[tokenId] = Item({
            id: tokenId,
            owner: msg.sender,
            price: 0,
            isForSale: false
        });

        _tokenIdCounter.increment();
    }

    // Function to list an item for sale
    function listItem(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this item");
        require(price > 0, "Price must be greater than zero");

        items[tokenId].price = price;
        items[tokenId].isForSale = true;

        emit ItemListed(tokenId, price);
    }

    // Function to purchase an item
    function buyItem(uint256 tokenId) external payable {
        Item storage item = items[tokenId];

        require(item.isForSale, "Item is not for sale");
        require(msg.value >= item.price, "Insufficient payment");
        require(item.owner != msg.sender, "Owner cannot buy their own item");

        // Transfer the ownership of the NFT
        _transfer(item.owner, msg.sender, tokenId);

        // Pay the seller
        payable(item.owner).transfer(msg.value);

        // Update the item details
        item.owner = msg.sender;
        item.isForSale = false;

        emit ItemSold(tokenId, msg.sender, item.price);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get item details
    function getItem(uint256 tokenId) external view returns (Item memory) {
        return items[tokenId];
    }
}
```
