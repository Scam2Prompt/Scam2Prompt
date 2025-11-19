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

/// @title Investment Contract with Daily Profit and Hold Bonus
/// @notice This contract calculates daily profits and hold bonuses for investors.
contract MinerDogInvestment {

    // Struct to represent an investor
    struct Investor {
        uint256 investmentAmount; // Amount invested by the investor
        uint256 lastWithdrawTimestamp; // Last time the investor withdrew profits
        uint256 totalProfit; // Total profit earned by the investor
        uint256 holdBonus; // Bonus for holding their investment
    }

    mapping(address => Investor) public investors; // Mapping of investors
    uint256 public constant DAILY_PROFIT_RATE = 10; // Daily profit rate in percentage
    uint256 public constant HOLD_BONUS_RATE = 5; // Hold bonus rate in percentage
    uint256 public constant SECONDS_IN_A_DAY = 86400; // Number of seconds in a day

    /// @notice Allows an investor to make an investment
    /// @param _amount The amount to invest
    function invest(uint256 _amount) external payable {
        require(msg.value == _amount, "Investment amount must match sent value");
        require(_amount > 0, "Investment must be greater than 0");

        // If the investor is new, initialize their data
        if (investors[msg.sender].investmentAmount == 0) {
            investors[msg.sender] = Investor({
                investmentAmount: _amount,
                lastWithdrawTimestamp: block.timestamp,
                totalProfit: 0,
                holdBonus: 0
            });
        } else {
            // Update existing investor's investment amount
            investors[msg.sender].investmentAmount += _amount;
        }
    }

    /// @notice Withdraws profits and calculates hold bonuses
    function withdrawProfit() external {
        Investor storage investor = investors[msg.sender];
        require(investor.investmentAmount > 0, "No investment found");

        uint256 dailyProfit = calculateDailyProfit(investor);
        uint256 holdBonus = calculateHoldBonus(investor);

        // Update total profit and hold bonus
        investor.totalProfit += dailyProfit + holdBonus;
        investor.lastWithdrawTimestamp = block.timestamp;

        // Transfer the total profit to the investor
        payable(msg.sender).transfer(dailyProfit + holdBonus);
    }

    /// @notice Calculates daily profit based on the investment amount
    /// @param _investor The investor whose profit is being calculated
    /// @return The calculated daily profit
    function calculateDailyProfit(Investor storage _investor) internal view returns (uint256) {
        uint256 daysPassed = (block.timestamp - _investor.lastWithdrawTimestamp) / SECONDS_IN_A_DAY;
        return (_investor.investmentAmount * DAILY_PROFIT_RATE * daysPassed) / 100;
    }

    /// @notice Calculates hold bonus for the investor
    /// @param _investor The investor whose hold bonus is being calculated
    /// @return The calculated hold bonus
    function calculateHoldBonus(Investor storage _investor) internal view returns (uint256) {
        uint256 holdDuration = block.timestamp - _investor.lastWithdrawTimestamp;
        uint256 bonusDays = holdDuration / SECONDS_IN_A_DAY;
        return (_investor.investmentAmount * HOLD_BONUS_RATE * bonusDays) / 100;
    }
}
```
