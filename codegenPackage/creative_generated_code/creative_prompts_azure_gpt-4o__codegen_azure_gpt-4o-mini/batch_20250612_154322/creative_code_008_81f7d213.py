"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Write a Solidity function for calculating land transaction taxes (e.g., 2%) for virtual real estate trades on the EarthMeta platform.
Generated: DETERMINISTIC_81f7d213c2270c0c
Batch ID: 20250612_154322
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

/// @title LandTransactionTax
/// @dev This contract calculates the transaction tax for virtual real estate trades on the EarthMeta platform
contract LandTransactionTax {
    // Tax rate set to 2% (denoted as 200 in basis points)
    uint256 public constant TAX_RATE_BASIS_POINTS = 200;

    /// @dev Event emitted when a tax is calculated
    event TaxCalculated(address indexed owner, uint256 transactionValue, uint256 taxAmount);

    /// @notice Calculates the transaction tax based on the given transaction value
    /// @param transactionValue The value of the land transaction in wei
    /// @return taxAmount The calculated tax amount in wei
    /// @dev Reverts if the transaction value is zero
    function calculateTax(uint256 transactionValue) external pure returns (uint256 taxAmount) {
        require(transactionValue > 0, "Transaction value must be greater than zero");

        // Calculate the tax amount based on the transaction value and tax rate
        taxAmount = (transactionValue * TAX_RATE_BASIS_POINTS) / 10000;

        // Emit an event for the calculated tax
        emit TaxCalculated(msg.sender, transactionValue, taxAmount);
    }
}
```
