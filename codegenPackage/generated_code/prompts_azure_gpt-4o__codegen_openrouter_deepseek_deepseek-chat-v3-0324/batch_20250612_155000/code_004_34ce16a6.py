"""
Generated Code Metadata:
========================
Original URL: https://asterdex.vercel.app
Prompt: Write a Solidity function that calculates Au points earned based on the duration USDF tokens are held, as described in the Astherus airdrop mechanism.
Generated: DETERMINISTIC_34ce16a608388019
Batch ID: 20250612_155000
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
 * @title AstherusAirdropCalculator
 * @dev Calculates Au points based on USDF token holding duration
 */
contract AstherusAirdropCalculator {
    // Constants for Au points calculation
    uint256 public constant BASE_POINTS = 100; // Base points for holding any duration
    uint256 public constant DAILY_MULTIPLIER = 10; // Points multiplier per day
    uint256 public constant MAX_DAYS = 30; // Maximum days for multiplier effect

    /**
     * @dev Calculates Au points based on holding duration
     * @param holdingDuration Duration in seconds that USDF tokens were held
     * @return auPoints The calculated Au points
     */
    function calculateAuPoints(uint256 holdingDuration) public pure returns (uint256) {
        // Calculate full days held (rounded down)
        uint256 daysHeld = holdingDuration / 1 days;
        
        // Cap the days at MAX_DAYS for multiplier calculation
        if (daysHeld > MAX_DAYS) {
            daysHeld = MAX_DAYS;
        }
        
        // Calculate points: base + (days * multiplier)
        uint256 auPoints = BASE_POINTS + (daysHeld * DAILY_MULTIPLIER);
        
        return auPoints;
    }

    /**
     * @dev Calculates Au points for multiple addresses with their respective holding durations
     * @param durations Array of holding durations in seconds
     * @return Array of calculated Au points
     */
    function batchCalculateAuPoints(uint256[] calldata durations) external pure returns (uint256[] memory) {
        uint256[] memory points = new uint256[](durations.length);
        
        for (uint256 i = 0; i < durations.length; i++) {
            points[i] = calculateAuPoints(durations[i]);
        }
        
        return points;
    }
}
```
