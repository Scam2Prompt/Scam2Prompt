"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Create a function in Solidity that calculates staking rewards for DOGE20 tokens based on a fixed supply and a two-year distribution period.
Generated: DETERMINISTIC_5981dda2bfc25cb9
Batch ID: 20250612_153400
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
 * @title DOGE20 Staking Rewards Calculator
 * @dev Calculates staking rewards based on fixed supply and two-year distribution period
 */
contract DOGE20StakingRewards {
    uint256 public constant TOTAL_REWARDS = 1000000000 * 10**18; // 1 billion DOGE20 tokens
    uint256 public constant DISTRIBUTION_PERIOD = 730 days; // 2 years in days
    uint256 public immutable startTime;
    
    /**
     * @dev Sets the staking start time to contract deployment time
     */
    constructor() {
        startTime = block.timestamp;
    }
    
    /**
     * @notice Calculates the available rewards at current block timestamp
     * @return availableRewards The amount of rewards available at current time
     */
    function getCurrentRewards() public view returns (uint256) {
        uint256 elapsedTime = block.timestamp - startTime;
        
        if (elapsedTime >= DISTRIBUTION_PERIOD) {
            return TOTAL_REWARDS;
        }
        
        return (TOTAL_REWARDS * elapsedTime) / DISTRIBUTION_PERIOD;
    }
    
    /**
     * @notice Calculates staking rewards for a given stake amount and duration
     * @param amount The amount of tokens staked
     * @param stakingDuration The duration of staking in seconds
     * @return rewards The calculated rewards for the stake
     */
    function calculateRewards(
        uint256 amount,
        uint256 stakingDuration
    ) external view returns (uint256 rewards) {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingDuration > 0, "Duration must be greater than 0");
        
        uint256 currentRewards = getCurrentRewards();
        uint256 timeFactor = (stakingDuration * 1e18) / DISTRIBUTION_PERIOD;
        
        rewards = (currentRewards * amount * timeFactor) / (TOTAL_REWARDS * 1e18);
    }
    
    /**
     * @notice Gets the remaining rewards yet to be distributed
     * @return remainingRewards The amount of rewards remaining
     */
    function getRemainingRewards() external view returns (uint256) {
        uint256 distributed = getCurrentRewards();
        return TOTAL_REWARDS - distributed;
    }
}
```
