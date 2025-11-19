"""
Generated Code Metadata:
========================
Original URL: https://pepelovesinu.pages.dev
Prompt: Create a Solidity function that calculates the bonus PLINU tokens received during Stage 3 of the token sale, based on the 10% bonus offer.
Generated: DETERMINISTIC_185011df1d808a5a
Batch ID: 20250612_153517
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
 * @title Token Sale Bonus Calculator
 * @notice Calculates the bonus PLINU tokens received during Stage 3 of the token sale.
 */
contract TokenSaleBonusCalculator {

    /**
     * @dev Calculates the bonus PLINU tokens received during Stage 3 of the token sale.
     * @param _tokensPurchased The number of PLINU tokens purchased during Stage 3.
     * @return The bonus PLINU tokens received.
     */
    function calculateBonusPLINU(uint256 _tokensPurchased) public pure returns (uint256) {
        // Define the bonus percentage for Stage 3 (10%)
        uint256 constant BONUS_PERCENTAGE = 10;

        // Check for zero tokens purchased
        require(_tokensPurchased > 0, "Tokens purchased must be greater than zero.");

        // Calculate the bonus PLINU tokens
        uint256 bonusTokens = (_tokensPurchased * BONUS_PERCENTAGE) / 100;

        return bonusTokens;
    }

    /**
     * @dev Calculates the total PLINU tokens received during Stage 3 of the token sale, including bonus.
     * @param _tokensPurchased The number of PLINU tokens purchased during Stage 3.
     * @return The total PLINU tokens received, including bonus.
     */
    function calculateTotalPLINU(uint256 _tokensPurchased) public pure returns (uint256) {
        // Calculate the bonus PLINU tokens
        uint256 bonusTokens = calculateBonusPLINU(_tokensPurchased);

        // Calculate the total PLINU tokens
        uint256 totalTokens = _tokensPurchased + bonusTokens;

        return totalTokens;
    }
}
```
