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

```python
# BatchAuction.sol
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BatchAuction
 * @dev A smart contract for conducting batch auctions of Fan Tokens on Farcaster
 * @notice This contract allows bidders to place bids during an auction period,
 *         then claims are processed after the auction concludes
 */
contract BatchAuction is Ownable, ReentrancyGuard {
    IERC20 public fanToken;
    IERC20 public paymentToken;
    
    uint256 public auctionStartTime;
    uint256 public auctionEndTime;
    uint256 public totalTokensForSale;
    uint256 public totalBids;
    uint256 public clearingPrice;
    bool public auctionSettled;
    
    struct Bid {
        address bidder;
        uint256 amount;
        uint256 price;
    }
    
    mapping(address => uint256) public bids;
    Bid[] public bidList;
    
    event BidPlaced(address indexed bidder, uint256 amount, uint256 price);
    event AuctionSettled(uint256 clearingPrice);
    event TokensClaimed(address indexed bidder, uint256 amount);
    
    /**
     * @dev Initialize the auction contract
     * @param _fanToken Address of the Fan Token being auctioned
     * @param _paymentToken Address of the token used for payments (e.g., USDC)
     * @param _totalTokensForSale Total amount of Fan Tokens to be sold
     * @param _auctionStartTime Timestamp when auction starts
     * @param _auctionDuration Duration of auction in seconds
     */
    constructor(
        address _fanToken,
        address _paymentToken,
        uint256 _totalTokensForSale,
        uint256 _auctionStartTime,
        uint256 _auctionDuration
    ) {
        require(_fanToken != address(0), "Invalid fan token address");
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_totalTokensForSale > 0, "Tokens for sale must be > 0");
        require(_auctionDuration > 0, "Auction duration must be > 0");
        
        fanToken = IERC20(_fanToken);
        paymentToken = IERC20(_paymentToken);
        totalTokensForSale = _totalTokensForSale;
        auctionStartTime = _auctionStartTime;
        auctionEndTime = _auctionStartTime + _auctionDuration;
    }
    
    /**
     * @dev Place a bid in the auction
     * @param amount Amount of Fan Tokens desired
     * @param price Price per token in paymentToken
     */
    function placeBid(uint256 amount, uint256 price) external nonReentrant {
        require(block.timestamp >= auctionStartTime, "Auction not started");
        require(block.timestamp < auctionEndTime, "Auction ended");
        require(amount > 0, "Amount must be > 0");
        require(price > 0, "Price must be > 0");
        
        uint256 totalPayment = amount * price;
        require(
            paymentToken.transferFrom(msg.sender, address(this), totalPayment),
            "Payment transfer failed"
        );
        
        bids[msg.sender] += amount;
        bidList.push(Bid(msg.sender, amount, price));
        totalBids += amount;
        
        emit BidPlaced(msg.sender, amount, price);
    }
    
    /**
     * @dev Settle the auction and calculate clearing price
     * @notice Only owner can call this after auction ends
     */
    function settleAuction() external onlyOwner {
        require(block.timestamp >= auctionEndTime, "Auction not ended");
        require(!auctionSettled, "Auction already settled");
        
        // Simple clearing price calculation (Dutch auction style)
        // In production, you would implement more sophisticated logic
        bidList.sort((a, b) => b.price - a.price);
        
        uint256 cumulativeAmount = 0;
        uint256 i = 0;
        
        while (i < bidList.length && cumulativeAmount < totalTokensForSale) {
            cumulativeAmount += bidList[i].amount;
            clearingPrice = bidList[i].price;
            i++;
        }
        
        auctionSettled = true;
        emit AuctionSettled(clearingPrice);
    }
    
    /**
     * @dev Allow bidders to claim their purchased tokens
     */
    function claimTokens() external nonReentrant {
        require(auctionSettled, "Auction not settled");
        require(bids[msg.sender] > 0, "No bids to claim");
        
        uint256 eligibleAmount = 0;
        uint256 refundAmount = 0;
        
        for (uint256 i = 0; i < bidList.length; i++) {
            if (bidList[i].bidder == msg.sender) {
                if (bidList[i].price >= clearingPrice) {
                    eligibleAmount += bidList[i].amount;
                } else {
                    refundAmount += bidList[i].amount * bidList[i].price;
                }
            }
        }
        
        // Transfer eligible tokens to bidder
        if (eligibleAmount > 0) {
            require(
                fanToken.transfer(msg.sender, eligibleAmount),
                "Token transfer failed"
            );
            emit TokensClaimed(msg.sender, eligibleAmount);
        }
        
        // Refund for bids below clearing price
        if (refundAmount > 0) {
            require(
                paymentToken.transfer(msg.sender, refundAmount),
                "Refund transfer failed"
            );
        }
        
        bids[msg.sender] = 0;
    }
    
    /**
     * @dev Withdraw remaining funds after auction settlement
     * @notice Only owner can call this
     */
    function withdrawRemainingFunds() external onlyOwner {
        require(auctionSettled, "Auction not settled");
        uint256 balance = paymentToken.balanceOf(address(this));
        paymentToken.transfer(owner(), balance);
    }
    
    /**
     * @dev Withdraw unsold tokens after auction settlement
     * @notice Only owner can call this
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(auctionSettled, "Auction not settled");
        uint256 unsold = totalTokensForSale - fanToken.balanceOf(address(this));
        if (unsold > 0) {
            fanToken.transfer(owner(), unsold);
        }
    }
}
```
