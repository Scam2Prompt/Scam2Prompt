"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Write a Solidity function for calculating staking rewards based on APY and lock duration, similar to the $SCOTTY staking mechanism.
Generated: DETERMINISTIC_c898d1b8dece6b66
Batch ID: 20250612_152109
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
 * @dev Contract to calculate staking rewards based on APY and lock duration.
 */
contract StakingRewards {
    // State variables
    uint256 private constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60; // Total seconds in a year

    /**
     * @notice Calculates staking rewards based on APY and lock duration.
     * @param principal Amount of tokens staked by the user.
     * @param apy Annual Percentage Yield (APY) in basis points (1% = 100 basis points).
     * @param lockDuration Duration of staking in seconds.
     * @return rewards The calculated staking reward.
     */
    function calculateRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockDuration
    ) external pure returns (uint256 rewards) {
        // Input validation
        require(principal > 0, "Principal amount must be greater than zero.");
        require(apy > 0, "APY must be greater than zero.");
        require(lockDuration > 0, "Lock duration must be greater than zero.");

        // Formula: Rewards = Principal * (APY / 10000) * (LockDuration / SecondsInYear)
        uint256 annualYield = (principal * apy) / 10000; // APY is provided in basis points
        rewards = (annualYield * lockDuration) / SECONDS_IN_YEAR;

        return rewards;
    }
}
```
