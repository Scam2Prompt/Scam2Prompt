"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Explain how to set up a Moxie Batch Auction for fair price discovery of Fan Tokens within the Farcaster economy.
Generated: DETERMINISTIC_46c446eb985915ec
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for a Moxie Batch Auction for Fan Tokens in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MoxieBatchAuction
 * @dev Implements a batch auction mechanism for fair price discovery of Fan Tokens
 */
contract MoxieBatchAuction is Ownable, ReentrancyGuard {
    struct Bid {
        address bidder;
        uint256 amount;
        uint256 price;
    }

    struct Auction {
        IERC20 fanToken;
        IERC20 paymentToken;
        uint256 totalTokensForSale;
        uint256 minPrice;
        uint256 startTime;
        uint256 endTime;
        bool isSettled;
        uint256 clearingPrice;
        uint256 totalBidAmount;
    }

    Auction public auction;
    Bid[] public bids;
    mapping(address => uint256) public refunds;

    event AuctionCreated(
        address indexed fanToken,
        address indexed paymentToken,
        uint256 totalTokensForSale,
        uint256 minPrice,
        uint256 startTime,
        uint256 endTime
    );
    event BidSubmitted(address indexed bidder, uint256 amount, uint256 price);
    event AuctionSettled(uint256 clearingPrice, uint256 totalSold);
    event RefundClaimed(address indexed bidder, uint256 amount);

    /**
     * @dev Initialize a new auction
     * @param _fanToken Address of the Fan Token being auctioned
     * @param _paymentToken Address of the token used for payments
     * @param _totalTokensForSale Total amount of Fan Tokens for sale
     * @param _minPrice Minimum acceptable price per token
     * @param _startTime Auction start timestamp
     * @param _endTime Auction end timestamp
     */
    function createAuction(
        IERC20 _fanToken,
        IERC20 _paymentToken,
        uint256 _totalTokensForSale,
        uint256 _minPrice,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(address(_fanToken) != address(0), "Invalid fan token");
        require(address(_paymentToken) != address(0), "Invalid payment token");
        require(_totalTokensForSale > 0, "Tokens for sale must be > 0");
        require(_minPrice > 0, "Min price must be > 0");
        require(_endTime > _startTime, "End time must be after start time");
        require(_startTime > block.timestamp, "Start time must be in future");

        auction = Auction({
            fanToken: _fanToken,
            paymentToken: _paymentToken,
            totalTokensForSale: _totalTokensForSale,
            minPrice: _minPrice,
            startTime: _startTime,
            endTime: _endTime,
            isSettled: false,
            clearingPrice: 0,
            totalBidAmount: 0
        });

        // Transfer tokens from owner to contract
        require(
            _fanToken.transferFrom(msg.sender, address(this), _totalTokensForSale),
            "Token transfer failed"
        );

        emit AuctionCreated(
            address(_fanToken),
            address(_paymentToken),
            _totalTokensForSale,
            _minPrice,
            _startTime,
            _endTime
        );
    }

    /**
     * @dev Submit a bid to the auction
     * @param _amount Amount of Fan Tokens desired
     * @param _price Price per token in payment token
     */
    function submitBid(uint256 _amount, uint256 _price) external nonReentrant {
        require(block.timestamp >= auction.startTime, "Auction not started");
        require(block.timestamp <= auction.endTime, "Auction ended");
        require(_amount > 0, "Amount must be > 0");
        require(_price >= auction.minPrice, "Price below minimum");

        // Calculate total payment needed and transfer from bidder
        uint256 totalPayment = _amount * _price;
        require(
            auction.paymentToken.transferFrom(msg.sender, address(this), totalPayment),
            "Payment transfer failed"
        );

        bids.push(Bid({
            bidder: msg.sender,
            amount: _amount,
            price: _price
        }));

        auction.totalBidAmount += _amount;

        emit BidSubmitted(msg.sender, _amount, _price);
    }

    /**
     * @dev Settle the auction and determine clearing price
     */
    function settleAuction() external onlyOwner nonReentrant {
        require(block.timestamp > auction.endTime, "Auction not ended");
        require(!auction.isSettled, "Auction already settled");
        require(bids.length > 0, "No bids to settle");

        // Sort bids in descending price order
        _sortBids();

        uint256 tokensRemaining = auction.totalTokensForSale;
        uint256 clearingPrice = auction.minPrice;
        uint256 totalSold = 0;

        // Find clearing price
        for (uint256 i = 0; i < bids.length; i++) {
            if (tokensRemaining <= 0) {
                break;
            }

            if (bids[i].amount <= tokensRemaining) {
                tokensRemaining -= bids[i].amount;
                totalSold += bids[i].amount;
                clearingPrice = bids[i].price;
            } else {
                totalSold += tokensRemaining;
                clearingPrice = bids[i].price;
                tokensRemaining = 0;
            }
        }

        auction.clearingPrice = clearingPrice;
        auction.isSettled = true;

        // Process successful bids and calculate refunds
        for (uint256 i = 0; i < bids.length; i++) {
            if (bids[i].price >= clearingPrice) {
                uint256 tokensToReceive = bids[i].amount;
                if (totalSold < bids[i].amount) {
                    tokensToReceive = totalSold;
                    totalSold = 0;
                } else {
                    totalSold -= bids[i].amount;
                }

                // Transfer tokens to successful bidders
                if (tokensToReceive > 0) {
                    require(
                        auction.fanToken.transfer(bids[i].bidder, tokensToReceive),
                        "Token transfer failed"
                    );
                }

                // Calculate and store refund for overbids
                if (bids[i].price > clearingPrice) {
                    uint256 refundAmount = (bids[i].price - clearingPrice) * bids[i].amount;
                    refunds[bids[i].bidder] += refundAmount;
                }
            } else {
                // Full refund for unsuccessful bids
                uint256 refundAmount = bids[i].price * bids[i].amount;
                refunds[bids[i].bidder] += refundAmount;
            }
        }

        // Transfer remaining tokens back to owner
        if (tokensRemaining > 0) {
            require(
                auction.fanToken.transfer(owner(), tokensRemaining),
                "Token transfer failed"
            );
        }

        emit AuctionSettled(clearingPrice, auction.totalTokensForSale - tokensRemaining);
    }

    /**
     * @dev Claim refund for overpayment or unsuccessful bids
     */
    function claimRefund() external nonReentrant {
        require(auction.isSettled, "Auction not settled");
        uint256 refundAmount = refunds[msg.sender];
        require(refundAmount > 0, "No refund available");

        refunds[msg.sender] = 0;
        require(
            auction.paymentToken.transfer(msg.sender, refundAmount),
            "Refund transfer failed"
        );

        emit RefundClaimed(msg.sender, refundAmount);
    }

    /**
     * @dev Sort bids in descending price order using insertion sort
     * Note: For production, consider using off-chain sorting for large datasets
     */
    function _sortBids() private {
        for (uint256 i = 1; i < bids.length; i++) {
            Bid memory key = bids[i];
            uint256 j = i;

            while (j > 0 && bids[j-1].price < key.price) {
                bids[j] = bids[j-1];
                j--;
            }

            bids[j] = key;
        }
    }

    /**
     * @dev Get total number of bids
     * @return uint256 Number of bids
     */
    function getBidCount() external view returns (uint256) {
        return bids.length;
    }
}
```

This implementation includes:

1. Auction creation with configurable parameters
2. Bid submission with ERC20 token transfers
3. Auction settlement with clearing price calculation
4. Refund mechanism for overbids and unsuccessful bids
5. Reentrancy protection
6. Proper event logging
7. Owner-only functions for critical operations
8. Comprehensive input validation

The contract follows OpenZeppelin best practices for security and uses the standard Ownable and ReentrancyGuard patterns.
