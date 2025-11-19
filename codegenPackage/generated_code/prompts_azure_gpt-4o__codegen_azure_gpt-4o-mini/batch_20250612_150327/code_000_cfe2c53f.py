"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Write a smart contract in Solidity that mimics the functionality of the BOI Coin presale, including token purchase using USDT, ETH, and BNB, and tracking raised funds.
Generated: DETERMINISTIC_cfe2c53f0cfc0699
Batch ID: 20250612_150327
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for BOI Coin
contract BOICoinPresale is Ownable {
    // State variables
    IERC20 public boiToken; // The BOI token to be sold
    IERC20 public usdtToken; // USDT token for purchases
    uint256 public rate; // Rate of BOI tokens per unit of currency
    uint256 public totalRaised; // Total funds raised in the presale
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _boiToken, IERC20 _usdtToken, uint256 _rate) {
        boiToken = _boiToken;
        usdtToken = _usdtToken;
        rate = _rate;
    }

    // Function to purchase tokens using USDT
    function buyWithUSDT(uint256 usdtAmount) external {
        require(usdtAmount > 0, "Amount must be greater than 0");
        require(usdtToken.transferFrom(msg.sender, address(this), usdtAmount), "USDT transfer failed");

        uint256 tokenAmount = usdtAmount * rate;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");

        contributions[msg.sender] += usdtAmount;
        totalRaised += usdtAmount;

        emit TokensPurchased(msg.sender, tokenAmount, "USDT");
    }

    // Function to purchase tokens using ETH
    function buyWithETH() external payable {
        require(msg.value > 0, "Amount must be greater than 0");

        uint256 tokenAmount = msg.value * rate;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit TokensPurchased(msg.sender, tokenAmount, "ETH");
    }

    // Function to purchase tokens using BNB
    function buyWithBNB() external payable {
        require(msg.value > 0, "Amount must be greater than 0");

        uint256 tokenAmount = msg.value * rate;
        require(boiToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit TokensPurchased(msg.sender, tokenAmount, "BNB");
    }

    // Function to withdraw funds raised in the presale
    function withdrawFunds() external onlyOwner {
        uint256 amount = address(this).balance;
        require(amount > 0, "No funds to withdraw");
        payable(owner()).transfer(amount);
        emit FundsWithdrawn(owner(), amount);
    }

    // Function to withdraw USDT tokens
    function withdrawUSDT(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(usdtToken.balanceOf(address(this)) >= amount, "Not enough USDT available");
        require(usdtToken.transfer(owner(), amount), "USDT transfer failed");
        emit FundsWithdrawn(owner(), amount);
    }

    // Function to set a new rate
    function setRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rate = newRate;
    }

    // Function to retrieve the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to retrieve the total raised amount
    function getTotalRaised() external view returns (uint256) {
        return totalRaised;
    }
}
```
