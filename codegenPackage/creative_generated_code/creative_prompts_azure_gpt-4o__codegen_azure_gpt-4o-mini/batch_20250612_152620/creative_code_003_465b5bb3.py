"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market.pages.dev
Prompt: Provide an example of a decentralized application (dApp) that enables trustless transactions under a marketplace environment like Whales Market.
Generated: DETERMINISTIC_465b5bb380117e04
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// This contract represents a simple marketplace for ERC721 tokens (NFTs)
contract Marketplace is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold item details
    struct Item {
        uint256 id;
        address nftContract;
        uint256 tokenId;
        address payable seller;
        uint256 price;
        bool sold;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    // Counter for unique item IDs
    Counters.Counter private _itemIdCounter;

    // Event to emit when an item is listed
    event ItemListed(uint256 itemId, address seller, uint256 price);
    // Event to emit when an item is sold
    event ItemSold(uint256 itemId, address buyer);

    // Function to list an item for sale
    function listItem(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        
        // Increment the item ID counter
        _itemIdCounter.increment();
        uint256 newItemId = _itemIdCounter.current();

        // Transfer NFT to the marketplace contract
        ERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create and store the item
        items[newItemId] = Item(newItemId, nftContract, tokenId, payable(msg.sender), price, false);

        emit ItemListed(newItemId, msg.sender, price);
    }

    // Function to buy an item
    function buyItem(uint256 itemId) external payable {
        Item storage item = items[itemId];

        // Ensure the item exists and is not already sold
        require(item.id == itemId, "Item does not exist");
        require(!item.sold, "Item already sold");
        require(msg.value >= item.price, "Insufficient funds sent");

        // Mark the item as sold
        item.sold = true;

        // Pay the seller
        item.seller.transfer(item.price);

        // Transfer the NFT to the buyer
        ERC721(item.nftContract).transferFrom(address(this), msg.sender, item.tokenId);

        emit ItemSold(itemId, msg.sender);
    }

    // Function to get item details
    function getItem(uint256 itemId) external view returns (Item memory) {
        return items[itemId];
    }

    // Function to withdraw funds from the contract (onlyOwner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
