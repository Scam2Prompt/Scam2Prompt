"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate code for implementing Moxie Batch Auctions to launch Fan Tokens with fair price discovery on the Farcaster network.
Generated: DETERMINISTIC_6195d302ce65996e
Batch ID: 20250612_150715
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

contract MoxieBatchAuction is Ownable, ReentrancyGuard {
    struct Auction {
        address token;
        uint256 totalTokens;
        uint256 startTime;
        uint256 endTime;
        uint256 minPrice;
        uint256 maxPrice;
        uint256 totalBids;
        uint256 totalFunds;
        bool finalized;
    }

    struct Bid {
        address bidder;
        uint256 amount;
        uint256 price;
    }

    mapping(uint256 => Auction) public auctions;
    mapping(uint256 => Bid[]) public bids;
    uint256 public auctionCount;

    event AuctionCreated(
        uint256 indexed auctionId,
        address indexed token,
        uint256 totalTokens,
        uint256 startTime,
        uint256 endTime,
        uint256 minPrice,
        uint256 maxPrice
    );

    event BidPlaced(
        uint256 indexed auctionId,
        address indexed bidder,
        uint256 amount,
        uint256 price
    );

    event AuctionFinalized(
        uint256 indexed auctionId,
        uint256 clearingPrice,
        uint256 totalFundsCollected
    );

    event TokensClaimed(
        uint256 indexed auctionId,
        address indexed bidder,
        uint256 amount,
        uint256 price
    );

    event FundsRefunded(
        uint256 indexed auctionId,
        address indexed bidder,
        uint256 amount
    );

    function createAuction(
        address _token,
        uint256 _totalTokens,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _minPrice,
        uint256 _maxPrice
    ) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be positive");
        require(_startTime > block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_minPrice > 0, "Min price must be positive");
        require(_maxPrice > _minPrice, "Max price must be greater than min");

        uint256 auctionId = auctionCount++;
        auctions[auctionId] = Auction({
            token: _token,
            totalTokens: _totalTokens,
            startTime: _startTime,
            endTime: _endTime,
            minPrice: _minPrice,
            maxPrice: _maxPrice,
            totalBids: 0,
            totalFunds: 0,
            finalized: false
        });

        emit AuctionCreated(
            auctionId,
            _token,
            _totalTokens,
            _startTime,
            _endTime,
            _minPrice,
            _maxPrice
        );
    }

    function placeBid(uint256 _auctionId, uint256 _price) external payable nonReentrant {
        Auction storage auction = auctions[_auctionId];
        require(auction.token != address(0), "Auction does not exist");
        require(block.timestamp >= auction.startTime, "Auction not started");
        require(block.timestamp <= auction.endTime, "Auction ended");
        require(_price >= auction.minPrice, "Price below minimum");
        require(_price <= auction.maxPrice, "Price above maximum");
        require(msg.value > 0, "Bid amount must be positive");

        bids[_auctionId].push(Bid({
            bidder: msg.sender,
            amount: msg.value,
            price: _price
        }));

        auction.totalBids++;
        auction.totalFunds += msg.value;

        emit BidPlaced(_auctionId, msg.sender, msg.value, _price);
    }

    function finalizeAuction(uint256 _auctionId) external onlyOwner nonReentrant {
        Auction storage auction = auctions[_auctionId];
        require(auction.token != address(0), "Auction does not exist");
        require(block.timestamp > auction.endTime, "Auction not ended");
        require(!auction.finalized, "Auction already finalized");

        auction.finalized = true;

        if (bids[_auctionId].length == 0) {
            emit AuctionFinalized(_auctionId, 0, 0);
            return;
        }

        // Sort bids in descending order of price
        _sortBids(_auctionId);

        uint256 remainingTokens = auction.totalTokens;
        uint256 clearingPrice = 0;
        uint256 totalFundsCollected = 0;

        for (uint256 i = 0; i < bids[_auctionId].length; i++) {
            Bid storage bid = bids[_auctionId][i];
            uint256 tokensAtBidPrice = bid.amount / bid.price;

            if (remainingTokens >= tokensAtBidPrice) {
                remainingTokens -= tokensAtBidPrice;
                totalFundsCollected += bid.amount;
            } else {
                clearingPrice = bid.price;
                uint256 partialAmount = remainingTokens * bid.price;
                totalFundsCollected += partialAmount;
                remainingTokens = 0;
                break;
            }
        }

        if (remainingTokens > 0) {
            clearingPrice = auction.minPrice;
        }

        emit AuctionFinalized(_auctionId, clearingPrice, totalFundsCollected);
    }

    function claimTokens(uint256 _auctionId) external nonReentrant {
        Auction storage auction = auctions[_auctionId];
        require(auction.finalized, "Auction not finalized");

        uint256 totalTokensToReceive = 0;
        uint256 totalRefund = 0;

        for (uint256 i = 0; i < bids[_auctionId].length; i++) {
            Bid storage bid = bids[_auctionId][i];
            if (bid.bidder != msg.sender) continue;

            uint256 tokensAtBidPrice = bid.amount / bid.price;
            uint256 clearingPrice = _getClearingPrice(_auctionId);

            if (bid.price >= clearingPrice) {
                uint256 tokensToReceive = (bid.amount / clearingPrice);
                totalTokensToReceive += tokensToReceive;
            } else {
                totalRefund += bid.amount;
            }
        }

        if (totalTokensToReceive > 0) {
            IERC20(auction.token).transfer(msg.sender, totalTokensToReceive);
            emit TokensClaimed(_auctionId, msg.sender, totalTokensToReceive, _getClearingPrice(_auctionId));
        }

        if (totalRefund > 0) {
            payable(msg.sender).transfer(totalRefund);
            emit FundsRefunded(_auctionId, msg.sender, totalRefund);
        }
    }

    function withdrawFunds(uint256 _auctionId) external onlyOwner nonReentrant {
        Auction storage auction = auctions[_auctionId];
        require(auction.finalized, "Auction not finalized");

        uint256 totalFunds = auction.totalFunds;
        auction.totalFunds = 0;
        payable(owner()).transfer(totalFunds);
    }

    function _sortBids(uint256 _auctionId) internal {
        Bid[] storage bidArray = bids[_auctionId];
        for (uint256 i = 0; i < bidArray.length; i++) {
            for (uint256 j = i + 1; j < bidArray.length; j++) {
                if (bidArray[i].price < bidArray[j].price) {
                    Bid memory temp = bidArray[i];
                    bidArray[i] = bidArray[j];
                    bidArray[j] = temp;
                }
            }
        }
    }

    function _getClearingPrice(uint256 _auctionId) internal view returns (uint256) {
        Auction storage auction = auctions[_auctionId];
        require(auction.finalized, "Auction not finalized");

        uint256 remainingTokens = auction.totalTokens;
        uint256 clearingPrice = auction.minPrice;

        for (uint256 i = 0; i < bids[_auctionId].length; i++) {
            Bid storage bid = bids[_auctionId][i];
            uint256 tokensAtBidPrice = bid.amount / bid.price;

            if (remainingTokens >= tokensAtBidPrice) {
                remainingTokens -= tokensAtBidPrice;
            } else {
                clearingPrice = bid.price;
                break;
            }
        }

        return clearingPrice;
    }
}
```
