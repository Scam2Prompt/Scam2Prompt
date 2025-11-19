"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Write a smart contract for a fan token auction using the Moxie Protocol on Farcaster.
Generated: DETERMINISTIC_76e865f6f0d07d84
Batch ID: 20250622_211215
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a Fan Token Auction using Moxie Protocol
contract FanTokenAuction is Ownable {
    using SafeMath for uint256;

    // Struct to hold auction details
    struct Auction {
        address payable seller; // Seller of the token
        uint256 startingPrice;  // Starting price of the auction
        uint256 highestBid;     // Highest bid placed
        address highestBidder;  // Address of the highest bidder
        uint256 endTime;        // End time of the auction
        bool ended;             // Status of the auction
    }

    // Mapping of token ID to its auction details
    mapping(uint256 => Auction) public auctions;

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 indexed tokenId, uint256 startingPrice, uint256 endTime);
    
    // Event emitted when a new bid is placed
    event NewBid(uint256 indexed tokenId, address indexed bidder, uint256 amount);
    
    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed tokenId, address winner, uint256 amount);

    // Function to create a new auction
    function createAuction(uint256 tokenId, uint256 startingPrice, uint256 duration) external onlyOwner {
        require(auctions[tokenId].endTime == 0, "Auction already exists for this token");

        // Create a new auction
        auctions[tokenId] = Auction({
            seller: payable(msg.sender),
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: address(0),
            endTime: block.timestamp.add(duration),
            ended: false
        });

        emit AuctionCreated(tokenId, startingPrice, auctions[tokenId].endTime);
    }

    // Function to place a bid on an auction
    function placeBid(uint256 tokenId) external payable {
        Auction storage auction = auctions[tokenId];

        // Ensure the auction is valid and not ended
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value > auction.highestBid && msg.value >= auction.startingPrice, "Bid not high enough");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update auction details with the new highest bid
        auction.highestBid = msg.value;
        auction.highestBidder = msg.sender;

        emit NewBid(tokenId, msg.sender, msg.value);
    }

    // Function to end the auction and transfer funds
    function endAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];

        // Ensure the auction is valid and has ended
        require(block.timestamp >= auction.endTime, "Auction not yet ended");
        require(!auction.ended, "Auction already ended");

        auction.ended = true;

        // Transfer the highest bid to the seller
        if (auction.highestBidder != address(0)) {
            auction.seller.transfer(auction.highestBid);
        }

        emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
    }

    // Function to withdraw funds in case of an error
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
