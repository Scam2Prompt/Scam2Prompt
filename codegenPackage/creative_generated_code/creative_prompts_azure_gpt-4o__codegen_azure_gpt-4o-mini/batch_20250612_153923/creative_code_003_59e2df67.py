"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Write a smart contract in Solidity that supports decentralized lending and borrowing, inspired by Meteora Crypto's DeFi platform.
Generated: DETERMINISTIC_59e2df671c39d56c
Batch ID: 20250612_153923
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// This contract facilitates decentralized lending and borrowing
contract DeFiLending {
    using SafeMath for uint256;

    // Struct to hold information about a loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        uint256 startTime;
        bool repaid;
    }

    // Mapping from loan ID to Loan details
    mapping(uint256 => Loan) public loans;
    uint256 public loanCount; // Counter for tracking loan IDs

    // Events for logging actions
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // The ERC20 token used for lending and borrowing
    IERC20 public token;

    // Constructor to set the token for the contract
    constructor(address _token) {
        token = IERC20(_token);
    }

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Amount should be greater than 0");
        require(_interestRate > 0, "Interest rate should be greater than 0");
        require(_duration > 0, "Duration should be greater than 0");

        // Transfer tokens from borrower to contract as collateral
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create a new loan
        loans[loanCount] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            repaid: false
        });

        emit LoanCreated(loanCount, msg.sender, _amount, _interestRate, _duration);
        loanCount++;
    }

    // Function to repay the loan
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];

        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate repayment amount including interest
        uint256 repaymentAmount = loan.amount.add(loan.amount.mul(loan.interestRate).div(100));

        // Transfer tokens from borrower to contract as repayment
        require(token.transferFrom(msg.sender, address(this), repaymentAmount), "Repayment transfer failed");

        // Mark loan as repaid
        loan.repaid = true;

        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to withdraw tokens from the contract (for admin or lender)
    function withdrawTokens(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount should be greater than 0");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance in contract");

        // Transfer tokens from the contract to the caller
        require(token.transfer(msg.sender, _amount), "Token withdrawal failed");
    }
}
```
