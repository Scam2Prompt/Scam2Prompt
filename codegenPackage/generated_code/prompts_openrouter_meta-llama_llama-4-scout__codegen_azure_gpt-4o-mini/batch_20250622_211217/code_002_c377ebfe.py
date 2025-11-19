"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Design a smart contract for a new DeFi lending platform inspired by Extra Finance's lending solutions.
Generated: DETERMINISTIC_c377ebfedc92f71a
Batch ID: 20250622_211217
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

// @title DeFi Lending Platform
// @notice This contract allows users to lend and borrow ERC20 tokens
contract DeFiLendingPlatform is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100 basis points)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping to store loans by their ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a new loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Function to create a new loan
    // @param _amount The amount of tokens to lend
    // @param _interestRate The interest rate for the loan in basis points
    // @param _duration The duration of the loan in seconds
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the borrower to the contract
        IERC20 token = IERC20(msg.sender);
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

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
        loanCounter++;
    }

    // Function to repay a loan
    // @param _loanId The ID of the loan to repay
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount.add(loan.amount.mul(loan.interestRate).div(10000));

        // Transfer tokens from the borrower to the contract
        IERC20 token = IERC20(msg.sender);
        require(token.transferFrom(msg.sender, address(this), totalRepayment), "Token transfer failed");

        // Mark the loan as repaid
        loan.isActive = false;

        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to withdraw tokens from the contract (only owner)
    // @param _amount The amount of tokens to withdraw
    function withdrawTokens(uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(msg.sender);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance in contract");
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }
}
```
