"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gicoin.trade
Prompt: Develop a smart contract in Solidity that mirrors GIC's tailored financial solutions for diverse global investment needs.
Generated: DETERMINISTIC_26dc48b50aa24e74
Batch ID: 20250612_150426
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

/// @title GIC Financial Solutions Smart Contract
/// @author Your Name
/// @notice This contract allows users to invest in tailored financial solutions
/// @dev This is a simplified representation for demonstration purposes

contract GICFinancialSolutions {
    // Struct to hold investment details
    struct Investment {
        uint256 amount;         // Amount invested
        uint256 startTime;      // Investment start time
        uint256 duration;       // Investment duration in seconds
        uint256 interestRate;   // Annual interest rate in basis points (1/100th of a percent)
        bool isActive;          // Investment status
    }

    // Mapping from user addresses to their investments
    mapping(address => Investment) private investments;

    // Event to log investment creation
    event InvestmentCreated(address indexed investor, uint256 amount, uint256 duration, uint256 interestRate);

    // Event to log investment withdrawal
    event InvestmentWithdrawn(address indexed investor, uint256 amount, uint256 interestEarned);

    /// @notice Create a new investment
    /// @param _duration Duration of the investment in seconds
    /// @param _interestRate Annual interest rate in basis points
    /// @dev Requires a non-zero amount to invest
    function createInvestment(uint256 _duration, uint256 _interestRate) external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");
        require(investments[msg.sender].isActive == false, "Existing active investment found");

        // Create the investment
        investments[msg.sender] = Investment({
            amount: msg.value,
            startTime: block.timestamp,
            duration: _duration,
            interestRate: _interestRate,
            isActive: true
        });

        // Emit an event for the investment creation
        emit InvestmentCreated(msg.sender, msg.value, _duration, _interestRate);
    }

    /// @notice Withdraw investment along with earned interest
    /// @dev Only allowed after the investment duration has elapsed
    function withdrawInvestment() external {
        Investment storage investment = investments[msg.sender];

        require(investment.isActive, "No active investment found");
        require(block.timestamp >= investment.startTime + investment.duration, "Investment duration not yet elapsed");

        // Calculate interest earned
        uint256 interestEarned = (investment.amount * investment.interestRate * investment.duration) / (365 days * 10000);
        uint256 totalAmount = investment.amount + interestEarned;

        // Mark investment as inactive
        investment.isActive = false;

        // Transfer total amount back to investor
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        // Emit an event for the withdrawal
        emit InvestmentWithdrawn(msg.sender, investment.amount, interestEarned);
    }

    /// @notice Get investment details for the caller
    /// @return amount Amount invested
    /// @return startTime Investment start time
    /// @return duration Investment duration in seconds
    /// @return interestRate Annual interest rate in basis points
    /// @return isActive Investment status
    function getInvestmentDetails() external view returns (uint256 amount, uint256 startTime, uint256 duration, uint256 interestRate, bool isActive) {
        Investment storage investment = investments[msg.sender];
        return (investment.amount, investment.startTime, investment.duration, investment.interestRate, investment.isActive);
    }
}
```
