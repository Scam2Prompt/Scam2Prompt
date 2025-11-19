"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Create a function in Solidity that calculates the daily profit and hold bonus for an investment contract, based on the structure used by MinerDog.
Generated: DETERMINISTIC_ba3bdef52fdd2a0f
Batch ID: 20250612_155753
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
 * @title InvestmentProfitCalculator
 * @dev A contract function to calculate daily profit and hold bonus for an investment contract
 */
contract InvestmentProfitCalculator {
    // Struct to represent an investor
    struct Investor {
        uint256 investmentAmount; // Amount invested by the user
        uint256 lastWithdrawTimestamp; // Timestamp of the last withdrawal
    }

    // Constants representing the MinerDog structure
    uint256 public constant DAILY_PROFIT_PERCENTAGE = 5; // 5% daily profit
    uint256 public constant HOLD_BONUS_INCREMENT = 1; // 1% bonus per day hold
    uint256 public constant MAX_HOLD_BONUS_PERCENTAGE = 10; // Maximum hold bonus of 10%

    /**
     * @dev Calculates the daily profit and hold bonus for a given investor.
     * @param investor The investor data (investment amount and last withdrawal timestamp).
     * @return dailyProfit The calculated daily profit.
     * @return holdBonus The calculated hold bonus.
     */
    function calculateDailyProfitAndHoldBonus(Investor memory investor)
        public
        view
        returns (uint256 dailyProfit, uint256 holdBonus)
    {
        require(investor.investmentAmount > 0, "Investment amount must be greater than zero");

        // Calculate the daily profit
        dailyProfit = (investor.investmentAmount * DAILY_PROFIT_PERCENTAGE) / 100;

        // Calculate the number of days since the last withdrawal
        uint256 daysHeld = (block.timestamp - investor.lastWithdrawTimestamp) / 1 days;

        // Calculate the hold bonus, with a cap at MAX_HOLD_BONUS_PERCENTAGE
        holdBonus = daysHeld * HOLD_BONUS_INCREMENT;
        if (holdBonus > MAX_HOLD_BONUS_PERCENTAGE) {
            holdBonus = MAX_HOLD_BONUS_PERCENTAGE;
        }

        // Convert hold bonus percentage to value
        holdBonus = (investor.investmentAmount * holdBonus) / 100;
    }
}
```

This Solidity code adheres to your requirements for clean, efficient, well-documented, and production-ready code.
