"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Create a smart contract in Solidity for managing fixed-term deposits and payouts, inspired by the roadmap features mentioned on profitproinvest.com.
Generated: DETERMINISTIC_923986c1395d560f
Batch ID: 20250612_150119
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

/// @title Fixed Term Deposit Smart Contract
/// @notice This contract allows users to create fixed-term deposits with specified interest rates and terms.
/// @dev Users can deposit funds, and after the term, they can withdraw their deposits along with the interest earned.

contract FixedTermDeposit {
    struct Deposit {
        uint256 amount;        // Amount deposited
        uint256 startTime;     // Start time of the deposit
        uint256 term;          // Term in seconds
        uint256 interestRate;  // Interest rate in basis points (1/100 of a percent)
        bool withdrawn;        // Flag to indicate if the deposit has been withdrawn
    }
    
    mapping(address => Deposit) private deposits; // Mapping from user address to their deposit
    uint256 public totalDeposits;                  // Total amount of deposits in the contract

    event DepositCreated(address indexed user, uint256 amount, uint256 term, uint256 interestRate);
    event DepositWithdrawn(address indexed user, uint256 amount, uint256 interest);
    
    /// @notice Allows users to create a fixed-term deposit
    /// @param _term Duration of the deposit in seconds
    /// @param _interestRate Interest rate in basis points
    function createDeposit(uint256 _term, uint256 _interestRate) external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        require(deposits[msg.sender].amount == 0, "Existing deposit found. Withdraw first.");

        deposits[msg.sender] = Deposit({
            amount: msg.value,
            startTime: block.timestamp,
            term: _term,
            interestRate: _interestRate,
            withdrawn: false
        });

        totalDeposits += msg.value;

        emit DepositCreated(msg.sender, msg.value, _term, _interestRate);
    }

    /// @notice Allows users to withdraw their deposits along with interest after the term
    function withdrawDeposit() external {
        Deposit storage userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No deposit found.");
        require(!userDeposit.withdrawn, "Deposit already withdrawn.");
        require(block.timestamp >= userDeposit.startTime + userDeposit.term, "Deposit term not yet completed.");

        uint256 interest = calculateInterest(userDeposit.amount, userDeposit.interestRate, userDeposit.term);
        uint256 totalAmount = userDeposit.amount + interest;

        userDeposit.withdrawn = true; // Mark as withdrawn
        totalDeposits -= userDeposit.amount; // Update total deposits

        // Transfer total amount to the user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed.");

        emit DepositWithdrawn(msg.sender, userDeposit.amount, interest);
    }

    /// @notice Calculates the interest for a given deposit
    /// @param _principal The principal amount deposited
    /// @param _interestRate The interest rate in basis points
    /// @param _term The duration of the deposit in seconds
    /// @return The calculated interest
    function calculateInterest(uint256 _principal, uint256 _interestRate, uint256 _term) private pure returns (uint256) {
        return (_principal * _interestRate * _term) / (10000 * 365 * 24 * 60 * 60); // Annualized interest calculation
    }

    /// @notice Allows the contract to receive Ether
    receive() external payable {}

    /// @notice Fallback function to revert any unintended Ether transfers
    fallback() external {
        revert("Invalid function call");
    }
}
```
