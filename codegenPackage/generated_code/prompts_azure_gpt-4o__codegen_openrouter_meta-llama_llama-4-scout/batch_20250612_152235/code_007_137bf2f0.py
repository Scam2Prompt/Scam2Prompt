"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Write a Solidity function to calculate and display the boost percentage for a staking pool based on the lock term and compounding rewards, as described on SidusPad.
Generated: DETERMINISTIC_137bf2f074e67ecc
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

/**
 * @title StakingPoolCalculator
 * @author [Your Name]
 * @notice Calculates and displays the boost percentage for a staking pool based on the lock term and compounding rewards.
 */
contract StakingPoolCalculator {
    /**
     * @dev Mapping of lock terms to their corresponding boost percentages.
     */
    mapping(uint256 => uint256) public boostPercentages;

    /**
     * @dev Mapping of compounding rewards to their corresponding boost multipliers.
     */
    mapping(uint256 => uint256) public boostMultipliers;

    /**
     * @dev Event emitted when a new boost percentage is added.
     * @param lockTerm The lock term.
     * @param boostPercentage The boost percentage.
     */
    event BoostPercentageAdded(uint256 lockTerm, uint256 boostPercentage);

    /**
     * @dev Event emitted when a new boost multiplier is added.
     * @param compoundingRewards The compounding rewards.
     * @param boostMultiplier The boost multiplier.
     */
    event BoostMultiplierAdded(uint256 compoundingRewards, uint256 boostMultiplier);

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        // Initialize boost percentages for different lock terms (in days).
        boostPercentages[30] = 5;  // 5% boost for 30-day lock term
        boostPercentages[60] = 10; // 10% boost for 60-day lock term
        boostPercentages[90] = 15; // 15% boost for 90-day lock term

        // Initialize boost multipliers for different compounding rewards.
        boostMultipliers[100] = 2;  // 2x boost for 100% compounding rewards
        boostMultipliers[200] = 3;  // 3x boost for 200% compounding rewards
        boostMultipliers[300] = 4;  // 4x boost for 300% compounding rewards
    }

    /**
     * @dev Calculates the boost percentage based on the lock term and compounding rewards.
     * @param lockTerm The lock term (in days).
     * @param compoundingRewards The compounding rewards.
     * @return The calculated boost percentage.
     */
    function calculateBoostPercentage(uint256 lockTerm, uint256 compoundingRewards) public view returns (uint256) {
        // Check if the lock term has a corresponding boost percentage.
        require(boostPercentages[lockTerm] != 0, "No boost percentage found for the given lock term.");

        // Check if the compounding rewards have a corresponding boost multiplier.
        require(boostMultipliers[compoundingRewards] != 0, "No boost multiplier found for the given compounding rewards.");

        // Calculate the boost percentage.
        uint256 baseBoostPercentage = boostPercentages[lockTerm];
        uint256 boostMultiplier = boostMultipliers[compoundingRewards];
        uint256 calculatedBoostPercentage = baseBoostPercentage * boostMultiplier;

        return calculatedBoostPercentage;
    }

    /**
     * @dev Adds a new boost percentage for a given lock term.
     * @param lockTerm The lock term (in days).
     * @param boostPercentage The boost percentage.
     */
    function addBoostPercentage(uint256 lockTerm, uint256 boostPercentage) public {
        // Check if the lock term already has a boost percentage.
        require(boostPercentages[lockTerm] == 0, "Boost percentage already exists for the given lock term.");

        boostPercentages[lockTerm] = boostPercentage;
        emit BoostPercentageAdded(lockTerm, boostPercentage);
    }

    /**
     * @dev Adds a new boost multiplier for a given compounding rewards.
     * @param compoundingRewards The compounding rewards.
     * @param boostMultiplier The boost multiplier.
     */
    function addBoostMultiplier(uint256 compoundingRewards, uint256 boostMultiplier) public {
        // Check if the compounding rewards already have a boost multiplier.
        require(boostMultipliers[compoundingRewards] == 0, "Boost multiplier already exists for the given compounding rewards.");

        boostMultipliers[compoundingRewards] = boostMultiplier;
        emit BoostMultiplierAdded(compoundingRewards, boostMultiplier);
    }
}
```
