"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Create a Solidity function that calculates the bonus PLINU tokens received during Stage 3 of the token sale, based on the 10% bonus offer.
Generated: DETERMINISTIC_185011df1d808a5a
Batch ID: 20250612_153517
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
 * @title TokenSaleBonusCalculator
 * @dev Provides functionality to calculate bonus PLINU tokens.
 */
contract TokenSaleBonusCalculator {
    // Constant for the Stage 3 bonus percentage (10%)
    uint256 public constant BONUS_PERCENTAGE_STAGE_3 = 10;

    /**
     * @dev Calculates the bonus PLINU tokens for Stage 3 of the token sale.
     * @param tokenAmount The number of PLINU tokens purchased.
     * @return bonusTokens The number of bonus PLINU tokens to be awarded.
     */
    function calculateStage3Bonus(uint256 tokenAmount) public pure returns (uint256 bonusTokens) {
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Calculate the bonus tokens (10% of tokenAmount)
        bonusTokens = (tokenAmount * BONUS_PERCENTAGE_STAGE_3) / 100;

        return bonusTokens;
    }
}
```
