"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telos-4ji.pages.dev
Prompt: Write a Solidity smart contract for deploying an NFT marketplace on Telos EVM, incorporating Telos' fixed-rate gas fee system to prevent front-running.
Generated: DETERMINISTIC_536e9ab243865f2f
Batch ID: 20250612_152018
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMarketplace
 * @dev This contract allows users to create, buy, and sell NFTs on the Telos EVM.
 */
contract NFTMarketplace is ERC721Holder, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _itemIds;
    Counters.Counter private _itemsSold;

    struct Item {
        uint256 itemId; // Unique identifier for the item
        address nftContract; // Address of the NFT contract
        uint256 tokenId; // Token ID of the NFT
        address payable seller; // Address of the seller
        address payable buyer; // Address of the buyer
        uint256 price; // Sale price of the NFT
        bool sold; // Status of the item
    }

    // Mapping from item ID to Item struct
    mapping(uint256 => Item) private idToItem;

    event ItemListed(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        uint256 price
    );

    event ItemSold(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address buyer,
        uint256 price
    );

    /**
     * @dev Lists an NFT for sale on the marketplace.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The token ID of the NFT.
     * @param price The sale price of the NFT.
     */
    function listItem(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero");

        _itemIds.increment();
        uint256 itemId = _itemIds.current();

        idToItem[itemId] = Item(
            itemId,
            nftContract,
            tokenId,
            payable(msg.sender),
            payable(address(0)), // Buyer is initially empty
            price,
            false
        );

        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);

        emit ItemListed(itemId, nftContract, tokenId, msg.sender, price);
    }

    /**
     * @dev Purchases an NFT listed on the marketplace.
     * @param itemId The ID of the item to purchase.
     */
    function purchaseItem(uint256 itemId) external payable {
        Item storage item = idToItem[itemId];

        require(item.itemId > 0, "Item does not exist");
        require(!item.sold, "Item is already sold");
        require(msg.value >= item.price, "Insufficient funds to purchase item");

        item.seller.transfer(msg.value);
        item.buyer = payable(msg.sender);
        item.sold = true;
        _itemsSold.increment();

        IERC721(item.nftContract).safeTransferFrom(address(this), msg.sender, item.tokenId);

        emit ItemSold(itemId, item.nftContract, item.tokenId, msg.sender, item.price);
    }

    /**
     * @dev Fetches the details of a specific item.
     * @param itemId The ID of the item.
     * @return The details of the item.
     */
    function fetchItem(uint256 itemId) external view returns (Item memory) {
        return idToItem[itemId];
    }

    /**
     * @dev Returns the total number of items listed on the marketplace.
     * @return The total number of items.
     */
    function totalItemsListed() external view returns (uint256) {
        return _itemIds.current();
    }
}
```
