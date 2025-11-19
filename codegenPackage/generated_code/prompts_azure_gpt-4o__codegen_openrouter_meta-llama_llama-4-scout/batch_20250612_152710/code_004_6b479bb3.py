"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a Solidity function that calculates compounded staking rewards for AITECH tokens based on the APY, lock term, and boost percentage, as described in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_6b479bb3bc55d16d
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Compounded Staking Rewards Calculator for AITECH tokens
 * @author [Your Name]
 * @notice Calculates compounded staking rewards based on APY, lock term, and boost percentage
 */
contract StakingRewardsCalculator {

    /**
     * @dev Calculates compounded staking rewards
     * @param principal The initial amount of AITECH tokens staked
     * @param apy The annual percentage yield (APY) as a decimal (e.g., 10% = 0.10)
     * @param lockTerm The lock term in days
     * @param boostPercentage The boost percentage as a decimal (e.g., 10% = 0.10)
     * @return The compounded staking rewards
     */
    function calculateCompoundedRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockTerm,
        uint256 boostPercentage
    ) public pure returns (uint256) {
        // Convert APY to a decimal for calculation
        uint256 apyDecimal = apy * 1e16; // 1e18 (1) * 1e-2 (2 decimals) = 1e16

        // Calculate the total boost factor
        uint256 boostFactor = 1e18 + (boostPercentage * 1e16); // 1e18 (1) + 1e16 (0.01) * boost

        // Calculate the daily interest rate
        uint256 dailyInterestRate = (apyDecimal * 1e18) / (365 * 1e18); // APY / 365 days

        // Calculate the number of compounding periods
        uint256 compoundingPeriods = lockTerm;

        // Calculate the compounded rewards using the formula: A = P * (1 + r/n)^(nt)
        // Where:
        //   A = the future value of the investment/loan, including interest
        //   P = principal investment amount (the initial deposit or loan amount)
        //   r = annual interest rate (in decimal)
        //   n = number of times that interest is compounded per year
        //   t = time the money is invested or borrowed for, in years
        uint256 compoundedRewards = principal * (1e18 + dailyInterestRate) ** compoundingPeriods;
        compoundedRewards = (compoundedRewards * boostFactor) / 1e18;

        // Return the compounded rewards minus the principal
        return compoundedRewards - principal;
    }

    /**
     * @dev Reverts if the input parameters are invalid
     * @param principal The initial amount of AITECH tokens staked
     * @param apy The annual percentage yield (APY) as a decimal (e.g., 10% = 0.10)
     * @param lockTerm The lock term in days
     * @param boostPercentage The boost percentage as a decimal (e.g., 10% = 0.10)
     */
    function validateInputs(
        uint256 principal,
        uint256 apy,
        uint256 lockTerm,
        uint256 boostPercentage
    ) public pure {
        require(principal > 0, "Principal must be greater than 0");
        require(apy > 0, "APY must be greater than 0");
        require(lockTerm > 0, "Lock term must be greater than 0");
        require(boostPercentage <= 1e18, "Boost percentage must not exceed 100%");
    }

    /**
     * @dev Calculates and returns compounded staking rewards with input validation
     * @param principal The initial amount of AITECH tokens staked
     * @param apy The annual percentage yield (APY) as a decimal (e.g., 10% = 0.10)
     * @param lockTerm The lock term in days
     * @param boostPercentage The boost percentage as a decimal (e.g., 10% = 0.10)
     * @return The compounded staking rewards
     */
    function getCompoundedRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockTerm,
        uint256 boostPercentage
    ) public pure returns (uint256) {
        validateInputs(principal, apy, lockTerm, boostPercentage);
        return calculateCompoundedRewards(principal, apy, lockTerm, boostPercentage);
    }
}
```
