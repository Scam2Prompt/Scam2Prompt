"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a function in Solidity to calculate the fee distribution between the global dividends pool and the referrer, based on the investment details provided on BibbyDivs.com.
Generated: DETERMINISTIC_e12964516fc15473
Batch ID: 20250612_150316
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

/// @title Fee Distribution Contract
/// @notice This contract calculates the fee distribution between the global dividends pool and the referrer.
contract FeeDistribution {

    // Constants for fee distribution percentages
    uint256 public constant DIVIDENDS_POOL_PERCENTAGE = 70; // 70% to dividends pool
    uint256 public constant REFERRER_PERCENTAGE = 30; // 30% to referrer

    // Events for logging fee distribution
    event FeeDistributed(uint256 totalAmount, uint256 dividendsPoolAmount, uint256 referrerAmount);

    /// @notice Calculate fee distribution based on the investment amount
    /// @param investmentAmount The total investment amount
    /// @param referrerAddress The address of the referrer
    /// @return dividendsPoolAmount Amount allocated to the dividends pool
    /// @return referrerAmount Amount allocated to the referrer
    function calculateFeeDistribution(uint256 investmentAmount, address referrerAddress) 
        external 
        returns (uint256 dividendsPoolAmount, uint256 referrerAmount) 
    {
        // Validate input parameters
        require(investmentAmount > 0, "Investment amount must be greater than zero.");
        require(referrerAddress != address(0), "Invalid referrer address.");

        // Calculate the amounts for both the dividends pool and the referrer
        dividendsPoolAmount = (investmentAmount * DIVIDENDS_POOL_PERCENTAGE) / 100;
        referrerAmount = (investmentAmount * REFERRER_PERCENTAGE) / 100;

        // Emit an event for logging purposes
        emit FeeDistributed(investmentAmount, dividendsPoolAmount, referrerAmount);
    }
}
```
