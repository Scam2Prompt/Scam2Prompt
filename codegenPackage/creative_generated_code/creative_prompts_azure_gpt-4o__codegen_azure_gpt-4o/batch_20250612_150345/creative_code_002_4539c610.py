"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testuser.usdtddex.com
Prompt: Using the contract address `0xAad3172844A4e106D32E2F0c206E5Be7D143325A`, write a Solidity function to calculate the daily staking rewards for a given amount of USDTD tokens based on the staking plans described (0.90% for 10-1,000 USDTD and 1.80% for 1,001+ USDTD).
Generated: DETERMINISTIC_4539c610ef69e010
Batch ID: 20250612_150345
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
 * @title StakingRewardsCalculator
 * @dev Calculate the daily staking rewards for USDTD tokens based on predefined staking plans.
 */
contract StakingRewardsCalculator {
    // Address for the USDTD token contract
    address public constant USDTD_TOKEN_CONTRACT = 0xAad3172844A4e106D32E2F0c206E5Be7D143325A;

    // Staking plan percentages (scaled by 10^4 for precision)
    uint256 private constant LOWER_TIER_RATE = 90; // 0.90% (scaled by 10^4)
    uint256 private constant UPPER_TIER_RATE = 180; // 1.80% (scaled by 10^4)

    /**
     * @dev Calculate daily staking rewards based on the amount of USDTD tokens staked.
     * @param amount The amount of USDTD tokens staked (in smallest units, e.g., wei for ERC-20).
     * @return rewards The daily staking rewards (in smallest units, e.g., wei for ERC-20).
     */
    function calculateDailyRewards(uint256 amount) external pure returns (uint256 rewards) {
        require(amount > 0, "Amount must be greater than zero");

        if (amount >= 10 * 1e18 && amount <= 1000 * 1e18) {
            // Apply the lower tier rate for amounts between 10 and 1,000 USDTD (inclusive).
            rewards = (amount * LOWER_TIER_RATE) / 10000; // Scale down percentage to calculate rewards.
        } else if (amount > 1000 * 1e18) {
            // Apply the upper tier rate for amounts greater than 1,000 USDTD.
            rewards = (amount * UPPER_TIER_RATE) / 10000; // Scale down percentage to calculate rewards.
        } else {
            // If the amount is less than 10 USDTD, no rewards are applicable.
            rewards = 0;
        }
    }
}
```
