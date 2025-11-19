"""
Generated Code Metadata:
========================
Original URL: https://testtt-ba0.pages.dev
Prompt: Develop a Solidity function to calculate the boosted capabilities of land based on the number of Farmers assigned to it, as described in Wolf Game.
Generated: DETERMINISTIC_180fed072363afb1
Batch ID: 20250612_151100
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
 * @title LandBooster
 * @dev Calculates boosted capabilities of land based on assigned Farmers
 */
contract LandBooster {
    // Base multiplier for unboosted land
    uint256 public constant BASE_MULTIPLIER = 100; // 100 = 1.00x
    
    // Maximum boost multiplier cap (e.g., 200 = 2.00x)
    uint256 public constant MAX_BOOST = 200;
    
    // Boost per Farmer (e.g., 10 = 0.10x per Farmer)
    uint256 public constant BOOST_PER_FARMER = 10;
    
    // Maximum number of Farmers that can be assigned to a land
    uint256 public constant MAX_FARMERS_PER_LAND = 10;
    
    /**
     * @dev Calculates the boosted multiplier for a land based on Farmers assigned
     * @param numFarmers Number of Farmers assigned to the land
     * @return boostMultiplier The calculated boost multiplier (100 = 1.00x)
     */
    function calculateBoost(uint256 numFarmers) public pure returns (uint256) {
        // Validate input
        require(numFarmers <= MAX_FARMERS_PER_LAND, "Exceeds max Farmers per land");
        
        // Calculate raw boost
        uint256 rawBoost = BASE_MULTIPLIER + (numFarmers * BOOST_PER_FARMER);
        
        // Apply cap if needed
        if (rawBoost > MAX_BOOST) {
            return MAX_BOOST;
        }
        
        return rawBoost;
    }
    
    /**
     * @dev Calculates the boosted output for a land
     * @param baseOutput Base output of the land without boost
     * @param numFarmers Number of Farmers assigned to the land
     * @return boostedOutput The calculated output after applying boost
     */
    function calculateBoostedOutput(uint256 baseOutput, uint256 numFarmers) public pure returns (uint256) {
        uint256 boostMultiplier = calculateBoost(numFarmers);
        return (baseOutput * boostMultiplier) / BASE_MULTIPLIER;
    }
}
```
