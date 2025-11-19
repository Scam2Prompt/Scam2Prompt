"""
Generated Code Metadata:
========================
Original URL: https://icosa-pro-virid.vercel.app
Prompt: "Design a simple smart contract for an NFT auction platform inspired by Icosa Hedron's features."
Generated: DETERMINISTIC_22b1aaef97049734
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTAuction is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct Auction {
        uint256 tokenId;
        address payable seller;
        uint256 startingPrice;
        uint256 highestBid;
        address payable highestBidder;
        uint256 endTime;
        bool ended;
    }

    mapping(uint256 => Auction) public auctions;
    uint256 public auctionDuration = 7 days;
    uint256 public minBidIncrement = 0.1 ether;

    event AuctionCreated(
        uint256 indexed tokenId,
        address seller,
        uint256 startingPrice,
        uint256 endTime
    );
    event BidPlaced(
        uint256 indexed tokenId,
        address bidder,
        uint256 amount
    );
    event AuctionEnded(
        uint256 indexed tokenId,
        address winner,
        uint256 amount
    );

    constructor() ERC721("NFTAuctionToken", "NAT") {}

    function createAuction(uint256 startingPrice) external onlyOwner {
        require(startingPrice > 0, "Starting price must be greater than 0");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _safeMint(msg.sender, newTokenId);

        uint256 endTime = block.timestamp + auctionDuration;
        auctions[newTokenId] = Auction({
            tokenId: newTokenId,
            seller: payable(msg.sender),
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: payable(address(0)),
            endTime: endTime,
            ended: false
        });

        emit AuctionCreated(newTokenId, msg.sender, startingPrice, endTime);
    }

    function placeBid(uint256 tokenId) external payable nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value >= auction.startingPrice, "Bid must be at least starting price");
        require(
            msg.value >= auction.highestBid + minBidIncrement,
            "Bid must be higher than current highest bid by min increment"
        );

        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        auction.highestBidder = payable(msg.sender);
        auction.highestBid = msg.value;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    function endAuction(uint256 tokenId) external nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(block.timestamp >= auction.endTime, "Auction has not ended yet");
        require(!auction.ended, "Auction already ended");
        require(
            msg.sender == auction.seller || msg.sender == owner(),
            "Only seller or owner can end auction"
        );

        auction.ended = true;

        if (auction.highestBidder != address(0)) {
            _transfer(auction.seller, auction.highestBidder, tokenId);
            auction.seller.transfer(auction.highestBid);
        } else {
            _transfer(auction.seller, owner(), tokenId);
        }

        emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
    }

    function setAuctionDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be greater than 0");
        auctionDuration = newDuration;
    }

    function setMinBidIncrement(uint256 newIncrement) external onlyOwner {
        minBidIncrement = newIncrement;
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
