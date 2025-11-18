"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://definerhodler.pages.dev
Prompt: Create a smart contract that supports configurable lending terms, including collateral and interest rates, inspired by DeFiner's lending model.
Generated: DETERMINISTIC_dfc0293f04daca89
Batch ID: 20250612_150613
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ConfigurableLending {
    using SafeMath for uint256;

    // Struct to hold lending terms
    struct LendingTerms {
        uint256 interestRate; // Interest rate in basis points (100 basis points = 1%)
        uint256 collateralAmount; // Amount of collateral required
        uint256 loanAmount; // Amount of loan
        bool active; // Status of the lending terms
    }

    // Mapping to hold user loans
    mapping(address => LendingTerms) public loans;

    // Events for logging
    event LoanRequested(address indexed borrower, uint256 amount, uint256 collateral);
    event LoanRepaid(address indexed borrower, uint256 amount);
    event TermsConfigured(address indexed lender, uint256 interestRate, uint256 collateralAmount);

    // Function to configure lending terms
    function configureTerms(uint256 _interestRate, uint256 _collateralAmount) external {
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_collateralAmount > 0, "Collateral amount must be greater than zero");

        // Store the lending terms for the caller
        loans[msg.sender] = LendingTerms({
            interestRate: _interestRate,
            collateralAmount: _collateralAmount,
            loanAmount: 0,
            active: true
        });

        emit TermsConfigured(msg.sender, _interestRate, _collateralAmount);
    }

    // Function for a borrower to request a loan
    function requestLoan(uint256 _loanAmount) external payable {
        LendingTerms storage terms = loans[msg.sender];

        require(terms.active, "Lending terms not active");
        require(msg.value >= terms.collateralAmount, "Insufficient collateral sent");
        require(_loanAmount > 0, "Loan amount must be greater than zero");

        terms.loanAmount = _loanAmount;

        // Transfer the loan amount to the borrower
        payable(msg.sender).transfer(_loanAmount);

        emit LoanRequested(msg.sender, _loanAmount, msg.value);
    }

    // Function to repay loan
    function repayLoan() external payable {
        LendingTerms storage terms = loans[msg.sender];

        require(terms.active, "No active loan found");
        require(msg.value >= terms.loanAmount.add(calculateInterest(terms.loanAmount, terms.interestRate)), "Insufficient amount to repay");

        // Resetting the loan terms
        terms.loanAmount = 0;

        // Return collateral to the borrower
        payable(msg.sender).transfer(msg.value.sub(terms.loanAmount.add(calculateInterest(terms.loanAmount, terms.interestRate))));

        emit LoanRepaid(msg.sender, terms.loanAmount);
    }

    // Function to calculate interest based on loan amount and interest rate
    function calculateInterest(uint256 _amount, uint256 _interestRate) internal pure returns (uint256) {
        return _amount.mul(_interestRate).div(10000); // Convert basis points to decimal
    }

    // Function to deactivate lending terms
    function deactivateTerms() external {
        LendingTerms storage terms = loans[msg.sender];
        terms.active = false;
    }

    // Function to retrieve the current lending terms
    function getLendingTerms() external view returns (LendingTerms memory) {
        return loans[msg.sender];
    }
}
```
