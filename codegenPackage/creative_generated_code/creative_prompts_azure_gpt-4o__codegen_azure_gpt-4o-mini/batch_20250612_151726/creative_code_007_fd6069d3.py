"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Write a Solidity function that automatically transfers 20% of presale funds to a liquidity wallet daily, as implemented in MoonBag's smart contract.
Generated: DETERMINISTIC_fd6069d3f9ebbb3b
Batch ID: 20250612_151726
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PresaleLiquidity is Ownable {
    using SafeMath for uint256;

    // Address of the liquidity wallet
    address payable public liquidityWallet;

    // Total funds raised during the presale
    uint256 public totalFunds;

    // Amount to be transferred daily
    uint256 public dailyTransferAmount;

    // Last transfer timestamp
    uint256 public lastTransferTime;

    // Event to log fund transfers
    event FundsTransferred(address indexed to, uint256 amount);

    // Constructor to initialize liquidity wallet and daily transfer amount
    constructor(address payable _liquidityWallet) {
        liquidityWallet = _liquidityWallet;
        dailyTransferAmount = totalFunds.mul(20).div(100);
        lastTransferTime = block.timestamp;
    }

    // Function to receive funds from the presale
    receive() external payable {
        totalFunds = totalFunds.add(msg.value);
    }

    // Function to transfer 20% of presale funds to liquidity wallet daily
    function transferToLiquidity() external onlyOwner {
        // Check if 24 hours have passed since the last transfer
        require(block.timestamp >= lastTransferTime + 1 days, "Transfer can only be done once every 24 hours");
        
        // Calculate the amount to transfer
        uint256 amountToTransfer = totalFunds.mul(20).div(100);
        
        // Ensure the contract has enough funds
        require(amountToTransfer <= address(this).balance, "Insufficient balance in contract");

        // Transfer funds to the liquidity wallet
        liquidityWallet.transfer(amountToTransfer);
        
        // Update the last transfer time
        lastTransferTime = block.timestamp;

        // Emit the transfer event
        emit FundsTransferred(liquidityWallet, amountToTransfer);
    }
}
```
