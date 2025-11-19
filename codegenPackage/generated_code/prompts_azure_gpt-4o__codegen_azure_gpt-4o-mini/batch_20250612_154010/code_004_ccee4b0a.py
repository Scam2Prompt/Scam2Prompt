"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Write a Solidity contract that implements the $PEPPER tokenomics, including liquidity management, token allocation across wallets, and gradual liquidation.
Generated: DETERMINISTIC_ccee4b0a1e09a7ea
Batch ID: 20250612_154010
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PepperToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // Total supply of 1 million tokens
    uint256 public liquidityAllocation; // Amount allocated for liquidity
    uint256 public teamAllocation; // Amount allocated for the team
    uint256 public marketingAllocation; // Amount allocated for marketing
    uint256 public gradualLiquidationAmount; // Amount to be liquidated gradually
    uint256 public lastLiquidationTime; // Last time liquidation occurred
    uint256 public liquidationInterval; // Time interval for liquidation

    // Events
    event LiquidityAdded(uint256 amount);
    event TokensLiquidated(uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("PepperToken", "PEPPER") {
        _mint(msg.sender, TOTAL_SUPPLY);
        liquidityAllocation = TOTAL_SUPPLY.mul(20).div(100); // 20% for liquidity
        teamAllocation = TOTAL_SUPPLY.mul(10).div(100); // 10% for team
        marketingAllocation = TOTAL_SUPPLY.mul(5).div(100); // 5% for marketing
        gradualLiquidationAmount = TOTAL_SUPPLY.mul(5).div(100); // 5% for gradual liquidation
        lastLiquidationTime = block.timestamp;
        liquidationInterval = 30 days; // Liquidate every 30 days
    }

    // Function to add liquidity
    function addLiquidity(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(msg.sender), "Insufficient balance to add liquidity");
        _transfer(msg.sender, address(this), amount);
        liquidityAllocation = liquidityAllocation.add(amount);
        emit LiquidityAdded(amount);
    }

    // Function to liquidate tokens gradually
    function liquidateTokens() external onlyOwner {
        require(block.timestamp >= lastLiquidationTime + liquidationInterval, "Liquidation not yet due");
        require(gradualLiquidationAmount <= balanceOf(address(this)), "Insufficient tokens for liquidation");

        // Transfer the gradual liquidation amount to the owner
        _transfer(address(this), msg.sender, gradualLiquidationAmount);
        lastLiquidationTime = block.timestamp;
        emit TokensLiquidated(gradualLiquidationAmount);
    }

    // Function to withdraw tokens from the contract (for emergencies)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to get the current allocations
    function getAllocations() external view returns (uint256, uint256, uint256) {
        return (liquidityAllocation, teamAllocation, marketingAllocation);
    }
}
```
