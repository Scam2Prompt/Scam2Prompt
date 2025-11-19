"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepelive.com
Prompt: Write a Solidity smart contract to facilitate the purchase of WEPE tokens during the presale, including a function to enforce floor pricing.
Generated: DETERMINISTIC_1187cc1e5050dd8f
Batch ID: 20250612_153812
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

contract WEPEPresale is Ownable, ReentrancyGuard {
    IERC20 public wepeToken;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;
    uint256 public pricePerToken; // Price in wei
    uint256 public minPurchase; // Minimum purchase amount in wei
    uint256 public maxPurchase; // Maximum purchase amount in wei
    bool public presaleFinalized;

    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tokens);
    event PresaleFinalized(uint256 tokensRemaining);

    constructor(
        address _wepeToken,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _totalTokensForSale,
        uint256 _pricePerToken,
        uint256 _minPurchase,
        uint256 _maxPurchase
    ) {
        require(_wepeToken != address(0), "Invalid token address");
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleEndTime > _presaleStartTime, "End time must be after start time");
        require(_totalTokensForSale > 0, "Total tokens must be > 0");
        require(_pricePerToken > 0, "Price must be > 0");
        require(_minPurchase > 0, "Min purchase must be > 0");
        require(_maxPurchase > _minPurchase, "Max purchase must be > min");

        wepeToken = IERC20(_wepeToken);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        totalTokensForSale = _totalTokensForSale;
        pricePerToken = _pricePerToken;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
    }

    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(!presaleFinalized, "Presale is finalized");
        require(msg.value >= minPurchase, "Amount below minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        require(contributions[msg.sender] + msg.value <= maxPurchase, "Exceeds personal cap");

        uint256 tokensToBuy = msg.value / pricePerToken;
        require(tokensSold + tokensToBuy <= totalTokensForSale, "Not enough tokens remaining");

        contributions[msg.sender] += msg.value;
        tokensSold += tokensToBuy;

        wepeToken.transfer(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, msg.value, tokensToBuy);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || tokensSold == totalTokensForSale, "Presale not ended");
        require(!presaleFinalized, "Already finalized");

        presaleFinalized = true;
        uint256 remainingTokens = totalTokensForSale - tokensSold;

        if (remainingTokens > 0) {
            wepeToken.transfer(owner(), remainingTokens);
        }

        emit PresaleFinalized(remainingTokens);
    }

    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        payable(owner()).transfer(address(this).balance);
    }

    function setPricePerToken(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be > 0");
        require(block.timestamp < presaleStartTime, "Presale already started");
        pricePerToken = _newPrice;
    }

    function extendPresale(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > presaleEndTime, "New end time must be after current");
        require(block.timestamp < presaleEndTime, "Presale already ended");
        presaleEndTime = _newEndTime;
    }

    function emergencyWithdrawTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not ended");
        uint256 balance = wepeToken.balanceOf(address(this));
        wepeToken.transfer(owner(), balance);
    }
}
```
