"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Design a simple DeFi system using smart contracts, including functions for lending, borrowing, and interest calculation.
Generated: DETERMINISTIC_4c3d1be1d21e9f65
Batch ID: 20250622_211652
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

/**
 * @title DeFi Lending and Borrowing Smart Contract
 * @dev A simple decentralized finance system for lending, borrowing, and interest calculation.
 */
contract DeFiSystem {
    // Struct to represent a loan
    struct Loan {
        uint256 amount; // Loan amount
        uint256 interestRate; // Interest rate (in basis points, e.g., 500 = 5%)
        uint256 startTime; // Timestamp when the loan was issued
        bool isActive; // Whether the loan is active
    }

    // Mapping to store loans for each borrower
    mapping(address => Loan) public loans;

    // Event emitted when a loan is issued
    event LoanIssued(address indexed borrower, uint256 amount, uint256 interestRate);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Event emitted when funds are lent to the contract
    event FundsLent(address indexed lender, uint256 amount);

    // Contract balance to track available funds for lending
    uint256 public contractBalance;

    // Interest rate for lending (in basis points, e.g., 500 = 5%)
    uint256 public lendingInterestRate = 500;

    // Modifier to ensure the caller has an active loan
    modifier hasActiveLoan() {
        require(loans[msg.sender].isActive, "No active loan found");
        _;
    }

    /**
     * @dev Lend funds to the contract.
     * @param _amount The amount to lend.
     */
    function lendFunds(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value does not match the specified amount");
        require(_amount > 0, "Amount must be greater than zero");

        contractBalance += _amount;

        emit FundsLent(msg.sender, _amount);
    }

    /**
     * @dev Borrow funds from the contract.
     * @param _amount The amount to borrow.
     */
    function borrowFunds(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_amount <= contractBalance, "Insufficient contract balance");

        // Ensure the borrower does not already have an active loan
        require(!loans[msg.sender].isActive, "Borrower already has an active loan");

        // Issue the loan
        loans[msg.sender] = Loan({
            amount: _amount,
            interestRate: lendingInterestRate,
            startTime: block.timestamp,
            isActive: true
        });

        // Update contract balance
        contractBalance -= _amount;

        // Transfer funds to the borrower
        payable(msg.sender).transfer(_amount);

        emit LoanIssued(msg.sender, _amount, lendingInterestRate);
    }

    /**
     * @dev Repay the loan.
     */
    function repayLoan() external payable hasActiveLoan {
        Loan storage loan = loans[msg.sender];

        // Calculate the interest accrued
        uint256 timeElapsed = block.timestamp - loan.startTime;
        uint256 interest = (loan.amount * loan.interestRate * timeElapsed) / (365 days * 10000);

        uint256 totalRepayment = loan.amount + interest;

        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        // Update contract balance
        contractBalance += totalRepayment;

        // Mark the loan as repaid
        loan.isActive = false;

        emit LoanRepaid(msg.sender, totalRepayment);

        // Refund excess repayment if any
        if (msg.value > totalRepayment) {
            payable(msg.sender).transfer(msg.value - totalRepayment);
        }
    }

    /**
     * @dev Get the details of the caller's loan.
     * @return amount The loan amount.
     * @return interestRate The interest rate.
     * @return startTime The start time of the loan.
     * @return isActive Whether the loan is active.
     */
    function getLoanDetails()
        external
        view
        hasActiveLoan
        returns (
            uint256 amount,
            uint256 interestRate,
            uint256 startTime,
            bool isActive
        )
    {
        Loan memory loan = loans[msg.sender];
        return (loan.amount, loan.interestRate, loan.startTime, loan.isActive);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        contractBalance += msg.value;
    }
}
```
