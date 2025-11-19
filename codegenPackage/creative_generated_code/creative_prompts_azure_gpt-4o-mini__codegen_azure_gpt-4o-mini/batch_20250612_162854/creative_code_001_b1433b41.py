"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write a smart contract using Moxie that facilitates a Batch Auction for Fan Tokens on the Farcaster network.
Generated: DETERMINISTIC_b1433b4166d77c20
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```moxie
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import Farcaster interfaces
import "farcaster/interfaces/IERC20.sol"; // Assuming there is an IERC20 interface

contract BatchAuction {
    // Define events for auction operations
    event AuctionCreated(uint256 indexed auctionId, address indexed creator, uint256 startTime, uint256 endTime);
    event BidPlaced(uint256 indexed auctionId, address indexed bidder, uint256 amount);
    event AuctionEnded(uint256 indexed auctionId, address indexed winner, uint256 amount);

    struct Auction {
        address token;
        uint256 startTime;
        uint256 endTime;
        uint256 highestBid;
        address highestBidder;
        bool ended;
    }

    // State variables
    mapping(uint256 => Auction) public auctions;
    uint256 public auctionCount;

    // Constructor to initialize auction count
    constructor() {
        auctionCount = 0;
    }

    // Function to create a new auction
    function createAuction(address _token, uint256 _duration) external returns (uint256) {
        // Validate input parameters
        require(_token != address(0), "Invalid token address");
        require(_duration > 0, "Duration must be greater than zero");

        auctionCount++;
        uint256 auctionId = auctionCount;

        auctions[auctionId] = Auction({
            token: _token,
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            highestBid: 0,
            highestBidder: address(0),
            ended: false
        });

        emit AuctionCreated(auctionId, msg.sender, block.timestamp, auctions[auctionId].endTime);
        return auctionId;
    }

    // Function to place a bid on an auction
    function placeBid(uint256 _auctionId, uint256 _amount) external {
        Auction storage auction = auctions[_auctionId];

        // Validate auction state
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(!auction.ended, "Auction is already ended");
        require(_amount > auction.highestBid, "Bid amount must be higher than the current highest bid");

        // Transfer the tokens from the bidder to the contract
        IERC20(auction.token).transferFrom(msg.sender, address(this), _amount);

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            IERC20(auction.token).transfer(auction.highestBidder, auction.highestBid);
        }

        // Update the auction with the new highest bid
        auction.highestBid = _amount;
        auction.highestBidder = msg.sender;

        emit BidPlaced(_auctionId, msg.sender, _amount);
    }

    // Function to end an auction and transfer the tokens to the winner
    function endAuction(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];

        // Validate auction state
        require(block.timestamp >= auction.endTime, "Auction is still ongoing");
        require(!auction.ended, "Auction is already ended");

        auction.ended = true;

        if (auction.highestBidder != address(0)) {
            // Transfer winning tokens to the auction creator
            IERC20(auction.token).transfer(auction.highestBidder, auction.highestBid);
            emit AuctionEnded(_auctionId, auction.highestBidder, auction.highestBid);
        }
    }

    // Function to withdraw tokens in case of an auction cancellation
    function withdrawTokens(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];

        // Validate auction cancellation
        require(auction.ended, "Auction has not ended yet");
        require(auction.highestBidder != address(0), "No bids were placed");

        // Refund the highest bid amount to the bidder
        require(msg.sender == auction.highestBidder, "Only highest bidder can withdraw");

        uint256 amount = auction.highestBid;
        auction.highestBid = 0; // Prevent re-entrancy

        IERC20(auction.token).transfer(msg.sender, amount);
    }
}
```
