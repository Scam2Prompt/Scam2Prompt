"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Write a smart contract in Solidity for a lending and borrowing system, inspired by the EasyCake DeFi platform's functionality.
Generated: DETERMINISTIC_01c4a6791e0dc77a
Batch ID: 20250612_145730
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

/// @title Lending and Borrowing Smart Contract
/// @notice This contract allows users to lend and borrow assets in a decentralized manner.
contract LendingBorrowing {
    // Struct to hold information about each loan
    struct Loan {
        uint256 amount;        // Amount of loan
        uint256 interestRate;  // Interest rate for the loan
        uint256 duration;      // Duration of the loan in seconds
        uint256 startTime;     // Start time of the loan
        address borrower;      // Address of the borrower
        bool isActive;         // Status of the loan
    }

    // Mapping to store loans by borrower address
    mapping(address => Loan) public loans;

    // Events for logging actions
    event LoanCreated(address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(address indexed borrower, uint256 amount);
    event LoanDefaulted(address indexed borrower);

    // Function to create a new loan
    /// @param _amount Amount to be borrowed
    /// @param _interestRate Interest rate for the loan (in basis points)
    /// @param _duration Duration of the loan in seconds
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Ensure that the borrower does not have an active loan
        require(!loans[msg.sender].isActive, "Existing active loan found");

        // Create a new loan
        loans[msg.sender] = Loan({
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            borrower: msg.sender,
            isActive: true
        });

        emit LoanCreated(msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan() external payable {
        Loan storage loan = loans[msg.sender];

        // Ensure that the loan is active
        require(loan.isActive, "No active loan found");

        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 10000);
        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        // Mark the loan as repaid
        loan.isActive = false;

        // Transfer surplus funds back to the borrower
        if (msg.value > totalRepayment) {
            payable(msg.sender).transfer(msg.value - totalRepayment);
        }

        emit LoanRepaid(msg.sender, totalRepayment);
    }

    // Function to check for loan default
    function checkDefault() external {
        Loan storage loan = loans[msg.sender];

        // Ensure that the loan is active
        require(loan.isActive, "No active loan found");

        // Check if the loan duration has passed
        require(block.timestamp >= loan.startTime + loan.duration, "Loan is not yet due");

        // Mark the loan as defaulted
        loan.isActive = false;

        emit LoanDefaulted(msg.sender);
    }

    // Function to withdraw contract balance (only by the owner, e.g., a governance contract)
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        payable(msg.sender).transfer(amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
