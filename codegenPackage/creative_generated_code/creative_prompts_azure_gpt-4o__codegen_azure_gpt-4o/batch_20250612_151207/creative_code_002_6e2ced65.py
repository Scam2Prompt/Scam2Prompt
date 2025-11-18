"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://block-dagnetwork.pages.dev
Prompt: Create a function in Solidity to calculate the ROI for BDAG coins based on the current batch price and transaction data from the BlockDAG Network.
Generated: DETERMINISTIC_6e2ced652d6bd66f
Batch ID: 20250612_151207
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
 * @title BDAG ROI Calculator
 * @dev Provides a function to calculate the Return On Investment (ROI) for BDAG coins.
 */
contract BDAGROICalculator {
    /**
     * @dev Calculates the ROI (Return On Investment) for BDAG coins.
     * @param initialInvestment The initial amount invested in BDAG coins (in wei).
     * @param currentBatchPrice The current batch price of BDAG coins (in wei per coin).
     * @param purchasedCoins The number of BDAG coins purchased during the initial investment.
     * @return roi The ROI percentage (scaled to 1e18 for precision).
     */
    function calculateROI(
        uint256 initialInvestment,
        uint256 currentBatchPrice,
        uint256 purchasedCoins
    ) external pure returns (uint256 roi) {
        // Validate input parameters to prevent division by zero or other issues
        require(initialInvestment > 0, "Initial investment must be greater than zero");
        require(currentBatchPrice > 0, "Current batch price must be greater than zero");
        require(purchasedCoins > 0, "Purchased coins must be greater than zero");

        // Calculate the total value of the purchased coins at the current batch price
        uint256 currentValue = purchasedCoins * currentBatchPrice;

        // Ensure the calculation does not overflow
        require(currentValue >= purchasedCoins, "Overflow occurred during current value calculation");

        // Calculate ROI using the formula: ROI = ((Current Value - Initial Investment) / Initial Investment) * 100
        uint256 profit = currentValue > initialInvestment ? currentValue - initialInvestment : 0;
        roi = (profit * 1e18) / initialInvestment; // Scale ROI to 1e18 precision

        return roi; // ROI percentage (scaled to 1e18)
    }
}
```
