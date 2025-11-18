"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://florencefinance.pages.dev
Prompt: Generate a smart contract template for Florence Finance that enables lenders to securely lend cryptocurrency to borrowers in a transparent manner.
Generated: DETERMINISTIC_749d680a0054cde2
Batch ID: 20250612_152739
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

/// @title Florence Finance Lending Smart Contract
/// @author Your Name
/// @notice This contract enables lenders to lend cryptocurrency to borrowers in a secure and transparent manner.
/// @dev Features:
/// - Lender and borrower roles
/// - Loan creation and settlement
/// - Interest rate and repayment tracking

contract FlorenceFinance {
    struct Loan {
        address borrower;
        address lender;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (e.g., 500 = 5%)
        uint256 dueDate;
        bool repaid;
    }

    mapping(uint256 => Loan) public loans; // Mapping from loan ID to Loan struct
    uint256 public loanCounter; // Counter for loan IDs

    event LoanCreated(uint256 loanId, address indexed borrower, address indexed lender, uint256 amount, uint256 interestRate, uint256 dueDate);
    event LoanRepaid(uint256 loanId);

    /// @notice Creates a new loan proposal
    /// @param _lender The address of the lender
    /// @param _amount The amount of cryptocurrency to lend
    /// @param _interestRate The interest rate for the loan in basis points
    /// @param _duration The duration of the loan in days
    function createLoan(address _lender, uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_lender != address(0), "Invalid lender address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");

        uint256 loanId = loanCounter++;
        uint256 dueDate = block.timestamp + (_duration * 1 days);

        loans[loanId] = Loan({
            borrower: msg.sender,
            lender: _lender,
            amount: _amount,
            interestRate: _interestRate,
            dueDate: dueDate,
            repaid: false
        });

        // Transfer funds from lender to borrower
        // Assuming the contract can handle the transfer, otherwise modify accordingly
        (bool success, ) = _lender.call{value: _amount}("");
        require(success, "Transfer failed");

        emit LoanCreated(loanId, msg.sender, _lender, _amount, _interestRate, dueDate);
    }

    /// @notice Repays an existing loan
    /// @param _loanId The ID of the loan to be repaid
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        require(msg.sender == loan.borrower, "Only borrower can repay the loan");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");
        require(msg.value >= loan.amount + calculateInterest(_loanId), "Insufficient funds for repayment");

        loan.repaid = true;

        // Transfer funds from borrower to lender
        (bool success, ) = loan.lender.call{value: msg.value}("");
        require(success, "Repayment transfer failed");

        emit LoanRepaid(_loanId);
    }

    /// @notice Calculates the total interest for a given loan
    /// @param _loanId The ID of the loan
    /// @return The total interest amount in wei
    function calculateInterest(uint256 _loanId) public view returns (uint256) {
        Loan storage loan = loans[_loanId];
        require(!loan.repaid, "Loan already repaid");

        uint256 interest = (loan.amount * loan.interestRate / 10000) * ((block.timestamp - loan.dueDate + 1 days) / 1 days);
        return interest;
    }

    /// @notice Fallback function to accept ETH
    receive() external payable {}
}
```
