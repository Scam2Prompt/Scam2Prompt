"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a Solidity function that calculates the percentage share of dividends for a token holder based on their token holdings and the total supply, as explained on BibbyDivs.com.
Generated: DETERMINISTIC_090ae5805cb815b3
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

/**
 * @title DividendCalculator
 * @dev Provides functionality to calculate a token holder's percentage share of dividends.
 */
contract DividendCalculator {
    /**
     * @notice Calculates the percentage share of dividends for a token holder.
     * @param holderBalance The token balance of the holder.
     * @param totalSupply The total supply of tokens for the contract.
     * @return percentageShare The percentage share (as a value between 0 and 100) of dividends for the token holder.
     */
    function calculateDividendShare(
        uint256 holderBalance,
        uint256 totalSupply
    ) public pure returns (uint256 percentageShare) {
        // Validate inputs to ensure no division by zero or invalid values
        require(totalSupply > 0, "Total supply must be greater than zero");
        require(holderBalance >= 0, "Holder balance cannot be negative");

        // Perform the calculation
        percentageShare = (holderBalance * 100) / totalSupply;

        // Return the calculated percentage share
        return percentageShare;
    }
}
```
