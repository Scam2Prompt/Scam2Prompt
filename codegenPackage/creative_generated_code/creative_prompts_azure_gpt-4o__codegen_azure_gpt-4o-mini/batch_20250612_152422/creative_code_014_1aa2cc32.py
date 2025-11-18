"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-2.pages.dev
Prompt: Write a smart contract to facilitate cross-chain lending using RACA's partnership with LEND Finance in the USM Metaverse.
Generated: DETERMINISTIC_1aa2cc321339c562
Batch ID: 20250612_152422
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
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title CrossChainLending
/// @author Your Name
/// @notice This contract facilitates cross-chain lending using RACA's partnership with LEND Finance.
contract CrossChainLending is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold lending details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        bool isActive;
    }

    // State variables
    IERC20 public racaToken; // RACA token contract
    Counters.Counter private loanIdCounter; // Counter for unique loan IDs
    mapping(uint256 => Loan) public loans; // Mapping to store loans by their ID

    // Events
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 loanId);
    event LoanDefaulted(uint256 loanId);

    // Constructor to set RACA token address
    constructor(IERC20 _racaToken) {
        racaToken = _racaToken;
    }

    /// @notice Create a new loan
    /// @param _amount Amount to loan
    /// @param _interestRate Interest rate for the loan (in basis points)
    /// @param _duration Duration of the loan in seconds
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than 0");
        require(_interestRate > 0, "Interest rate must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        // Transfer RACA tokens from borrower to contract
        require(racaToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        uint256 loanId = loanIdCounter.current();
        loans[loanId] = Loan(msg.sender, _amount, _interestRate, _duration, true);
        loanIdCounter.increment();

        emit LoanCreated(loanId, msg.sender, _amount, _interestRate, _duration);
    }

    /// @notice Repay a loan
    /// @param _loanId ID of the loan to repay
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only borrower can repay the loan");

        uint256 repaymentAmount = loan.amount + (loan.amount * loan.interestRate) / 10000; // Calculate repayment amount

        // Transfer repayment amount from borrower to contract
        require(racaToken.transferFrom(msg.sender, address(this), repaymentAmount), "Repayment transfer failed");

        loan.isActive = false; // Mark loan as repaid

        emit LoanRepaid(_loanId);
    }

    /// @notice Default on a loan
    /// @param _loanId ID of the loan to default on
    function defaultLoan(uint256 _loanId) external onlyOwner {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");

        loan.isActive = false; // Mark loan as defaulted

        emit LoanDefaulted(_loanId);
    }

    /// @notice Retrieve loan details
    /// @param _loanId ID of the loan
    /// @return Loan details
    function getLoanDetails(uint256 _loanId) external view returns (Loan memory) {
        return loans[_loanId];
    }
}
```
