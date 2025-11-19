"""
Generated Code Metadata:
========================
Original URL: https://radiant.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that implements a simple lending and borrowing mechanism using Radiant's omnichain protocol, with dynamic APR based on market conditions.
Generated: DETERMINISTIC_e6146aad09705b33
Batch ID: 20250622_211705
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

// Interface for the Radiant's omnichain protocol
interface IRadiantOmnichain {
    function getMarketConditions() external view returns (uint256);
}

contract LendingBorrowing is Ownable {
    // Struct to hold loan details
    struct Loan {
        uint256 amount;
        uint256 interestRate; // APR in basis points (1% = 100 basis points)
        uint256 dueDate;
        bool isActive;
    }

    // Mapping to track loans for each borrower
    mapping(address => Loan) public loans;

    // ERC20 token used for lending and borrowing
    IERC20 public token;
    IRadiantOmnichain public radiant;

    // Events for logging actions
    event LoanCreated(address indexed borrower, uint256 amount, uint256 interestRate, uint256 dueDate);
    event LoanRepaid(address indexed borrower, uint256 amount);
    event LoanDefaulted(address indexed borrower);

    // Constructor to initialize the contract with token and Radiant protocol
    constructor(IERC20 _token, IRadiantOmnichain _radiant) {
        token = _token;
        radiant = _radiant;
    }

    // Function to create a loan
    function createLoan(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Fetch current market conditions to determine APR
        uint256 marketCondition = radiant.getMarketConditions();
        uint256 interestRate = calculateAPR(marketCondition);

        // Transfer tokens to the borrower
        token.transfer(msg.sender, _amount);

        // Create the loan
        loans[msg.sender] = Loan({
            amount: _amount,
            interestRate: interestRate,
            dueDate: block.timestamp + _duration,
            isActive: true
        });

        emit LoanCreated(msg.sender, _amount, interestRate, loans[msg.sender].dueDate);
    }

    // Function to calculate APR based on market conditions
    function calculateAPR(uint256 marketCondition) internal pure returns (uint256) {
        // Example logic for APR calculation
        // This can be adjusted based on actual market conditions
        return marketCondition * 10; // 10 basis points per unit of market condition
    }

    // Function to repay a loan
    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to repay");
        
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 10000); // Calculate total repayment

        // Transfer tokens from borrower to contract
        token.transferFrom(msg.sender, address(this), totalRepayment);

        // Mark loan as repaid
        loan.isActive = false;

        emit LoanRepaid(msg.sender, totalRepayment);
    }

    // Function to check for loan defaults
    function checkForDefaults() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to check");

        if (block.timestamp > loan.dueDate) {
            // Mark loan as defaulted
            loan.isActive = false;
            emit LoanDefaulted(msg.sender);
        }
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        token.transfer(msg.sender, _amount);
    }
}
```
