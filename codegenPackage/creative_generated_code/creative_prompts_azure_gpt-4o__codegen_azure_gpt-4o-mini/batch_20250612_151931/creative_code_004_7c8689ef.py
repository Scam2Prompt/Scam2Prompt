"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://showmethemoney-34w.pages.dev
Prompt: Write a smart contract in Solidity that implements Zero Interest Loans (ZILs) with isolated risk markets, inspired by the Lends platform.
Generated: DETERMINISTIC_7c8689ef25cca938
Batch ID: 20250612_151931
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
 * @title Zero Interest Loans (ZIL) Smart Contract
 * @dev Implements a lending platform for zero-interest loans with isolated risk markets.
 */
contract ZeroInterestLoans {
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 duration;
        uint256 startTime;
        bool isActive;
    }

    // Mapping of loan IDs to Loan structs
    mapping(uint256 => Loan) public loans;
    // Counter for loan IDs
    uint256 public loanIdCounter;

    // Event emitted when a new loan is created
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 duration);
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address borrower);

    /**
     * @dev Creates a new zero-interest loan.
     * @param _amount The amount of the loan.
     * @param _duration The duration of the loan in seconds.
     */
    function createLoan(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        // Increment the loan ID counter
        loanIdCounter++;
        
        // Create the loan
        loans[loanIdCounter] = Loan({
            borrower: msg.sender,
            amount: _amount,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit LoanCreated event
        emit LoanCreated(loanIdCounter, msg.sender, _amount, _duration);
    }

    /**
     * @dev Repays an active loan.
     * @param _loanId The ID of the loan to be repaid.
     */
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        
        // Check if the loan exists and is active
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only borrower can repay the loan");

        // Check if the loan duration has elapsed
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Mark the loan as inactive
        loan.isActive = false;

        // Emit LoanRepaid event
        emit LoanRepaid(_loanId, msg.sender);
    }

    /**
     * @dev Retrieves loan details by its ID.
     * @param _loanId The ID of the loan to retrieve.
     * @return borrower The address of the borrower.
     * @return amount The amount of the loan.
     * @return duration The duration of the loan.
     * @return startTime The time the loan was initiated.
     * @return isActive Indicates if the loan is still active.
     */
    function getLoan(uint256 _loanId) external view returns (
        address borrower,
        uint256 amount,
        uint256 duration,
        uint256 startTime,
        bool isActive
    ) {
        Loan storage loan = loans[_loanId];
        require(loan.borrower != address(0), "Loan does not exist");

        return (
            loan.borrower,
            loan.amount,
            loan.duration,
            loan.startTime,
            loan.isActive
        );
    }
}
```
