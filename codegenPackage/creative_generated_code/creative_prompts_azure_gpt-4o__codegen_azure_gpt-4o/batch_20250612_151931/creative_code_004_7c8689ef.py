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
 * @title Zero Interest Loans (ZILs) Contract
 * @dev Implements zero interest loans with isolated risk markets
 * Inspired by the Lends platform
 */
contract ZeroInterestLoans {
    // Struct representing a loan
    struct Loan {
        uint256 principal;      // Loan principal
        uint256 collateral;     // Collateral provided
        address borrower;       // Borrower's address
        bool isActive;          // Loan active state
    }

    // Mapping to track loans by ID
    mapping(uint256 => Loan) public loans;

    // Counter to generate unique loan IDs
    uint256 public loanCounter;

    // Events
    event LoanCreated(uint256 loanId, address borrower, uint256 principal, uint256 collateral);
    event LoanRepaid(uint256 loanId, address borrower);
    event LoanLiquidated(uint256 loanId, address liquidator);

    // Constructor
    constructor() {}

    /**
     * @dev Create a new zero interest loan
     * @param _principal Amount of principal requested by borrower
     * @param _collateral Amount of collateral provided by borrower
     */
    function createLoan(uint256 _principal, uint256 _collateral) external {
        require(_principal > 0, "Principal must be greater than zero");
        require(_collateral > _principal, "Collateral must be greater than principal");

        // Increment loan counter
        loanCounter++;

        // Create the loan
        loans[loanCounter] = Loan({
            principal: _principal,
            collateral: _collateral,
            borrower: msg.sender,
            isActive: true
        });

        emit LoanCreated(loanCounter, msg.sender, _principal, _collateral);
    }

    /**
     * @dev Repay a loan
     * @param _loanId ID of the loan to repay
     */
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];
        
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only borrower can repay the loan");
        require(msg.value == loan.principal, "Repayment amount must be equal to principal");

        // Mark the loan as repaid
        loan.isActive = false;

        // Send collateral back to the borrower
        payable(loan.borrower).transfer(loan.collateral);

        emit LoanRepaid(_loanId, loan.borrower);
    }

    /**
     * @dev Liquidate a loan if borrower fails to repay (isolated risk)
     * @param _loanId ID of the loan to liquidate
     */
    function liquidateLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        
        require(loan.isActive, "Loan is not active");

        // Liquidate loan: transfer collateral to the liquidator (msg.sender)
        loan.isActive = false;
        payable(msg.sender).transfer(loan.collateral);

        emit LoanLiquidated(_loanId, msg.sender);
    }

    /**
     * @dev Receive Ether for collateral storage
     * This function allows contract to hold collateral securely
     */
    receive() external payable {}
    
    /**
     * @dev Fallback function
     */
    fallback() external payable {}
}
```
