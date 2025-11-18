"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty-financial.io
Prompt: Create a smart contract in Solidity to facilitate borrowing crypto using the WLF protocol.
Generated: DETERMINISTIC_83a70b5aeed7b1f8
Batch ID: 20250612_153848
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for borrowing crypto using the WLF protocol
contract WLFProtocol is Ownable {
    // Struct to represent a loan
    struct Loan {
        uint256 amount;
        uint256 interestRate; // in basis points
        uint256 duration; // loan duration in seconds
        uint256 startTime;
        address borrower;
        bool isActive;
    }

    // Events for logging loan activities
    event LoanCreated(uint256 indexed loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 indexed loanId, address indexed borrower, uint256 amount);
    event LoanDefaulted(uint256 indexed loanId, address indexed borrower);

    // Mapping of loans by their IDs
    mapping(uint256 => Loan) private loans;
    uint256 public nextLoanId;

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external onlyOwner {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be positive");
        require(_duration > 0, "Duration must be greater than zero");

        loans[nextLoanId] = Loan({
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            borrower: msg.sender,
            isActive: true
        });

        emit LoanCreated(nextLoanId, msg.sender, _amount, _interestRate, _duration);
        nextLoanId++;
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate) / 10000; // calculating total repayment
        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        loan.isActive = false; // Mark loan as repaid
        emit LoanRepaid(_loanId, msg.sender, totalRepayment);

        // Transfer the funds to the contract owner (lender)
        payable(owner()).transfer(totalRepayment);
    }

    // Function to check loan status
    function checkLoanStatus(uint256 _loanId) external view returns (Loan memory) {
        return loans[_loanId];
    }

    // Function to handle loan defaults
    function handleDefault(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(block.timestamp > loan.startTime + loan.duration, "Loan duration has not expired");

        loan.isActive = false; // Mark loan as defaulted
        emit LoanDefaulted(_loanId, loan.borrower);
    }
}
```
