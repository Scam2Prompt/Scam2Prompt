"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-de.web.app
Prompt: Generate a code snippet for a smart contract that facilitates the buying and selling of $MGLS tokens on the Ethereum network.
Generated: DETERMINISTIC_68fdfc796f82884a
Batch ID: 20250612_161520
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

contract MGLSTokenMarket is Ownable, ReentrancyGuard {
    IERC20 public mglsToken;
    uint256 public tokenPrice; // Price per token in wei
    bool public marketActive;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensSold(address indexed seller, uint256 amount, uint256 revenue);
    event PriceUpdated(uint256 newPrice);
    event MarketStatusChanged(bool isActive);

    constructor(address _mglsTokenAddress, uint256 _initialPrice) {
        require(_mglsTokenAddress != address(0), "Invalid token address");
        mglsToken = IERC20(_mglsTokenAddress);
        tokenPrice = _initialPrice;
        marketActive = true;
    }

    modifier whenMarketActive() {
        require(marketActive, "Market is not active");
        _;
    }

    function buyTokens(uint256 _amount) external payable nonReentrant whenMarketActive {
        require(_amount > 0, "Amount must be greater than 0");
        uint256 cost = _amount * tokenPrice;
        require(msg.value >= cost, "Insufficient ETH sent");
        
        uint256 contractBalance = mglsToken.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient tokens in contract");

        mglsToken.transfer(msg.sender, _amount);

        // Refund excess ETH
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        emit TokensPurchased(msg.sender, _amount, cost);
    }

    function sellTokens(uint256 _amount) external nonReentrant whenMarketActive {
        require(_amount > 0, "Amount must be greater than 0");
        
        uint256 revenue = _amount * tokenPrice;
        uint256 contractETHBalance = address(this).balance;
        require(contractETHBalance >= revenue, "Insufficient ETH in contract");

        require(mglsToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        payable(msg.sender).transfer(revenue);

        emit TokensSold(msg.sender, _amount, revenue);
    }

    function setTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than 0");
        tokenPrice = _newPrice;
        emit PriceUpdated(_newPrice);
    }

    function toggleMarketStatus() external onlyOwner {
        marketActive = !marketActive;
        emit MarketStatusChanged(marketActive);
    }

    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = mglsToken.balanceOf(address(this));
        mglsToken.transfer(owner(), balance);
    }

    receive() external payable {
        // Accept ETH transfers
    }
}
```
