"""
Generated Code Metadata:
========================
Original URL: https://raca3-2.pages.dev
Prompt: Write a smart contract to facilitate cross-chain lending using RACA's partnership with LEND Finance in the USM Metaverse.
Generated: DETERMINISTIC_1aa2cc321339c562
Batch ID: 20250612_152422
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

// Interface for LEND Finance
interface ILendFinance {
    function lend(address borrower, uint256 amount) external returns (bool);
    function repay(address borrower, uint256 amount) external returns (bool);
}

// Smart contract for cross-chain lending
contract CrossChainLending is Ownable {
    // State variables
    IERC20 public racaToken; // RACA token contract
    ILendFinance public lendFinance; // LEND Finance contract
    mapping(address => uint256) public loans; // Track loans for each borrower

    // Events
    event LoanIssued(address indexed borrower, uint256 amount);
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Constructor to initialize the contract with RACA and LEND Finance addresses
    constructor(address _racaToken, address _lendFinance) {
        require(_racaToken != address(0), "Invalid RACA token address");
        require(_lendFinance != address(0), "Invalid LEND Finance address");
        
        racaToken = IERC20(_racaToken);
        lendFinance = ILendFinance(_lendFinance);
    }

    // Function to issue a loan
    function issueLoan(uint256 amount) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(racaToken.balanceOf(address(this)) >= amount, "Insufficient RACA balance in contract");

        // Lend the amount to the borrower
        bool success = lendFinance.lend(msg.sender, amount);
        require(success, "Loan issuance failed");

        // Update loan balance
        loans[msg.sender] += amount;

        // Emit loan issued event
        emit LoanIssued(msg.sender, amount);
    }

    // Function to repay a loan
    function repayLoan(uint256 amount) external {
        require(amount > 0, "Repayment amount must be greater than zero");
        require(loans[msg.sender] >= amount, "Repayment exceeds loan amount");

        // Transfer RACA tokens from borrower to contract
        racaToken.transferFrom(msg.sender, address(this), amount);

        // Repay the loan
        bool success = lendFinance.repay(msg.sender, amount);
        require(success, "Loan repayment failed");

        // Update loan balance
        loans[msg.sender] -= amount;

        // Emit loan repaid event
        emit LoanRepaid(msg.sender, amount);
    }

    // Function to withdraw RACA tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(racaToken.balanceOf(address(this)) >= amount, "Insufficient RACA balance in contract");

        // Transfer RACA tokens to owner
        racaToken.transfer(msg.sender, amount);
    }

    // Function to check the loan balance of a borrower
    function getLoanBalance(address borrower) external view returns (uint256) {
        return loans[borrower];
    }
}
```
