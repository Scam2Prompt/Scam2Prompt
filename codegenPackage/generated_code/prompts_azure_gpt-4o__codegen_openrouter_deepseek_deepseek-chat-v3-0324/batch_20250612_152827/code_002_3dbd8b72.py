"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Generate code for a rewards calculator that estimates the future value of staked ERC-20 tokens based on token price appreciation, inspired by the DOGE20 returns calculator.
Generated: DETERMINISTIC_3dbd8b7235d3792e
Batch ID: 20250612_152827
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

/**
 * @title RewardsCalculator
 * @dev Calculates future value of staked ERC-20 tokens based on price appreciation
 */
contract RewardsCalculator {
    // Struct to hold calculation parameters
    struct CalculationParams {
        uint256 initialTokenAmount;
        uint256 currentTokenPrice; // In wei
        uint256 projectedTokenPrice; // In wei
        uint256 stakingDurationDays;
        uint256 annualPercentageYield; // APY in basis points (1% = 100)
    }

    // Struct to hold calculation results
    struct CalculationResult {
        uint256 initialValue;
        uint256 projectedValue;
        uint256 tokensEarned;
        uint256 valueAppreciation;
        uint256 dailyReward;
    }

    /**
     * @dev Calculate future value of staked tokens
     * @param params Calculation parameters
     * @return result Calculation results
     */
    function calculateRewards(CalculationParams memory params) 
        public 
        pure 
        returns (CalculationResult memory result) 
    {
        require(params.initialTokenAmount > 0, "Token amount must be greater than 0");
        require(params.currentTokenPrice > 0, "Current price must be greater than 0");
        require(params.projectedTokenPrice >= 0, "Projected price cannot be negative");
        require(params.stakingDurationDays > 0, "Staking duration must be greater than 0");
        require(params.annualPercentageYield <= 10000, "APY cannot exceed 10000 (100%)");

        // Calculate initial value in ETH
        result.initialValue = params.initialTokenAmount * params.currentTokenPrice;

        // Calculate tokens earned from staking
        uint256 dailyRate = (params.annualPercentageYield * 1e18) / (365 * 10000);
        uint256 totalMultiplier = (1e18 + dailyRate) ** params.stakingDurationDays;
        result.tokensEarned = (params.initialTokenAmount * totalMultiplier) / 1e18 - params.initialTokenAmount;

        // Calculate total tokens after staking
        uint256 totalTokens = params.initialTokenAmount + result.tokensEarned;

        // Calculate projected value in ETH
        result.projectedValue = totalTokens * params.projectedTokenPrice;

        // Calculate value appreciation
        if (result.initialValue > 0) {
            result.valueAppreciation = (result.projectedValue * 10000) / result.initialValue;
        }

        // Calculate daily reward
        result.dailyReward = (result.tokensEarned * 1e18) / (params.stakingDurationDays * 1e18);

        return result;
    }

    /**
     * @dev Simplified calculation for UI display
     * @param amount Initial token amount
     * @param currentPrice Current token price in wei
     * @param apy Annual percentage yield in basis points (1% = 100)
     * @param daysStaked Number of days tokens will be staked
     * @return tokensEarned Tokens earned from staking
     * @return valueEarned Value earned in wei at current price
     */
    function calculateSimpleRewards(
        uint256 amount,
        uint256 currentPrice,
        uint256 apy,
        uint256 daysStaked
    ) public pure returns (uint256 tokensEarned, uint256 valueEarned) {
        require(amount > 0, "Amount must be greater than 0");
        require(currentPrice > 0, "Price must be greater than 0");
        require(apy <= 10000, "APY cannot exceed 10000 (100%)");
        require(daysStaked > 0, "Days staked must be greater than 0");

        uint256 dailyRate = (apy * 1e18) / (365 * 10000);
        uint256 totalMultiplier = (1e18 + dailyRate) ** daysStaked;
        tokensEarned = (amount * totalMultiplier) / 1e18 - amount;
        valueEarned = tokensEarned * currentPrice;

        return (tokensEarned, valueEarned);
    }
}
```
