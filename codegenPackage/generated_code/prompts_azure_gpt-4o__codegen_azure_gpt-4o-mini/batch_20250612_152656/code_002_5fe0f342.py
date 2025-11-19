"""
Generated Code Metadata:
========================
Original URL: https://claim-stu.pages.dev
Prompt: Generate a smart contract template for an isolated lending system with shared liquidity, ensuring it meets security standards like those audited by Immunefi.
Generated: DETERMINISTIC_5fe0f3423e14bc92
Batch ID: 20250612_152656
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Isolated Lending System with Shared Liquidity
 * @dev This contract allows users to lend and borrow assets in an isolated manner while sharing liquidity.
 */
contract IsolatedLending is Ownable, ReentrancyGuard {
    // Struct to hold lending information
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1/100th of a percent)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping of loan IDs to Loan structs
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Event emitted when a loan is defaulted
    event LoanDefaulted(uint256 loanId, address indexed borrower);

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Increment loan counter to create a unique loan ID
        loanCounter++;

        // Create a new loan
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit loan creation event
        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external nonReentrant {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate) / 10000;

        // Transfer the repayment amount from borrower to the contract
        // Assuming the contract has been approved to spend the borrower's tokens
        IERC20 token = IERC20(address(this)); // Replace with actual token address
        require(token.transferFrom(msg.sender, address(this), totalRepayment), "Transfer failed");

        // Mark loan as repaid
        loan.isActive = false;

        // Emit loan repayment event
        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to check if a loan has defaulted
    function checkLoanStatus(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(block.timestamp > loan.startTime + loan.duration, "Loan duration has not expired");

        // Mark loan as defaulted
        loan.isActive = false;

        // Emit loan default event
        emit LoanDefaulted(_loanId, loan.borrower);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient balance");

        payable(_to).transfer(_amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
