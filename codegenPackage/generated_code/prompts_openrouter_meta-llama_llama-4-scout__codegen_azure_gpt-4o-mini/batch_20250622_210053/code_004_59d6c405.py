"""
Generated Code Metadata:
========================
Original URL: https://auroraplus.pages.dev
Prompt: Develop a simple lending and borrowing smart contract on Aurora+, using a programming language like Rust or Solidity.
Generated: DETERMINISTIC_59d6c405a3b160b4
Batch ID: 20250622_210053
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

/// @title Simple Lending and Borrowing Smart Contract
/// @author Your Name
/// @notice This contract allows users to lend and borrow tokens
/// @dev This contract is designed for educational purposes and may require further security audits for production use

contract LendingBorrowing {
    // Struct to hold information about each loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
        uint256 duration; // Duration of the loan in seconds
        uint256 startTime; // Timestamp when the loan was taken
        bool isActive; // Status of the loan
    }

    // Mapping to store loans by their ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter; // Counter to keep track of loan IDs

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Function to create a new loan
    /// @param _amount The amount of tokens to lend
    /// @param _interestRate The interest rate for the loan in basis points
    /// @param _duration The duration of the loan in seconds
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Create a new loan
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
        loanCounter++;
    }

    // Function to repay a loan
    /// @param _loanId The ID of the loan to repay
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 10000); // Calculate total repayment amount

        require(msg.value >= totalRepayment, "Insufficient funds to repay the loan");

        // Mark the loan as repaid
        loan.isActive = false;

        // Transfer the repayment amount to the contract owner (or lender)
        payable(address(this)).transfer(totalRepayment);

        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to withdraw funds from the contract (for the lender)
    function withdraw() external {
        // Only the contract owner should be able to withdraw funds
        require(msg.sender == address(this), "Only the contract can withdraw funds");
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept incoming Ether
    receive() external payable {}
}
```
