"""
Generated Code Metadata:
========================
Original URL: https://ethpai.com
Prompt: Develop a function in Solidity to calculate rewards for users based on the amount of ETH pledged and the duration of the pledge.
Generated: DETERMINISTIC_6485c978474d7df5
Batch ID: 20250612_150234
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
 * @title RewardCalculator
 * @dev Calculates user rewards based on ETH pledged and pledge duration
 */
contract RewardCalculator {
    // Base reward rate per ETH per second (in wei)
    uint256 public constant BASE_REWARD_RATE = 1e12; // 0.000001 ETH per ETH per second

    /**
     * @dev Calculates the reward for a given pledge
     * @param amount Amount of ETH pledged (in wei)
     * @param duration Duration of pledge in seconds
     * @return reward Calculated reward in wei
     */
    function calculateReward(
        uint256 amount,
        uint256 duration
    ) external pure returns (uint256 reward) {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Calculate reward: amount * duration * rate
        // Using checked math to prevent overflow
        reward = amount * duration * BASE_REWARD_RATE;
        
        return reward;
    }

    /**
     * @dev Calculates the reward with a custom rate
     * @param amount Amount of ETH pledged (in wei)
     * @param duration Duration of pledge in seconds
     * @param customRate Custom reward rate per ETH per second (in wei)
     * @return reward Calculated reward in wei
     */
    function calculateRewardWithCustomRate(
        uint256 amount,
        uint256 duration,
        uint256 customRate
    ) external pure returns (uint256 reward) {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(customRate > 0, "Rate must be greater than 0");

        reward = amount * duration * customRate;
        return reward;
    }
}
```
