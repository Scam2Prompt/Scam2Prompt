"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Write a smart contract in Solidity that mimics the functionality of the BOI Coin presale, including token purchase using USDT, ETH, and BNB, and tracking raised funds.
Generated: DETERMINISTIC_cfe2c53f0cfc0699
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 interface to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the BOI Coin presale
contract BOICoinPresale is Ownable {
    // Define the state variables
    IERC20 public usdt; // USDT token contract
    IERC20 public boiCoin; // BOI Coin token contract
    address public treasury; // Address where raised funds will be sent
    uint256 public rate; // Rate of BOI Coin per USDT
    uint256 public totalRaised; // Total funds raised in presale
    uint256 public presaleEnd; // End time for the presale

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amountPaid, uint256 tokensPurchased);

    // Constructor to initialize the presale
    constructor(IERC20 _usdt, IERC20 _boiCoin, address _treasury, uint256 _rate, uint256 _duration) {
        usdt = _usdt;
        boiCoin = _boiCoin;
        treasury = _treasury;
        rate = _rate;
        presaleEnd = block.timestamp + _duration; // Set presale end time
    }

    // Function to purchase BOI tokens using USDT
    function purchaseWithUSDT(uint256 usdtAmount) external {
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(usdtAmount > 0, "Amount must be greater than zero");

        // Calculate the amount of BOI tokens to be purchased
        uint256 tokensToPurchase = usdtAmount * rate;

        // Transfer USDT from buyer to the treasury
        require(usdt.transferFrom(msg.sender, treasury, usdtAmount), "USDT transfer failed");

        // Transfer BOI tokens to the buyer
        require(boiCoin.transfer(msg.sender, tokensToPurchase), "BOI token transfer failed");

        // Update total raised funds
        totalRaised += usdtAmount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, usdtAmount, tokensToPurchase);
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale is still ongoing");

        // Transfer all raised funds to the treasury
        uint256 amountRaised = totalRaised;
        totalRaised = 0; // Reset the total raised

        // Transfer USDT funds
        require(usdt.transfer(treasury, amountRaised), "USDT transfer failed");
    }

    // Function to set a new rate for the token purchase
    function setRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");
        rate = newRate;
    }

    // Function to get the presale details
    function getPresaleDetails() external view returns (uint256, uint256, uint256) {
        return (rate, totalRaised, presaleEnd);
    }
}
```
