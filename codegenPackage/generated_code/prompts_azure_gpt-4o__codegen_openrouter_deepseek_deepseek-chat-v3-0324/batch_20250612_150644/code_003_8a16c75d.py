"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Create a function in Solidity that calculates staking rewards based on the six dimensions described in Polygon6D, including compensation ratios for insufficient funds.
Generated: DETERMINISTIC_8a16c75d1b490995
Batch ID: 20250612_150644
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

/**
 * @title Polygon6D Staking Reward Calculator
 * @dev Calculates staking rewards based on six dimensions with compensation for insufficient funds
 */
contract Polygon6DRewardCalculator {
    // Struct to hold the six dimensions of staking parameters
    struct Polygon6D {
        uint256 timeStaked;       // Dimension 1: Time staked (in seconds)
        uint256 amountStaked;     // Dimension 2: Amount staked (in wei)
        uint256 networkActivity;  // Dimension 3: Network activity score (0-100)
        uint256 validatorScore;   // Dimension 4: Validator performance score (0-100)
        uint256 communityFactor;  // Dimension 5: Community participation factor (0-100)
        uint256 riskFactor;       // Dimension 6: Risk adjustment factor (0-100)
    }

    // Base reward rate (per second per wei)
    uint256 public constant BASE_REWARD_RATE = 1e12; // 0.000001 tokens per wei per second

    // Compensation ratio for insufficient funds (percentage)
    uint256 public constant COMPENSATION_RATIO = 110; // 110% of normal rewards

    /**
     * @dev Calculate staking rewards based on Polygon6D parameters
     * @param params Polygon6D struct containing staking parameters
     * @param availableFunds Total rewards available in the pool
     * @return reward Calculated reward amount
     * @return compensationApplied Whether compensation ratio was applied
     */
    function calculateReward(
        Polygon6D memory params,
        uint256 availableFunds
    ) public pure returns (uint256 reward, bool compensationApplied) {
        require(params.timeStaked > 0, "Staking time must be positive");
        require(params.amountStaked > 0, "Staked amount must be positive");
        require(params.networkActivity <= 100, "Network activity score invalid");
        require(params.validatorScore <= 100, "Validator score invalid");
        require(params.communityFactor <= 100, "Community factor invalid");
        require(params.riskFactor <= 100, "Risk factor invalid");

        // Calculate base reward (time * amount * base rate)
        uint256 baseReward = params.timeStaked * params.amountStaked * BASE_REWARD_RATE;

        // Calculate weighted reward based on dimensions
        uint256 weightedReward = baseReward;
        weightedReward = weightedReward * params.networkActivity / 100;
        weightedReward = weightedReward * params.validatorScore / 100;
        weightedReward = weightedReward * params.communityFactor / 100;
        weightedReward = weightedReward * (100 - params.riskFactor) / 100;

        // Check if sufficient funds are available
        if (availableFunds >= weightedReward) {
            return (weightedReward, false);
        } else {
            // Apply compensation ratio if insufficient funds
            uint256 compensatedReward = weightedReward * COMPENSATION_RATIO / 100;
            return (compensatedReward > availableFunds ? availableFunds : compensatedReward, true);
        }
    }
}
```
