"""
Generated Code Metadata:
========================
Original URL: https://lanimal443331.github.io
Prompt: Design a smart contract for a decentralized autonomous organization (DAO) that utilizes LBPs for fundraising, ensuring equitable distribution and community-driven price discovery.
Generated: DETERMINISTIC_9082f74346e17825
Batch ID: 20250622_211009
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DAO Fundraising Contract with Liquidity Bootstrapping Pool (LBP)
 * @notice Implements a DAO fundraising mechanism using LBP for fair price discovery
 */
contract DAOLBPFundraiser is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public saleToken;
    
    // Payment token (typically stablecoin)
    IERC20 public paymentToken;
    
    // LBP parameters
    uint256 public startTime;
    uint256 public endTime;
    uint256 public initialWeight;
    uint256 public finalWeight;
    uint256 public initialPrice;
    uint256 public totalTokensForSale;
    
    // Track raised funds
    uint256 public totalRaised;
    
    // Track token allocations
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokenAllocations;
    
    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);
    event FundsWithdrawn(address indexed recipient, uint256 amount);
    event SaleExtended(uint256 newEndTime);
    event SaleConcluded(uint256 totalRaised);
    
    /**
     * @dev Constructor to initialize the LBP sale
     * @param _saleToken Address of the token being sold
     * @param _paymentToken Address of the payment token
     * @param _startTime Sale start time (unix timestamp)
     * @param _endTime Sale end time (unix timestamp)
     * @param _initialWeight Initial weight (percentage)
     * @param _finalWeight Final weight (percentage)
     * @param _initialPrice Initial price per token
     * @param _totalTokensForSale Total tokens available for sale
     */
    constructor(
        address _saleToken,
        address _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _initialWeight,
        uint256 _finalWeight,
        uint256 _initialPrice,
        uint256 _totalTokensForSale
    ) {
        require(_startTime >= block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_initialWeight > 0 && _finalWeight > 0, "Weights must be positive");
        require(_initialPrice > 0, "Initial price must be positive");
        require(_totalTokensForSale > 0, "Token amount must be positive");
        
        saleToken = IERC20(_saleToken);
        paymentToken = IERC20(_paymentToken);
        startTime = _startTime;
        endTime = _endTime;
        initialWeight = _initialWeight;
        finalWeight = _finalWeight;
        initialPrice = _initialPrice;
        totalTokensForSale = _totalTokensForSale;
    }
    
    /**
     * @dev Calculate current token price based on LBP weights
     * @return Current token price
     */
    function currentPrice() public view returns (uint256) {
        if (block.timestamp < startTime) {
            return initialPrice;
        }
        if (block.timestamp >= endTime) {
            return _calculatePrice(endTime);
        }
        return _calculatePrice(block.timestamp);
    }
    
    /**
     * @dev Internal price calculation based on time elapsed
     * @param _currentTime Timestamp to calculate price for
     * @return Calculated price
     */
    function _calculatePrice(uint256 _currentTime) internal view returns (uint256) {
        uint256 elapsed = _currentTime.sub(startTime);
        uint256 duration = endTime.sub(startTime);
        
        uint256 weight = initialWeight.sub(
            initialWeight.sub(finalWeight).mul(elapsed).div(duration)
        );
        
        return initialPrice.mul(initialWeight).div(weight);
    }
    
    /**
     * @dev Purchase tokens during the sale
     * @param amount Amount of payment tokens to spend
     */
    function purchaseTokens(uint256 amount) external nonReentrant {
        require(block.timestamp >= startTime, "Sale has not started");
        require(block.timestamp <= endTime, "Sale has ended");
        require(amount > 0, "Amount must be positive");
        
        uint256 price = currentPrice();
        uint256 tokensToReceive = amount.mul(1e18).div(price);
        
        require(
            saleToken.balanceOf(address(this)) >= tokensToReceive,
            "Not enough tokens remaining"
        );
        
        // Transfer payment tokens from buyer
        paymentToken.transferFrom(msg.sender, address(this), amount);
        
        // Update records
        contributions[msg.sender] = contributions[msg.sender].add(amount);
        tokenAllocations[msg.sender] = tokenAllocations[msg.sender].add(tokensToReceive);
        totalRaised = totalRaised.add(amount);
        
        // Transfer tokens to buyer
        saleToken.transfer(msg.sender, tokensToReceive);
        
        emit TokensPurchased(msg.sender, tokensToReceive, price);
    }
    
    /**
     * @dev Withdraw raised funds (owner only)
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > endTime, "Sale must be completed");
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        paymentToken.transfer(owner(), balance);
        emit FundsWithdrawn(owner(), balance);
    }
    
    /**
     * @dev Extend sale duration (owner only)
     * @param newEndTime New end time
     */
    function extendSale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > endTime, "New end time must be later");
        require(block.timestamp < endTime, "Sale already ended");
        
        endTime = newEndTime;
        emit SaleExtended(newEndTime);
    }
    
    /**
     * @dev Emergency withdraw remaining tokens after sale (owner only)
     */
    function emergencyWithdrawTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale must be completed");
        uint256 remaining = saleToken.balanceOf(address(this));
        require(remaining > 0, "No tokens remaining");
        
        saleToken.transfer(owner(), remaining);
    }
    
    /**
     * @dev Get user contribution and allocation
     * @param user Address to query
     * @return contribution Payment token amount contributed
     * @return allocation Token amount allocated
     */
    function getUserInfo(address user) external view returns (uint256 contribution, uint256 allocation) {
        return (contributions[user], tokenAllocations[user]);
    }
}
```
