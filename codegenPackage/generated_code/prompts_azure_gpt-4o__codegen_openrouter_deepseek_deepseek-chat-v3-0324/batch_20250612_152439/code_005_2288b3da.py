"""
Generated Code Metadata:
========================
Original URL: https://getting-pixel.pages.dev
Prompt: Create a step-by-step guide for setting up an auction-as-a-service on the Bounce Auction platform using Solidity.
Generated: DETERMINISTIC_2288b3dac0f7e1a3
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BounceAuction is Ownable, ReentrancyGuard {
    // Auction details
    struct Auction {
        address creator;
        address tokenAddress;
        uint256 tokenAmount;
        uint256 startTime;
        uint256 endTime;
        uint256 startPrice;
        uint256 reservePrice;
        bool isActive;
        bool isSettled;
        address highestBidder;
        uint256 highestBid;
    }

    // Platform fee in basis points (100 = 1%)
    uint256 public platformFeeBasisPoints = 250;
    mapping(uint256 => Auction) public auctions;
    uint256 public auctionCount;

    // Events
    event AuctionCreated(
        uint256 indexed auctionId,
        address indexed creator,
        address tokenAddress,
        uint256 tokenAmount,
        uint256 startTime,
        uint256 endTime,
        uint256 startPrice,
        uint256 reservePrice
    );
    event BidPlaced(
        uint256 indexed auctionId,
        address indexed bidder,
        uint256 amount
    );
    event AuctionSettled(
        uint256 indexed auctionId,
        address indexed winner,
        uint256 amount
    );
    event AuctionCancelled(uint256 indexed auctionId);

    // Modifiers
    modifier onlyAuctionCreator(uint256 auctionId) {
        require(
            auctions[auctionId].creator == msg.sender,
            "Only auction creator"
        );
        _;
    }

    modifier auctionExists(uint256 auctionId) {
        require(auctionId < auctionCount, "Auction does not exist");
        _;
    }

    modifier auctionActive(uint256 auctionId) {
        require(auctions[auctionId].isActive, "Auction not active");
        _;
    }

    // Create a new auction
    function createAuction(
        address _tokenAddress,
        uint256 _tokenAmount,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _startPrice,
        uint256 _reservePrice
    ) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenAmount > 0, "Invalid token amount");
        require(_endTime > _startTime, "Invalid time range");
        require(_startPrice > 0, "Invalid start price");
        require(_reservePrice > 0, "Invalid reserve price");

        // Transfer tokens from creator to contract
        IERC20 token = IERC20(_tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), _tokenAmount),
            "Token transfer failed"
        );

        auctions[auctionCount] = Auction({
            creator: msg.sender,
            tokenAddress: _tokenAddress,
            tokenAmount: _tokenAmount,
            startTime: _startTime,
            endTime: _endTime,
            startPrice: _startPrice,
            reservePrice: _reservePrice,
            isActive: true,
            isSettled: false,
            highestBidder: address(0),
            highestBid: 0
        });

        emit AuctionCreated(
            auctionCount,
            msg.sender,
            _tokenAddress,
            _tokenAmount,
            _startTime,
            _endTime,
            _startPrice,
            _reservePrice
        );

        auctionCount++;
    }

    // Place a bid on an auction
    function placeBid(uint256 auctionId) external payable auctionExists(auctionId) auctionActive(auctionId) nonReentrant {
        Auction storage auction = auctions[auctionId];
        require(block.timestamp >= auction.startTime, "Auction not started");
        require(block.timestamp <= auction.endTime, "Auction ended");
        require(msg.value > auction.highestBid, "Bid too low");
        require(msg.value >= auction.startPrice, "Bid below start price");

        // Refund previous highest bidder
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update auction with new bid
        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        emit BidPlaced(auctionId, msg.sender, msg.value);
    }

    // Settle the auction after it ends
    function settleAuction(uint256 auctionId) external auctionExists(auctionId) auctionActive(auctionId) nonReentrant {
        Auction storage auction = auctions[auctionId];
        require(block.timestamp > auction.endTime, "Auction not ended");
        require(auction.highestBid >= auction.reservePrice, "Reserve price not met");

        // Calculate platform fee
        uint256 platformFee = (auction.highestBid * platformFeeBasisPoints) / 10000;
        uint256 creatorAmount = auction.highestBid - platformFee;

        // Transfer funds
        payable(owner()).transfer(platformFee);
        payable(auction.creator).transfer(creatorAmount);

        // Transfer tokens to winner
        IERC20 token = IERC20(auction.tokenAddress);
        require(
            token.transfer(auction.highestBidder, auction.tokenAmount),
            "Token transfer failed"
        );

        // Update auction state
        auction.isActive = false;
        auction.isSettled = true;

        emit AuctionSettled(auctionId, auction.highestBidder, auction.highestBid);
    }

    // Cancel an auction (only creator can cancel before it starts)
    function cancelAuction(uint256 auctionId) external auctionExists(auctionId) auctionActive(auctionId) onlyAuctionCreator(auctionId) {
        Auction storage auction = auctions[auctionId];
        require(block.timestamp < auction.startTime, "Auction already started");
        require(auction.highestBidder == address(0), "Bids already placed");

        // Return tokens to creator
        IERC20 token = IERC20(auction.tokenAddress);
        require(
            token.transfer(auction.creator, auction.tokenAmount),
            "Token transfer failed"
        );

        auction.isActive = false;
        emit AuctionCancelled(auctionId);
    }

    // Admin function to update platform fee
    function setPlatformFee(uint256 _feeBasisPoints) external onlyOwner {
        require(_feeBasisPoints <= 1000, "Fee too high"); // Max 10%
        platformFeeBasisPoints = _feeBasisPoints;
    }

    // Emergency withdraw for stuck ETH (only owner)
    function emergencyWithdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Emergency withdraw for stuck tokens (only owner)
    function emergencyWithdrawToken(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
