"""
Generated Code Metadata:
========================
Original URL: https://plnksale.vercel.app
Prompt: Create a smart contract for a token presale with features like whale allocation sharing, max buy limits, and contributor verification, similar to the Baby Maga presale.
Generated: DETERMINISTIC_c8eba12952b86685
Batch ID: 20250612_152235
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

contract TokenPresale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public maxBuyPerUser; // Max tokens a user can buy
    uint256 public minBuyPerUser; // Min tokens a user can buy
    uint256 public totalTokensForSale;
    uint256 public totalTokensSold;
    uint256 public whaleAllocationThreshold; // Amount above which allocation is shared
    uint256 public whaleAllocationSharePercentage; // Percentage of excess allocation to be shared

    // Contributor tracking
    mapping(address => uint256) public contributions;
    mapping(address => bool) public whitelist;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleExtended(uint256 newEndTime);
    event PresaleParametersUpdated();
    event WhitelistUpdated(address[] addresses, bool status);

    constructor(
        IERC20 _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _maxBuyPerUser,
        uint256 _minBuyPerUser,
        uint256 _totalTokensForSale,
        uint256 _whaleAllocationThreshold,
        uint256 _whaleAllocationSharePercentage
    ) {
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleEndTime > _presaleStartTime, "End time must be after start time");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_maxBuyPerUser > _minBuyPerUser, "Max buy must be greater than min buy");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than 0");
        require(_whaleAllocationThreshold > _maxBuyPerUser, "Whale threshold must be greater than max buy");
        require(_whaleAllocationSharePercentage <= 100, "Share percentage must be <= 100");

        token = _token;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        maxBuyPerUser = _maxBuyPerUser;
        minBuyPerUser = _minBuyPerUser;
        totalTokensForSale = _totalTokensForSale;
        whaleAllocationThreshold = _whaleAllocationThreshold;
        whaleAllocationSharePercentage = _whaleAllocationSharePercentage;
    }

    modifier onlyPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    function buyTokens() external payable nonReentrant onlyPresaleActive {
        require(whitelist[msg.sender], "Address not whitelisted");
        
        uint256 tokenAmount = msg.value.mul(1e18).div(tokenPrice);
        uint256 newContribution = contributions[msg.sender].add(tokenAmount);

        require(tokenAmount >= minBuyPerUser, "Purchase amount too low");
        require(newContribution <= maxBuyPerUser, "Purchase exceeds max allocation");
        require(totalTokensSold.add(tokenAmount) <= totalTokensForSale, "Not enough tokens remaining");

        // Handle whale allocation sharing
        if (newContribution > whaleAllocationThreshold) {
            uint256 excessAmount = newContribution.sub(whaleAllocationThreshold);
            uint256 sharedAmount = excessAmount.mul(whaleAllocationSharePercentage).div(100);
            tokenAmount = whaleAllocationThreshold.add(sharedAmount);
            
            // Adjust total tokens sold
            totalTokensSold = totalTokensSold.add(tokenAmount).sub(contributions[msg.sender]);
        } else {
            totalTokensSold = totalTokensSold.add(tokenAmount);
        }

        contributions[msg.sender] = contributions[msg.sender].add(tokenAmount);
        
        // Transfer tokens to buyer
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");
        
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    function extendPresale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > presaleEndTime, "New end time must be after current end time");
        presaleEndTime = newEndTime;
        emit PresaleExtended(newEndTime);
    }

    function updatePresaleParameters(
        uint256 _tokenPrice,
        uint256 _maxBuyPerUser,
        uint256 _minBuyPerUser,
        uint256 _whaleAllocationThreshold,
        uint256 _whaleAllocationSharePercentage
    ) external onlyOwner {
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_maxBuyPerUser > _minBuyPerUser, "Max buy must be greater than min buy");
        require(_whaleAllocationThreshold > _maxBuyPerUser, "Whale threshold must be greater than max buy");
        require(_whaleAllocationSharePercentage <= 100, "Share percentage must be <= 100");

        tokenPrice = _tokenPrice;
        maxBuyPerUser = _maxBuyPerUser;
        minBuyPerUser = _minBuyPerUser;
        whaleAllocationThreshold = _whaleAllocationThreshold;
        whaleAllocationSharePercentage = _whaleAllocationSharePercentage;

        emit PresaleParametersUpdated();
    }

    function updateWhitelist(address[] calldata addresses, bool status) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = status;
        }
        emit WhitelistUpdated(addresses, status);
    }

    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale must be ended");
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale must be ended");
        uint256 remainingTokens = totalTokensForSale.sub(totalTokensSold);
        if (remainingTokens > 0) {
            require(token.transfer(owner(), remainingTokens), "Token transfer failed");
        }
    }

    function getContribution(address user) external view returns (uint256) {
        return contributions[user];
    }

    function getPresaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }

    function getTokensRemaining() external view returns (uint256) {
        return totalTokensForSale.sub(totalTokensSold);
    }
}
```
