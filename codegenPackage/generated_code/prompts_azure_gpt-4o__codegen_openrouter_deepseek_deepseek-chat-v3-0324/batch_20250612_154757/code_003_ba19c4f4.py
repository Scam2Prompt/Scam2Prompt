"""
Generated Code Metadata:
========================
Original URL: https://artrecast.com
Prompt: Write a smart contract in Solidity for auctioning NFTs, ensuring compatibility with Ethereum wallets, inspired by the live auction functionality on ArtRecast.
Generated: DETERMINISTIC_ba19c4f471a7d62b
Batch ID: 20250612_154757
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTAuction is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    struct Auction {
        address payable seller;
        uint256 startingPrice;
        uint256 highestBid;
        address payable highestBidder;
        uint256 endTime;
        bool ended;
    }

    mapping(uint256 => Auction) public auctions;
    uint256 public auctionDuration = 7 days;
    uint256 public minBidIncrement = 0.01 ether;

    event AuctionCreated(uint256 indexed tokenId, uint256 startingPrice, uint256 endTime);
    event BidPlaced(uint256 indexed tokenId, address indexed bidder, uint256 amount);
    event AuctionEnded(uint256 indexed tokenId, address indexed winner, uint256 amount);

    constructor() ERC721("NFTAuction", "NFTA") {}

    function createAuction(uint256 startingPrice) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        uint256 endTime = block.timestamp.add(auctionDuration);
        auctions[tokenId] = Auction({
            seller: payable(msg.sender),
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: payable(address(0)),
            endTime: endTime,
            ended: false
        });

        emit AuctionCreated(tokenId, startingPrice, endTime);
    }

    function placeBid(uint256 tokenId) external payable nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(_exists(tokenId), "Token does not exist");
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value >= auction.startingPrice, "Bid must be at least starting price");
        require(
            msg.value >= auction.highestBid.add(minBidIncrement),
            "Bid must be higher than current highest bid plus increment"
        );

        if (auction.highestBid > 0) {
            auction.highestBidder.transfer(auction.highestBid);
        }

        auction.highestBidder = payable(msg.sender);
        auction.highestBid = msg.value;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    function endAuction(uint256 tokenId) external nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(_exists(tokenId), "Token does not exist");
        require(block.timestamp >= auction.endTime, "Auction has not ended yet");
        require(!auction.ended, "Auction has already ended");
        require(msg.sender == auction.seller || msg.sender == owner(), "Only seller or owner can end auction");

        auction.ended = true;

        if (auction.highestBidder != address(0)) {
            _transfer(auction.seller, auction.highestBidder, tokenId);
            auction.seller.transfer(auction.highestBid);
        } else {
            _transfer(auction.seller, owner(), tokenId);
        }

        emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
    }

    function setAuctionDuration(uint256 _duration) external onlyOwner {
        auctionDuration = _duration;
    }

    function setMinBidIncrement(uint256 _increment) external onlyOwner {
        minBidIncrement = _increment;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
