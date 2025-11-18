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

/**
 * @title StakingRewardCalculator
 * @dev A contract to calculate staking rewards dynamically based on lock term and APY boost.
 */
contract StakingRewardCalculator {

    // Structure to hold staking information
    struct StakingInfo {
        uint256 amount; // Amount staked
        uint256 lockTerm; // Lock term in days
        uint256 apyBoost; // APY boost in percentage
    }

    /**
     * @dev Calculates the staking rewards based on the given parameters.
     * @param _stakingInfo Staking information containing amount, lock term, and APY boost.
     * @return reward The calculated staking reward.
     */
    function calculateReward(StakingInfo memory _stakingInfo) public pure returns (uint256 reward) {
        // Validate inputs
        require(_stakingInfo.amount > 0, "Staked amount must be greater than zero");
        require(_stakingInfo.lockTerm > 0, "Lock term must be greater than zero");
        require(_stakingInfo.apyBoost >= 0, "APY boost must not be negative");

        // APY is represented as a percentage, convert it to a decimal
        uint256 apy = 5; // Base APY (5% as an example)
        uint256 effectiveAPY = apy + _stakingInfo.apyBoost;

        // Calculate the total reward:
        // Formula: reward = (amount * (effectiveAPY / 100) * (lockTerm / 365))
        reward = (_stakingInfo.amount * effectiveAPY * _stakingInfo.lockTerm) / (100 * 365);
    }
}
```
