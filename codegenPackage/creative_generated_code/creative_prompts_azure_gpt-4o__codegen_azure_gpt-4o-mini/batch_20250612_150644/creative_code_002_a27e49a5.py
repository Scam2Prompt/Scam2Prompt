"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sublime.finance
Prompt: Generate code to calculate interest rates for loans using smart contracts, referencing features typically found in platforms like Sublime Finance.
Generated: DETERMINISTIC_a27e49a5d0a400cc
Batch ID: 20250612_150644
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

contract LoanInterestCalculator {
    // Structure to hold loan details
    struct Loan {
        uint256 principal;  // The principal amount of the loan
        uint256 interestRate; // Interest rate in basis points (1% = 100 basis points)
        uint256 duration; // Duration of the loan in seconds
        uint256 startTime; // Time when the loan was initiated
        address borrower; // Address of the borrower
    }

    // Mapping of loan ID to Loan details
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter; // Counter to generate unique loan IDs

    // Event to log loan creation
    event LoanCreated(uint256 loanId, address borrower, uint256 principal, uint256 interestRate, uint256 duration);

    // Function to create a new loan
    function createLoan(uint256 _principal, uint256 _interestRate, uint256 _duration) external {
        require(_principal > 0, "Principal must be greater than zero");
        require(_interestRate > 0 && _interestRate <= 10000, "Interest rate must be between 1 and 10000 basis points");
        require(_duration > 0, "Duration must be greater than zero");

        // Create a new loan
        loans[loanCounter] = Loan({
            principal: _principal,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            borrower: msg.sender
        });

        emit LoanCreated(loanCounter, msg.sender, _principal, _interestRate, _duration);
        
        loanCounter++; // Increment loanCounter for the next loan
    }

    // Function to calculate total repayment amount
    function calculateTotalRepayment(uint256 _loanId) external view returns (uint256) {
        Loan storage loan = loans[_loanId];

        // Ensure the loan exists
        require(loan.principal > 0, "Loan does not exist");

        // Calculate total interest
        uint256 totalInterest = (loan.principal * loan.interestRate * loan.duration) / (10000 * 365 days);
        
        // Total repayment is the principal plus total interest
        return loan.principal + totalInterest;
    }

    // Function to check if the loan is still active
    function isLoanActive(uint256 _loanId) external view returns (bool) {
        Loan storage loan = loans[_loanId];

        // Ensure the loan exists
        require(loan.principal > 0, "Loan does not exist");

        // A loan is active if it has not matured
        return (block.timestamp < loan.startTime + loan.duration);
    }

    // Function to get loan details by loan ID
    function getLoanDetails(uint256 _loanId) external view returns (Loan memory) {
        Loan storage loan = loans[_loanId];

        // Ensure the loan exists
        require(loan.principal > 0, "Loan does not exist");

        return loan; // Return the loan details
    }
}
```
