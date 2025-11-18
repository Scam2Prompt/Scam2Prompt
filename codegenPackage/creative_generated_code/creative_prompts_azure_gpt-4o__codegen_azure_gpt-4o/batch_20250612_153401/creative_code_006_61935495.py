"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Create a Solidity function to calculate the number of "DRE" tokens a buyer should receive based on the input FTM amount, using the rates provided (e.g., 250 FTM = 99,500 DRE).
Generated: DETERMINISTIC_61935495eafde771
Batch ID: 20250612_153401
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
 * @title TokenCalculator
 * @dev Contract to calculate the amount of "DRE" tokens a buyer should receive based on input FTM amount.
 */
contract TokenCalculator {
    // Conversion rate constants
    uint256 private constant FTM_TO_DRE_RATE = 398; // 1 FTM = 398 DRE
    uint256 private constant RATE_DECIMALS = 2; // To account for fractional rates

    /**
     * @dev Calculates the amount of DRE tokens based on the input FTM amount.
     * @param ftmAmount The amount of FTM tokens the buyer wants to exchange.
     * @return dreAmount The amount of DRE tokens the buyer will receive.
     */
    function calculateDRE(uint256 ftmAmount) external pure returns (uint256 dreAmount) {
        // Input validation
        require(ftmAmount > 0, "FTM amount must be greater than zero");

        // Perform the conversion using the fixed rate
        // Multiply by the rate and divide by 10^RATE_DECIMALS to handle fractional rates
        dreAmount = (ftmAmount * FTM_TO_DRE_RATE) / (10 ** RATE_DECIMALS);

        return dreAmount;
    }
}
```
