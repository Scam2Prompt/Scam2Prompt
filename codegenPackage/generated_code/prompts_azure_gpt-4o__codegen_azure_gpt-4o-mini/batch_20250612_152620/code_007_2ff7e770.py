"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a function in Solidity that calculates monthly and daily reward rates for $POODL staking, as described on the Poodl Inu platform.
Generated: DETERMINISTIC_2ff7e770781a684e
Batch ID: 20250612_152620
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

contract PoodlStaking {
    // State variables to hold the total staked amount and reward rate
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate in basis points (1 basis point = 0.01%)

    // Event to log reward calculations
    event RewardCalculated(uint256 monthlyReward, uint256 dailyReward);

    // Constructor to initialize the contract with a reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        totalStaked += amount;
        // Logic to transfer tokens from the user to the contract would go here
    }

    // Function to calculate monthly and daily reward rates
    function calculateRewards() external view returns (uint256 monthlyReward, uint256 dailyReward) {
        // Ensure total staked amount is greater than zero to avoid division by zero
        require(totalStaked > 0, "No tokens staked");

        // Calculate monthly reward based on the total staked amount and reward rate
        monthlyReward = (totalStaked * rewardRate * 30) / 10000; // 30 days in a month
        dailyReward = monthlyReward / 30; // Daily reward is monthly reward divided by 30

        // Emit an event with the calculated rewards
        emit RewardCalculated(monthlyReward, dailyReward);
    }

    // Function to withdraw staked tokens (not implemented in this example)
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= totalStaked, "Insufficient staked amount");
        totalStaked -= amount;
        // Logic to transfer tokens back to the user would go here
    }
}
```
