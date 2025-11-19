"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiethereum.com
Prompt: Write a smart contract in Solidity for a decentralized lending platform on Ethereum.
Generated: DETERMINISTIC_2993ebeae66cd860
Batch ID: 20250612_135940
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
 * @title Decentralized Lending Platform
 * @notice A smart contract that allows users to lend and borrow assets in a decentralized manner.
 */
contract LendingPlatform {
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (e.g., 500 = 5%)
        uint256 dueDate;
        bool isPaid;
    }

    address public owner;
    uint256 public totalLoans;
    mapping(uint256 => Loan) public loans;

    // Events for logging
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 dueDate);
    event LoanRepaid(uint256 loanId, address indexed borrower);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier loanExists(uint256 loanId) {
        require(loanId < totalLoans, "Loan does not exist");
        _;
    }

    modifier loanNotPaid(uint256 loanId) {
        require(!loans[loanId].isPaid, "Loan has already been paid");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Create a new loan
     * @param _amount Amount of the loan
     * @param _interestRate Interest rate in basis points
     * @param _duration Duration in days until the loan is due
     */
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external onlyOwner {
        require(_amount > 0, "Loan amount must be greater than 0");
        require(_interestRate > 0, "Interest rate must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        uint256 loanId = totalLoans++;
        uint256 dueDate = block.timestamp + (_duration * 1 days);

        loans[loanId] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            dueDate: dueDate,
            isPaid: false
        });

        emit LoanCreated(loanId, msg.sender, _amount, _interestRate, dueDate);
    }

    /**
     * @notice Repay a loan
     * @param loanId ID of the loan to repay
     */
    function repayLoan(uint256 loanId) external payable loanExists(loanId) loanNotPaid(loanId) {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");
        require(msg.value == loan.amount + calculateInterest(loan.amount, loan.interestRate), "Incorrect repayment amount");

        loan.isPaid = true;

        // Transfer funds to the owner (lender)
        payable(owner).transfer(msg.value);

        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @notice Calculate interest based on the principal and interest rate
     * @param principal The principal amount
     * @param interestRate The interest rate in basis points
     * @return The interest amount
     */
    function calculateInterest(uint256 principal, uint256 interestRate) public pure returns (uint256) {
        return (principal * interestRate) / 10000; // Basis points to percentage
    }

    /**
     * @notice Get loan details
     * @param loanId ID of the loan
     * @return The details of the loan
     */
    function getLoanDetails(uint256 loanId) external view loanExists(loanId) returns (Loan memory) {
        return loans[loanId];
    }

    /**
     * @notice Fallback function to prevent ether being sent directly to the contract
     */
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
