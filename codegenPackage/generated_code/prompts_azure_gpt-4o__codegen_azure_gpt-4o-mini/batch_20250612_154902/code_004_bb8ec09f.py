"""
Generated Code Metadata:
========================
Original URL: https://opensea-blockchain-eight.vercel.app
Prompt: Create a smart contract template for a marketplace clone inspired by the Opeasea Clone website, ensuring wallet connection support.
Generated: DETERMINISTIC_bb8ec09fb98580d3
Batch ID: 20250612_154902
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Marketplace contract for buying and selling NFTs
contract Marketplace is Ownable, ERC721Holder {
    // Struct to represent an item for sale
    struct Item {
        uint256 id;
        address nftContract;
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isSold;
    }

    // Mapping to store items by their ID
    mapping(uint256 => Item) public items;
    // Counter for item IDs
    uint256 public itemCount;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed id, address indexed seller, address indexed nftContract, uint256 tokenId, uint256 price);
    // Event emitted when an item is sold
    event ItemSold(uint256 indexed id, address indexed buyer, address indexed seller, uint256 price);

    // Function to list an NFT for sale
    function listItem(address _nftContract, uint256 _tokenId, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Transfer the NFT to the marketplace contract
        IERC721(_nftContract).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Increment item count and create a new item
        itemCount++;
        items[itemCount] = Item(itemCount, _nftContract, _tokenId, msg.sender, _price, false);

        emit ItemListed(itemCount, msg.sender, _nftContract, _tokenId, _price);
    }

    // Function to buy an NFT
    function buyItem(uint256 _id) external payable {
        Item storage item = items[_id];

        require(_id > 0 && _id <= itemCount, "Item does not exist");
        require(!item.isSold, "Item already sold");
        require(msg.value >= item.price, "Insufficient funds sent");

        // Mark the item as sold
        item.isSold = true;

        // Transfer the NFT to the buyer
        IERC721(item.nftContract).safeTransferFrom(address(this), msg.sender, item.tokenId);

        // Transfer the funds to the seller
        payable(item.seller).transfer(item.price);

        emit ItemSold(_id, msg.sender, item.seller, item.price);
    }

    // Function to withdraw unsold NFTs (only owner can call this)
    function withdrawUnsoldItem(uint256 _id) external onlyOwner {
        Item storage item = items[_id];

        require(_id > 0 && _id <= itemCount, "Item does not exist");
        require(!item.isSold, "Item already sold");

        // Transfer the NFT back to the seller
        IERC721(item.nftContract).safeTransferFrom(address(this), item.seller, item.tokenId);
        
        // Remove the item from the mapping
        delete items[_id];
    }

    // Function to get item details
    function getItem(uint256 _id) external view returns (Item memory) {
        require(_id > 0 && _id <= itemCount, "Item does not exist");
        return items[_id];
    }
}
```
