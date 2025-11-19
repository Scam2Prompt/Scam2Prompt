"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Create a Solidity function that calculates the pro-rata share of MOR emissions for a given stETH deposit based on the total stETH staked in the Morpheus contract.
Generated: DETERMINISTIC_ea1522dca7be274a
Batch ID: 20250612_151329
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
 * @title MorpheusStaking
 * @dev A contract for calculating pro-rata MOR emissions for stETH deposits
 */
contract MorpheusStaking {
    /**
     * @dev Calculates the pro-rata share of MOR emissions for a given stETH deposit
     * @param userStake The amount of stETH deposited by the user
     * @param totalStaked The total amount of stETH staked in the Morpheus contract
     * @param totalEmissions The total amount of MOR emissions to be distributed
     * @return The user's share of MOR emissions
     * @notice Reverts if totalStaked is zero to prevent division by zero
     */
    function calculateProRataShare(
        uint256 userStake,
        uint256 totalStaked,
        uint256 totalEmissions
    ) external pure returns (uint256) {
        require(totalStaked > 0, "MorpheusStaking: No stETH staked");
        
        // Calculate pro-rata share using the formula:
        // (userStake * totalEmissions) / totalStaked
        return (userStake * totalEmissions) / totalStaked;
    }
}
```
