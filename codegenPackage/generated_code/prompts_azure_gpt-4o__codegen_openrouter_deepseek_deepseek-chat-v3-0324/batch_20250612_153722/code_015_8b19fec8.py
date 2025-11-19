"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Write a Solidity function to calculate reward multipliers based on the number of $STARS tokens held, as incentivized in the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8b19fec8ec803a5d
Batch ID: 20250612_153722
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
 * @title STARS Reward Multiplier Calculator
 * @dev Calculates reward multipliers based on STARS token holdings
 */
contract StarsRewardCalculator {
    // Thresholds for different multiplier tiers (in STARS tokens)
    uint256[] public tierThresholds = [
        1000 ether,    // Tier 1: 1,000 STARS
        5000 ether,    // Tier 2: 5,000 STARS
        10000 ether,   // Tier 3: 10,000 STARS
        50000 ether,   // Tier 4: 50,000 STARS
        100000 ether   // Tier 5: 100,000 STARS
    ];

    // Multipliers corresponding to each tier (in basis points, where 10000 = 1x)
    uint256[] public tierMultipliers = [
        11000,  // 1.1x for Tier 1
        12500,  // 1.25x for Tier 2
        15000,  // 1.5x for Tier 3
        20000,  // 2x for Tier 4
        30000   // 3x for Tier 5
    ];

    /**
     * @dev Calculate reward multiplier based on STARS token holdings
     * @param starsBalance The user's STARS token balance (in wei)
     * @return multiplier The reward multiplier in basis points (e.g., 11000 = 1.1x)
     */
    function calculateRewardMultiplier(uint256 starsBalance) public view returns (uint256 multiplier) {
        require(tierThresholds.length == tierMultipliers.length, "Invalid tier configuration");

        // Default multiplier is 1x (10000 basis points)
        multiplier = 10000;

        // Check each tier from highest to lowest
        for (uint256 i = tierThresholds.length; i > 0; i--) {
            if (starsBalance >= tierThresholds[i - 1]) {
                multiplier = tierMultipliers[i - 1];
                break;
            }
        }

        return multiplier;
    }

    /**
     * @dev Get the number of reward tiers
     * @return count The number of reward tiers
     */
    function getTierCount() public view returns (uint256 count) {
        return tierThresholds.length;
    }

    /**
     * @dev Get threshold and multiplier for a specific tier
     * @param tierIndex The index of the tier (0-based)
     * @return threshold The threshold amount for the tier (in wei)
     * @return multiplier The multiplier for the tier (in basis points)
     */
    function getTierDetails(uint256 tierIndex) public view returns (uint256 threshold, uint256 multiplier) {
        require(tierIndex < tierThresholds.length, "Invalid tier index");
        return (tierThresholds[tierIndex], tierMultipliers[tierIndex]);
    }
}
```
