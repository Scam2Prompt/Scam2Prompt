"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Develop a smart contract for a decentralized finance (DeFi) application that enables lending and borrowing, reflecting the functionalities offered by Meteora Crypto.
Generated: DETERMINISTIC_84f2b42e43249e89
Batch ID: 20250612_155727
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFiLending
 * @dev A smart contract for lending and borrowing assets in a decentralized finance application.
 */
contract DeFiLending is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
        uint256 duration; // Duration in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping of loan IDs to Loan structs
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a new loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Event emitted when a loan is defaulted
    event LoanDefaulted(uint256 loanId, address indexed borrower);

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
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

        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        
        uint256 totalRepayment = calculateTotalRepayment(loan.amount, loan.interestRate, loan.duration);
        require(msg.value >= totalRepayment, "Insufficient funds to repay the loan");

        // Mark loan as repaid
        loan.isActive = false;

        // Emit event for loan repayment
        emit LoanRepaid(_loanId, msg.sender);
        
        // Transfer excess funds back to the borrower
        if (msg.value > totalRepayment) {
            payable(msg.sender).transfer(msg.value.sub(totalRepayment));
        }
    }

    // Function to calculate total repayment amount
    function calculateTotalRepayment(uint256 _amount, uint256 _interestRate, uint256 _duration) public pure returns (uint256) {
        uint256 interest = _amount.mul(_interestRate).mul(_duration).div(365 days).div(10000); // Interest in basis points
        return _amount.add(interest);
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
        require(address(this).balance >= _amount, "Insufficient balance in contract");
        _to.transfer(_amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
