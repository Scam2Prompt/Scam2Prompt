"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: "Generate a smart contract code for a lending platform on Polkadot's Moonbeam network, incorporating community governance and security audits like Moonwell."
Generated: DETERMINISTIC_324a15a70cb97aad
Batch ID: 20250622_204816
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LendingPlatform contract for managing loans and community governance
contract LendingPlatform is Ownable {
    using SafeMath for uint256;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping to store loans by ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a new loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Community governance variables
    mapping(address => uint256) public votes;
    uint256 public totalVotes;

    // Modifier to check if the loan exists
    modifier loanExists(uint256 loanId) {
        require(loanId < loanCounter, "Loan does not exist");
        _;
    }

    // Function to create a new loan
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(loanCounter, msg.sender, amount, interestRate, duration);
        loanCounter++;
    }

    // Function to repay a loan
    function repayLoan(uint256 loanId) external loanExists(loanId) {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount.add(loan.amount.mul(loan.interestRate).div(10000));

        // Transfer the repayment amount (assuming the contract holds the token)
        require(IERC20(address(this)).transferFrom(msg.sender, address(this), totalRepayment), "Transfer failed");

        loan.isActive = false;

        emit LoanRepaid(loanId, msg.sender);
    }

    // Function for community governance voting
    function vote(address proposal) external {
        require(votes[msg.sender] == 0, "You have already voted");
        votes[msg.sender] = 1; // Simple voting mechanism
        totalVotes++;
    }

    // Function to withdraw funds (only for the owner)
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(address(this)).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount to the owner
        require(IERC20(address(this)).transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to check the status of a loan
    function getLoanStatus(uint256 loanId) external view loanExists(loanId) returns (Loan memory) {
        return loans[loanId];
    }
}
```
