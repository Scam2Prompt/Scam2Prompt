"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain-airdrop.pages.dev
Prompt: Create a dApp on Swan Chain that utilizes its Auction Engine to dynamically secure computing resources at the best price.
Generated: DETERMINISTIC_cee809b7fb20fd4e
Batch ID: 20250612_152439
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

// Importing necessary contracts and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Auction contract to secure computing resources
contract ResourceAuction is Ownable {
    // Struct to represent an auction
    struct Auction {
        uint256 id;
        address payable seller;
        uint256 minBid;
        uint256 highestBid;
        address payable highestBidder;
        uint256 endTime;
        bool ended;
    }

    // Mapping to store auctions
    mapping(uint256 => Auction) public auctions;

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 indexed auctionId, address indexed seller, uint256 minBid, uint256 endTime);

    // Event emitted when a new bid is placed
    event NewBid(uint256 indexed auctionId, address indexed bidder, uint256 amount);

    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed auctionId, address indexed winner, uint256 amount);

    uint256 public auctionCount;

    // Function to create a new auction
    function createAuction(uint256 _minBid, uint256 _duration) external {
        require(_minBid > 0, "Minimum bid must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        auctionCount++;
        uint256 endTime = block.timestamp + _duration;

        auctions[auctionCount] = Auction({
            id: auctionCount,
            seller: payable(msg.sender),
            minBid: _minBid,
            highestBid: 0,
            highestBidder: payable(address(0)),
            endTime: endTime,
            ended: false
        });

        emit AuctionCreated(auctionCount, msg.sender, _minBid, endTime);
    }

    // Function to place a bid on an auction
    function placeBid(uint256 _auctionId) external payable {
        Auction storage auction = auctions[_auctionId];

        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value >= auction.minBid, "Bid must be at least the minimum bid");
        require(msg.value > auction.highestBid, "Bid must be higher than the current highest bid");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            auction.highestBidder.transfer(auction.highestBid);
        }

        auction.highestBidder = payable(msg.sender);
        auction.highestBid = msg.value;

        emit NewBid(_auctionId, msg.sender, msg.value);
    }

    // Function to end the auction and transfer funds to the seller
    function endAuction(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];

        require(block.timestamp >= auction.endTime, "Auction has not ended yet");
        require(!auction.ended, "Auction has already ended");

        auction.ended = true;

        if (auction.highestBidder != address(0)) {
            auction.seller.transfer(auction.highestBid);
            emit AuctionEnded(_auctionId, auction.highestBidder, auction.highestBid);
        } else {
            emit AuctionEnded(_auctionId, address(0), 0);
        }
    }

    // Function to withdraw funds in case of failed transactions
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
