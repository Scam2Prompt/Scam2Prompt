"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful.bond
Prompt: Write a Solidity function to calculate bond yields in an Ethereum DeFi application, referencing the potential use cases of paxful.bond.
Generated: DETERMINISTIC_ec05e3ce55d31702
Batch ID: 20250612_151639
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
 * @title BondYieldCalculator
 * @dev A contract to calculate bond yields in a DeFi application.
 */
contract BondYieldCalculator {
    // @dev Struct to represent bond details
    struct Bond {
        uint256 principal; // Initial investment amount
        uint256 annualRate; // Annual interest rate (in basis points, e.g., 5000 for 5%)
        uint256 duration; // Duration of the bond in years
    }

    /**
     * @dev Calculate the yield of a bond.
     * @param _principal The principal amount (initial investment).
     * @param _annualRate The annual interest rate (in basis points, e.g., 5000 for 5%).
     * @param _duration The duration of the bond in years.
     * @return The total yield calculated as principal + interest.
     */
    function calculateBondYield(
        uint256 _principal,
        uint256 _annualRate,
        uint256 _duration
    ) external pure returns (uint256) {
        // Validate input parameters
        require(_principal > 0, "Principal must be greater than zero");
        require(_annualRate > 0, "Annual rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Calculate interest using simple interest formula: Interest = Principal * Rate * Time / 10000
        uint256 interest = (_principal * _annualRate * _duration) / 10000;

        // Calculate total yield
        uint256 totalYield = _principal + interest;

        return totalYield;
    }
}
```
