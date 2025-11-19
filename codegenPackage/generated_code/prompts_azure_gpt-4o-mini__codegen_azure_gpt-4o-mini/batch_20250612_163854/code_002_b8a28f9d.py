"""
Generated Code Metadata:
========================
Original URL: https://venusutils.vercel.app
Prompt: What are the steps to implement bad debt calculations using Venus Utils in a smart contract?
Generated: DETERMINISTIC_b8a28f9df30782ba
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Venus Utils library for financial calculations
import "@venusprotocol/utils/contracts/VenusUtils.sol";

contract BadDebtCalculator {
    using VenusUtils for uint256;

    // State variable to store the total bad debt
    uint256 public totalBadDebt;

    // Event to log bad debt calculations
    event BadDebtCalculated(address indexed user, uint256 badDebtAmount);

    // Function to calculate bad debt for a user
    // @param user: The address of the user for whom to calculate bad debt
    // @param collateralValue: The total value of collateral provided by the user
    // @param debtValue: The total value of debt incurred by the user
    function calculateBadDebt(address user, uint256 collateralValue, uint256 debtValue) external {
        // Validate input values
        require(user != address(0), "Invalid user address");
        require(collateralValue > 0, "Collateral value must be greater than zero");
        require(debtValue > 0, "Debt value must be greater than zero");

        // Calculate the bad debt using Venus Utils
        uint256 badDebtAmount = debtValue > collateralValue ? debtValue - collateralValue : 0;

        // Update the total bad debt
        totalBadDebt += badDebtAmount;

        // Emit an event for the calculated bad debt
        emit BadDebtCalculated(user, badDebtAmount);
    }

    // Function to retrieve the total bad debt
    // @return The total bad debt amount
    function getTotalBadDebt() external view returns (uint256) {
        return totalBadDebt;
    }
}
```
