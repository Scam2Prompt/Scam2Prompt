"""
Generated Code Metadata:
========================
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Design a smart contract for a decentralized autonomous organization (DAO) that utilizes LBPs for fundraising and token sales, ensuring fair and transparent distribution of tokens.
Generated: DETERMINISTIC_15bd88bbfdfe2b53
Batch ID: 20250622_205030
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

contract DAOLBP is Ownable, ReentrancyGuard {
    IERC20 public token;
    IERC20 public paymentToken;
    
    uint256 public startTime;
    uint256 public endTime;
    uint256 public initialPrice;
    uint256 public finalPrice;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;
    
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensClaimed;
    
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    constructor(
        address _token,
        address _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _initialPrice,
        uint256 _finalPrice,
        uint256 _totalTokensForSale
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_paymentToken != address(0), "Payment token address cannot be zero");
        require(_endTime > _startTime, "End time must be after start time");
        require(_initialPrice > 0 && _finalPrice > 0, "Prices must be positive");
        require(_totalTokensForSale > 0, "Total tokens for sale must be positive");
        
        token = IERC20(_token);
        paymentToken = IERC20(_paymentToken);
        startTime = _startTime;
        endTime = _endTime;
        initialPrice = _initialPrice;
        finalPrice = _finalPrice;
        totalTokensForSale = _totalTokensForSale;
    }
    
    function currentPrice() public view returns (uint256) {
        if (block.timestamp < startTime) {
            return initialPrice;
        } else if (block.timestamp >= endTime) {
            return finalPrice;
        } else {
            uint256 timeElapsed = block.timestamp - startTime;
            uint256 duration = endTime - startTime;
            return initialPrice - ((initialPrice - finalPrice) * timeElapsed) / duration;
        }
    }
    
    function buyTokens(uint256 paymentAmount) external nonReentrant {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale not active");
        require(paymentAmount > 0, "Payment amount must be positive");
        
        uint256 price = currentPrice();
        uint256 tokenAmount = (paymentAmount * 1e18) / price;
        
        require(tokenAmount > 0, "Token amount must be positive");
        require(tokensSold + tokenAmount <= totalTokensForSale, "Not enough tokens remaining");
        
        paymentToken.transferFrom(msg.sender, address(this), paymentAmount);
        
        contributions[msg.sender] += paymentAmount;
        tokensSold += tokenAmount;
        
        emit TokensPurchased(msg.sender, tokenAmount, paymentAmount);
    }
    
    function claimTokens() external nonReentrant {
        require(block.timestamp > endTime, "Sale not ended yet");
        require(contributions[msg.sender] > 0, "No contributions");
        require(tokensClaimed[msg.sender] == 0, "Already claimed");
        
        uint256 price = currentPrice();
        uint256 tokenAmount = (contributions[msg.sender] * 1e18) / price;
        
        require(tokenAmount > 0, "No tokens to claim");
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance");
        
        tokensClaimed[msg.sender] = tokenAmount;
        token.transfer(msg.sender, tokenAmount);
        
        emit TokensClaimed(msg.sender, tokenAmount);
    }
    
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > endTime, "Sale not ended yet");
        
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        paymentToken.transfer(owner(), balance);
        
        emit FundsWithdrawn(owner(), balance);
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale not ended yet");
        
        uint256 unsoldTokens = totalTokensForSale - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens");
        
        token.transfer(owner(), unsoldTokens);
    }
    
    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp < startTime || block.timestamp > endTime, "Cannot emergency withdraw during sale");
        
        uint256 tokenBalance = token.balanceOf(address(this));
        if (tokenBalance > 0) {
            token.transfer(owner(), tokenBalance);
        }
        
        uint256 paymentBalance = paymentToken.balanceOf(address(this));
        if (paymentBalance > 0) {
            paymentToken.transfer(owner(), paymentBalance);
        }
    }
}
```
