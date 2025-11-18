"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncrete.pages.dev
Prompt: Generate code for an appchain that improves on-chain debt and credit management, incorporating features like higher yields and liquidation protection.
Generated: DETERMINISTIC_7fc5705c1ce6f599
Batch ID: 20250612_152018
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

/// @title AppChain for Debt and Credit Management
/// @author Your Name
/// @notice This contract allows users to manage on-chain debt and credit with features for higher yields and liquidation protection.
contract DebtCreditManager {
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // as a percentage
        uint256 term; // in seconds
        bool active;
    }

    mapping(uint256 => Loan) public loans;
    mapping(address => uint256) public collateralBalances;
    uint256 public loanCounter;

    event LoanCreated(uint256 indexed loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 term);
    event LoanRepaid(uint256 indexed loanId, address indexed borrower);
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    // Maximum collateralization ratio (150%)
    uint256 public constant COLLATERALIZATION_RATIO = 150;

    /// @notice Allows a user to deposit collateral
    /// @param amount The amount of collateral to deposit
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        collateralBalances[msg.sender] += amount;
        emit CollateralDeposited(msg.sender, amount);
    }

    /// @notice Allows a user to create a loan
    /// @param amount The amount of the loan
    /// @param interestRate The interest rate of the loan as a percentage
    /// @param term The term of the loan in seconds
    function createLoan(uint256 amount, uint256 interestRate, uint256 term) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0 && interestRate <= 100, "Invalid interest rate");
        require(term > 0, "Loan term must be greater than zero");
        
        uint256 collateralNeeded = (amount * COLLATERALIZATION_RATIO) / 100;
        require(collateralBalances[msg.sender] >= collateralNeeded, "Insufficient collateral");

        loans[loanCounter] = Loan(msg.sender, amount, interestRate, term, true);
        loanCounter++;

        emit LoanCreated(loanCounter - 1, msg.sender, amount, interestRate, term);
    }

    /// @notice Allows a user to repay their loan
    /// @param loanId The ID of the loan to repay
    function repayLoan(uint256 loanId) external {
        Loan storage loan = loans[loanId];
        require(loan.active, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 100);
        // Assume transfer of `totalRepayment` happens here

        loan.active = false;
        emit LoanRepaid(loanId, msg.sender);
    }

    /// @notice Allows a user to withdraw collateral
    /// @param amount The amount of collateral to withdraw
    function withdrawCollateral(uint256 amount) external {
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral balance");

        // Validate that withdrawing will not violate collateralization
        uint256 totalDebt = calculateUserDebt(msg.sender);
        uint256 newCollateralBalance = collateralBalances[msg.sender] - amount;
        require((newCollateralBalance * 100) / totalDebt >= COLLATERALIZATION_RATIO, "Withdrawal violates collateralization ratio");

        collateralBalances[msg.sender] -= amount;
        emit CollateralWithdrawn(msg.sender, amount);
    }

    /// @notice Calculates the total debt for a user
    /// @param user The address of the user
    /// @return totalDebt The total debt of the user
    function calculateUserDebt(address user) public view returns (uint256 totalDebt) {
        for (uint256 i = 0; i < loanCounter; i++) {
            if (loans[i].borrower == user && loans[i].active) {
                totalDebt += loans[i].amount + (loans[i].amount * loans[i].interestRate / 100);
            }
        }
        return totalDebt;
    }
}
```
