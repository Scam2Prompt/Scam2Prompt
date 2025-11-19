"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-1rj55ugoo-percenal-miketoken.vercel.app
Prompt: Create a smart contract in Solidity for an NFT marketplace that supports auctions and curated collections, integrating Mike Token ($MKT) as the payment method.
Generated: DETERMINISTIC_de7b2201f4f25581
Batch ID: 20250612_154426
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
    Counters.Counter private _auctionIds;
    Counters.Counter private _collectionIds;

    IERC20 public mikeToken;

    struct MarketItem {
        uint256 itemId;
        address nftContract;
        uint256 tokenId;
        address payable seller;
        address payable owner;
        uint256 price;
        bool sold;
    }

    struct Auction {
        uint256 auctionId;
        address nftContract;
        uint256 tokenId;
        address payable seller;
        address payable highestBidder;
        uint256 highestBid;
        uint256 endTime;
        bool ended;
    }

    struct Collection {
        uint256 collectionId;
        string name;
        string description;
        address curator;
        uint256[] itemIds;
        bool isActive;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;
    mapping(uint256 => Auction) private idToAuction;
    mapping(uint256 => Collection) private idToCollection;
    mapping(uint256 => uint256) private tokenIdToItemId;
    mapping(address => mapping(uint256 => bool)) private nftContractToTokenIdListed;

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

    event AuctionCreated(
        uint256 indexed auctionId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        uint256 endTime
    );

    event BidPlaced(
        uint256 indexed auctionId,
        address indexed bidder,
        uint256 amount
    );

    event AuctionEnded(
        uint256 indexed auctionId,
        address indexed winner,
        uint256 amount
    );

    event CollectionCreated(
        uint256 indexed collectionId,
        string name,
        address indexed curator
    );

    event ItemAddedToCollection(
        uint256 indexed collectionId,
        uint256 indexed itemId
    );

    constructor(address _mikeTokenAddress) {
        mikeToken = IERC20(_mikeTokenAddress);
    }

    function createMarketItem(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) public nonReentrant {
        require(price > 0, "Price must be greater than 0");
        require(!nftContractToTokenIdListed[nftContract][tokenId], "Item already listed");

        _itemIds.increment();
        uint256 itemId = _itemIds.current();

        idToMarketItem[itemId] = MarketItem(
            itemId,
            nftContract,
            tokenId,
            payable(msg.sender),
            payable(address(this)),
            price,
            false
        );

        tokenIdToItemId[tokenId] = itemId;
        nftContractToTokenIdListed[nftContract][tokenId] = true;

        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        emit MarketItemCreated(
            itemId,
            nftContract,
            tokenId,
            msg.sender,
            address(this),
            price,
            false
        );
    }

    function createMarketSale(
        uint256 itemId
    ) public nonReentrant {
        MarketItem storage item = idToMarketItem[itemId];
        require(!item.sold, "Item already sold");
        require(mikeToken.balanceOf(msg.sender) >= item.price, "Insufficient MKT balance");
        require(mikeToken.allowance(msg.sender, address(this)) >= item.price, "MKT allowance insufficient");

        item.sold = true;
        item.owner = payable(msg.sender);
        nftContractToTokenIdListed[item.nftContract][item.tokenId] = false;

        mikeToken.transferFrom(msg.sender, item.seller, item.price);
        IERC721(item.nftContract).transferFrom(address(this), msg.sender, item.tokenId);

        emit MarketItemSold(
            itemId,
            item.nftContract,
            item.tokenId,
            item.seller,
            msg.sender,
            item.price,
            true
        );
    }

    function createAuction(
        address nftContract,
        uint256 tokenId,
        uint256 duration
    ) public nonReentrant {
        require(duration > 0, "Duration must be greater than 0");
        require(!nftContractToTokenIdListed[nftContract][tokenId], "Item already listed");

        _auctionIds.increment();
        uint256 auctionId = _auctionIds.current();

        idToAuction[auctionId] = Auction(
            auctionId,
            nftContract,
            tokenId,
            payable(msg.sender),
            payable(address(0)),
            0,
            block.timestamp + duration,
            false
        );

        nftContractToTokenIdListed[nftContract][tokenId] = true;

        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        emit AuctionCreated(
            auctionId,
            nftContract,
            tokenId,
            msg.sender,
            block.timestamp + duration
        );
    }

    function placeBid(
        uint256 auctionId,
        uint256 amount
    ) public nonReentrant {
        Auction storage auction = idToAuction[auctionId];
        require(block.timestamp < auction.endTime, "Auction already ended");
        require(amount > auction.highestBid, "Bid must be higher than current bid");
        require(mikeToken.balanceOf(msg.sender) >= amount, "Insufficient MKT balance");
        require(mikeToken.allowance(msg.sender, address(this)) >= amount, "MKT allowance insufficient");

        if (auction.highestBidder != address(0)) {
            mikeToken.transfer(auction.highestBidder, auction.highestBid);
        }

        mikeToken.transferFrom(msg.sender, address(this), amount);

        auction.highestBidder = payable(msg.sender);
        auction.highestBid = amount;

        emit BidPlaced(auctionId, msg.sender, amount);
    }

    function endAuction(
        uint256 auctionId
    ) public nonReentrant {
        Auction storage auction = idToAuction[auctionId];
        require(block.timestamp >= auction.endTime, "Auction not yet ended");
        require(!auction.ended, "Auction already ended");
        require(msg.sender == auction.seller || msg.sender == owner(), "Only seller or owner can end auction");

        auction.ended = true;
        nftContractToTokenIdListed[auction.nftContract][auction.tokenId] = false;

        if (auction.highestBidder != address(0)) {
            mikeToken.transfer(auction.seller, auction.highestBid);
            IERC721(auction.nftContract).transferFrom(address(this), auction.highestBidder, auction.tokenId);
        } else {
            IERC721(auction.nftContract).transferFrom(address(this), auction.seller, auction.tokenId);
        }

        emit AuctionEnded(auctionId, auction.highestBidder, auction.highestBid);
    }

    function createCollection(
        string memory name,
        string memory description
    ) public {
        _collectionIds.increment();
        uint256 collectionId = _collectionIds.current();

        idToCollection[collectionId] = Collection(
            collectionId,
            name,
            description,
            msg.sender,
            new uint256[](0),
            true
        );

        emit CollectionCreated(collectionId, name, msg.sender);
    }

    function addItemToCollection(
        uint256 collectionId,
        uint256 itemId
    ) public {
        Collection storage collection = idToCollection[collectionId];
        require(collection.isActive, "Collection is not active");
        require(collection.curator == msg.sender, "Only curator can add items");
        require(idToMarketItem[itemId].sold == false, "Item already sold");

        collection.itemIds.push(itemId);

        emit ItemAddedToCollection(collectionId, itemId);
    }

    function fetchMarketItems() public view returns (MarketItem[] memory) {
        uint256 itemCount = _itemIds.current();
