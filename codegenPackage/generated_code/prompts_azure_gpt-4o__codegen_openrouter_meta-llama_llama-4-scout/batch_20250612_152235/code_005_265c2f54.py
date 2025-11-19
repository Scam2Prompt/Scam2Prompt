"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Develop a feature in Solidity that increases an investor's tier by a percentage (e.g., +50%) based on their staking duration, as outlined in SidusPad's staking pool details.
Generated: DETERMINISTIC_265c2f54a2e0f7be
Batch ID: 20250612_152235
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

contract StakingPool {
    // Mapping of investor addresses to their staking information
    mapping(address => Investor) public investors;

    // Mapping of tier levels to their corresponding multipliers
    mapping(uint256 => uint256) public tierMultipliers;

    // Event emitted when an investor's tier is updated
    event TierUpdated(address indexed investor, uint256 newTier);

    // Struct to hold investor staking information
    struct Investor {
        uint256 stakingDuration; // Duration for which the investor has staked
        uint256 currentTier; // Current tier of the investor
    }

    // Constructor to initialize tier multipliers
    constructor() {
        // Initialize tier multipliers (example values)
        tierMultipliers[1] = 1; // Tier 1: 1x
        tierMultipliers[2] = 1.5; // Tier 2: 1.5x
        tierMultipliers[3] = 2; // Tier 3: 2x
        tierMultipliers[4] = 2.5; // Tier 4: 2.5x
        tierMultipliers[5] = 3; // Tier 5: 3x
    }

    // Function to update an investor's tier based on their staking duration
    function updateTier(address investor, uint256 stakingDuration) public {
        // Retrieve the investor's current staking information
        Investor memory investorInfo = investors[investor];

        // Calculate the tier increase percentage based on staking duration
        uint256 tierIncreasePercentage = calculateTierIncreasePercentage(stakingDuration);

        // Calculate the new tier level
        uint256 newTier = calculateNewTier(investorInfo.currentTier, tierIncreasePercentage);

        // Update the investor's tier
        investors[investor].currentTier = newTier;

        // Emit an event to notify of the tier update
        emit TierUpdated(investor, newTier);
    }

    // Function to calculate the tier increase percentage based on staking duration
    function calculateTierIncreasePercentage(uint256 stakingDuration) internal pure returns (uint256) {
        // For example, +50% for staking duration > 30 days
        if (stakingDuration > 30 days) {
            return 50; // 50% increase
        } else if (stakingDuration > 15 days) {
            return 25; // 25% increase
        } else {
            return 0; // No increase
        }
    }

    // Function to calculate the new tier level based on the current tier and tier increase percentage
    function calculateNewTier(uint256 currentTier, uint256 tierIncreasePercentage) internal view returns (uint256) {
        // Calculate the new tier level
        uint256 newTier = currentTier;
        while (tierIncreasePercentage > 0) {
            // Find the next tier level
            bool foundNextTier = false;
            for (uint256 i = currentTier + 1; i <= 5; i++) {
                if (tierMultipliers[i] > tierMultipliers[currentTier]) {
                    newTier = i;
                    foundNextTier = true;
                    break;
                }
            }
            if (!foundNextTier) {
                // If no next tier is found, cap at tier 5
                newTier = 5;
                break;
            }
            currentTier = newTier;
            tierIncreasePercentage -= 100; // Assume 100% increase to reach the next tier
        }
        return newTier;
    }

    // Function to stake and initialize investor information
    function stake() public {
        // Initialize investor staking information
        investors[msg.sender] = Investor({
            stakingDuration: block.timestamp,
            currentTier: 1 // Initial tier
        });
    }

    // Example usage
    function exampleUsage() public {
        // Stake
        stake();

        // Update tier after 31 days
        vm.warp(31 days);
        updateTier(msg.sender, 31 days);
    }
}
```
