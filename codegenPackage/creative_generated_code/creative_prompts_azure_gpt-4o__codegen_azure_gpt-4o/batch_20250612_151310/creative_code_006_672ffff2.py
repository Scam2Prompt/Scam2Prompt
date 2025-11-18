"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubatewhitelist.pages.dev
Prompt: Develop a function in Solidity that calculates staking rewards dynamically based on lock term and APY boost, as described on Decubate's whitelist portal.
Generated: DETERMINISTIC_672ffff2b05c2fdb
Batch ID: 20250612_151310
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

/// @title StakingRewardsCalculator
/// @notice A smart contract for calculating staking rewards dynamically based on lock term and APY boost.
contract StakingRewardsCalculator {
    // State variables
    uint256 public constant BASE_APY = 10; // Base APY in percentage (e.g., 10%)
    uint256 public constant APY_BOOST_PER_TERM = 2; // APY boost per lock term in percentage (e.g., 2%)

    /// @notice Calculates staking rewards based on the lock term and APY boost.
    /// @param principal The amount of tokens staked by the user.
    /// @param lockTermInDays The lock term in days (e.g., 30, 60, 90 days).
    /// @return rewards The calculated staking rewards.
    function calculateStakingRewards(uint256 principal, uint256 lockTermInDays) external pure returns (uint256 rewards) {
        require(principal > 0, "Principal must be greater than zero");
        require(lockTermInDays > 0, "Lock term must be greater than zero");
        require(lockTermInDays % 30 == 0, "Lock term must be in multiples of 30 days");

        // Calculate the number of 30-day terms (e.g., 30 days = 1 term, 60 days = 2 terms, etc.)
        uint256 lockTermInMonths = lockTermInDays / 30;

        // Calculate total APY with boosts
        uint256 totalAPY = BASE_APY + (lockTermInMonths * APY_BOOST_PER_TERM);

        // Calculate rewards: Rewards = (Principal * APY * Lock Term in Years) / 100
        uint256 lockTermInYears = lockTermInDays / 365; // Convert lock term to years (integer division)
        rewards = (principal * totalAPY * lockTermInYears) / 100;

        return rewards;
    }
}
```
