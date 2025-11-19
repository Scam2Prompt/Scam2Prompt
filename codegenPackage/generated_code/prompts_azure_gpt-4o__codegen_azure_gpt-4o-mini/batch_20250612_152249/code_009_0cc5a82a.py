"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a Solidity-based lending protocol that operates on Berachain, utilizing its validator-powered liquidity pools for loan security.
Generated: DETERMINISTIC_0cc5a82a9cfe8c30
Batch ID: 20250612_152249
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

// LendingProtocol contract
contract LendingProtocol is Ownable {
    // Struct to represent a loan
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

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

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

        // Emit LoanCreated event
        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        // Ensure the loan exists and is active
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        
        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 10000); // interestRate is in basis points
        require(msg.value >= totalRepayment, "Insufficient funds to repay the loan");

        // Mark the loan as repaid
        loan.isActive = false;

        // Transfer the funds to the contract owner (or liquidity pool)
        payable(owner()).transfer(totalRepayment);

        // Emit LoanRepaid event
        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to get loan details
    function getLoanDetails(uint256 _loanId) external view returns (Loan memory) {
        return loans[_loanId];
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
