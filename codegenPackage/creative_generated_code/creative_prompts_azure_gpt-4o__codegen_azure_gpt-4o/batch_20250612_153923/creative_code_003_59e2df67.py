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
pragma solidity ^0.8.18;

/**
 * @title Decentralized Lending and Borrowing Contract
 * @dev A smart contract for managing decentralized lending and borrowing,
 * inspired by Meteora Crypto's DeFi platform.
 */
contract DecentralizedLending {
    // Data structure for lenders
    struct Lender {
        uint256 balance;
    }

    // Data structure for borrowers
    struct Borrower {
        uint256 borrowedAmount;
        uint256 collateralAmount;
    }

    // Mapping of lenders and borrowers
    mapping(address => Lender) public lenders;
    mapping(address => Borrower) public borrowers;

    // Events
    event DepositLender(address indexed lender, uint256 amount);
    event WithdrawLender(address indexed lender, uint256 amount);
    event BorrowFunds(address indexed borrower, uint256 amount, uint256 collateral);
    event RepayLoan(address indexed borrower, uint256 amount);
    event LiquidateBorrower(address indexed borrower);

    // Interest rate and collateral ratio
    uint256 public constant INTEREST_RATE = 5; // 5% annual interest rate
    uint256 public constant COLLATERAL_RATIO = 150; // 150% collateral requirement

    // Modifier to ensure only positive amounts
    modifier positiveAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero.");
        _;
    }

    // Function for lenders to deposit funds
    function depositFunds() external payable positiveAmount(msg.value) {
        lenders[msg.sender].balance += msg.value;
        emit DepositLender(msg.sender, msg.value);
    }

    // Function for lenders to withdraw funds
    function withdrawFunds(uint256 amount) external positiveAmount(amount) {
        Lender storage lender = lenders[msg.sender];
        require(lender.balance >= amount, "Insufficient balance.");
        lender.balance -= amount;
        payable(msg.sender).transfer(amount);
        emit WithdrawLender(msg.sender, amount);
    }

    // Function for borrowers to request a loan
    function borrow(uint256 amount) external payable positiveAmount(amount) {
        require(
            msg.value >= (amount * COLLATERAL_RATIO) / 100,
            "Insufficient collateral provided."
        );

        Borrower storage borrower = borrowers[msg.sender];
        borrower.borrowedAmount += amount;
        borrower.collateralAmount += msg.value;

        payable(msg.sender).transfer(amount);
        emit BorrowFunds(msg.sender, amount, msg.value);
    }

    // Function for borrowers to repay a loan
    function repayLoan() external payable {
        Borrower storage borrower = borrowers[msg.sender];
        require(borrower.borrowedAmount > 0, "No outstanding loan to repay.");
        require(msg.value > 0, "Repayment amount must be greater than zero.");

        uint256 interest = (borrower.borrowedAmount * INTEREST_RATE) / 100;

        require(
            msg.value >= borrower.borrowedAmount + interest,
            "Repayment amount insufficient to cover loan and interest."
        );
        
        borrower.borrowedAmount = 0;
        payable(msg.sender).transfer(borrower.collateralAmount);
        borrower.collateralAmount = 0;

        emit RepayLoan(msg.sender, msg.value);
    }

    // Function to liquidate borrowers who fail to repay
    function liquidate(address borrowerAddress) external {
        Borrower storage borrower = borrowers[borrowerAddress];
        require(borrower.borrowedAmount > 0, "No outstanding loan to liquidate.");

        uint256 interest = (borrower.borrowedAmount * INTEREST_RATE) / 100;

        // If collateral is insufficient to cover the debt, liquidate the borrower
        require(
            borrower.collateralAmount < borrower.borrowedAmount + interest,
            "Borrower is not eligible for liquidation."
        );

        borrower.borrowedAmount = 0;
        borrower.collateralAmount = 0;

        emit LiquidateBorrower(borrowerAddress);
    }

    // Fallback function to accept Ether
    receive() external payable {}

    /**
     * @dev Helper function to check lender balance
     * @param lenderAddress The address of the lender
     * @return balance The balance of the lender
     */
    function getLenderBalance(address lenderAddress) external view returns (uint256 balance) {
        return lenders[lenderAddress].balance;
    }

    /**
     * @dev Helper function to check borrower loan details
     * @param borrowerAddress The address of the borrower
     * @return borrowedAmount, collateralAmount
     */
    function getBorrowerDetails(address borrowerAddress)
        external
        view
        returns (uint256 borrowedAmount, uint256 collateralAmount)
    {
        Borrower storage borrower = borrowers[borrowerAddress];
        return (borrower.borrowedAmount, borrower.collateralAmount);
    }
}
```
