"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Write a smart contract in Solidity for a cross-game, cross-chain decentralized player network's token sale, with a first-come-first-served allocation mechanism.
Generated: DETERMINISTIC_23f67c1a11b205cb
Batch ID: 20250622_210443
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

contract CrossGameTokenSale is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public hardCap;
    uint256 public totalSold;
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    bool public saleActive;
    uint256 public minPurchase;
    uint256 public maxPurchase;

    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);
    event SaleStarted(uint256 startTime, uint256 endTime);
    event SaleEnded(uint256 endTime);
    event TokensWithdrawn(uint256 amount);

    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _hardCap,
        uint256 _minPurchase,
        uint256 _maxPurchase
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_hardCap > 0, "Hard cap must be greater than zero");
        require(_minPurchase > 0, "Min purchase must be greater than zero");
        require(_maxPurchase > _minPurchase, "Max purchase must be greater than min purchase");

        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        hardCap = _hardCap;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
    }

    modifier whenSaleActive() {
        require(saleActive, "Sale is not active");
        require(block.timestamp >= saleStartTime, "Sale has not started");
        require(block.timestamp <= saleEndTime, "Sale has ended");
        _;
    }

    function startSale(uint256 duration) external onlyOwner {
        require(!saleActive, "Sale is already active");
        require(duration > 0, "Duration must be greater than zero");

        saleStartTime = block.timestamp;
        saleEndTime = saleStartTime + duration;
        saleActive = true;

        emit SaleStarted(saleStartTime, saleEndTime);
    }

    function endSale() external onlyOwner {
        require(saleActive, "Sale is not active");
        saleActive = false;
        saleEndTime = block.timestamp;

        emit SaleEnded(saleEndTime);
    }

    function buyTokens() external payable nonReentrant whenSaleActive {
        require(msg.value >= minPurchase, "Amount sent is below minimum purchase");
        require(msg.value <= maxPurchase, "Amount sent exceeds maximum purchase");
        require(totalSold + (msg.value / tokenPrice) <= hardCap, "Purchase would exceed hard cap");

        uint256 tokenAmount = msg.value / tokenPrice;
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance");

        contributions[msg.sender] += msg.value;
        totalSold += tokenAmount;

        token.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    function withdrawTokens() external onlyOwner {
        require(!saleActive, "Sale is still active");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        token.transfer(owner(), balance);

        emit TokensWithdrawn(balance);
    }

    function withdrawFunds() external onlyOwner {
        require(!saleActive, "Sale is still active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero");
        tokenPrice = newPrice;
    }

    function setPurchaseLimits(uint256 newMin, uint256 newMax) external onlyOwner {
        require(newMin > 0, "Min purchase must be greater than zero");
        require(newMax > newMin, "Max purchase must be greater than min purchase");
        minPurchase = newMin;
        maxPurchase = newMax;
    }

    function emergencyWithdraw() external onlyOwner {
        saleActive = false;
        uint256 balance = token.balanceOf(address(this));
        if (balance > 0) {
            token.transfer(owner(), balance);
        }
        uint256 ethBalance = address(this).balance;
        if (ethBalance > 0) {
            payable(owner()).transfer(ethBalance);
        }
    }
}
```
