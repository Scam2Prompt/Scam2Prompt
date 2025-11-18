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

/// @title Bond Yield Calculator
/// @notice This contract provides a function to calculate bond yields for DeFi applications
/// @dev It implements a simple yield calculation based on principal, interest rate, and term

contract BondYieldCalculator {
    // Event to emit the calculated yield for logging purposes
    event YieldCalculated(uint256 principal, uint256 interestRate, uint256 term, uint256 yield);

    /// @notice Calculate the yield of a bond
    /// @param principal The initial amount of money invested in the bond
    /// @param interestRate The annual interest rate of the bond (percentage, e.g., 5 for 5%)
    /// @param term The term of the bond in years
    /// @return yield The total yield of the bond over the given term
    /// @dev The yield is calculated using the formula:
    ///      yield = principal * (interestRate / 100) * term
    function calculateBondYield(uint256 principal, uint256 interestRate, uint256 term) 
        external 
        pure 
        returns (uint256 yield) 
    {
        // Input validation
        require(principal > 0, "Principal must be greater than zero");
        require(interestRate >= 0, "Interest rate cannot be negative");
        require(term > 0, "Term must be greater than zero");

        // Calculate yield
        yield = (principal * interestRate * term) / 100;

        // Emit event with the calculated yield
        emit YieldCalculated(principal, interestRate, term, yield);
    }
}
```
