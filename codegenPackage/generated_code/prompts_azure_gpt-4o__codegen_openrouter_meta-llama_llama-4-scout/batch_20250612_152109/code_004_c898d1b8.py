"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-com.pages.dev
Prompt: Write a Solidity function for calculating staking rewards based on APY and lock duration, similar to the $SCOTTY staking mechanism.
Generated: DETERMINISTIC_c898d1b8dece6b66
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title StakingRewardsCalculator
 * @author [Your Name]
 * @notice Calculates staking rewards based on APY and lock duration.
 */
contract StakingRewardsCalculator {
    /**
     * @dev Calculates staking rewards.
     * @param principal The initial staked amount.
     * @param apy The annual percentage yield (APY).
     * @param lockDuration The lock duration in seconds.
     * @param totalSecondsInAYear The total seconds in a year (default: 31,536,000).
     * @return The calculated staking rewards.
     */
    function calculateStakingRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockDuration,
        uint256 totalSecondsInAYear
    ) public pure returns (uint256) {
        // Ensure inputs are valid
        require(principal > 0, "Principal must be greater than 0");
        require(apy > 0, "APY must be greater than 0");
        require(lockDuration > 0, "Lock duration must be greater than 0");
        require(totalSecondsInAYear > 0, "Total seconds in a year must be greater than 0");

        // Calculate the staking rewards
        uint256 rewards = (principal * apy * lockDuration) / (totalSecondsInAYear * 100);

        return rewards;
    }

    /**
     * @dev Calculates staking rewards with default total seconds in a year.
     * @param principal The initial staked amount.
     * @param apy The annual percentage yield (APY).
     * @param lockDuration The lock duration in seconds.
     * @return The calculated staking rewards.
     */
    function calculateStakingRewardsDefault(
        uint256 principal,
        uint256 apy,
        uint256 lockDuration
    ) public pure returns (uint256) {
        uint256 totalSecondsInAYear = 31536000; // 31,536,000 seconds in a non-leap year
        return calculateStakingRewards(principal, apy, lockDuration, totalSecondsInAYear);
    }
}
```
