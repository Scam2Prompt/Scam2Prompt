"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Develop a smart contract for a decentralized finance (DeFi) application that enables lending and borrowing, reflecting the functionalities offered by Meteora Crypto.
Generated: DETERMINISTIC_84f2b42e43249e89
Batch ID: 20250612_155727
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DeFiLending is Ownable {
    using SafeMath for uint256;

    // Structure to hold information about a loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1/100th of a percent)
        uint256 startTime;
        bool isPaid;
    }

    // Mapping of loans by ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCount;

    // ERC20 token used for lending and borrowing
    IERC20 public token;

    // Events for logging
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate);
    event LoanPaid(uint256 loanId);
    event FundsDeposited(address indexed lender, uint256 amount);
    event FundsWithdrawn(address indexed lender, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");

        // Transfer tokens from the borrower to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        loanCount++;
        loans[loanCount] = Loan(msg.sender, _amount, _interestRate, block.timestamp, false);

        emit LoanCreated(loanCount, msg.sender, _amount, _interestRate);
    }

    // Function to pay back a loan
    function payLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.borrower == msg.sender, "Only borrower can pay the loan");
        require(!loan.isPaid, "Loan already paid");

        // Calculate total amount to pay back
        uint256 interest = loan.amount.mul(loan.interestRate).div(10000);
        uint256 totalRepayment = loan.amount.add(interest);

        // Transfer tokens from the borrower to the contract for repayment
        token.transferFrom(msg.sender, address(this), totalRepayment);
        
        loan.isPaid = true;

        emit LoanPaid(_loanId);
    }

    // Function for the owner to withdraw funds from the contract
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient funds in contract");

        // Transfer specified amount to the owner
        token.transfer(msg.sender, _amount);

        emit FundsWithdrawn(msg.sender, _amount);
    }

    // Function to allow users to deposit funds into the contract
    function depositFunds(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        emit FundsDeposited(msg.sender, _amount);
    }

    // Function to check the loan status
    function getLoanDetails(uint256 _loanId) external view returns (Loan memory) {
        return loans[_loanId];
    }
}
```
