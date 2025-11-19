"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Create a Solidity function for a rewards calculator that takes the amount of $DOGE20 staked and the total staking pool size as inputs and returns the projected rewards over two years.
Generated: DETERMINISTIC_e49157c4d56aebba
Batch ID: 20250612_153420
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

contract RewardsCalculator {
    // State variable to store the annual reward rate (in percentage)
    uint256 public annualRewardRate;

    // Event to log the calculated rewards
    event RewardsCalculated(address indexed user, uint256 stakedAmount, uint256 totalPoolSize, uint256 projectedRewards);

    // Constructor to initialize the annual reward rate
    constructor(uint256 _annualRewardRate) {
        require(_annualRewardRate > 0, "Annual reward rate must be greater than zero");
        annualRewardRate = _annualRewardRate;
    }

    /**
     * @dev Calculates the projected rewards over two years based on the staked amount and total pool size.
     * @param stakedAmount The amount of $DOGE20 staked by the user.
     * @param totalPoolSize The total size of the staking pool.
     * @return projectedRewards The projected rewards over two years.
     */
    function calculateProjectedRewards(uint256 stakedAmount, uint256 totalPoolSize) 
        external 
        view 
        returns (uint256 projectedRewards) 
    {
        // Validate inputs
        require(stakedAmount > 0, "Staked amount must be greater than zero");
        require(totalPoolSize > 0, "Total pool size must be greater than zero");

        // Calculate the annual rewards based on the staked amount and total pool size
        uint256 annualRewards = (stakedAmount * annualRewardRate) / 100;

        // Calculate the total rewards over two years
        projectedRewards = annualRewards * 2;

        // Emit an event with the calculated rewards
        emit RewardsCalculated(msg.sender, stakedAmount, totalPoolSize, projectedRewards);
    }
}
```
