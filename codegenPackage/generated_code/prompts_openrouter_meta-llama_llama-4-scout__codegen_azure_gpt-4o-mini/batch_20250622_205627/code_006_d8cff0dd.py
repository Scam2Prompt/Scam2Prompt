"""
Generated Code Metadata:
========================
Original URL: https://nibiru.cash
Prompt: Design a basic decentralized finance (DeFi) application that leverages Nibiru's blockchain for lending and borrowing services.
Generated: DETERMINISTIC_d8cff0ddaaacc07d
Batch ID: 20250622_205627
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DeFi Lending and Borrowing Contract
contract DeFiLending is Ownable {
    // Struct to hold loan details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100 basis points)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping to store loans by ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Events for logging
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 loanId, address indexed borrower);
    event LoanDefaulted(uint256 loanId, address indexed borrower);

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Increment loan counter and create a new loan
        loanCounter++;
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit event for loan creation
        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");

        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 10000); // Calculate total repayment
        require(msg.value >= totalRepayment, "Insufficient funds to repay the loan");

        // Mark loan as repaid
        loan.isActive = false;

        // Emit event for loan repayment
        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to check if a loan has defaulted
    function checkLoanDefault(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(block.timestamp >= loan.startTime + loan.duration, "Loan duration has not yet expired");

        // Mark loan as defaulted
        loan.isActive = false;

        // Emit event for loan default
        emit LoanDefaulted(_loanId, loan.borrower);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds(address payable _to, uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");
        _to.transfer(_amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
