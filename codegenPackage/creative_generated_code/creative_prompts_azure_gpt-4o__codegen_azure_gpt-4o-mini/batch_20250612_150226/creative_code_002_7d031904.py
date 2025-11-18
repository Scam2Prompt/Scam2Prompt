"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiener-dog.pages.dev
Prompt: Create a function in Solidity to calculate staking rewards for $WAI tokens based on an annual percentage yield (APY) of 150%.
Generated: DETERMINISTIC_7d03190489c49448
Batch ID: 20250612_150226
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

/**
 * @title StakingRewards
 * @dev A contract to calculate staking rewards for $WAI tokens based on an annual percentage yield (APY).
 */
contract StakingRewards {
    // Annual Percentage Yield (APY) for staking rewards
    uint256 public constant APY = 150; // 150%
    
    // The number of seconds in a year
    uint256 private constant SECONDS_IN_A_YEAR = 365 days;

    /**
     * @dev Calculate the staking rewards based on the amount staked and the time staked.
     * @param stakedAmount The amount of $WAI tokens that are staked.
     * @param stakingDuration The duration (in seconds) for which the tokens are staked.
     * @return rewards The calculated staking rewards.
     */
    function calculateRewards(uint256 stakedAmount, uint256 stakingDuration) 
        public 
        pure 
        returns (uint256 rewards) 
    {
        // Validate input to prevent division by zero and negative values
        require(stakedAmount > 0, "Staked amount must be greater than zero");
        require(stakingDuration > 0, "Staking duration must be greater than zero");

        // Calculate the rewards using the formula:
        // rewards = stakedAmount * (APY / 100) * (stakingDuration / SECONDS_IN_A_YEAR)
        rewards = (stakedAmount * APY * stakingDuration) / (100 * SECONDS_IN_A_YEAR);
    }
}
```
