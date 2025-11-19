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

/**
 * @title NFT Auction Platform
 * @dev A simple smart contract for an NFT auction platform inspired by Icosa Hedron's features.
 */
contract NFTAuction {
    // Struct to represent an auction
    struct Auction {
        address seller; // Address of the seller
        address highestBidder; // Address of the highest bidder
        uint256 highestBid; // Highest bid amount
        uint256 startTime; // Auction start time
        uint256 endTime; // Auction end time
        bool active; // Auction status
    }

    // Mapping to store auctions by their ID
    mapping(uint256 => Auction) public auctions;

    // Mapping to store pending withdrawals for bidders
    mapping(address => uint256) public pendingWithdrawals;

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 auctionId, address seller, uint256 startTime, uint256 endTime);

    // Event emitted when a new bid is placed
    event NewBid(uint256 auctionId, address bidder, uint256 amount);

    // Event emitted when an auction is finalized
    event AuctionFinalized(uint256 auctionId, address winner, uint256 amount);

    // Modifier to check if the auction is active
    modifier isActive(uint256 auctionId) {
        require(auctions[auctionId].active, "Auction is not active");
        require(block.timestamp < auctions[auctionId].endTime, "Auction has ended");
        _;
    }

    // Modifier to check if the auction has ended
    modifier hasEnded(uint256 auctionId) {
        require(block.timestamp >= auctions[auctionId].endTime, "Auction has not ended yet");
        _;
    }

    /**
     * @dev Create a new auction.
     * @param auctionId Unique ID for the auction.
     * @param duration Duration of the auction in seconds.
     */
    function createAuction(uint256 auctionId, uint256 duration) external {
        require(auctions[auctionId].seller == address(0), "Auction ID already exists");
        require(duration > 0, "Duration must be greater than zero");

        auctions[auctionId] = Auction({
            seller: msg.sender,
            highestBidder: address(0),
            highestBid: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            active: true
        });

        emit AuctionCreated(auctionId, msg.sender, block.timestamp, block.timestamp + duration);
    }

    /**
     * @dev Place a bid on an active auction.
     * @param auctionId ID of the auction to bid on.
     */
    function placeBid(uint256 auctionId) external payable isActive(auctionId) {
        Auction storage auction = auctions[auctionId];
        require(msg.value > auction.highestBid, "Bid amount must be higher than the current highest bid");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            pendingWithdrawals[auction.highestBidder] += auction.highestBid;
        }

        // Update auction with new highest bid
        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        emit NewBid(auctionId, msg.sender, msg.value);
    }

    /**
     * @dev Finalize an auction and transfer funds to the seller.
     * @param auctionId ID of the auction to finalize.
     */
    function finalizeAuction(uint256 auctionId) external hasEnded(auctionId) {
        Auction storage auction = auctions[auctionId];
        require(auction.active, "Auction is already finalized");
        require(auction.seller == msg.sender || msg.sender == auction.highestBidder, "Only seller or highest bidder can finalize");

        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer funds to the seller
            payable(auction.seller).transfer(auction.highestBid);
            emit AuctionFinalized(auctionId, auction.highestBidder, auction.highestBid);
        } else {
            // No bids were placed, auction ended without a winner
            emit AuctionFinalized(auctionId, address(0), 0);
        }
    }

    /**
     * @dev Withdraw pending funds for a bidder.
     */
    function withdrawFunds() external {
        uint256 amount = pendingWithdrawals[msg.sender];
        require(amount > 0, "No funds to withdraw");

        pendingWithdrawals[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
```
