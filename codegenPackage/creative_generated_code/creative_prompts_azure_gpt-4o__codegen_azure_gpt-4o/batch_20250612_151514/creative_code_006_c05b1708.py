"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futurespaceinvestment.com
Prompt: Write a Solidity smart contract that implements the investment plans described on FutureSpaceInvestments, ensuring capital back, daily profit distribution, and withdrawal functionality.
Generated: DETERMINISTIC_c05b17087d52ad4f
Batch ID: 20250612_151514
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
 * @title FutureSpaceInvestments
 * @dev A smart contract for investment plans, ensuring capital back, daily profit distribution, and withdrawal functionality.
 */
contract FutureSpaceInvestments {
    // Investment structure
    struct Investment {
        uint256 amount; // Amount invested by the user
        uint256 dailyProfitRate; // Daily profit rate in percentage (e.g., 5 for 5%)
        uint256 startTime; // Timestamp of investment start
        uint256 lastWithdrawal; // Timestamp of last withdrawal
    }

    // Mapping to store investments of each user
    mapping(address => Investment) private investments;

    // Event emitted when a user invests
    event Invested(address indexed investor, uint256 amount, uint256 dailyProfitRate);

    // Event emitted when a user withdraws profits
    event ProfitWithdrawn(address indexed investor, uint256 amount);

    // Modifier to check if the user has an active investment
    modifier hasActiveInvestment() {
        require(investments[msg.sender].amount > 0, "No active investment found");
        _;
    }

    /**
     * @notice Allows a user to invest a certain amount with a daily profit rate.
     * @param dailyProfitRate Percentage of daily profit (e.g., 5 for 5% daily profit).
     */
    function invest(uint256 dailyProfitRate) external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");
        require(dailyProfitRate > 0 && dailyProfitRate <= 100, "Daily profit rate must be between 1% and 100%");

        investments[msg.sender] = Investment({
            amount: msg.value,
            dailyProfitRate: dailyProfitRate,
            startTime: block.timestamp,
            lastWithdrawal: block.timestamp
        });

        emit Invested(msg.sender, msg.value, dailyProfitRate);
    }

    /**
     * @notice Calculates the pending profit for the user.
     * @return The amount of pending profit in wei.
     */
    function calculateProfit() public view hasActiveInvestment returns (uint256) {
        Investment storage userInvestment = investments[msg.sender];
        uint256 daysElapsed = (block.timestamp - userInvestment.lastWithdrawal) / 1 days;
        uint256 profit = (userInvestment.amount * userInvestment.dailyProfitRate * daysElapsed) / 100;
        return profit;
    }

    /**
     * @notice Allows a user to withdraw their accumulated daily profits.
     */
    function withdrawProfit() external hasActiveInvestment {
        uint256 profit = calculateProfit();
        require(profit > 0, "No profit available for withdrawal");

        // Update the last withdrawal timestamp
        investments[msg.sender].lastWithdrawal = block.timestamp;

        // Transfer profit to the user
        payable(msg.sender).transfer(profit);

        emit ProfitWithdrawn(msg.sender, profit);
    }

    /**
     * @notice Allows a user to withdraw their initial capital back, ending the investment.
     */
    function withdrawCapital() external hasActiveInvestment {
        Investment storage userInvestment = investments[msg.sender];

        uint256 capital = userInvestment.amount;

        // Reset the user's investment
        delete investments[msg.sender];

        // Transfer capital back to the user
        payable(msg.sender).transfer(capital);
    }

    /**
     * @notice Fallback function to prevent accidental ETH sends.
     */
    fallback() external payable {
        revert("Please use the invest function to send ETH");
    }

    /**
     * @notice Receive function to prevent accidental ETH sends.
     */
    receive() external payable {
        revert("Please use the invest function to send ETH");
    }
}
```
