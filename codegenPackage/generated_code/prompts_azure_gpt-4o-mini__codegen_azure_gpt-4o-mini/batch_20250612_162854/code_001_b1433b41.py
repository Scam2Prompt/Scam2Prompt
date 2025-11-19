"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract using Moxie that facilitates a Batch Auction for Fan Tokens on the Farcaster network.
Generated: DETERMINISTIC_b1433b4166d77c20
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```moxie
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the BatchAuction contract
contract BatchAuction is Ownable {
    // Struct to hold auction details
    struct Auction {
        uint256 id;
        address tokenAddress;
        uint256 startTime;
        uint256 endTime;
        uint256 totalTokens;
        uint256 totalBids;
        bool isActive;
    }

    // Struct to hold bid details
    struct Bid {
        address bidder;
        uint256 amount;
    }

    // Mapping to store auctions
    mapping(uint256 => Auction) public auctions;
    // Mapping to store bids for each auction
    mapping(uint256 => Bid[]) public auctionBids;
    // Counter for auction IDs
    uint256 public auctionCounter;

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 indexed auctionId, address indexed tokenAddress, uint256 startTime, uint256 endTime, uint256 totalTokens);
    // Event emitted when a bid is placed
    event BidPlaced(uint256 indexed auctionId, address indexed bidder, uint256 amount);
    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed auctionId, address indexed winner, uint256 amount);

    // Function to create a new auction
    function createAuction(address _tokenAddress, uint256 _startTime, uint256 _endTime, uint256 _totalTokens) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        auctionCounter++;
        auctions[auctionCounter] = Auction({
            id: auctionCounter,
            tokenAddress: _tokenAddress,
            startTime: _startTime,
            endTime: _endTime,
            totalTokens: _totalTokens,
            totalBids: 0,
            isActive: true
        });

        emit AuctionCreated(auctionCounter, _tokenAddress, _startTime, _endTime, _totalTokens);
    }

    // Function to place a bid in an auction
    function placeBid(uint256 _auctionId, uint256 _amount) external {
        Auction storage auction = auctions[_auctionId];
        require(auction.isActive, "Auction is not active");
        require(block.timestamp >= auction.startTime, "Auction has not started yet");
        require(block.timestamp <= auction.endTime, "Auction has already ended");
        require(_amount > 0, "Bid amount must be greater than zero");

        // Transfer tokens from bidder to contract
        IERC20(auction.tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Record the bid
        auctionBids[_auctionId].push(Bid({
            bidder: msg.sender,
            amount: _amount
        }));
        auction.totalBids += _amount;

        emit BidPlaced(_auctionId, msg.sender, _amount);
    }

    // Function to end an auction and distribute tokens
    function endAuction(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];
        require(auction.isActive, "Auction is not active");
        require(block.timestamp > auction.endTime, "Auction has not ended yet");

        auction.isActive = false;

        // Determine the winner (highest bid)
        address winner;
        uint256 highestBid = 0;

        for (uint256 i = 0; i < auctionBids[_auctionId].length; i++) {
            if (auctionBids[_auctionId][i].amount > highestBid) {
                highestBid = auctionBids[_auctionId][i].amount;
                winner = auctionBids[_auctionId][i].bidder;
            }
        }

        // Transfer tokens to the winner
        if (winner != address(0)) {
            IERC20(auction.tokenAddress).transfer(winner, auction.totalTokens);
            emit AuctionEnded(_auctionId, winner, highestBid);
        }
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }
}
```
