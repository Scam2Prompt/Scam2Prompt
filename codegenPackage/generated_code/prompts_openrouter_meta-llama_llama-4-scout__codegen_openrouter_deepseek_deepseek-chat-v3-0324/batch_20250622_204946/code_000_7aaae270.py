"""
Generated Code Metadata:
========================
Original URL: https://slothanacoin.pages.dev
Prompt: Write a Solidity smart contract for a cryptocurrency presale similar to Slothana's $SLOTH presale.
Generated: DETERMINISTIC_7aaae270e98e40b9
Batch ID: 20250622_204946
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

contract Presale is Ownable, ReentrancyGuard {
    IERC20 public token;
    IERC20 public paymentToken;
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per payment token unit
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalContributed;
    uint256 public totalTokensSold;
    
    bool public presaleFinalized;
    bool public tokensClaimable;
    
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensPurchased;
    
    event Contributed(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed buyer, uint256 amount);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensSold);
    
    constructor(
        address _token,
        address _paymentToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_paymentToken != address(0), "Payment token address cannot be zero");
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleEndTime > _presaleStartTime, "End time must be after start time");
        require(_presaleRate > 0, "Presale rate must be positive");
        require(_minContribution > 0, "Min contribution must be positive");
        require(_maxContribution > _minContribution, "Max contribution must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");
        
        token = IERC20(_token);
        paymentToken = IERC20(_paymentToken);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
    }
    
    function contribute(uint256 amount) external nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        require(!presaleFinalized, "Presale already finalized");
        require(amount >= minContribution, "Amount below minimum");
        require(amount <= maxContribution, "Amount exceeds maximum");
        require(totalContributed + amount <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = amount * presaleRate;
        require(token.balanceOf(address(this)) >= totalTokensSold + tokenAmount, "Not enough tokens left");
        
        paymentToken.transferFrom(msg.sender, address(this), amount);
        
        contributions[msg.sender] += amount;
        tokensPurchased[msg.sender] += tokenAmount;
        totalContributed += amount;
        totalTokensSold += tokenAmount;
        
        emit Contributed(msg.sender, amount);
    }
    
    function claimTokens() external nonReentrant {
        require(tokensClaimable, "Tokens not yet claimable");
        require(tokensPurchased[msg.sender] > 0, "No tokens to claim");
        
        uint256 amount = tokensPurchased[msg.sender];
        tokensPurchased[msg.sender] = 0;
        
        token.transfer(msg.sender, amount);
        emit TokensClaimed(msg.sender, amount);
    }
    
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalContributed == hardCap, "Presale not ended");
        require(!presaleFinalized, "Already finalized");
        
        presaleFinalized = true;
        tokensClaimable = true;
        
        emit PresaleFinalized(totalContributed, totalTokensSold);
    }
    
    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        uint256 balance = paymentToken.balanceOf(address(this));
        paymentToken.transfer(owner(), balance);
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        uint256 unsold = token.balanceOf(address(this)) - totalTokensSold;
        token.transfer(owner(), unsold);
    }
    
    function emergencyWithdraw() external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        presaleFinalized = true;
        uint256 balance = paymentToken.balanceOf(address(this));
        paymentToken.transfer(owner(), balance);
    }
    
    function extendPresale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > presaleEndTime, "New end time must be after current");
        presaleEndTime = newEndTime;
    }
    
    function setTokensClaimable(bool _claimable) external onlyOwner {
        tokensClaimable = _claimable;
    }
    
    function getTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
    
    function getPaymentTokenBalance() external view returns (uint256) {
        return paymentToken.balanceOf(address(this));
    }
}
```
