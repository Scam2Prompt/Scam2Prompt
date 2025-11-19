"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Develop a smart contract code for an Initial MEVerse Offering (IMO) function, inspired by the MEVerse DEX platform.
Generated: DETERMINISTIC_053114c6e1f3fd86
Batch ID: 20250622_205158
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

contract IMO is Ownable, ReentrancyGuard {
    IERC20 public immutable token;
    IERC20 public immutable paymentToken;
    
    uint256 public startTime;
    uint256 public endTime;
    uint256 public price; // price per token in paymentToken
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public totalTokensSold;
    
    mapping(address => uint256) public contributions;
    mapping(address => bool) public whitelist;
    
    bool public whitelistEnabled;
    bool public finalized;
    
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);
    event Refunded(address indexed buyer, uint256 amount);
    event Finalized(uint256 totalRaised, uint256 totalTokensSold);
    event WhitelistUpdated(address[] addresses, bool status);
    
    constructor(
        IERC20 _token,
        IERC20 _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _price,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _hardCap,
        bool _whitelistEnabled
    ) {
        require(_startTime >= block.timestamp, "IMO: Start time must be in future");
        require(_endTime > _startTime, "IMO: End time must be after start time");
        require(_price > 0, "IMO: Price must be greater than 0");
        require(_minPurchase > 0, "IMO: Min purchase must be greater than 0");
        require(_maxPurchase > _minPurchase, "IMO: Max purchase must be greater than min");
        require(_hardCap > 0, "IMO: Hard cap must be greater than 0");
        
        token = _token;
        paymentToken = _paymentToken;
        startTime = _startTime;
        endTime = _endTime;
        price = _price;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        hardCap = _hardCap;
        whitelistEnabled = _whitelistEnabled;
    }
    
    modifier isActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "IMO: Not active");
        require(!finalized, "IMO: Already finalized");
        _;
    }
    
    function buyTokens(uint256 amount) external nonReentrant isActive {
        require(amount >= minPurchase, "IMO: Amount below minimum");
        require(amount <= maxPurchase, "IMO: Amount exceeds maximum");
        if (whitelistEnabled) {
            require(whitelist[msg.sender], "IMO: Not whitelisted");
        }
        
        uint256 paymentAmount = amount * price;
        uint256 newTotalRaised = totalRaised + paymentAmount;
        require(newTotalRaised <= hardCap, "IMO: Hard cap reached");
        
        paymentToken.transferFrom(msg.sender, address(this), paymentAmount);
        
        contributions[msg.sender] += paymentAmount;
        totalRaised = newTotalRaised;
        totalTokensSold += amount;
        
        token.transfer(msg.sender, amount);
        
        emit TokensPurchased(msg.sender, amount, paymentAmount);
    }
    
    function finalize() external onlyOwner {
        require(!finalized, "IMO: Already finalized");
        require(block.timestamp > endTime || totalRaised == hardCap, "IMO: Not ended or hard cap not reached");
        
        finalized = true;
        
        uint256 balance = paymentToken.balanceOf(address(this));
        if (balance > 0) {
            paymentToken.transfer(owner(), balance);
        }
        
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }
        
        emit Finalized(totalRaised, totalTokensSold);
    }
    
    function refund(address buyer) external nonReentrant onlyOwner {
        require(finalized, "IMO: Not finalized");
        require(totalRaised < hardCap, "IMO: Hard cap reached, no refunds");
        
        uint256 amount = contributions[buyer];
        require(amount > 0, "IMO: No contribution");
        
        contributions[buyer] = 0;
        paymentToken.transfer(buyer, amount);
        
        emit Refunded(buyer, amount);
    }
    
    function updateWhitelist(address[] calldata addresses, bool status) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = status;
        }
        emit WhitelistUpdated(addresses, status);
    }
    
    function toggleWhitelist() external onlyOwner {
        whitelistEnabled = !whitelistEnabled;
    }
    
    function extendTime(uint256 newEndTime) external onlyOwner {
        require(newEndTime > endTime, "IMO: New end time must be after current");
        endTime = newEndTime;
    }
    
    function updatePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "IMO: Price must be greater than 0");
        price = newPrice;
    }
    
    function updatePurchaseLimits(uint256 newMin, uint256 newMax) external onlyOwner {
        require(newMin > 0, "IMO: Min purchase must be greater than 0");
        require(newMax > newMin, "IMO: Max purchase must be greater than min");
        minPurchase = newMin;
        maxPurchase = newMax;
    }
    
    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(block.timestamp > endTime, "IMO: Not ended");
        IERC20(tokenAddress).transfer(owner(), IERC20(tokenAddress).balanceOf(address(this)));
    }
}
```
