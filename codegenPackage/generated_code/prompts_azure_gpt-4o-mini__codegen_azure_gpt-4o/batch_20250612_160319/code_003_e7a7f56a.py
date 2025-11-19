"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Generate a Solidity function that calculates the total USDC rewards based on the number of $UPRINT tokens held by a user.
Generated: DETERMINISTIC_e7a7f56aadc1ddb0
Batch ID: 20250612_160319
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
 * @title RewardsCalculator
 * @dev A contract to calculate USDC rewards based on the number of $UPRINT tokens held by a user.
 */
contract RewardsCalculator {
    // Mapping to store the number of $UPRINT tokens held by each user
    mapping(address => uint256) public uprintBalances;

    // USDC reward rate per $UPRINT token (e.g., 0.01 USDC per $UPRINT)
    uint256 public rewardRate;

    /**
     * @dev Constructor to initialize the reward rate.
     * @param _rewardRate The USDC reward rate per $UPRINT token (in smallest unit, e.g., wei for USDC).
     */
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to calculate the total USDC rewards for a user based on their $UPRINT balance.
     * @param user The address of the user.
     * @return The total USDC rewards for the user (in smallest unit, e.g., wei for USDC).
     */
    function calculateRewards(address user) external view returns (uint256) {
        // Get the user's $UPRINT balance
        uint256 userBalance = uprintBalances[user];

        // Calculate the total rewards
        uint256 totalRewards = userBalance * rewardRate;

        return totalRewards;
    }

    /**
     * @dev Function to update the $UPRINT balance of a user (for demonstration purposes).
     * @param user The address of the user.
     * @param balance The new $UPRINT balance of the user.
     */
    function updateUprintBalance(address user, uint256 balance) external {
        require(user != address(0), "Invalid user address");
        uprintBalances[user] = balance;
    }

    /**
     * @dev Function to update the reward rate (for demonstration purposes).
     * @param _rewardRate The new USDC reward rate per $UPRINT token.
     */
    function updateRewardRate(uint256 _rewardRate) external {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }
}
```
