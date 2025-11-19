"""
Generated Code Metadata:
========================
Original URL: https://artocean.org
Prompt: "Design a smart contract for an NFT marketplace that incorporates features similar to Artlife, including NFT creation, bidding, and transfer functionalities."
Generated: DETERMINISTIC_fb5c4bf9519122ae
Batch ID: 20250622_212208
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    Counters.Counter private _itemsSold;

    uint256 public listingPrice = 0.025 ether;

    struct MarketItem {
        uint256 tokenId;
        address payable seller;
        address payable owner;
        uint256 price;
        bool sold;
    }

    struct Bid {
        address bidder;
        uint256 amount;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;
    mapping(uint256 => Bid[]) private tokenIdToBids;
    mapping(uint256 => address) private tokenIdToHighestBidder;
    mapping(uint256 => uint256) private tokenIdToHighestBid;

    event MarketItemCreated (
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    event BidPlaced (
        uint256 indexed tokenId,
        address bidder,
        uint256 amount
    );

    event ItemSold (
        uint256 indexed tokenId,
        address seller,
        address buyer,
        uint256 price
    );

    constructor() ERC721("NFT Marketplace", "NFTM") {}

    function updateListingPrice(uint256 _listingPrice) public payable onlyOwner {
        listingPrice = _listingPrice;
    }

    function createToken(string memory tokenURI, uint256 price) public payable returns (uint) {
        require(price > 0, "Price must be at least 1 wei");
        require(msg.value == listingPrice, "Price must be equal to listing price");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        createMarketItem(newTokenId, price);
        return newTokenId;
    }

    function createMarketItem(uint256 tokenId, uint256 price) private {
        require(price > 0, "Price must be at least 1 wei");

        idToMarketItem[tokenId] = MarketItem(
            tokenId,
            payable(msg.sender),
            payable(address(this)),
            price,
            false
        );

        _transfer(msg.sender, address(this), tokenId);
        emit MarketItemCreated(tokenId, msg.sender, address(this), price, false);
    }

    function resellToken(uint256 tokenId, uint256 price) public payable nonReentrant {
        require(idToMarketItem[tokenId].owner == msg.sender, "Only item owner can perform this operation");
        require(msg.value == listingPrice, "Price must be equal to listing price");
        require(price > 0, "Price must be at least 1 wei");

        idToMarketItem[tokenId].sold = false;
        idToMarketItem[tokenId].price = price;
        idToMarketItem[tokenId].seller = payable(msg.sender);
        idToMarketItem[tokenId].owner = payable(address(this));
        _itemsSold.decrement();

        _transfer(msg.sender, address(this), tokenId);
        emit MarketItemCreated(tokenId, msg.sender, address(this), price, false);
    }

    function createMarketSale(uint256 tokenId) public payable nonReentrant {
        uint256 price = idToMarketItem[tokenId].price;
        address seller = idToMarketItem[tokenId].seller;
        require(msg.value == price, "Please submit the asking price in order to complete the purchase");
        require(idToMarketItem[tokenId].sold == false, "Item is already sold");

        idToMarketItem[tokenId].owner = payable(msg.sender);
        idToMarketItem[tokenId].sold = true;
        idToMarketItem[tokenId].seller = payable(address(0));
        _itemsSold.increment();

        _transfer(address(this), msg.sender, tokenId);
        payable(seller).transfer(msg.value);
        emit ItemSold(tokenId, seller, msg.sender, price);
    }

    function placeBid(uint256 tokenId) public payable nonReentrant {
        require(idToMarketItem[tokenId].sold == false, "Item is already sold");
        require(msg.value > 0, "Bid amount must be greater than 0");
        
        uint256 highestBid = tokenIdToHighestBid[tokenId];
        require(msg.value > highestBid, "Bid must be higher than current highest bid");

        // Refund previous highest bidder
        if (highestBid > 0) {
            payable(tokenIdToHighestBidder[tokenId]).transfer(highestBid);
        }

        tokenIdToBids[tokenId].push(Bid(msg.sender, msg.value));
        tokenIdToHighestBidder[tokenId] = msg.sender;
        tokenIdToHighestBid[tokenId] = msg.value;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    function acceptBid(uint256 tokenId) public nonReentrant {
        require(idToMarketItem[tokenId].seller == msg.sender, "Only seller can accept bids");
        require(tokenIdToHighestBid[tokenId] > 0, "No bids placed for this item");

        address highestBidder = tokenIdToHighestBidder[tokenId];
        uint256 highestBid = tokenIdToHighestBid[tokenId];

        idToMarketItem[tokenId].owner = payable(highestBidder);
        idToMarketItem[tokenId].sold = true;
        idToMarketItem[tokenId].seller = payable(address(0));
        _itemsSold.increment();

        _transfer(address(this), highestBidder, tokenId);
        payable(msg.sender).transfer(highestBid);
        emit ItemSold(tokenId, msg.sender, highestBidder, highestBid);

        // Reset bid data
        delete tokenIdToBids[tokenId];
        delete tokenIdToHighestBidder[tokenId];
        delete tokenIdToHighestBid[tokenId];
    }

    function fetchMarketItems() public view returns (MarketItem[] memory) {
        uint256 itemCount = _tokenIds.current();
        uint256 unsoldItemCount = _tokenIds.current() - _itemsSold.current();
        uint256 currentIndex = 0;

        MarketItem[] memory items = new MarketItem[](unsoldItemCount);
        for (uint256 i = 0; i < itemCount; i++) {
            if (idToMarketItem[i + 1].owner == address(this)) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchMyNFTs() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _tokenIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchItemsCreated() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _tokenIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].seller == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].seller == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchBids(uint256 tokenId
