"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-blockchain-eight.vercel.app
Prompt: Create a smart contract template for a marketplace clone inspired by the Opeasea Clone website, ensuring wallet connection support.
Generated: DETERMINISTIC_bb8ec09fb98580d3
Batch ID: 20250612_154902
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Marketplace contract for creating and trading NFTs
contract Marketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent an item for sale
    struct Item {
        uint256 id;
        address nftContract;
        uint256 tokenId;
        address seller;
        uint256 price;
        bool sold;
    }

    // Events
    event ItemListed(uint256 id, address indexed seller, address indexed nftContract, uint256 indexed tokenId, uint256 price);
    event ItemSold(uint256 id, address indexed buyer, uint256 price);
    event ItemRemoved(uint256 id);

    // Mapping from item ID to Item struct
    mapping(uint256 => Item) public items;
    Counters.Counter private _itemIdCounter;

    // Function to list an NFT for sale
    function listItem(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        // Increment item ID and create a new item
        _itemIdCounter.increment();
        uint256 newItemId = _itemIdCounter.current();

        items[newItemId] = Item({
            id: newItemId,
            nftContract: nftContract,
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            sold: false
        });

        // Transfer the NFT to this contract
        ERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        emit ItemListed(newItemId, msg.sender, nftContract, tokenId, price);
    }

    // Function to buy an NFT
    function buyItem(uint256 itemId) external payable {
        Item storage item = items[itemId];
        
        require(item.id != 0, "Item does not exist");
        require(!item.sold, "Item already sold");
        require(msg.value >= item.price, "Insufficient funds sent");

        // Mark item as sold
        item.sold = true;

        // Transfer the NFT to the buyer
        ERC721(item.nftContract).transferFrom(address(this), msg.sender, item.tokenId);
        
        // Transfer the funds to the seller
        payable(item.seller).transfer(msg.value);

        emit ItemSold(itemId, msg.sender, item.price);
    }

    // Function to remove an item from the marketplace (only callable by the seller)
    function removeItem(uint256 itemId) external {
        Item storage item = items[itemId];

        require(item.id != 0, "Item does not exist");
        require(!item.sold, "Item already sold");
        require(item.seller == msg.sender, "Only seller can remove the item");
        
        // Return the NFT to the seller
        ERC721(item.nftContract).transferFrom(address(this), msg.sender, item.tokenId);
        
        // Remove the item from the mapping
        delete items[itemId];

        emit ItemRemoved(itemId);
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        payable(owner()).transfer(balance);
    }
}
```
