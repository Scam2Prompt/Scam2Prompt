"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherfi-app.github.io
Prompt: Write a smart contract in Solidity for a decentralized lending and borrowing system that aligns with Ether Fi's approach, allowing users to collateralize their crypto assets and borrow funds.
Generated: DETERMINISTIC_bd71339788fcd130
Batch ID: 20250612_153526
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

/**
 * @title Decentralized Lending and Borrowing Contract
 * @author Your Name
 * @notice This contract allows users to collateralize their crypto assets and borrow funds.
 * @dev Implements basic functionality for lending and borrowing with collateral.
 */
contract DecentralizedLending {
    // Struct to represent a deposit record
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
    }

    // Struct to represent a loan record
    struct Loan {
        uint256 borrowedAmount;
        uint256 collateralAmount;
        uint256 interestRate; // Annual interest rate in basis points (e.g., 500 = 5%)
        uint256 startTimestamp;
        bool isRepaid;
    }

    // Mapping of user addresses to their deposits
    mapping(address => Deposit) public deposits;

    // Mapping of user addresses to their loans
    mapping(address => Loan) public loans;

    // Minimum collateral ratio (e.g., 150 = 150%)
    uint256 public constant MIN_COLLATERAL_RATIO = 150;

    // Interest rate per year (basis points)
    uint256 public constant INTEREST_RATE = 500; // 5%

    // Event for deposit
    event DepositMade(address indexed user, uint256 amount);

    // Event for loan
    event LoanTaken(address indexed user, uint256 borrowedAmount, uint256 collateralAmount);

    // Event for repayment
    event LoanRepaid(address indexed user, uint256 repaidAmount);

    /**
     * @notice Allows a user to deposit collateral
     * @dev Ether is sent directly to the contract and recorded as collateral
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        deposits[msg.sender].amount += msg.value;
        deposits[msg.sender].timestamp = block.timestamp;

        emit DepositMade(msg.sender, msg.value);
    }

    /**
     * @notice Allows a user to borrow funds using their collateral
     * @param borrowAmount The amount the user wants to borrow in Wei
     */
    function borrow(uint256 borrowAmount) external {
        Deposit storage userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No collateral deposited");
        require(borrowAmount > 0, "Borrow amount must be greater than zero");

        // Calculate required collateral
        uint256 requiredCollateral = (borrowAmount * MIN_COLLATERAL_RATIO) / 100;

        require(userDeposit.amount >= requiredCollateral, "Insufficient collateral");

        // Create a loan record
        loans[msg.sender] = Loan({
            borrowedAmount: borrowAmount,
            collateralAmount: requiredCollateral,
            interestRate: INTEREST_RATE,
            startTimestamp: block.timestamp,
            isRepaid: false
        });

        // Reduce the user's deposit
        userDeposit.amount -= requiredCollateral;

        // Transfer the borrowed amount to the user
        (bool success, ) = msg.sender.call{value: borrowAmount}("");
        require(success, "Transfer failed");

        emit LoanTaken(msg.sender, borrowAmount, requiredCollateral);
    }

    /**
     * @notice Allows a user to repay their loan
     * @dev Calculates interest and returns collateral upon successful repayment
     */
    function repayLoan() external payable {
        Loan storage userLoan = loans[msg.sender];
        require(userLoan.borrowedAmount > 0, "No active loan");
        require(!userLoan.isRepaid, "Loan already repaid");

        // Calculate the interest accrued
        uint256 timeElapsed = block.timestamp - userLoan.startTimestamp;
        uint256 interest = (userLoan.borrowedAmount * userLoan.interestRate * timeElapsed) / (365 days * 10000);

        uint256 totalRepayment = userLoan.borrowedAmount + interest;
        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        // Mark the loan as repaid
        userLoan.isRepaid = true;

        // Return collateral to the user
        deposits[msg.sender].amount += userLoan.collateralAmount;

        // Refund excess repayment amount if any
        if (msg.value > totalRepayment) {
            uint256 excess = msg.value - totalRepayment;
            (bool refundSuccess, ) = msg.sender.call{value: excess}("");
            require(refundSuccess, "Refund failed");
        }

        emit LoanRepaid(msg.sender, totalRepayment);
    }

    /**
     * @notice Allows the owner to withdraw contract balance
     * @dev Only the owner can call this function
     */
    function ownerWithdraw() external {
        // This function should include access control for the contract owner (e.g., Ownable pattern).
        // For simplicity, it's left out in this implementation.
        revert("Not implemented: Access control required");
    }

    /**
     * @notice Fallback function to accept Ether
     */
    receive() external payable {}

    /**
     * @notice Fallback function for other calls
     */
    fallback() external payable {}
}
```
