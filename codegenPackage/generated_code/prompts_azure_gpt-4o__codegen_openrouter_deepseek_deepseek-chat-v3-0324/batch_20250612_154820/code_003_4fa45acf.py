"""
Generated Code Metadata:
========================
Original URL: https://binaryxs.org
Prompt: Write a smart contract in Solidity for a decentralized NFT marketplace like BinaryX's Asset Marketplace, supporting BNX token transactions.
Generated: DETERMINISTIC_4fa45acf57dd223b
Batch ID: 20250612_154820
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is ReentrancyGuard, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _itemIds;
    Counters.Counter private _itemsSold;

    IERC20 public bnxToken;

    struct MarketItem {
        uint256 itemId;
        address nftContract;
        uint256 tokenId;
        address payable seller;
        address payable owner;
        uint256 price;
        bool sold;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;

    event MarketItemCreated(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    event MarketItemSold(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    constructor(address _bnxTokenAddress) {
        bnxToken = IERC20(_bnxTokenAddress);
    }

    function createMarketItem(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) public nonReentrant {
        require(price > 0, "Price must be at least 1 wei");
        require(
            IERC721(nftContract).ownerOf(tokenId) == msg.sender,
            "You must own the NFT to list it"
        );
        require(
            IERC721(nftContract).getApproved(tokenId) == address(this),
            "Marketplace must be approved to transfer NFT"
        );

        _itemIds.increment();
        uint256 itemId = _itemIds.current();

        idToMarketItem[itemId] = MarketItem(
            itemId,
            nftContract,
            tokenId,
            payable(msg.sender),
            payable(address(0)),
            price,
            false
        );

        emit MarketItemCreated(
            itemId,
            nftContract,
            tokenId,
            msg.sender,
            address(0),
            price,
            false
        );
    }

    function createMarketSale(
        uint256 itemId
    ) public nonReentrant {
        MarketItem storage item = idToMarketItem[itemId];
        uint256 price = item.price;
        uint256 tokenId = item.tokenId;

        require(!item.sold, "Item already sold");
        require(
            bnxToken.balanceOf(msg.sender) >= price,
            "Insufficient BNX balance"
        );
        require(
            bnxToken.allowance(msg.sender, address(this)) >= price,
            "Marketplace not approved to spend BNX"
        );

        // Transfer BNX from buyer to seller
        bool success = bnxToken.transferFrom(msg.sender, item.seller, price);
        require(success, "BNX transfer failed");

        // Transfer NFT from seller to buyer
        IERC721(item.nftContract).safeTransferFrom(item.seller, msg.sender, tokenId);

        item.owner = payable(msg.sender);
        item.sold = true;
        _itemsSold.increment();

        emit MarketItemSold(
            itemId,
            item.nftContract,
            tokenId,
            item.seller,
            msg.sender,
            price,
            true
        );
    }

    function fetchMarketItems() public view returns (MarketItem[] memory) {
        uint256 itemCount = _itemIds.current();
        uint256 unsoldItemCount = _itemIds.current() - _itemsSold.current();
        uint256 currentIndex = 0;

        MarketItem[] memory items = new MarketItem[](unsoldItemCount);
        for (uint256 i = 1; i <= itemCount; i++) {
            if (!idToMarketItem[i].sold) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchMyNFTs() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].owner == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].owner == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchItemsCreated() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].seller == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].seller == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function updateBnxTokenAddress(address _newBnxTokenAddress) public onlyOwner {
        require(_newBnxTokenAddress != address(0), "Invalid address");
        bnxToken = IERC20(_newBnxTokenAddress);
    }
}
```
