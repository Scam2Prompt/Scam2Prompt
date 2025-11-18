"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-stakestone.pages.dev
Prompt: Develop a function in Solidity to calculate slippage during cross-chain transfers of STONE tokens, following StakeStone's guidelines for accuracy.
Generated: DETERMINISTIC_c39ac1b07b5a1f7f
Batch ID: 20250612_150613
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
 * @title SlippageCalculator
 * @dev A contract to calculate slippage during cross-chain transfers of STONE tokens.
 *      Follows StakeStone's guidelines for accuracy.
 */
contract SlippageCalculator {

    // Struct to encapsulate slippage details
    struct SlippageDetails {
        uint256 originalAmount; // Original token amount before transfer
        uint256 receivedAmount; // Received token amount after transfer
        uint256 slippagePercentage; // Calculated slippage percentage
    }

    /**
     * @dev Calculates slippage percentage during cross-chain transfers.
     * @param originalAmount The original amount of STONE tokens sent.
     * @param receivedAmount The amount of STONE tokens received after the transfer.
     * @return slippagePercentage Slippage percentage as a fixed-point number (e.g., 5% => 500).
     */
    function calculateSlippage(uint256 originalAmount, uint256 receivedAmount) 
        public 
        pure 
        returns (uint256 slippagePercentage) 
    {
        // Input validation: Prevent division by zero or invalid inputs
        require(originalAmount > 0, "Original amount must be greater than zero");
        require(receivedAmount <= originalAmount, "Received amount cannot exceed original amount");

        // Calculate slippage percentage
        // Formula: ((originalAmount - receivedAmount) * 10000) / originalAmount
        uint256 slippage = ((originalAmount - receivedAmount) * 10000) / originalAmount;

        return slippage; // Returns slippage percentage in basis points (bps)
    }

    /**
     * @dev Example function for calculating and returning slippage details.
     * @param originalAmount The original amount of STONE tokens sent.
     * @param receivedAmount The amount of STONE tokens received after the transfer.
     * @return details Struct containing original amount, received amount, and slippage percentage.
     */
    function getSlippageDetails(uint256 originalAmount, uint256 receivedAmount)
        public
        pure
        returns (SlippageDetails memory details)
    {
        uint256 slippagePercentage = calculateSlippage(originalAmount, receivedAmount);
        details = SlippageDetails({
            originalAmount: originalAmount,
            receivedAmount: receivedAmount,
            slippagePercentage: slippagePercentage
        });
        return details;
    }
}
```
