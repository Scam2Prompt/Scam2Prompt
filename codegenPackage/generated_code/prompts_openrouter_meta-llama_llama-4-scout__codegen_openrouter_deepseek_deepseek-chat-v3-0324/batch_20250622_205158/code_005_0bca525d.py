"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Design a simple smart contract for a token presale using Solidity that includes functionality similar to the BOI token sale.
Generated: DETERMINISTIC_0bca525deca85d7c
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

contract TokenPresale is Ownable, ReentrancyGuard {
    IERC20 public token;
    address public tokenWallet;
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalRaised;
    
    mapping(address => uint256) public contributions;
    
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event PresaleExtended(uint256 newEndTime);
    event PresaleFinalized(uint256 totalRaised);
    
    constructor(
        address _token,
        address _tokenWallet,
        uint256 _presaleStartTime,
        uint256 _presaleDuration,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenWallet != address(0), "Token wallet cannot be zero");
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleDuration > 0, "Duration must be positive");
        require(_presaleRate > 0, "Rate must be positive");
        require(_minContribution > 0, "Min contribution must be positive");
        require(_maxContribution > _minContribution, "Max must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");
        
        token = IERC20(_token);
        tokenWallet = _tokenWallet;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime + _presaleDuration;
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
    }
    
    receive() external payable {
        buyTokens();
    }
    
    function buyTokens() public payable nonReentrant {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(msg.value <= maxContribution, "Contribution exceeds maximum");
        require(totalRaised + msg.value <= hardCap, "Hard cap reached");
        
        uint256 tokenAmount = msg.value * presaleRate;
        require(token.balanceOf(tokenWallet) >= tokenAmount, "Insufficient tokens in wallet");
        
        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;
        
        require(token.transferFrom(tokenWallet, msg.sender, tokenAmount), "Token transfer failed");
        
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }
    
    function extendPresale(uint256 additionalDuration) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale has already ended");
        presaleEndTime += additionalDuration;
        emit PresaleExtended(presaleEndTime);
    }
    
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        payable(owner()).transfer(address(this).balance);
    }
    
    function remainingTokens() external view returns (uint256) {
        return token.balanceOf(tokenWallet);
    }
    
    function presaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime && totalRaised < hardCap;
    }
    
    function emergencyWithdrawTokens(address _token) external onlyOwner {
        require(_token != address(token), "Cannot withdraw sale token");
        IERC20 emergencyToken = IERC20(_token);
        emergencyToken.transfer(owner(), emergencyToken.balanceOf(address(this)));
    }
}
```
