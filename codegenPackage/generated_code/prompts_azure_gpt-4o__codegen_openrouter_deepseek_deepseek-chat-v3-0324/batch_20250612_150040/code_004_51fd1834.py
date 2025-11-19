"""
Generated Code Metadata:
========================
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Provide a step-by-step guide to integrate a high-to-low pricing mechanism into a decentralized application (dApp) for token sales, inspired by Fjord Foundry's methodology.
Generated: DETERMINISTIC_51fd183429b05c9a
Batch ID: 20250612_150040
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

contract DutchAuction is Ownable, ReentrancyGuard {
    IERC20 public token;
    IERC20 public paymentToken;
    
    uint256 public startTime;
    uint256 public endTime;
    uint256 public startPrice;
    uint256 public endPrice;
    uint256 public totalTokens;
    uint256 public tokensSold;
    uint256 public minCommitment;
    
    mapping(address => uint256) public commitments;
    
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);
    event AuctionFinalized(uint256 totalRaised, uint256 tokensSold);
    event RefundClaimed(address indexed buyer, uint256 amount);
    
    constructor(
        address _token,
        address _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _startPrice,
        uint256 _endPrice,
        uint256 _totalTokens,
        uint256 _minCommitment
    ) {
        require(_startTime >= block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_startPrice > _endPrice, "Start price must be higher than end price");
        require(_totalTokens > 0, "Total tokens must be positive");
        require(_minCommitment > 0, "Min commitment must be positive");
        
        token = IERC20(_token);
        paymentToken = IERC20(_paymentToken);
        startTime = _startTime;
        endTime = _endTime;
        startPrice = _startPrice;
        endPrice = _endPrice;
        totalTokens = _totalTokens;
        minCommitment = _minCommitment;
    }
    
    function getCurrentPrice() public view returns (uint256) {
        if (block.timestamp < startTime) {
            return startPrice;
        }
        if (block.timestamp >= endTime) {
            return endPrice;
        }
        
        uint256 timeElapsed = block.timestamp - startTime;
        uint256 totalDuration = endTime - startTime;
        uint256 priceRange = startPrice - endPrice;
        
        return startPrice - ((priceRange * timeElapsed) / totalDuration);
    }
    
    function commitTokens(uint256 amount) external nonReentrant {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Auction not active");
        require(amount >= minCommitment, "Amount below minimum commitment");
        
        uint256 currentPrice = getCurrentPrice();
        uint256 tokenAmount = (amount * 1e18) / currentPrice;
        
        require(token.balanceOf(address(this)) >= tokensSold + tokenAmount, "Not enough tokens remaining");
        
        paymentToken.transferFrom(msg.sender, address(this), amount);
        commitments[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;
        
        emit TokensPurchased(msg.sender, tokenAmount, currentPrice);
    }
    
    function finalizeAuction() external onlyOwner {
        require(block.timestamp > endTime, "Auction not ended");
        
        uint256 totalRaised = paymentToken.balanceOf(address(this));
        paymentToken.transfer(owner(), totalRaised);
        
        emit AuctionFinalized(totalRaised, tokensSold);
    }
    
    function claimTokens() external nonReentrant {
        require(block.timestamp > endTime, "Auction not ended");
        require(commitments[msg.sender] > 0, "No tokens to claim");
        
        uint256 tokenAmount = commitments[msg.sender];
        commitments[msg.sender] = 0;
        token.transfer(msg.sender, tokenAmount);
    }
    
    function refundExcessTokens() external onlyOwner {
        require(block.timestamp > endTime, "Auction not ended");
        
        uint256 remainingTokens = token.balanceOf(address(this)) - tokensSold;
        require(remainingTokens > 0, "No excess tokens");
        
        token.transfer(owner(), remainingTokens);
    }
    
    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > endTime + 30 days, "Emergency withdraw too early");
        
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }
        
        uint256 remainingFunds = paymentToken.balanceOf(address(this));
        if (remainingFunds > 0) {
            paymentToken.transfer(owner(), remainingFunds);
        }
    }
}
```
