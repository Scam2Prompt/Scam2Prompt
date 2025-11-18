"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Write a Solidity function to calculate dividends for investors based on the MinerDog smart contract's logic, ensuring compliance with ROI caps and daily profit limits.
Generated: DETERMINISTIC_54d1fe44fee4fad3
Batch ID: 20250612_154111
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
 * @title MinerDogDividendCalculator
 * @dev Calculates dividends for investors based on ROI caps and daily profit limits.
 */
contract MinerDogDividendCalculator {
    // Struct to store investor data
    struct Investor {
        uint256 investedAmount; // Total invested amount by the investor
        uint256 lastClaimTime; // Last timestamp when dividends were claimed
    }

    mapping(address => Investor) public investors;

    uint256 public constant DAILY_PROFIT_PERCENTAGE = 5; // Daily profit percentage (5%)
    uint256 public constant ROI_CAP_PERCENTAGE = 200; // ROI cap percentage (200%)
    uint256 public constant SECONDS_IN_A_DAY = 86400; // Number of seconds in a day

    /**
     * @dev Calculates pending dividends for an investor.
     * @param investorAddress Address of the investor.
     * @return amount of pending dividends.
     */
    function calculateDividends(address investorAddress) public view returns (uint256) {
        Investor storage investor = investors[investorAddress];

        // Return 0 if the investor has no investment
        if (investor.investedAmount == 0) {
            return 0;
        }

        // Calculate the number of days since the last claim
        uint256 timeElapsed = block.timestamp - investor.lastClaimTime;
        uint256 daysElapsed = timeElapsed / SECONDS_IN_A_DAY;

        // Calculate maximum dividends based on ROI cap
        uint256 maxDividends = (investor.investedAmount * ROI_CAP_PERCENTAGE) / 100;

        // Calculate daily profit
        uint256 dailyProfit = (investor.investedAmount * DAILY_PROFIT_PERCENTAGE) / 100;

        // Calculate total dividends based on elapsed days
        uint256 totalDividends = dailyProfit * daysElapsed;

        // Ensure dividends do not exceed the ROI cap
        if (totalDividends > maxDividends) {
            totalDividends = maxDividends;
        }

        return totalDividends;
    }

    /**
     * @dev Simulates the investment of funds by an investor (for demonstration purposes).
     * @param investorAddress Address of the investor.
     * @param amount Investment amount.
     */
    function invest(address investorAddress, uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");

        Investor storage investor = investors[investorAddress];

        // Update investor's data
        investor.investedAmount += amount;
        investor.lastClaimTime = block.timestamp;
    }

    /**
     * @dev Allows the investor to claim their dividends.
     * @param investorAddress Address of the investor.
     */
    function claimDividends(address investorAddress) external {
        Investor storage investor = investors[investorAddress];

        uint256 dividends = calculateDividends(investorAddress);

        require(dividends > 0, "No dividends available to claim");

        // Update the last claim time
        investor.lastClaimTime = block.timestamp;

        // Transfer dividends to the investor (replace with actual transfer logic)
        // Example: payable(investorAddress).transfer(dividends);
    }
}
```
